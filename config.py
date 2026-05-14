import os
from dotenv import load_dotenv

load_dotenv()

# ─── Gemini ───────────────────────────────────────────
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash-image"

# ─── 출력 설정 ────────────────────────────────────────
OUTPUT_DIR     = os.path.join(os.path.dirname(__file__), "output")
IMAGE_FORMAT   = "png"          # png | jpg

# ─── 프롬프트 엔진 설정 ───────────────────────────────
DEFAULT_ASPECT  = "3:4"         # 세로형 인물 기본값
BATCH_SIZE      = 4             # 배치 생성 기본 수량
RANDOM_SEED     = None          # None = 매번 다름

# ─── 프로바이더 선택 ──────────────────────────────────
ACTIVE_PROVIDER = "pollinations"      # gemini | stability | midjourney