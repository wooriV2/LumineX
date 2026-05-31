"""
dashboard.py - Claude Asset Engine 대시보드 (모바일 반응형)
"""

import json
import streamlit as st
import plotly.graph_objects as go
from datetime import date
from decimal import Decimal
from pathlib import Path
import yfinance as yf

from asset_engine.config import load_kis_config
from asset_engine.models.asset import AssetRole, AssetType, Exchange, Market
from asset_engine.models.asset import Asset
from asset_engine.models.money import Currency, Money
from asset_engine.models.portfolio import FxRates
from asset_engine.presets.buffett_compound_defense import BUFFETT_COMPOUND_DEFENSE
from asset_engine.providers.fx_provider import YFinanceFxProvider
from asset_engine.providers.indicator_provider import YFinanceIndicatorProvider
from asset_engine.providers.kis_broker import KISAdapter
from asset_engine.providers.fdr_provider import FDRProvider
from asset_engine.providers.dart_provider import DARTProvider
from asset_engine.engine.regime import RegimeEngine
from asset_engine.engine.rebalance import RebalanceEngine
from asset_engine.engine.safety import create_safety_guard
from asset_engine.engine.correlation_guard import CorrelationGuard, default_guard
from asset_engine.engine.scoring import StockScorer
from asset_engine.engine.scoring_cache import get_or_fetch_score, invalidate_all_cache
from asset_engine.models.action import AlertLevel


# =============================================================================
# 설정
# =============================================================================

TRANSACTION_COST = 0.00015   # 수수료 0.015%
TAX_TRANSACTION = 0.0018     # 거래세 0.18%

ROLE_MAP = {
    "360750": AssetRole.CORE,
    "360750": AssetRole.CORE,
    "000660": AssetRole.GROWTH,
    "005930": AssetRole.CORE,
    "030200": AssetRole.INCOME,
}

DART_CORP_CODES = {
    "005930": "00126380",
    "000660": "00164779",
    "030200": "00104899",
    "360750": None,
}

PRESET = BUFFETT_COMPOUND_DEFENSE

ROLE_COLOR = {
    "Core": "#4C9EEB",
    "Income": "#00C896",
    "Growth": "#9B59B6",
    "Hedge": "#F5A623",
    "Special": "#E74C3C",
}

# 추천 후보 모드별 파일
BUY_CANDIDATES_DIR = Path("cache/recommend_buy")
BUCKETS_PATH = Path("cache/buckets.json")
MODE_FILE_MAP = {
    "🏛️ 버핏형": "buffett",
    "⚖️ 균형형": "balanced",
    "🚀 성장형": "growth",
}


# =============================================================================
# 페이지 설정
# =============================================================================

st.set_page_config(
    page_title="Claude Asset Engine",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .main { background-color: #0E1117; }
    div[data-testid="stMetric"] {
        background: #1E2130;
        border-radius: 12px;
        padding: 12px;
        border: 1px solid #2D3250;
    }
    div[data-testid="stMetric"] label { font-size: 11px !important; }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] { font-size: 16px !important; }
    .stButton > button { min-height: 44px; font-size: 15px; }
    .stTabs [data-baseweb="tab"] { font-size: 14px; padding: 10px 16px; }
    [data-testid="column"] { padding: 0 4px !important; }
    section[data-testid="stSidebar"] { min-width: 260px; max-width: 300px; }
    details summary { min-height: 44px; display: flex; align-items: center; }
    @media (max-width: 768px) {
        div[data-testid="stMetric"] { padding: 8px; }
        div[data-testid="stMetric"] label { font-size: 10px !important; }
        div[data-testid="stMetric"] [data-testid="stMetricValue"] { font-size: 13px !important; }
        h1 { font-size: 1.4rem !important; }
        h3 { font-size: 1.1rem !important; }
    }
</style>
""", unsafe_allow_html=True)


# =============================================================================
# 데이터 로딩
# =============================================================================

@st.cache_data(ttl=300)
def load_data(is_paper: bool):
    config = load_kis_config(is_paper=is_paper)
    adapter = KISAdapter(
        app_key=config.app_key,
        app_secret=config.app_secret,
        account_no=config.account_no,
        is_paper=config.is_paper,
    )
    portfolio = adapter.get_portfolio(role_map=ROLE_MAP)

    fx_provider = YFinanceFxProvider()
    fx_rate = fx_provider.get_rate(Currency.USD, Currency.KRW)
    fx = FxRates(
        base=Currency.KRW,
        rates={Currency.USD: fx_rate},
        as_of=date.today(),
    )

    prices = {}
    for pos in portfolio.positions:
        try:
            prices[pos.asset.ticker] = adapter.get_current_price(pos.asset)
        except Exception:
            try:
                kr_provider = FDRProvider()
                prices[pos.asset.ticker] = kr_provider.get_current_price(pos.asset)
            except Exception:
                pass

    indicator = YFinanceIndicatorProvider()
    snapshot = indicator.get_market_snapshot()

    regime_engine = RegimeEngine(preset=PRESET)
    regime, _ = regime_engine.determine_regime(snapshot)

    rebalance_engine = RebalanceEngine(preset=PRESET)
    total = portfolio.total_value(prices, fx)
    output = rebalance_engine.run(
        portfolio=portfolio,
        prices=prices,
        fx=fx,
        regime=regime,
        peak_value=total,
    )

    return {
        "portfolio": portfolio,
        "prices": prices,
        "fx": fx,
        "fx_rate": fx_rate,
        "snapshot": snapshot,
        "regime": regime,
        "output": output,
        "total": total,
        "adapter": adapter,
    }


def fetch_score_for(ticker: str, name: str, corp_code: str) -> object:
    dart = DARTProvider()
    scorer = StockScorer(preset=PRESET)
    ttm, label = dart.get_ttm_financials(corp_code)
    trend = dart.get_trend_metrics(corp_code, years=10)
    latest_year = dart.get_latest_fiscal_year(corp_code)
    dividend = dart.get_dividend_history(corp_code, year=latest_year)
    yf_ticker = yf.Ticker(f"{ticker}.KS")
    info = yf_ticker.info
    current_price = info.get("currentPrice") or info.get("regularMarketPrice") or 0
    per = info.get("trailingPE") or 0
    if per == 0 and current_price > 0:
        shares = info.get("sharesOutstanding") or 0
        net_income = float(ttm.get("net_income", 0))
        if shares > 0 and net_income > 0:
            per = current_price / (net_income / shares)
    pbr = info.get("priceToBook") or 0
    if pbr == 0 and current_price > 0:
        shares = info.get("sharesOutstanding") or 0
        total_equity = float(ttm.get("total_equity", 0))
        if shares > 0 and total_equity > 0:
            pbr = current_price / (total_equity / shares)
    beta = info.get("beta") or 1.0
    div_yield_raw = info.get("dividendYield") or 0
    div_yield = div_yield_raw * 100 if div_yield_raw <= 1 else div_yield_raw
    market_data = {"per": per, "pbr": pbr, "beta": beta, "dividend_yield": div_yield}
    return scorer.score(
        ticker=ticker, name=name, ttm=ttm,
        market_data=market_data, dividend=dividend,
        trend=trend, data_label=label,
    )


def load_buy_candidates_by_mode(mode: str):
    safe = MODE_FILE_MAP.get(mode, "unknown")
    path = BUY_CANDIDATES_DIR / f"{safe}.json"
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def load_buckets() -> dict:
    if not BUCKETS_PATH.exists():
        return {}
    try:
        with open(BUCKETS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_buckets(data: dict) -> None:
    with open(BUCKETS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)        


def get_current_price_by_ticker(ticker: str, is_paper: bool) -> tuple:
    try:
        config = load_kis_config(is_paper=is_paper)
        adapter = KISAdapter(
            app_key=config.app_key,
            app_secret=config.app_secret,
            account_no=config.account_no,
            is_paper=config.is_paper,
        )
        asset = Asset(
            ticker=ticker, name=ticker,
            market=Market.KR, asset_type=AssetType.STOCK,
            currency=Currency.KRW, exchange=Exchange.KRX,
            candidate_roles=[AssetRole.CORE],
        )
        price = adapter.get_current_price(asset)
        try:
            info = yf.Ticker(f"{ticker}.KS").info
            name = info.get("longName") or info.get("shortName") or ticker
        except Exception:
            name = ticker
        return price, name
    except Exception as e:
        return None, str(e)


def place_manual_order(ticker: str, name: str, quantity: int, is_paper: bool, side: str = "buy") -> str:
    config = load_kis_config(is_paper=is_paper)
    adapter = KISAdapter(
        app_key=config.app_key,
        app_secret=config.app_secret,
        account_no=config.account_no,
        is_paper=config.is_paper,
    )
    asset = Asset(
        ticker=ticker, name=name,
        market=Market.KR, asset_type=AssetType.STOCK,
        currency=Currency.KRW, exchange=Exchange.KRX,
        candidate_roles=[AssetRole.CORE],
    )
    if side == "buy":
        return adapter.place_buy_order(asset=asset, quantity=Decimal(str(quantity)))
    else:
        return adapter.place_sell_order(asset=asset, quantity=Decimal(str(quantity)))


# =============================================================================
# 사이드바
# =============================================================================

with st.sidebar:
    st.markdown("### ⚙️ 설정")
    is_paper = st.toggle("모의투자", value=False)
    st.markdown("---")
    if st.button("🔄 데이터 새로고침", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    st.markdown("---")
    st.markdown("### 📋 프리셋")
    st.markdown(f"**{PRESET.name}**")
    st.markdown(f"기본 목표: {PRESET.target_return.baseline*100:.0f}%")
    st.markdown(f"도전 목표: {PRESET.target_return.stretch*100:.0f}%")
    st.markdown("---")
    st.markdown("### 🎯 목표 비중")
    for role in AssetRole:
        target = PRESET.role_targets.get(role)
        color = ROLE_COLOR.get(role.value, "#8B9AB0")
        st.markdown(
            f"<span style='color:{color}'>■</span> **{role.value}**: {target*100:.0f}%",
            unsafe_allow_html=True,
        )


# =============================================================================
# 메인
# =============================================================================

st.markdown("# 📊 Claude Asset Engine")
st.markdown(f"*{date.today().strftime('%Y년 %m월 %d일')} 기준*")
st.markdown("---")

with st.spinner("데이터 조회 중..."):
    try:
        data = load_data(is_paper=is_paper)
    except Exception as e:
        st.error(f"데이터 로딩 실패: {e}")
        st.stop()

portfolio = data["portfolio"]
prices = data["prices"]
fx = data["fx"]
snapshot = data["snapshot"]
regime = data["regime"]
output = data["output"]
total = data["total"]

# =============================================================================
# 탭 구조
# =============================================================================

tab_overview, tab_core, tab_satellite, tab_positions, tab_rebalance, tab_analysis, tab_recommend, tab_manual = st.tabs([
    "📊 개요", "🏛️ Core", "🚀 Satellite", "📋 포지션", "⚖️ 리밸런싱", "📈 종목분석", "🎯 추천 후보", "🔍 수동 매수"
])


# ── TAB 1: 개요 ──────────────────────────────────────────────────────────────
with tab_overview:
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="💰 총액", value=f"{total.amount:,.0f} KRW")
    with col2:
        st.metric(label="🌍 레짐", value=regime.value)

    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric(label="📉 MDD", value=f"{output.current_mdd*100:.1f}%")
    with col4:
        cash_weight = portfolio.cash_weight(prices, fx)
        st.metric(
            label="💵 현금",
            value=f"{cash_weight*100:.1f}%",
            delta=f"목표 {PRESET.constraints.normal_cash_weight*100:.0f}%",
        )
    with col5:
        st.metric(
            label="📋 제안",
            value=f"{len(output.actions)}건",
            delta=f"알림 {len(output.alerts)}건",
        )

    st.markdown("---")
    st.markdown("### 🌍 시장 지표")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="S&P500", value=f"{snapshot.sp500:,.0f}",
            delta=f"MA200 {'위' if not snapshot.is_below_ma200() else '아래'}",
        )
        dd = snapshot.sp500_drawdown_from_52w_high * 100
        st.metric(label="52주 고점 대비", value=f"{dd:.1f}%")
    with col2:
        st.metric(label="VIX", value=f"{snapshot.vix:.1f}",
                  delta="정상" if snapshot.vix < 25 else "주의")
        st.metric(label="환율", value=f"{data['fx_rate']:,.0f} KRW", delta="1 USD")

    st.markdown("---")
    chart_tab1, chart_tab2 = st.tabs(["역할별 비중", "포트폴리오 구성"])

    with chart_tab1:
        role_alloc = portfolio.allocation_by_role(prices, fx)
        roles, currents, targets, colors = [], [], [], []
        for role in AssetRole:
            current = float(role_alloc.get(role, 0))
            target = float(PRESET.role_targets.get(role))
            if current > 0 or target > 0:
                roles.append(role.value)
                currents.append(round(current * 100, 1))
                targets.append(round(target * 100, 1))
                colors.append(ROLE_COLOR.get(role.value, "#8B9AB0"))
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name="현재", x=roles, y=currents, marker_color=colors, opacity=0.9,
            text=[f"{v}%" for v in currents], textposition="outside",
        ))
        fig.add_trace(go.Bar(
            name="목표", x=roles, y=targets, marker_color=colors, opacity=0.3,
            text=[f"{v}%" for v in targets], textposition="outside",
        ))
        fig.update_layout(
            barmode="group", plot_bgcolor="#0E1117", paper_bgcolor="#0E1117",
            font_color="#FFFFFF", height=280, margin=dict(t=30, b=20, l=0, r=0),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            yaxis=dict(gridcolor="#2D3250", ticksuffix="%"),
            xaxis=dict(gridcolor="#2D3250"),
        )
        st.plotly_chart(fig, use_container_width=True)

    with chart_tab2:
        labels, values, pie_colors = [], [], []
        for pos in portfolio.positions:
            if pos.asset.ticker in prices:
                price = prices[pos.asset.ticker]
                value = pos.market_value_in(price, fx, Currency.KRW)
                labels.append(pos.asset.name)
                values.append(float(value.amount))
                pie_colors.append(ROLE_COLOR.get(pos.role.value, "#8B9AB0"))
        cash_total = portfolio.total_cash(fx)
        if not cash_total.is_zero():
            labels.append("현금")
            values.append(float(cash_total.amount))
            pie_colors.append("#8B9AB0")
        if values:
            fig2 = go.Figure(go.Pie(
                labels=labels, values=values, marker_colors=pie_colors,
                hole=0.5, textinfo="label+percent", textfont_size=11,
            ))
            fig2.update_layout(
                plot_bgcolor="#0E1117", paper_bgcolor="#0E1117",
                font_color="#FFFFFF", height=280,
                margin=dict(t=20, b=20, l=0, r=0), showlegend=False,
            )
            st.plotly_chart(fig2, use_container_width=True)

    if output.alerts:
        st.markdown("### 🔔 알림")
        for alert in output.alerts:
            if alert.level == AlertLevel.CRITICAL:
                st.error(f"🚨 **{alert.title}**: {alert.message}")
            elif alert.level == AlertLevel.WARNING:
                st.warning(f"⚠️ **{alert.title}**: {alert.message}")
            else:
                st.info(f"ℹ️ **{alert.title}**: {alert.message}")

# ── TAB Core ──────────────────────────────────────────────────────────────────
with tab_core:
    buckets = load_buckets()
    core = buckets.get("core", {})
    targets = core.get("targets", {})
    last_rebalance = core.get("last_rebalance", "미실행")
    rebalance_cycle = core.get("rebalance_cycle", "monthly")
    core_total = core.get("initial_total", 0)
    core_tickers = set(targets.keys())

    # Core 종목 필터링 (portfolio에서 buckets.json Core 티커 기준)
    core_positions = [p for p in portfolio.positions if p.asset.ticker in core_tickers]

    # Core 합산 계산
    core_eval = Decimal("0")
    core_cost = Decimal("0")
    core_pnl  = Decimal("0")
    for pos in core_positions:
        if pos.asset.ticker in prices:
            p_obj = prices[pos.asset.ticker]
            core_eval += pos.market_value(p_obj).amount
            core_cost += pos.cost_basis().amount
            core_pnl  += pos.unrealized_pnl(p_obj).amount

    core_pnl_rate = float(core_pnl / core_cost * 100) if core_cost > 0 else 0
    core_cash = Decimal(str(core_total)) - core_cost
    c_color = "#00C896" if core_pnl >= 0 else "#FF4E6A"
    c_sign  = "+" if core_pnl >= 0 else ""

    # ── 상단 요약 (한투 앱 스타일) ──
    st.markdown(
        f"<div style='background:linear-gradient(135deg,#111520,#161C2A);border-radius:14px;"
        f"padding:18px 22px;border:1px solid #1E2535;margin-bottom:14px'>"
        f"<div style='color:#4A5470;font-size:10px;font-weight:700;letter-spacing:0.1em;"
        f"text-transform:uppercase;margin-bottom:6px'>Core 버킷 평가손익</div>"
        f"<div style='display:flex;align-items:baseline;gap:12px;margin-bottom:14px'>"
        f"<span style='color:{c_color};font-size:28px;font-weight:700;"
        f"font-family:JetBrains Mono,monospace'>{c_sign}{float(core_pnl):,.0f}</span>"
        f"<span style='color:{c_color};font-size:16px;font-weight:700'>"
        f"{c_sign}{core_pnl_rate:.2f}%</span></div>"
        f"<div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:16px'>"
        f"<div><div style='color:#4A5470;font-size:10px;margin-bottom:3px'>평가금액</div>"
        f"<div style='color:#C8D0E0;font-size:14px;font-weight:600;"
        f"font-family:JetBrains Mono,monospace'>{float(core_eval):,.0f}</div></div>"
        f"<div><div style='color:#4A5470;font-size:10px;margin-bottom:3px'>매입금액</div>"
        f"<div style='color:#C8D0E0;font-size:14px;font-weight:600;"
        f"font-family:JetBrains Mono,monospace'>{float(core_cost):,.0f}</div></div>"
        f"<div><div style='color:#4A5470;font-size:10px;margin-bottom:3px'>잔여현금</div>"
        f"<div style='color:#C8D0E0;font-size:14px;font-weight:600;"
        f"font-family:JetBrains Mono,monospace'>{float(core_cash):,.0f}</div></div>"
        f"<div><div style='color:#4A5470;font-size:10px;margin-bottom:3px'>마지막 리밸런싱</div>"
        f"<div style='color:#C8D0E0;font-size:12px;font-weight:600'>{last_rebalance or '미실행'}</div></div>"
        f"</div></div>",
        unsafe_allow_html=True,
    )

    # ── 실제 보유 현황 테이블 ──
    st.markdown("<div class='section-header'>실제 보유 현황</div>", unsafe_allow_html=True)

    # 현재가 조회 (리밸런싱 계산용)
    core_prices = {}
    for ticker in targets:
        if targets[ticker].get("is_fund"):
            continue
        try:
            cfg = load_kis_config(is_paper=is_paper)
            adp = KISAdapter(app_key=cfg.app_key, app_secret=cfg.app_secret,
                             account_no=cfg.account_no, is_paper=cfg.is_paper)
            asset_obj = Asset(ticker=ticker, name=targets[ticker]["name"],
                              market=Market.KR, asset_type=AssetType.STOCK,
                              currency=Currency.KRW, exchange=Exchange.KRX,
                              candidate_roles=[AssetRole.CORE])
            core_prices[ticker] = float(adp.get_current_price(asset_obj).amount)
        except Exception:
            core_prices[ticker] = 0

    if core_positions:
        st.markdown(
            "<div style='display:grid;grid-template-columns:2.5fr 1.2fr 0.8fr 1.1fr 1.1fr 1.2fr 0.9fr;"
            "background:#0F1320;border-radius:8px 8px 0 0;padding:7px 14px;border:1px solid #1A2030'>"
            "<div class='lbl'>종목명</div>"
            "<div class='lbl' style='text-align:right'>평가손익</div>"
            "<div class='lbl' style='text-align:right'>보유</div>"
            "<div class='lbl' style='text-align:right'>매입단가</div>"
            "<div class='lbl' style='text-align:right'>현재가</div>"
            "<div class='lbl' style='text-align:right'>평가금액</div>"
            "<div class='lbl' style='text-align:right'>비중</div>"
            "</div>",
            unsafe_allow_html=True,
        )
        for i, pos in enumerate(core_positions):
            tk = pos.asset.ticker
            if tk not in prices:
                continue
            p_obj   = prices[tk]
            pnl_pos = pos.unrealized_pnl(p_obj)
            cost_p  = pos.cost_basis()
            val_pos = pos.market_value(p_obj)
            avg_p   = float(cost_p.amount / pos.quantity) if pos.quantity > 0 else 0
            pnl_r   = float(pnl_pos.amount / cost_p.amount * 100) if cost_p.amount > 0 else 0
            weight  = float(val_pos.amount / core_eval * 100) if core_eval > 0 else 0
            target_pct = targets.get(tk, {}).get("target_pct", 0)
            diff_pct = weight - target_pct
            w_color = "#00C896" if abs(diff_pct) <= 2 else "#F5A623" if abs(diff_pct) <= 5 else "#FF4E6A"
            pc = "#00C896" if pnl_r >= 0 else "#FF4E6A"
            ps = "+" if pnl_r >= 0 else ""
            br = "border-radius:0 0 8px 8px" if i == len(core_positions)-1 else "border-radius:0"
            st.markdown(
                f"<div style='display:grid;grid-template-columns:2.5fr 1.2fr 0.8fr 1.1fr 1.1fr 1.2fr 0.9fr;"
                f"background:#111520;padding:10px 14px;{br};"
                f"border:1px solid #1A2030;border-top:none;align-items:center'>"
                f"<div><div style='font-size:13px;font-weight:600;color:#C8D0E0'>{pos.asset.name}</div>"
                f"<div style='color:#3A4560;font-size:10px;font-family:JetBrains Mono,monospace;margin-top:1px'>{tk}</div></div>"
                f"<div style='text-align:right'>"
                f"<div style='color:{pc};font-size:12px;font-weight:700;font-family:JetBrains Mono,monospace'>{ps}{pnl_r:.2f}%</div>"
                f"<div style='color:{pc};font-size:10px;opacity:0.8'>{ps}{float(pnl_pos.amount):,.0f}</div></div>"
                f"<div style='text-align:right;color:#C8D0E0;font-size:13px;font-weight:600;"
                f"font-family:JetBrains Mono,monospace'>{int(pos.quantity):,}주</div>"
                f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                f"font-family:JetBrains Mono,monospace'>{avg_p:,.0f}</div>"
                f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                f"font-family:JetBrains Mono,monospace'>{float(p_obj.amount):,.0f}</div>"
                f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                f"font-family:JetBrains Mono,monospace'>{float(val_pos.amount):,.0f}</div>"
                f"<div style='text-align:right'>"
                f"<div style='color:{w_color};font-size:12px;font-weight:700'>{weight:.1f}%</div>"
                f"<div style='color:{w_color};font-size:9px'>목표 {target_pct}%</div></div>"
                f"</div>",
                unsafe_allow_html=True,
            )
    else:
        st.info("KIS 잔고에서 Core 종목을 찾을 수 없습니다.")

    # ── 종목별 목표 비중 (하단 expander) ──
    st.markdown("<hr class='divider-line'>", unsafe_allow_html=True)
    with st.expander("📊 종목별 목표 비중 설정 보기", expanded=False):
        st.markdown(
            "<div style='display:grid;grid-template-columns:2.5fr 0.8fr 1.2fr 1fr 1fr;"
            "background:#0F1320;border-radius:8px 8px 0 0;padding:7px 14px;border:1px solid #1A2030'>"
            "<div class='lbl'>종목명</div>"
            "<div class='lbl' style='text-align:right'>목표비중</div>"
            "<div class='lbl' style='text-align:right'>목표금액</div>"
            "<div class='lbl' style='text-align:right'>현재가</div>"
            "<div class='lbl' style='text-align:right'>목표수량</div>"
            "</div>",
            unsafe_allow_html=True,
        )
        ticker_items = list(targets.items())
        for i, (ticker, info) in enumerate(ticker_items):
            target_pct = info["target_pct"]
            target_amt = core_total * target_pct / 100
            is_fund = info.get("is_fund", False)
            br = "border-radius:0 0 8px 8px" if i == len(ticker_items)-1 else "border-radius:0"
            if is_fund:
                st.markdown(
                    f"<div style='display:grid;grid-template-columns:2.5fr 0.8fr 1.2fr 1fr 1fr;"
                    f"background:#111520;padding:10px 14px;{br};"
                    f"border:1px solid #1A2030;border-top:none;align-items:center'>"
                    f"<div><div style='font-size:13px;font-weight:600;color:#C8D0E0'>{info['name']}</div>"
                    f"<div style='margin-top:2px'><span style='background:#F5A62320;color:#F5A623;"
                    f"padding:1px 6px;border-radius:4px;font-size:9px;font-weight:700'>펀드</span></div></div>"
                    f"<div style='text-align:right;color:#4C9EEB;font-weight:700;"
                    f"font-family:JetBrains Mono,monospace'>{target_pct}%</div>"
                    f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                    f"font-family:JetBrains Mono,monospace'>{target_amt:,.0f}</div>"
                    f"<div style='text-align:right;color:#3A4560;font-size:11px'>-</div>"
                    f"<div style='text-align:right;color:#3A4560;font-size:11px'>-</div>"
                    f"</div>", unsafe_allow_html=True)
            else:
                cp = core_prices.get(ticker, 0)
                tq = int(target_amt / cp) if cp > 0 else 0
                st.markdown(
                    f"<div style='display:grid;grid-template-columns:2.5fr 0.8fr 1.2fr 1fr 1fr;"
                    f"background:#111520;padding:10px 14px;{br};"
                    f"border:1px solid #1A2030;border-top:none;align-items:center'>"
                    f"<div><div style='font-size:13px;font-weight:600;color:#C8D0E0'>{info['name']}</div>"
                    f"<div style='color:#3A4560;font-size:10px;font-family:JetBrains Mono,monospace;margin-top:1px'>{ticker}</div></div>"
                    f"<div style='text-align:right;color:#4C9EEB;font-size:14px;font-weight:700;"
                    f"font-family:JetBrains Mono,monospace'>{target_pct}%</div>"
                    f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                    f"font-family:JetBrains Mono,monospace'>{target_amt:,.0f}</div>"
                    f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                    f"font-family:JetBrains Mono,monospace'>{cp:,.0f}</div>"
                    f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                    f"font-family:JetBrains Mono,monospace'>{tq:,}주</div>"
                    f"</div>", unsafe_allow_html=True)

    # Core 리밸런싱
    st.markdown("<hr class='divider-line'>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>Core 리밸런싱</div>", unsafe_allow_html=True)
    st.caption("현재 보유 수량 vs 목표 수량 비교 → 매수/매도 제안")

    if st.button("📊 리밸런싱 계산", use_container_width=True, key="core_rebal_calc"):
        st.session_state["core_rebal_show"] = True

    if st.session_state.get("core_rebal_show"):
        rebal_actions = []
        for ticker, info in targets.items():
            if info.get("is_fund"):
                continue
            target_pct = info["target_pct"]
            target_amt = core_total * target_pct / 100
            current_price = core_prices.get(ticker, 0)
            if current_price <= 0:
                continue
            target_qty = int(target_amt / current_price)

            # 현재 보유 수량 조회
            try:
                config = load_kis_config(is_paper=is_paper)
                adapter = KISAdapter(
                    app_key=config.app_key,
                    app_secret=config.app_secret,
                    account_no=config.account_no,
                    is_paper=config.is_paper,
                )
                portfolio_data = adapter.get_portfolio(role_map=ROLE_MAP)
                current_qty = 0
                for pos in portfolio_data.positions:
                    if pos.asset.ticker == ticker:
                        current_qty = int(pos.quantity)
                        break
            except Exception:
                current_qty = 0

            diff_qty = target_qty - current_qty
            if diff_qty == 0:
                continue

            # 허용밴드 체크
            band_pct = core.get("band_pct", 2.0)
            min_order_amount = core.get("min_order_amount", 100000)
            current_pct = (current_qty * current_price / core_total * 100) if core_total > 0 else 0
            lower_band = target_pct - band_pct
            upper_band = target_pct + band_pct
            amt = abs(diff_qty) * current_price

            # 허용밴드 내이거나 최소 주문금액 미만이면 스킵
            if lower_band <= current_pct <= upper_band:
                continue
            if amt < min_order_amount:
                continue

            action = "BUY" if diff_qty > 0 else "SELL"
            color = "#00C896" if action == "BUY" else "#E74C3C"

            rebal_actions.append({
                "ticker": ticker,
                "name": info["name"],
                "action": action,
                "current_qty": current_qty,
                "target_qty": target_qty,
                "diff_qty": abs(diff_qty),
                "price": current_price,
                "amount": amt,
                "color": color,
                "current_pct": round(current_pct, 1),
                "lower_band": lower_band,
                "upper_band": upper_band,
            })

        if not rebal_actions:
            st.success("✅ 리밸런싱 불필요! 모든 종목이 목표 수량입니다.")
        else:
            st.session_state["core_rebal_actions"] = rebal_actions

    if st.session_state.get("core_rebal_actions"):
        rebal_list = st.session_state["core_rebal_actions"]
        
        # 전체 요약
        total_buy = sum(a["amount"] for a in rebal_list if a["action"] == "BUY")
        total_sell = sum(a["amount"] for a in rebal_list if a["action"] == "SELL")
        st.info(f"📋 총 {len(rebal_list)}종목 | 매수 {total_buy:,.0f}원 | 매도 {total_sell:,.0f}원")

        # 전체 일괄 실행 버튼
        if st.button("🚀 전체 일괄 실행", type="primary", use_container_width=True, key="cr_bulk"):
            st.session_state["cr_bulk_confirm"] = True

        if st.session_state.get("cr_bulk_confirm"):
            st.warning(f"⚠️ 정말 {len(rebal_list)}종목 전체 주문하시겠습니까?")
            col_bulk_yes, col_bulk_no = st.columns(2)
            with col_bulk_yes:
                if st.button("🔴 전체 일괄 확인 - 실행", type="primary",
                             use_container_width=True, key="cr_bulk_final"):
                    config = load_kis_config(is_paper=is_paper)
                    adapter = KISAdapter(
                        app_key=config.app_key,
                        app_secret=config.app_secret,
                        account_no=config.account_no,
                        is_paper=config.is_paper,
                    )
                    success_list, fail_list = [], []
                    progress = st.progress(0, text="일괄 주문 중...")
                    for i, a in enumerate(rebal_list):
                        try:
                            asset = Asset(
                                ticker=a["ticker"], name=a["name"],
                                market=Market.KR, asset_type=AssetType.STOCK,
                                currency=Currency.KRW, exchange=Exchange.KRX,
                                candidate_roles=[AssetRole.CORE],
                            )
                            if a["action"] == "BUY":
                                adapter.place_buy_order(asset=asset, quantity=Decimal(str(a["diff_qty"])))
                            else:
                                adapter.place_sell_order(asset=asset, quantity=Decimal(str(a["diff_qty"])))
                            success_list.append(a["name"])
                        except Exception as e:
                            fail_list.append(f"{a['name']}: {e}")
                        progress.progress(int((i+1)/len(rebal_list)*100),
                                          text=f"{a['name']} 주문 중... ({i+1}/{len(rebal_list)})")
                    progress.empty()
                    buckets["core"]["last_rebalance"] = str(date.today())
                    save_buckets(buckets)
                    if success_list:
                        st.success(f"✅ 완료: {', '.join(success_list)}")
                    if fail_list:
                        for fail_msg in fail_list:
                            st.error(f"❌ 실패: {fail_msg}")
                    st.session_state["cr_bulk_confirm"] = None
                    st.session_state["core_rebal_actions"] = None
                    st.cache_data.clear()
            with col_bulk_no:
                if st.button("취소", key="cr_bulk_no", use_container_width=True):
                    st.session_state["cr_bulk_confirm"] = None

        # 수정
        st.markdown("---")
        if st.session_state.get("core_rebal_actions"):
            for idx, a in enumerate(st.session_state["core_rebal_actions"]):
                st.markdown(
                    f"<div style='background:#1E2130; border-radius:10px; padding:12px; "
                    f"border:1px solid #2D3250; margin-bottom:6px'>"
                    f"<div style='display:flex; justify-content:space-between'>"
                    f"<span><strong>{a['name']}</strong> "
                    f"<code style='font-size:11px; color:#8B9AB0'>{a['ticker']}</code></span>"
                    f"<span style='color:{a['color']}; font-weight:700'>{a['action']} {a['diff_qty']}주</span>"
                    f"</div>"
                    f"<div style='color:#8B9AB0; font-size:12px; margin-top:4px'>"
                    f"현재 {a['current_qty']}주 ({a.get('current_pct', 0):.1f}%) → "
                    f"목표 {a['target_qty']}주 ({a['price'] * a['target_qty'] / core_total * 100:.1f}%) | "
                    f"허용밴드 {a.get('lower_band', 0):.1f}%~{a.get('upper_band', 0):.1f}% | "
                    f"현재가 {a['price']:,.0f}원 | 예상금액 {a['amount']:,.0f}원"
                    f"</div></div>",
                    unsafe_allow_html=True,
                )

            cr_key = f"core_rebal_{idx}"

            # 수량 조정 슬라이더
            max_qty = max(a["diff_qty"] * 2, 1)
            adjusted_qty = st.slider(
                f"{a['name']} 주문 수량 조정",
                min_value=1,
                max_value=int(max_qty),
                value=int(a["diff_qty"]),
                key=f"cr_qty_{cr_key}",
            )
            adjusted_amount = adjusted_qty * a["price"]
            st.caption(f"조정 금액: {adjusted_amount:,.0f}원 (원래 {a['diff_qty']}주 → {adjusted_qty}주)")

            if st.button(f"✅ {a['name']} {a['action']} 승인",
                         key=f"cr_approve_{cr_key}", use_container_width=True):
                st.session_state[f"cr_confirm_{cr_key}"] = True

            if st.session_state.get(f"cr_confirm_{cr_key}"):
                st.warning(
                    f"⚠️ 정말 실행? **{a['action']} {a['name']}** | "
                    f"{adjusted_qty}주 | {adjusted_amount:,.0f}원"
                )
                col_yes, col_no = st.columns(2)
                with col_yes:
                    if st.button("🔴 최종 확인 - 실행",
                                 key=f"cr_final_{cr_key}",
                                 type="primary", use_container_width=True):
                        try:
                            config = load_kis_config(is_paper=is_paper)
                            adapter = KISAdapter(
                                app_key=config.app_key,
                                app_secret=config.app_secret,
                                account_no=config.account_no,
                                is_paper=config.is_paper,
                            )
                            asset = Asset(
                                ticker=a["ticker"], name=a["name"],
                                market=Market.KR, asset_type=AssetType.STOCK,
                                currency=Currency.KRW, exchange=Exchange.KRX,
                                candidate_roles=[AssetRole.CORE],
                            )
                            if a["action"] == "BUY":
                                order_id = adapter.place_buy_order(
                                    asset=asset, quantity=Decimal(str(adjusted_qty))
                                )
                            else:
                                order_id = adapter.place_sell_order(
                                    asset=asset, quantity=Decimal(str(adjusted_qty))
                                )
                            buckets["core"]["last_rebalance"] = str(date.today())
                            save_buckets(buckets)
                            st.success(f"✅ {a['name']} {a['action']} 완료!")
                            st.session_state[f"cr_confirm_{cr_key}"] = None
                            st.session_state["core_rebal_actions"] = None
                            st.session_state["core_rebal_show"] = False
                            st.cache_data.clear()
                        except Exception as e:
                            st.error(f"주문 실패: {e}")
                with col_no:
                    if st.button("취소", key=f"cr_no_{cr_key}",
                                 use_container_width=True):
                        st.session_state[f"cr_confirm_{cr_key}"] = None
            st.markdown("---")

    st.markdown("---")

    # 자금 투입/인출
    st.markdown("#### 💰 자금 관리")
    col_in, col_out = st.columns(2)
    with col_in:
        st.markdown("**➕ 자금 투입**")
        add_amount = st.number_input(
            "투입 금액 (원)", min_value=0, value=0, step=100000,
            key="core_add_amount"
        )
        if st.button("➕ Core 투입 실행", use_container_width=True, key="core_add_btn"):
            if add_amount > 0:
                buckets["core"]["initial_total"] = core_total + add_amount
                buckets["transfers"].append({
                    "date": str(date.today()),
                    "bucket": "core",
                    "type": "deposit",
                    "amount": add_amount,
                })
                save_buckets(buckets)
                st.success(f"✅ {add_amount:,.0f}원 투입 완료!")
                st.rerun()
            else:
                st.warning("금액을 입력하세요.")

    with col_out:
        st.markdown("**➖ 자금 인출**")
        withdraw_amount = st.number_input(
            "인출 금액 (원)", min_value=0, value=0, step=100000,
            key="core_withdraw_amount"
        )
        if st.button("➖ Core 인출 실행", use_container_width=True, key="core_withdraw_btn"):
            if withdraw_amount > 0 and withdraw_amount <= core_total:
                st.session_state["core_withdraw_confirm"] = True
            elif withdraw_amount > core_total:
                st.error("인출 금액이 총액을 초과합니다.")
            else:
                st.warning("금액을 입력하세요.")

        if st.session_state.get("core_withdraw_confirm"):
            st.warning(f"⚠️ {withdraw_amount:,.0f}원 인출하시겠습니까?")
            col_yes, col_no = st.columns(2)
            with col_yes:
                if st.button("🔴 인출 확정", key="core_withdraw_yes",
                             type="primary", use_container_width=True):
                    buckets["core"]["initial_total"] = core_total - withdraw_amount
                    buckets["transfers"].append({
                        "date": str(date.today()),
                        "bucket": "core",
                        "type": "withdraw",
                        "amount": withdraw_amount,
                    })
                    save_buckets(buckets)
                    st.success(f"✅ {withdraw_amount:,.0f}원 인출 완료!")
                    st.session_state["core_withdraw_confirm"] = False
                    st.rerun()
            with col_no:
                if st.button("취소", key="core_withdraw_no", use_container_width=True):
                    st.session_state["core_withdraw_confirm"] = False

    # 자금 이동 내역
    transfers = [t for t in buckets.get("transfers", []) if t["bucket"] == "core"]
    if transfers:
        st.markdown("---")
        st.markdown("#### 📋 자금 이동 내역")
        for t in reversed(transfers[-10:]):
            icon = "➕" if t["type"] == "deposit" else "➖"
            color = "#00C896" if t["type"] == "deposit" else "#E74C3C"
            st.markdown(
                f"<div style='color:{color}; font-size:13px'>"
                f"{icon} {t['date']} | {t['amount']:,.0f} KRW</div>",
                unsafe_allow_html=True,
            )


# ── TAB Satellite ──────────────────────────────────────────────────────────────
with tab_satellite:
    buckets = load_buckets()
    satellite = buckets.get("satellite", {})
    sat_total = satellite.get("initial_total", 0)
    sat_holdings = satellite.get("holdings", {})
    sat_last_rebalance = satellite.get("last_rebalance", "미실행")
    sat_tickers = set(sat_holdings.keys())

    # 포트폴리오 구성 규칙 로드
    rules = satellite.get("rules", {})
    max_stocks = rules.get("max_stocks", 20)
    max_single_pct = rules.get("max_single_pct", 5.0)
    max_sector_pct = rules.get("max_sector_pct", 25.0)
    min_entry_score = rules.get("min_entry_score", 70.0)
    min_hold_score = rules.get("min_hold_score", 60.0)
    min_cash_pct = rules.get("min_cash_pct", 5.0)

    # KIS 잔고 기준 Satellite 종목 필터링
    sat_positions = [p for p in portfolio.positions if p.asset.ticker in sat_tickers]

    # Satellite 합산 계산
    sat_eval = Decimal("0")
    sat_cost = Decimal("0")
    sat_pnl  = Decimal("0")
    for pos in sat_positions:
        if pos.asset.ticker in prices:
            p_obj = prices[pos.asset.ticker]
            sat_eval += pos.market_value(p_obj).amount
            sat_cost += pos.cost_basis().amount
            sat_pnl  += pos.unrealized_pnl(p_obj).amount

    sat_pnl_rate = float(sat_pnl / sat_cost * 100) if sat_cost > 0 else 0
    s_color = "#00C896" if sat_pnl >= 0 else "#FF4E6A"
    s_sign  = "+" if sat_pnl >= 0 else ""

    # ── 상단 요약 ──
    st.markdown(
        f"<div style='background:linear-gradient(135deg,#111520,#161C2A);border-radius:14px;"
        f"padding:18px 22px;border:1px solid #1E2535;margin-bottom:14px'>"
        f"<div style='color:#4A5470;font-size:10px;font-weight:700;letter-spacing:0.1em;"
        f"text-transform:uppercase;margin-bottom:6px'>Satellite 버킷 평가손익</div>"
        f"<div style='display:flex;align-items:baseline;gap:12px;margin-bottom:14px'>"
        f"<span style='color:{s_color};font-size:28px;font-weight:700;"
        f"font-family:JetBrains Mono,monospace'>{s_sign}{float(sat_pnl):,.0f}</span>"
        f"<span style='color:{s_color};font-size:16px;font-weight:700'>"
        f"{s_sign}{sat_pnl_rate:.2f}%</span></div>"
        f"<div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:16px'>"
        f"<div><div style='color:#4A5470;font-size:10px;margin-bottom:3px'>평가금액</div>"
        f"<div style='color:#C8D0E0;font-size:14px;font-weight:600;"
        f"font-family:JetBrains Mono,monospace'>{float(sat_eval):,.0f}</div></div>"
        f"<div><div style='color:#4A5470;font-size:10px;margin-bottom:3px'>매입금액</div>"
        f"<div style='color:#C8D0E0;font-size:14px;font-weight:600;"
        f"font-family:JetBrains Mono,monospace'>{float(sat_cost):,.0f}</div></div>"
        f"<div><div style='color:#4A5470;font-size:10px;margin-bottom:3px'>보유 종목</div>"
        f"<div style='color:#C8D0E0;font-size:14px;font-weight:600'>"
        f"{len(sat_positions)}개 / 최대 {max_stocks}개</div></div>"
        f"<div><div style='color:#4A5470;font-size:10px;margin-bottom:3px'>마지막 리밸런싱</div>"
        f"<div style='color:#C8D0E0;font-size:12px;font-weight:600'>{sat_last_rebalance or '미실행'}</div></div>"
        f"</div></div>",
        unsafe_allow_html=True,
    )

    # 규칙 설정 UI
    with st.expander("⚙️ 포트폴리오 구성 규칙 설정", expanded=False):
        st.caption("변경 후 저장 버튼을 누르세요.")
        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            new_max_stocks = st.slider("최대 종목 수", 10, 30, max_stocks, key="rule_max_stocks")
            new_min_entry = st.slider("신규 편입 최소 점수", 60, 85, int(min_entry_score), key="rule_min_entry")
        with col_r2:
            new_max_single = st.slider("종목당 최대 비중 (%)", 3, 15, int(max_single_pct), key="rule_max_single")
            new_min_hold = st.slider("보유 유지 최소 점수", 50, 75, int(min_hold_score), key="rule_min_hold")
        with col_r3:
            new_max_sector = st.slider("섹터 최대 비중 (%)", 15, 50, int(max_sector_pct), key="rule_max_sector")
            new_min_cash = st.slider("현금 최소 비중 (%)", 0, 20, int(min_cash_pct), key="rule_min_cash")

        if st.button("💾 규칙 저장", use_container_width=True, key="save_rules"):
            buckets["satellite"]["rules"] = {
                "max_stocks": new_max_stocks,
                "max_single_pct": float(new_max_single),
                "max_sector_pct": float(new_max_sector),
                "min_entry_score": float(new_min_entry),
                "min_hold_score": float(new_min_hold),
                "min_cash_pct": float(new_min_cash),
            }
            save_buckets(buckets)
            st.success("✅ 규칙 저장 완료!")
            st.rerun()

    st.markdown("<hr class='divider-line'>", unsafe_allow_html=True)

    # 포트폴리오 규칙 위반 경보
    violations = []
    if len(sat_holdings) > max_stocks:
        violations.append(f"⚠️ 종목 수 초과: {len(sat_holdings)}개 (한도 {max_stocks}개)")
    for ticker, holding in sat_holdings.items():
        if holding.get("total_score", 100) < min_hold_score:
            violations.append(f"⚠️ {holding.get('name', ticker)}: 점수 {holding.get('total_score', 0):.0f}점 (유지기준 {min_hold_score:.0f}점)")
    if violations:
        for v in violations:
            st.warning(v)

    # ── 실제 보유 현황 테이블 (KIS 잔고 기준 + buckets 메타데이터) ──
    st.markdown("<div class='section-header'>보유 종목 현황</div>", unsafe_allow_html=True)
    if sat_positions:
        st.markdown(
            "<div style='display:grid;grid-template-columns:2fr 1.1fr 0.7fr 1fr 1fr 1.1fr 0.8fr;"
            "background:#0F1320;border-radius:8px 8px 0 0;padding:7px 14px;border:1px solid #1A2030'>"
            "<div class='lbl'>종목명</div>"
            "<div class='lbl' style='text-align:right'>평가손익</div>"
            "<div class='lbl' style='text-align:right'>보유</div>"
            "<div class='lbl' style='text-align:right'>매입단가</div>"
            "<div class='lbl' style='text-align:right'>현재가</div>"
            "<div class='lbl' style='text-align:right'>평가금액</div>"
            "<div class='lbl' style='text-align:center'>상태/매도</div>"
            "</div>",
            unsafe_allow_html=True,
        )
        for i, pos in enumerate(sat_positions):
            tk = pos.asset.ticker
            if tk not in prices:
                continue
            p_obj   = prices[tk]
            pnl_pos = pos.unrealized_pnl(p_obj)
            cost_p  = pos.cost_basis()
            val_pos = pos.market_value(p_obj)
            avg_p   = float(cost_p.amount / pos.quantity) if pos.quantity > 0 else 0
            pnl_r   = float(pnl_pos.amount / cost_p.amount * 100) if cost_p.amount > 0 else 0
            pc = "#00C896" if pnl_r >= 0 else "#FF4E6A"
            ps = "+" if pnl_r >= 0 else ""
            meta        = sat_holdings.get(tk, {})
            entry_score = meta.get("entry_score", 0)
            total_score = meta.get("total_score", 0)
            momentum    = meta.get("momentum_score", 0)
            score_drop  = entry_score - total_score
            thesis_break = momentum < 40 or total_score < min_hold_score or score_drop >= 15
            if thesis_break:
                status_txt   = "🔴매도검토"
                status_color = "#FF4E6A"
                row_bg = "#130D10"
            elif score_drop >= 10:
                status_txt   = "⚠️하락주의"
                status_color = "#F5A623"
                row_bg = "#131208"
            else:
                status_txt   = "✅유지"
                status_color = "#00C896"
                row_bg = "#111520"

            br = "border-radius:0 0 8px 8px" if i == len(sat_positions)-1 else "border-radius:0"
            col_row, col_btn = st.columns([11, 1])
            with col_row:
                st.markdown(
                    f"<div style='display:grid;grid-template-columns:2fr 1.1fr 0.7fr 1fr 1fr 1.1fr 0.8fr;"
                    f"background:{row_bg};padding:10px 14px;{br};"
                    f"border:1px solid #1A2030;border-top:none;align-items:center'>"
                    f"<div><div style='font-size:13px;font-weight:600;color:#C8D0E0'>{pos.asset.name}</div>"
                    f"<div style='color:#3A4560;font-size:10px;font-family:JetBrains Mono,monospace;margin-top:1px'>"
                    f"{tk} · 편입 {meta.get('entry_date','')}</div></div>"
                    f"<div style='text-align:right'>"
                    f"<div style='color:{pc};font-size:12px;font-weight:700;font-family:JetBrains Mono,monospace'>{ps}{pnl_r:.2f}%</div>"
                    f"<div style='color:{pc};font-size:10px;opacity:0.8'>{ps}{float(pnl_pos.amount):,.0f}</div></div>"
                    f"<div style='text-align:right;color:#C8D0E0;font-size:13px;font-weight:600;"
                    f"font-family:JetBrains Mono,monospace'>{int(pos.quantity):,}주</div>"
                    f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                    f"font-family:JetBrains Mono,monospace'>{avg_p:,.0f}</div>"
                    f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                    f"font-family:JetBrains Mono,monospace'>{float(p_obj.amount):,.0f}</div>"
                    f"<div style='text-align:right;color:#C8D0E0;font-size:12px;"
                    f"font-family:JetBrains Mono,monospace'>{float(val_pos.amount):,.0f}</div>"
                    f"<div style='text-align:center'>"
                    f"<span style='color:{status_color};font-size:10px;font-weight:700'>{status_txt}</span></div>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
            with col_btn:
                if st.button("매도", key=f"sat_del_{tk}", use_container_width=True):
                    del sat_holdings[tk]
                    buckets["satellite"]["holdings"] = sat_holdings
                    save_buckets(buckets)
                    st.success(f"✅ {pos.asset.name} 매도됨!")
                    st.rerun()
    elif sat_holdings:
        st.info("KIS 잔고와 매칭되는 Satellite 종목이 없습니다. 잔고를 확인해 주세요.")
    else:
        st.info("보유 종목이 없습니다. 추천 엔진에서 편입하세요.")

    st.markdown("---")

    # Satellite 분기 교체

    st.markdown("#### 🔄 분기 교체 관리")
    if sat_holdings:
        # 하위 30% 매도 후보 계산
        sorted_holdings = sorted(
            sat_holdings.items(),
            key=lambda x: x[1].get("total_score", 0)
        )
        bottom_30_count = max(1, int(len(sorted_holdings) * 0.3))
        sell_candidates = sorted_holdings[:bottom_30_count]

        st.caption(f"보유 {len(sat_holdings)}종목 중 하위 30% → {bottom_30_count}종목 매도 후보")
        st.markdown("**📉 매도 후보 (하위 30%)**")

        for ticker, holding in sell_candidates:
            momentum = holding.get("momentum_score", 0)
            total_score = holding.get("total_score", 0)
            early_exit = momentum < 40

            status_color = "#E74C3C" if early_exit else "#F5A623"
            status_text = "⚠️ 조기매도" if early_exit else "🔄 교체 후보"

            st.markdown(
                f"<div style='background:#1E2130; border-radius:10px; padding:12px; "
                f"border:1px solid {status_color}40; margin-bottom:6px'>"
                f"<div style='display:flex; justify-content:space-between'>"
                f"<span><strong>{holding.get('name', ticker)}</strong> "
                f"<code style='font-size:11px; color:#8B9AB0'>{ticker}</code></span>"
                f"<span style='color:{status_color}; font-size:12px'>{status_text}</span>"
                f"</div>"
                f"<div style='color:#8B9AB0; font-size:12px; margin-top:4px'>"
                f"총점: {total_score}점 | 모멘텀: {momentum}점 | "
                f"편입일: {holding.get('entry_date', '-')}"
                f"</div></div>",
                unsafe_allow_html=True,
            )

            sc_key = f"sat_sell_{ticker}"
            if st.button(f"📉 {holding.get('name', ticker)} 매도 승인",
                         key=f"sc_btn_{sc_key}", use_container_width=True):
                st.session_state[f"sc_confirm_{sc_key}"] = True

            if st.session_state.get(f"sc_confirm_{sc_key}"):
                st.warning(f"⚠️ {holding.get('name', ticker)} 매도 후 Satellite에서 제거합니다.")
                col_yes, col_no = st.columns(2)
                with col_yes:
                    if st.button("🔴 매도 확정", key=f"sc_final_{sc_key}",
                                 type="primary", use_container_width=True):
                        try:
                            config = load_kis_config(is_paper=is_paper)
                            adapter = KISAdapter(
                                app_key=config.app_key,
                                app_secret=config.app_secret,
                                account_no=config.account_no,
                                is_paper=config.is_paper,
                            )
                            asset = Asset(
                                ticker=ticker,
                                name=holding.get("name", ticker),
                                market=Market.KR,
                                asset_type=AssetType.STOCK,
                                currency=Currency.KRW,
                                exchange=Exchange.KRX,
                                candidate_roles=[AssetRole.CORE],
                            )
                            portfolio_data = adapter.get_portfolio(role_map=ROLE_MAP)
                            sell_qty = 0
                            for pos in portfolio_data.positions:
                                if pos.asset.ticker == ticker:
                                    sell_qty = int(pos.quantity)
                                    break
                            if sell_qty > 0:
                                order_id = adapter.place_sell_order(
                                    asset=asset,
                                    quantity=Decimal(str(sell_qty))
                                )
                                st.success(f"✅ {holding.get('name', ticker)} 매도 완료!")
                            del sat_holdings[ticker]
                            buckets["satellite"]["holdings"] = sat_holdings
                            buckets["satellite"]["last_rebalance"] = str(date.today())
                            save_buckets(buckets)
                            st.session_state[f"sc_confirm_{sc_key}"] = None
                            st.cache_data.clear()
                            st.rerun()
                        except Exception as e:
                            st.error(f"매도 실패: {e}")
                with col_no:
                    if st.button("취소", key=f"sc_no_{sc_key}",
                                 use_container_width=True):
                        st.session_state[f"sc_confirm_{sc_key}"] = None
    else:
        st.info("보유 종목이 없어 분기 교체를 진행할 수 없습니다.")

    st.markdown("---")

    # 추천 엔진 BUY 종목 연동
    st.markdown("#### 🎯 편입 후보 (추천 엔진 BUY)")
    sat_mode = st.selectbox(
        "전략 모드", options=["🏛️ 버핏형", "⚖️ 균형형", "🚀 성장형"],
        key="sat_mode"
    )
    sat_candidates_data = load_buy_candidates_by_mode(sat_mode)
    if sat_candidates_data:
        candidates = sat_candidates_data.get("buy_candidates", [])
        # 이미 보유 중인 종목 제외
        new_candidates = [c for c in candidates if c["ticker"] not in sat_holdings]
        st.caption(f"신규 편입 가능: {len(new_candidates)}종목")
        for c in new_candidates[:10]:
            score = c["score"]
            # 규칙 검증
            rule_ok = True
            rule_msg = ""
            if score < min_entry_score:
                rule_ok = False
                rule_msg = f"점수 미달 ({score:.0f}점 < {min_entry_score:.0f}점)"
            elif len(sat_holdings) >= max_stocks:
                rule_ok = False
                rule_msg = f"종목 수 한도 초과 ({max_stocks}개)"

            col_info, col_btn = st.columns([4, 1])
            with col_info:
                score_color = "#00C896" if rule_ok else "#E74C3C"
                st.markdown(
                    f"**{c['name']}** `{c['ticker']}` | "
                    f"<span style='color:{score_color}'>총점 {score:.0f}점</span> | "
                    f"모멘텀 {c.get('momentum_score', 0):.0f}점"
                    + (f" | ⚠️ {rule_msg}" if not rule_ok else ""),
                    unsafe_allow_html=True,
                )
            with col_btn:
                # CorrelationGuard 검증
                corr_ok, corr_violation = default_guard.check_candidate(
                    candidate_ticker=c["ticker"],
                    candidate_name=c["name"],
                    candidate_sector=c.get("sector", ""),
                    current_holdings=sat_holdings,
                )
                if rule_ok and corr_ok:
                    if st.button("편입", key=f"sat_add_{c['ticker']}", use_container_width=True):
                        sat_holdings[c["ticker"]] = {
                            "name": c["name"],
                            "entry_date": str(date.today()),
                            "entry_score": score,
                            "total_score": score,
                            "momentum_score": c.get("momentum_score", 0),
                            "sector": c.get("sector", ""),
                        }
                        buckets["satellite"]["holdings"] = sat_holdings
                        save_buckets(buckets)
                        st.success(f"✅ {c['name']} 편입됨!")
                        st.rerun()
                elif not corr_ok:
                    st.button("⛔ 상관관계", key=f"sat_add_{c['ticker']}", use_container_width=True, disabled=True)
                    st.caption(f"⚠️ {corr_violation.reason[:40]}")
                else:
                    st.button("차단", key=f"sat_add_{c['ticker']}", use_container_width=True, disabled=True)
    else:
        st.info("추천 엔진을 먼저 실행하세요.")

    st.markdown("---")

    # 자금 투입/인출
    st.markdown("#### 💰 자금 관리")
    col_in, col_out = st.columns(2)
    with col_in:
        st.markdown("**➕ 자금 투입**")
        sat_add = st.number_input(
            "투입 금액 (원)", min_value=0, value=0, step=100000,
            key="sat_add_amount"
        )
        if st.button("➕ Satellite 투입", use_container_width=True, key="sat_add_btn"):
            if sat_add > 0:
                buckets["satellite"]["initial_total"] = sat_total + sat_add
                buckets["transfers"].append({
                    "date": str(date.today()),
                    "bucket": "satellite",
                    "type": "deposit",
                    "amount": sat_add,
                })
                save_buckets(buckets)
                st.success(f"✅ {sat_add:,.0f}원 투입 완료!")
                st.rerun()
            else:
                st.warning("금액을 입력하세요.")

    with col_out:
        st.markdown("**➖ 자금 인출**")
        sat_withdraw = st.number_input(
            "인출 금액 (원)", min_value=0, value=0, step=100000,
            key="sat_withdraw_amount"
        )
        if st.button("➖ Satellite 인출", use_container_width=True, key="sat_withdraw_btn"):
            if sat_withdraw > 0 and sat_withdraw <= sat_total:
                st.session_state["sat_withdraw_confirm"] = True
            elif sat_withdraw > sat_total:
                st.error("인출 금액이 총액을 초과합니다.")
            else:
                st.warning("금액을 입력하세요.")

        if st.session_state.get("sat_withdraw_confirm"):
            st.warning(f"⚠️ {sat_withdraw:,.0f}원 인출하시겠습니까?")
            col_yes, col_no = st.columns(2)
            with col_yes:
                if st.button("🔴 인출 확정", key="sat_withdraw_yes",
                             type="primary", use_container_width=True):
                    buckets["satellite"]["initial_total"] = sat_total - sat_withdraw
                    buckets["transfers"].append({
                        "date": str(date.today()),
                        "bucket": "satellite",
                        "type": "withdraw",
                        "amount": sat_withdraw,
                    })
                    save_buckets(buckets)
                    st.success(f"✅ {sat_withdraw:,.0f}원 인출 완료!")
                    st.session_state["sat_withdraw_confirm"] = False
                    st.rerun()
            with col_no:
                if st.button("취소", key="sat_withdraw_no", use_container_width=True):
                    st.session_state["sat_withdraw_confirm"] = False

    # 자금 이동 내역
    sat_transfers = [t for t in buckets.get("transfers", []) if t["bucket"] == "satellite"]
    if sat_transfers:
        st.markdown("---")
        st.markdown("#### 📋 자금 이동 내역")
        for t in reversed(sat_transfers[-10:]):
            icon = "➕" if t["type"] == "deposit" else "➖"
            color = "#00C896" if t["type"] == "deposit" else "#E74C3C"
            st.markdown(
                f"<div style='color:{color}; font-size:13px'>"
                f"{icon} {t['date']} | {t['amount']:,.0f} KRW</div>",
                unsafe_allow_html=True,
            )

# ── TAB 2: 포지션 ─────────────────────────────────────────────────────────────
with tab_positions:
    total_pnl = Decimal("0")
    for pos in portfolio.positions:
        if pos.asset.ticker in prices:
            total_pnl += pos.unrealized_pnl(prices[pos.asset.ticker]).amount

    pnl_color = "#00C896" if total_pnl >= 0 else "#E74C3C"
    pnl_sign = "+" if total_pnl >= 0 else ""
    st.markdown(
        f"**총 손익: <span style='color:{pnl_color}'>{pnl_sign}{total_pnl:,.0f} KRW</span>**",
        unsafe_allow_html=True,
    )
    st.markdown(f"**{len(portfolio.positions)}종목 보유**")
    st.markdown("---")

    for pos in portfolio.positions:
        ticker = pos.asset.ticker
        if ticker not in prices:
            continue
        price = prices[ticker]
        pnl = pos.unrealized_pnl(price)
        pnl_rate = pnl.amount / pos.cost_basis().amount * 100
        value = pos.market_value(price)
        role_color = ROLE_COLOR.get(pos.role.value, "#8B9AB0")
        pnl_color2 = "#00C896" if pnl_rate >= 0 else "#E74C3C"
        pnl_sign2 = "+" if pnl_rate >= 0 else ""

        st.markdown(
            f"<div style='background:#1E2130; border-radius:12px; padding:14px; "
            f"border:1px solid #2D3250; margin-bottom:10px'>"
            f"<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:6px'>"
            f"<span><span style='color:{role_color}'>■</span> "
            f"<strong>{pos.asset.name}</strong> "
            f"<code style='font-size:11px; color:#8B9AB0'>{ticker}</code></span>"
            f"<span style='background:{role_color}20; color:{role_color}; "
            f"padding:2px 8px; border-radius:10px; font-size:11px'>{pos.role.value}</span>"
            f"</div>"
            f"<div style='display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; font-size:13px'>"
            f"<div><div style='color:#8B9AB0; font-size:11px'>보유수량</div>"
            f"<div><strong>{pos.quantity:.0f}주</strong></div></div>"
            f"<div><div style='color:#8B9AB0; font-size:11px'>현재가</div>"
            f"<div><strong>{price}</strong></div></div>"
            f"<div><div style='color:#8B9AB0; font-size:11px'>평가액</div>"
            f"<div><strong>{value}</strong></div></div>"
            f"</div>"
            f"<div style='margin-top:8px; font-size:14px; font-weight:700; color:{pnl_color2}'>"
            f"{pnl_sign2}{pnl_rate:.1f}% &nbsp; ({pnl_sign2}{pnl.amount:,.0f} KRW)"
            f"</div></div>",
            unsafe_allow_html=True,
        )


# ── TAB 3: 리밸런싱 ───────────────────────────────────────────────────────────
with tab_rebalance:
    guard = create_safety_guard(is_paper=is_paper)

    if output.actions:
        st.info("💡 **Level 2 반자동**: 승인 → 이중 확인 → 실제 주문")
        st.markdown("---")

        for i, action in enumerate(output.actions):
            ok, reason = guard.check(action)
            icon = "📈" if action.is_buy() else "📉"
            color = "#00C896" if action.is_buy() else "#E74C3C"

            st.markdown(
                f"<div style='background:#1E2130; border-radius:12px; padding:14px; "
                f"border:1px solid #2D3250; margin-bottom:10px'>"
                f"<div style='font-size:16px; font-weight:700; margin-bottom:4px'>"
                f"{icon} {action.asset.name} "
                f"<span style='color:{color}; font-size:14px'>{action.action_type}</span></div>"
                f"<div style='color:#8B9AB0; font-size:12px; margin-bottom:4px'>"
                f"{action.current_weight*100:.1f}% → {action.target_weight*100:.1f}% "
                f"&nbsp;|&nbsp; {action.suggested_amount} | {action.suggested_quantity:.0f}주</div>"
                f"<div style='color:#8B9AB0; font-size:12px'>"
                f"이유: {action.reason} &nbsp;|&nbsp; 우선순위: {action.priority}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

            if not ok:
                st.markdown(f"🚫 **차단됨**: {reason}")
            else:
                col_approve, col_reject = st.columns(2)
                with col_approve:
                    if st.button("✅ 승인", key=f"approve_{i}",
                                 type="primary", use_container_width=True):
                        st.session_state[f"confirm_{i}"] = True
                with col_reject:
                    if st.button("❌ 거부", key=f"reject_{i}", use_container_width=True):
                        st.session_state[f"confirm_{i}"] = False
                        st.warning(f"{action.asset.name} 거부됨.")

            if st.session_state.get(f"confirm_{i}") is True:
                qty_str = f" | {action.suggested_quantity:.0f}주" if action.suggested_quantity else ""

                # 포트폴리오 변화 미리보기
                st.markdown("#### 📊 주문 전/후 포트폴리오 변화 미리보기")
                total_amount = float(total.amount)
                order_amount = float(action.suggested_amount.amount) if action.suggested_amount else 0
                order_pct = order_amount / total_amount * 100 if total_amount > 0 else 0

                # 현재 비중
                current_pct = float(action.current_weight * 100)
                # 주문 후 예상 비중
                if action.is_buy():
                    after_pct = current_pct + order_pct
                else:
                    after_pct = current_pct - order_pct

                # 예상 거래비용
                est_cost = order_amount * (TRANSACTION_COST + TAX_TRANSACTION)
                
                col_p1, col_p2, col_p3, col_p4 = st.columns(4)
                with col_p1:
                    st.metric("현재 비중", f"{current_pct:.1f}%")
                with col_p2:
                    delta = f"+{after_pct - current_pct:.1f}%" if action.is_buy() else f"{after_pct - current_pct:.1f}%"
                    st.metric("주문 후 비중", f"{after_pct:.1f}%", delta=delta)
                with col_p3:
                    st.metric("주문 금액", f"{order_amount:,.0f}원")
                with col_p4:
                    st.metric("예상 거래비용", f"{est_cost:,.0f}원")

                st.warning(
                    f"⚠️ 정말 실행? **{action.action_type}** "
                    f"{action.asset.name} | {action.suggested_amount}{qty_str}"
                )
                col_yes, col_no = st.columns(2)
                with col_yes:
                    if st.button("🔴 최종 확인 - 실행", key=f"final_yes_{i}",
                                 type="primary", use_container_width=True):
                        try:
                            config = load_kis_config(is_paper=is_paper)
                            adapter = KISAdapter(
                                app_key=config.app_key,
                                app_secret=config.app_secret,
                                account_no=config.account_no,
                                is_paper=config.is_paper,
                            )
                            if action.is_buy():
                                order_id = adapter.place_buy_order(
                                    asset=action.asset,
                                    quantity=action.suggested_quantity or Decimal("1"),
                                )
                            else:
                                order_id = adapter.place_sell_order(
                                    asset=action.asset,
                                    quantity=action.suggested_quantity or Decimal("1"),
                                )
                            guard.record_order(action)
                            st.session_state[f"confirm_{i}"] = None
                            st.success(f"✅ 주문 완료! {order_id or '체결 확인 중'}")
                            st.cache_data.clear()
                        except Exception as e:
                            st.error(f"주문 실패: {e}")
                with col_no:
                    if st.button("취소", key=f"final_no_{i}", use_container_width=True):
                        st.session_state[f"confirm_{i}"] = None

            st.markdown("---")
    else:
        st.success("✅ 리밸런싱 불필요.")


# ── TAB 4: 종목 분석 ──────────────────────────────────────────────────────────
with tab_analysis:
    st.caption("TTM + 10년 추세 기반 | DART 재무데이터 + yfinance | 24시간 캐시")

    if st.button("🔄 스코어 갱신", use_container_width=True, key="refresh_score"):
        invalidate_all_cache()
        st.rerun()

    st.markdown("---")

    for pos in portfolio.positions:
        ticker = pos.asset.ticker
        corp_code = DART_CORP_CODES.get(ticker)

        if not corp_code:
            st.caption(f"  {pos.asset.name}: ETF/펀드는 스코어링 미지원")
            continue

        with st.spinner(f"{pos.asset.name} 분석 중..."):
            try:
                result = get_or_fetch_score(
                    ticker=ticker,
                    name=pos.asset.name,
                    fetch_fn=lambda t=ticker, n=pos.asset.name, cc=corp_code: fetch_score_for(t, n, cc),
                )

                decision_color = {
                    "BUY": "#00C896", "WATCH": "#F5A623", "AVOID": "#E74C3C",
                }.get(result.decision, "#8B9AB0")
                role_color = ROLE_COLOR.get(pos.role.value, "#8B9AB0")
                bar_width = int(result.total_score)

                st.markdown(
                    f"<div style='background:#1E2130; border-radius:12px; padding:14px; "
                    f"border:1px solid #2D3250; margin-bottom:6px'>"
                    f"<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:8px'>"
                    f"<span><span style='color:{role_color}'>■</span> "
                    f"<strong>{result.name}</strong> "
                    f"<code style='font-size:11px; color:#8B9AB0'>{ticker}</code></span>"
                    f"<span style='background:{decision_color}30; color:{decision_color}; "
                    f"padding:3px 10px; border-radius:10px; font-size:13px; font-weight:700'>"
                    f"{result.decision} {result.total_score:.0f}점</span>"
                    f"</div>"
                    f"<div style='background:#2D3250; border-radius:4px; height:5px; margin-bottom:10px'>"
                    f"<div style='background:{decision_color}; width:{bar_width}%; "
                    f"height:5px; border-radius:4px'></div></div>"
                    f"<div style='display:grid; grid-template-columns:repeat(5,1fr); gap:6px; text-align:center'>"
                    f"<div><div style='color:#8B9AB0; font-size:10px'>우량성</div>"
                    f"<div style='font-size:15px; font-weight:700'>{result.quality_score:.0f}</div></div>"
                    f"<div><div style='color:#8B9AB0; font-size:10px'>밸류</div>"
                    f"<div style='font-size:15px; font-weight:700'>{result.valuation_score:.0f}</div></div>"
                    f"<div><div style='color:#8B9AB0; font-size:10px'>배당</div>"
                    f"<div style='font-size:15px; font-weight:700'>{result.dividend_score:.0f}</div></div>"
                    f"<div><div style='color:#8B9AB0; font-size:10px'>성장</div>"
                    f"<div style='font-size:15px; font-weight:700'>{result.growth_score:.0f}</div></div>"
                    f"<div><div style='color:#8B9AB0; font-size:10px'>리스크</div>"
                    f"<div style='font-size:15px; font-weight:700'>{result.risk_score:.0f}</div></div>"
                    f"</div>"
                    f"{'<div style=margin-top:6px;font-size:11px;color:#8B9AB0>' + result.data_label + '</div>' if hasattr(result, 'data_label') and result.data_label else ''}"
                    f"</div>",
                    unsafe_allow_html=True,
                )

                if result.reasons or result.warnings:
                    with st.expander("상세 분석 보기"):
                        if result.reasons:
                            st.markdown("**긍정 요인:**")
                            for r in result.reasons:
                                st.markdown(f"  ✅ {r}")
                        if result.warnings:
                            st.markdown("**주의 요인:**")
                            for w in result.warnings:
                                st.markdown(f"  ⚠️ {w}")

                st.markdown("---")

            except Exception as e:
                st.warning(f"{pos.asset.name} 분석 실패: {e}")


# ── TAB 5: 추천 후보 ──────────────────────────────────────────────────────────
with tab_recommend:
    st.markdown("### 🎯 추천 편입 후보")
    st.info("💡 각 전략 모드별 BUY 종목입니다. 추천 엔진을 먼저 실행하세요.")
    st.caption("streamlit run recommend.py --server.port 8502")

    # 백테스트 리포트 표시
    REPORT_PATH = Path("cache/backtest_report.json")
    if REPORT_PATH.exists():
        try:
            with open(REPORT_PATH, "r", encoding="utf-8") as f:
                report = json.load(f)
            st.markdown("#### 📊 추천 전략 백테스트 리포트")
            col1, col2, col3 = st.columns(3)
            for i, (mode_file, mode_label) in enumerate([
                ("buffett", "🏛️ 버핏형"), ("balanced", "⚖️ 균형형"), ("growth", "🚀 성장형")
            ]):
                d = report.get(mode_file, {})
                if not d:
                    continue
                with [col1, col2, col3][i]:
                    cagr_color = "#00C896" if d.get("avg_cagr", 0) > 0 else "#E74C3C"
                    st.markdown(
                        f"<div style='background:#1E2130; border-radius:10px; padding:12px; "
                        f"border:1px solid #2D3250; text-align:center'>"
                        f"<div style='font-size:14px; font-weight:700; margin-bottom:8px'>{mode_label}</div>"
                        f"<div style='color:{cagr_color}; font-size:20px; font-weight:700'>"
                        f"{d.get('avg_cagr', 0):.1f}%</div>"
                        f"<div style='color:#8B9AB0; font-size:11px'>평균 CAGR</div>"
                        f"<div style='margin-top:6px; font-size:12px'>"
                        f"MDD {d.get('avg_mdd', 0):.1f}% | "
                        f"Sharpe {d.get('avg_sharpe', 0):.2f} | "
                        f"승률 {d.get('win_rate', 0):.0f}%</div>"
                        f"<div style='color:#8B9AB0; font-size:10px; margin-top:4px'>"
                        f"{d.get('period', '')} | {d.get('generated_at', '')}</div>"
                        f"</div>",
                        unsafe_allow_html=True,
                    )
        except Exception:
            pass

    st.markdown("---")

    mode_tab1, mode_tab2, mode_tab3 = st.tabs(["🏛️ 버핏형", "⚖️ 균형형", "🚀 성장형"])

    def render_candidate_tab(mode_name, tab):
        with tab:
            data_rc = load_buy_candidates_by_mode(mode_name)
            if not data_rc:
                st.info(f"{mode_name} 추천 데이터가 없습니다.")
                st.code("streamlit run recommend.py --server.port 8502", language="bash")
                return

            generated_at = data_rc.get("generated_at", "")
            candidates = data_rc.get("buy_candidates", [])
            st.markdown(f"*실행: {generated_at} | BUY {len(candidates)}종목*")
            st.markdown("---")

            if not candidates:
                st.warning(f"{mode_name} BUY 후보가 없습니다.")
                return

            for idx, c in enumerate(candidates):
                color = "#00C896"
                score = c.get("score", 0)
                bar_width = int(score)
                market_badge = "🔵 코스피" if c.get("market") == "KOSPI" else "🟠 코스닥"
                per_str = f"{c['per']:.1f}배" if c.get("per") else "-"
                pbr_str = f"{c['pbr']:.1f}배" if c.get("pbr") else "-"
                roe_str = f"{c['roe']*100:.1f}%" if c.get("roe") else "-"
                div_str = f"{c['dividend_yield']*100:.1f}%" if c.get("dividend_yield") else "-"

                st.markdown(
                    f"<div style='background:#1E2130; border-radius:14px; padding:16px; "
                    f"border:1px solid #2D3250; margin-bottom:8px'>"
                    f"<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:6px'>"
                    f"<span style='font-size:16px; font-weight:700'>"
                    f"{c['name']} "
                    f"<code style='font-size:11px; color:#8B9AB0'>{c['ticker']}</code> "
                    f"<span style='font-size:11px; color:#8B9AB0'>{market_badge}</span>"
                    f"</span>"
                    f"<span style='background:{color}30; color:{color}; padding:3px 12px; "
                    f"border-radius:10px; font-size:14px; font-weight:700'>"
                    f"BUY {score:.0f}점</span>"
                    f"</div>"
                    f"<div style='background:#2D3250; border-radius:8px; padding:7px 12px; "
                    f"margin-bottom:8px; font-size:12px; color:#FFFFFF'>💡 {c.get('reason', '')}</div>"
                    f"<div style='background:#0E1117; border-radius:4px; height:4px; margin-bottom:10px'>"
                    f"<div style='background:{color}; width:{bar_width}%; height:4px; border-radius:4px'></div>"
                    f"</div>"
                    f"<div style='display:grid; grid-template-columns:repeat(5,1fr); gap:6px; "
                    f"text-align:center; margin-bottom:8px'>"
                    f"<div style='background:#0E1117; border-radius:6px; padding:6px'>"
                    f"<div style='color:#8B9AB0; font-size:10px'>우량성</div>"
                    f"<div style='font-size:13px; font-weight:700; color:#00C896'>{c.get('quality_score', 0):.0f}</div></div>"
                    f"<div style='background:#0E1117; border-radius:6px; padding:6px'>"
                    f"<div style='color:#8B9AB0; font-size:10px'>밸류</div>"
                    f"<div style='font-size:13px; font-weight:700; color:#4C9EEB'>{c.get('valuation_score', 0):.0f}</div></div>"
                    f"<div style='background:#0E1117; border-radius:6px; padding:6px'>"
                    f"<div style='color:#8B9AB0; font-size:10px'>성장</div>"
                    f"<div style='font-size:13px; font-weight:700; color:#9B59B6'>{c.get('growth_score', 0):.0f}</div></div>"
                    f"<div style='background:#0E1117; border-radius:6px; padding:6px'>"
                    f"<div style='color:#8B9AB0; font-size:10px'>모멘텀</div>"
                    f"<div style='font-size:13px; font-weight:700; color:#F5A623'>{c.get('momentum_score', 0):.0f}</div></div>"
                    f"<div style='background:#0E1117; border-radius:6px; padding:6px'>"
                    f"<div style='color:#8B9AB0; font-size:10px'>안정성</div>"
                    f"<div style='font-size:13px; font-weight:700; color:#00C896'>{c.get('stability_score', 0):.0f}</div></div>"
                    f"</div>"
                    f"<div style='display:grid; grid-template-columns:repeat(4,1fr); gap:6px; "
                    f"font-size:11px; color:#8B9AB0'>"
                    f"<div>ROE: <strong style='color:#fff'>{roe_str}</strong></div>"
                    f"<div>PER: <strong style='color:#fff'>{per_str}</strong></div>"
                    f"<div>PBR: <strong style='color:#fff'>{pbr_str}</strong></div>"
                    f"<div>배당(참고): <strong style='color:#fff'>{div_str}</strong></div>"
                    f"</div></div>",
                    unsafe_allow_html=True,
                )

                rc_key = f"rc_{mode_name}_{idx}"
                if st.button(f"🔍 {c['name']} 편입 검토", key=f"btn_{rc_key}", use_container_width=True):
                    st.session_state[f"rc_open_{rc_key}"] = True

                if st.session_state.get(f"rc_open_{rc_key}"):
                    with st.spinner(f"{c['name']} 현재가 조회 중..."):
                        price_obj, stock_name = get_current_price_by_ticker(c["ticker"], is_paper)
                    if price_obj:
                        current_price = float(price_obj.amount)
                        st.info(f"📊 **{c['name']}** 현재가: **{current_price:,.0f} KRW**")
                        qty = st.number_input(
                            "매수 수량 (주)", min_value=1, max_value=10000, value=1, step=1,
                            key=f"qty_{rc_key}",
                        )
                        total_amt = current_price * qty
                        st.caption(f"예상 금액: {total_amt:,.0f} KRW")
                        col_buy, col_cancel = st.columns(2)
                        with col_buy:
                            if st.button("✅ 매수 승인", key=f"approve_{rc_key}",
                                         type="primary", use_container_width=True):
                                st.session_state[f"rc_confirm_{rc_key}"] = True
                        with col_cancel:
                            if st.button("취소", key=f"cancel_{rc_key}", use_container_width=True):
                                st.session_state[f"rc_open_{rc_key}"] = False
                                st.session_state[f"rc_confirm_{rc_key}"] = None

                        if st.session_state.get(f"rc_confirm_{rc_key}"):
                            st.warning(
                                f"⚠️ 정말 실행? **BUY {c['name']}** | "
                                f"{qty}주 | {total_amt:,.0f} KRW"
                            )
                            col_yes, col_no = st.columns(2)
                            with col_yes:
                                if st.button("🔴 최종 확인 - 실행", key=f"final_{rc_key}",
                                             type="primary", use_container_width=True):
                                    try:
                                        order_id = place_manual_order(
                                            ticker=c["ticker"], name=c["name"],
                                            quantity=qty, is_paper=is_paper, side="buy",
                                        )
                                        st.success(f"✅ 주문 완료! {order_id or '체결 확인 중'}")
                                        st.session_state[f"rc_open_{rc_key}"] = False
                                        st.session_state[f"rc_confirm_{rc_key}"] = None
                                        st.cache_data.clear()
                                    except Exception as e:
                                        st.error(f"주문 실패: {e}")
                            with col_no:
                                if st.button("취소", key=f"final_no_{rc_key}", use_container_width=True):
                                    st.session_state[f"rc_confirm_{rc_key}"] = None
                    else:
                        st.error(f"현재가 조회 실패: {stock_name}")
                st.markdown("---")

    render_candidate_tab("🏛️ 버핏형", mode_tab1)
    render_candidate_tab("⚖️ 균형형", mode_tab2)
    render_candidate_tab("🚀 성장형", mode_tab3)


# ── TAB 6: 수동 매수 ──────────────────────────────────────────────────────────
with tab_manual:
    st.markdown("### 🔍 종목 검색 매수")
    st.caption("티커(종목코드) 입력 → 현재가 조회 → 수량 입력 → 매수")
    st.markdown("---")

    col_ticker, col_search = st.columns([3, 1])
    with col_ticker:
        manual_ticker = st.text_input(
            "종목코드 입력 (예: 005930)",
            placeholder="6자리 종목코드",
            key="manual_ticker",
        ).strip()
    with col_search:
        st.markdown("<div style='margin-top:28px'>", unsafe_allow_html=True)
        search_btn = st.button("🔍 조회", use_container_width=True, key="search_btn")
        st.markdown("</div>", unsafe_allow_html=True)

    if search_btn and manual_ticker:
        if len(manual_ticker) != 6 or not manual_ticker.isdigit():
            st.error("6자리 숫자 종목코드를 입력하세요.")
        else:
            with st.spinner(f"{manual_ticker} 조회 중..."):
                price_obj, stock_name = get_current_price_by_ticker(manual_ticker, is_paper)
            if price_obj:
                current_price = float(price_obj.amount)
                st.session_state["manual_price"] = current_price
                st.session_state["manual_name"] = stock_name
                st.session_state["manual_ticker_confirmed"] = manual_ticker
                st.success(f"✅ **{stock_name}** ({manual_ticker}) | 현재가: **{current_price:,.0f} KRW**")
            else:
                st.error(f"조회 실패: {stock_name}")

    if st.session_state.get("manual_price") and st.session_state.get("manual_ticker_confirmed"):
        current_price = st.session_state["manual_price"]
        stock_name = st.session_state["manual_name"]
        confirmed_ticker = st.session_state["manual_ticker_confirmed"]

        st.markdown("---")
        st.markdown(f"**{stock_name}** `{confirmed_ticker}` | 현재가: **{current_price:,.0f} KRW**")

        col_side, col_qty = st.columns(2)
        with col_side:
            order_side = st.selectbox("매수/매도", options=["매수", "매도"], key="manual_side")
        with col_qty:
            manual_qty = st.number_input(
                "수량 (주)", min_value=1, max_value=100000, value=1, step=1,
                key="manual_qty",
            )

        total_amt = current_price * manual_qty
        side_str = "BUY" if order_side == "매수" else "SELL"
        side_color = "#00C896" if order_side == "매수" else "#E74C3C"
        st.markdown(
            f"<div style='background:#1E2130; border-radius:10px; padding:12px; margin:8px 0'>"
            f"<span style='color:{side_color}; font-weight:700'>{side_str}</span> "
            f"{stock_name} | {manual_qty}주 | "
            f"<strong>{total_amt:,.0f} KRW</strong>"
            f"</div>",
            unsafe_allow_html=True,
        )

        if st.button("✅ 승인", type="primary", use_container_width=True, key="manual_approve"):
            st.session_state["manual_confirm"] = True

        if st.session_state.get("manual_confirm"):
            st.warning(
                f"⚠️ 정말 실행? **{side_str} {stock_name}** | "
                f"{manual_qty}주 | {total_amt:,.0f} KRW"
            )
            col_yes, col_no = st.columns(2)
            with col_yes:
                if st.button("🔴 최종 확인 - 실행", type="primary",
                             use_container_width=True, key="manual_final"):
                    try:
                        order_id = place_manual_order(
                            ticker=confirmed_ticker, name=stock_name,
                            quantity=manual_qty, is_paper=is_paper,
                            side="buy" if order_side == "매수" else "sell",
                        )
                        st.success(f"✅ 주문 완료! {order_id or '체결 확인 중'}")
                        # Satellite holdings 자동 저장 (매수 시)
                        if order_side == "매수":
                            buckets = load_buckets()
                            if confirmed_ticker not in buckets["satellite"]["holdings"]:
                                buckets["satellite"]["holdings"][confirmed_ticker] = {
                                    "name": stock_name,
                                    "entry_date": datetime.now().strftime("%Y-%m-%d"),
                                    "entry_score": 0.0,
                                    "total_score": 0.0,
                                    "momentum_score": 0.0,
                                    "sector": "기타"
                                }
                                save_buckets(buckets)
                        st.session_state["manual_confirm"] = False
                        st.session_state["manual_price"] = None
                        st.session_state["manual_ticker_confirmed"] = None
                        st.cache_data.clear()
                    except Exception as e:
                        st.error(f"주문 실패: {e}")
            with col_no:
                if st.button("취소", use_container_width=True, key="manual_cancel"):
                    st.session_state["manual_confirm"] = False


# =============================================================================
# 푸터
# =============================================================================

mode_text = "모의투자" if is_paper else "실전투자"
st.markdown(
    f"<div style='text-align:center; color:#8B9AB0; font-size:12px; margin-top:20px'>"
    f"Claude Asset Engine | BUFFETT_COMPOUND_DEFENSE | {mode_text} | 데이터 5분 캐시"
    f"</div>",
    unsafe_allow_html=True,
)