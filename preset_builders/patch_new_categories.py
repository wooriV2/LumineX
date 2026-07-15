"""
patch_new_categories.py
========================
작업 내용:
  1. presets_meta.py — 🔊 Acoustic Levitation Glamour 확장 12종 (13~24번) 추가
  2. presets_meta.py — 🔥 Body × Element Glamour 12종 신규 추가
  3. presets_meta.py — 💃 Body × Luxury Setting Glamour 12종 신규 추가
  4. hof_tier.py     — HOF 12종 추가
                       Acoustic 확장 HOF 4종: latina_silk_thread_web,
                         amazon_lightning_arc, black_glamour_obsidian_float,
                         brazil_petal_carnival
                       Element HOF 4종: bbw_water_goddess, latina_storm_goddess,
                         vs_angel_ice_goddess, hot_glamour_plasma_goddess
                       Luxury HOF 4종: super_glamour_versailles,
                         amazon_dubai_penthouse, latina_rio_carnival,
                         vs_angel_paris_runway

저장: C:\\Dev\\LumineX\\preset_builders\\patch_new_categories.py
실행: python preset_builders/patch_new_categories.py
"""

from pathlib import Path

BASE      = Path("C:/Dev/LumineX")
META_PATH = BASE / "core/presets_meta.py"
HOF_PATH  = BASE / "core/hof_tier.py"

# ══════════════════════════════════════════════════════════════════════════
# 1. PRESET DATA
# ══════════════════════════════════════════════════════════════════════════

# ── Acoustic 확장 (13~24번) ──────────────────────────────────────────────
ACOUSTIC_EXPANSION = '''\
    "🔊 Acoustic Levitation Glamour 2": [
        {
            "id": "acoustic_super_glamour_diamond_dust",
            "name": "Diamond Dust",
            "prompt": "Professional fashion photograph, full body shot. Model: supreme hourglass goddess, impossibly cinched waist, maximum curves, millions of diamond dust particles levitating in acoustic nodes creating total diamond atmosphere around her perfect figure — 24k diamond particles suspended in sound field. Body: spectacular extreme hourglass figure, warm golden skin, voluminous platinum waves catching diamond light, expression commanding. Wearing: ultra-minimal black micro string bikini — diamond dust settling on curves as living diamond skin, black stiletto thigh-high platform boots 6-inch heel catching diamond fire, diamond choker + matching earrings. Environment: dark luxury studio, diamond particle cloud filling entire frame, figure at maximum density center. Lighting: single hard diamond-white spot, particles creating total prismatic fire, golden skin blazing through diamond cloud. Style: super glamour acoustic diamond editorial, sound making diamonds float. Shot on Hasselblad X2D, acoustic diamond grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_bbw_soap_bubble_galaxy",
            "name": "Soap Bubble Galaxy",
            "prompt": "Professional fashion photograph, full body shot. Model: magnificent super BBW goddess, full voluminous curves commanding entire frame, thousands of giant soap bubbles levitating in acoustic nodes creating galaxy of iridescent spheres — bubbles 5-30cm diameter suspended at precise sound field positions. Body: supremely full magnificent figure, deep mahogany skin, massive voluminous natural afro, serene commanding expression. Wearing: minimal deep purple micro dress — soap bubbles surrounding every magnificent curve, each bubble reflecting full-body rainbow spectrum, purple patent thigh-high platform boots 5-inch heel with bubble clusters orbiting, no jewelry — bubble galaxy is the crown. Environment: black infinity studio, bubble galaxy filling full frame around figure, each bubble a miniature universe. Lighting: rainbow-spectrum studio, each bubble acting as prism creating full rainbow interior, mahogany skin warm in bubble light. Style: super BBW acoustic soap bubble galaxy editorial, sound suspending universe. Shot on Phase One XF IQ4, acoustic bubble grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_latina_silk_thread_web",
            "name": "Silk Thread Web",
            "prompt": "Professional fashion photograph, full body shot. Model: Colombian extreme hourglass goddess, sculpted maximum curves, hundreds of gold silk threads levitating in acoustic nodes weaving living web structure around her dramatic figure — threads suspended in complex 3D acoustic architecture. Body: extreme hourglass physique, olive-bronze skin, long dark waves threaded with gold silk caught in acoustic field. Wearing: gold micro string bikini — silk threads suspended in acoustic nodes forming elaborate golden web gown around curves, gold stiletto thigh-high platform boots 6-inch heel with thread spirals at boots, gold ear cuffs. Environment: dark opulent studio, silk thread web architecture filling frame, threads catching light as golden lines, figure at web center. Lighting: warm gold key, silk threads catching light as liquid gold lines, bronze skin glowing through thread architecture. Style: Colombian acoustic silk thread editorial, sound weaving gold. Shot on Hasselblad X2D, acoustic silk grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "acoustic_bust_queen_crystal_shard",
            "name": "Crystal Shard",
            "prompt": "Professional fashion photograph, full body shot. Model: legendary bust goddess, impossibly full bust with perfect cinched waist, hundreds of rose quartz crystal shards levitating in acoustic nodes forming living crystal armor — crystals 3-25cm suspended precisely around her figure. Body: legendary bust physique, cream skin, long auburn waves, expression fierce-regal. Wearing: minimal deep rose micro corset barely containing legendary curves — rose quartz crystals suspended in acoustic nodes forming shoulder armor, bust framework, hip panels as living crystal couture, rose gold stiletto thigh-high platform boots 5-inch heel, crystal choker with rose quartz drops. Environment: dark rose-tinted studio, rose quartz crystals filling frame with pink prismatic light, crystal architecture defining curves. Lighting: rose-pink side lighting, crystals creating total warm rose prismatic fire, cream skin luminous in rose crystal light. Style: bust queen acoustic crystal editorial, sound building rose armor. Shot on Phase One XF IQ4, acoustic crystal grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_amazon_lightning_arc",
            "name": "Lightning Arc",
            "prompt": "Professional fashion photograph, full body shot. Model: 185cm amazon goddess, towering powerful physique, dozens of plasma lightning arcs levitating in acoustic nodes around her tall frame — electric arcs 10-60cm suspended in sound field creating living lightning architecture. Body: extreme tall powerful physique, bronze-copper skin, natural afro with electric edges, expression storm-commanding. Wearing: minimal silver metallic micro sports bra + micro thong — lightning arcs suspended at acoustic nodes from crown to boots creating full-body electric armor, silver chrome thigh-high platform stiletto boots 6-inch heel with arc discharge at boot tops, silver arm cuffs. Environment: dark storm studio, lightning arcs creating blue-white electric architecture around towering figure, ozone effect visible. Lighting: plasma blue-white from lightning arc positions only, figure lit by own electric constellation, bronze skin edge-lit by arc discharge. Style: amazon acoustic lightning editorial, sound commanding electricity. Shot on Hasselblad X2D, acoustic lightning grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "acoustic_vs_angel_feather_vortex",
            "name": "Feather Vortex",
            "prompt": "Professional fashion photograph, full body shot. Model: Victoria's Secret perfect angel physique, flawless proportions, thousands of white swan feathers levitating in acoustic upward vortex around her perfect figure — feathers tracing luminous spiral acoustic paths. Body: VS perfect hourglass physique, sun-kissed golden skin, waist-length beach waves catching feather wind, expression angelic-fierce. Wearing: white micro lace triangle bikini — feather vortex forming natural angel-wing silhouette in air around figure, individual feathers landing and lifting off perfect curves, white patent platform stiletto boots 5-inch heel with feather spirals at base, pearl drop earrings. Environment: dark ethereal studio, feather vortex rising full frame, long-exposure feather trails as white luminous spiral lines. Lighting: single overhead heavenly white beam, feathers edge-lit in white arcs, golden skin warm through feather architecture. Style: VS angel acoustic feather vortex editorial, sound building wings. Shot on Phase One XF IQ4, acoustic feather grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_black_glamour_obsidian_float",
            "name": "Obsidian Float",
            "prompt": "Professional fashion photograph, full body shot. Model: extreme black glamour goddess, maximum mocha-ebony hourglass, hundreds of polished obsidian fragments levitating in acoustic nodes creating living black mirror armor — obsidian shards 2-20cm suspended in sound field. Body: spectacular ebony hourglass physique, jet-black skin, voluminous natural coils, expression dark-regal. Wearing: minimal gold micro string bikini — obsidian fragments suspended in acoustic nodes forming dark mirror armor panels, each shard reflecting distorted gold figure multiplied, gold stiletto thigh-high platform boots 6-inch heel with obsidian clusters, gold serpent armband. Environment: deep black studio, obsidian fragments floating in constellation around figure, each shard a dark mirror, gold catching obsidian reflections. Lighting: single gold key spot, obsidian shards creating black mirror reflections of gold light, jet skin edge-lit in gold obsidian reflections. Style: black glamour acoustic obsidian editorial, sound floating darkness. Shot on Hasselblad X2D, acoustic obsidian grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "acoustic_hot_glamour_ember_silk",
            "name": "Ember Silk",
            "prompt": "Professional fashion photograph, full body shot. Model: hot glamour cinched-waist goddess, perfect dramatic curves, glowing fire embers AND shredded silk threads simultaneously levitating in acoustic nodes — dual-material suspension, embers and silk interweaving around figure. Body: dramatic hot glamour hourglass, warm caramel skin, loose dark waves catching ember-wind and silk threads. Wearing: deep crimson ultra-sheer micro silk slip dress — embers suspended at acoustic nodes creating warm constellation, silk threads also suspended creating living veil between ember points, crimson stiletto thigh-high platform boots 5-inch heel, ruby drop earrings. Environment: dark romantic studio, ember+silk dual suspension filling frame, embers glowing through silk thread veil. Lighting: ember amber-warm from node positions, silk threads catching edge light as luminous lines, caramel skin warm in dual ember-silk light. Style: hot glamour acoustic ember-silk editorial, sound weaving fire and silk. Shot on Phase One XF IQ4, acoustic ember-silk grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_brazil_petal_carnival",
            "name": "Petal Carnival",
            "prompt": "Professional fashion photograph, full body shot. Model: Brazilian carnival booty goddess, maximum dramatic hip-to-waist ratio, extreme full hips, thousands of tropical carnival feathers AND petals simultaneously levitating in acoustic nodes — carnival atmosphere suspended in sound field. Body: extreme Brazilian carnival physique, rich terra-cotta skin, voluminous dark carnival waves adorned with suspended petals. Wearing: minimal carnival micro samba bikini in gold and tropical colors — feathers and petals suspended at acoustic nodes forming full carnival costume silhouette in air, gold platform carnival boots 5-inch heel with feather clusters, carnival gold headdress elements levitating in formation. Environment: dark carnival studio, feather-petal suspension filling frame as living carnival costume, figure at celebration center. Lighting: warm carnival gold-amber, feathers and petals catching light as carnival fire, terra-cotta skin golden in carnival light. Style: Brazilian acoustic carnival editorial, sound building carnival costume. Shot on Hasselblad X2D, acoustic carnival grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "acoustic_supermodel_glass_bead_curtain",
            "name": "Glass Bead Curtain",
            "prompt": "Professional fashion photograph, full body shot. Model: 185cm+ supermodel extreme tall goddess, impossibly long legs, thousands of crystal glass beads levitating in acoustic nodes forming full-length bead curtain wall she stands within — beads 1-3cm diameter at precise sound positions. Body: extreme tall supermodel physique, alabaster skin, severe sleek high ponytail, cheekbones cutting, expression high-fashion-cold. Wearing: minimal white micro bandeau + micro thong — glass bead curtain surrounding tall figure, beads at multiple acoustic layers creating transparent crystal room around her, clear platform stiletto mules 6-inch heel at bead curtain base, single geometric crystal ear cuff. Environment: white studio, full-length crystal bead curtain filling frame floor to ceiling around tall figure, each bead prismatic point of light. Lighting: overhead white spot, beads creating prismatic crystal fire ceiling to floor, alabaster skin through crystal architecture. Style: supermodel acoustic glass bead editorial, sound making crystal room. Shot on Phase One XF IQ4, acoustic bead grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_powerlifter_steel_chain",
            "name": "Steel Chain",
            "prompt": "Professional fashion photograph, full body shot. Model: powerlifter muscle goddess, extreme defined musculature with feminine curves, dozens of heavy steel chains levitating in acoustic nodes around powerful figure — chains 1-3cm link, 30-80cm lengths, suspended in sound field. Body: extreme powerlifter physique, defined everywhere, bronze-iron skin, severe warrior braid, expression iron-fierce. Wearing: minimal matte black micro sports bra + micro shorts — steel chains suspended at acoustic nodes from crown to boots forming chain armor, each chain link catching hard light as metal lightning, matte black platform combat boots 5-inch with chain clusters orbiting, iron cuff bracelets. Environment: dark industrial forge, chains hanging from acoustic nodes in perfect geometry around figure, steam visible. Lighting: forge-hard directional industrial, chain links creating metal specular grid, bronze skin in chiaroscuro between chain armor. Style: powerlifter acoustic steel chain editorial, sound suspending iron. Shot on Hasselblad X2D, acoustic steel grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_miniature_snow_globe",
            "name": "Snow Globe",
            "prompt": "Professional fashion photograph, full body shot. Model: petite miniature goddess, 148cm ultra-compact perfect figure, inside acoustic snow globe effect — thousands of tiny snowflakes and glitter suspended in acoustic nodes creating snow globe atmosphere around tiny figure. Body: ultra-petite compact figure, porcelain skin, platinum hair in perfect ballerina bun, expression wide-eyed ethereal. Wearing: ultra-minimal white micro ballet leotard — snowflakes and silver glitter suspended at every acoustic node position surrounding tiny figure creating living snow globe, transparent platform crystal heels 4-inch, snowflake crystal hair pins in bun. Environment: dark studio, snowflake-glitter suspension surrounding entire tiny figure creating perfect snow globe effect, figure as snow globe figurine. Lighting: cool blue-white overhead, snowflakes creating crystalline light scatter, porcelain skin luminous in snow globe atmosphere. Style: miniature acoustic snow globe editorial, sound making winter. Shot on Phase One XF IQ4, acoustic snow grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
    ],\
'''

# ── Body × Element Glamour ───────────────────────────────────────────────
ELEMENT_CATEGORY = '''\
    "🔥 Body × Element Glamour": [
        {
            "id": "element_super_glamour_fire_goddess",
            "name": "Fire Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: supreme hourglass fire goddess, impossibly cinched waist, maximum curves, standing at center of active volcanic fire field — real fire elements responding to her body. Body: spectacular extreme hourglass, deep copper skin glowing in fire light, voluminous dark waves with fire-touched edges. Wearing: minimal deep red metallic micro string bikini — fire licking at curves from below, heat distortion visible around perfect silhouette, red patent thigh-high platform stiletto boots 6-inch heel, ruby fire crystal choker. Environment: active volcano edge, lava pools below, fire pillars rising around figure, volcanic atmosphere. Lighting: volcanic amber-red from all fire positions, molten glow on copper skin from below and sides, dramatic volcanic chiaroscuro. Style: super glamour elemental fire goddess editorial. Shot on Phase One XF IQ4, volcanic fire grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "element_bbw_water_goddess",
            "name": "Water Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: supreme BBW water goddess, magnificent full figure commanding ocean waves — water elements responding and conforming to her body. Body: supremely full magnificent figure, deep ebony skin, voluminous natural locs with water droplets, serene commanding expression. Wearing: minimal deep blue micro string bikini — ocean waves rising and wrapping around full magnificent figure, water conforming to every curve as living water dress, blue patent thigh-high platform stiletto boots 5-inch heel in surf, no jewelry — ocean is the crown. Environment: dramatic ocean shore, storm waves rising and bowing to figure, seafoam at her command. Lighting: stormy silver-blue ocean light, white water catching light against ebony skin, dramatic sky behind. Style: super BBW elemental water goddess editorial. Shot on Hasselblad X2D, ocean storm grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "element_amazon_lightning_goddess",
            "name": "Lightning Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: 185cm amazon lightning goddess, towering powerful physique commanding storm — lightning responding to her raised hand. Body: extreme tall powerful physique, bronze-copper skin, natural afro with electric corona, storm-commanding expression. Wearing: minimal silver metallic micro sports bra + micro thong — lightning bolts arcing to and from her body from multiple directions, silver chrome thigh-high platform stiletto boots 6-inch heel, silver armband and ankle cuffs. Environment: open storm field, multiple lightning strikes around figure, purple-charged atmosphere, dark storm sky. Lighting: lightning-flash electric blue-white from multiple arc positions, bronze skin in electric strobe, storm atmosphere. Style: amazon elemental lightning goddess editorial. Shot on Phase One XF IQ4, electric storm grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "element_petite_wind_goddess",
            "name": "Wind Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: petite miniature wind goddess, ultra-compact tiny figure commanding massive wind currents — wind elements creating scale contrast with small figure. Body: ultra-petite compact figure, ivory skin, platinum hair exploding in wind vortex dramatically larger than tiny body. Wearing: ultra-minimal white micro silk slip dress — fabric caught in wind vortex creating massive white flag behind tiny figure, white platform stiletto boots 4-inch heel standing in wind center, no jewelry — wind is everything. Environment: open cliff edge, massive wind current visible through fabric and hair movement, dramatic sky scale-contrasting tiny figure. Lighting: dramatic natural side light, wind-caught fabric creating massive luminous white shape against dark sky, tiny figure as wind goddess axis. Style: petite elemental wind goddess editorial, small figure commanding vast forces. Shot on Hasselblad X2D, wind cliff grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "element_bust_queen_lava_goddess",
            "name": "Lava Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: legendary bust goddess commanding lava flows — molten rock elements parting and conforming around her legendary figure. Body: legendary bust physique, cream-golden skin lit from below by lava, auburn waves with heat-shimmer edges. Wearing: minimal black metallic micro corset — lava flows parting around her boots, heat distortion creating shimmering aura around legendary curves, black patent thigh-high platform boots 5-inch heel on cooled lava rock, obsidian choker. Environment: active lava field, molten lava flows parting around her like sea, volcanic steam rising, red sky. Lighting: lava red-orange from below and sides, molten glow on cream skin from rising lava light, volcanic atmospheric depth. Style: bust queen elemental lava goddess editorial. Shot on Phase One XF IQ4, volcanic lava grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "element_latina_storm_goddess",
            "name": "Storm Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: Colombian storm goddess, extreme hourglass commanding tropical storm — wind, rain, and lightning responding to her dramatic figure. Body: extreme Colombian hourglass, olive-copper skin soaked in storm rain, dark waves plastered in perfect storm-goddess formation. Wearing: minimal gold micro string bikini — soaked gold fabric clinging to every extreme curve, rain cascading off dramatic silhouette, storm lightning behind, gold stiletto thigh-high platform boots 6-inch heel in storm water, gold ear studs. Environment: tropical storm epicenter, horizontal rain, lightning behind, palm trees bending, storm surge around boots. Lighting: storm lightning flash + warm amber from below, wet bronze skin in electric storm light, dramatic storm atmosphere. Style: Colombian elemental storm goddess editorial, Formula D wet variant. Shot on Hasselblad X2D, tropical storm grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "element_vs_angel_ice_goddess",
            "name": "Ice Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: VS perfect angel ice goddess, flawless proportions commanding arctic ice — ice elements forming around her perfect body. Body: VS perfect hourglass, snow-pale skin, ice-white waves, expression cold-angelic. Wearing: minimal white micro lace bikini — ice crystals forming on skin and fabric creating ice angel wings behind, frost patterns on perfect curves, white platform crystal heel boots 5-inch with ice formations, diamond ice choker. Environment: arctic glacier, ice formations rising around her, aurora borealis above, frozen breath visible. Lighting: aurora blue-green + ice crystal white reflection, pale skin luminous in arctic light, ice formations catching aurora. Style: VS angel elemental ice goddess editorial. Shot on Phase One XF IQ4, arctic ice grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "element_black_glamour_void_goddess",
            "name": "Void Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: extreme black glamour void goddess, maximum ebony hourglass commanding cosmic void — darkness and stars responding to her figure. Body: spectacular jet-black hourglass, deep ebony skin absorbing light, voluminous natural coils with star-dust edges, expression cosmic-commanding. Wearing: minimal galaxy-pattern micro string bikini — cosmic void opening around her figure, stars and nebula swirling, darkness responding to curve, gold thigh-high platform stiletto boots 6-inch heel in starfield, constellation choker. Environment: cosmic void backdrop, galaxies and nebulae swirling around figure, stars orbiting her silhouette, infinite dark space. Lighting: cosmic starlight from all galaxy positions, pure ebony skin as void center, stars edge-lighting black curves. Style: black glamour elemental void goddess editorial. Shot on Hasselblad X2D, cosmic void grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "element_hot_glamour_plasma_goddess",
            "name": "Plasma Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: hot glamour plasma goddess, dramatic cinched-waist curves commanding plasma energy — solar plasma elements conforming to her dramatic figure. Body: dramatic hot glamour hourglass, warm caramel skin with plasma glow, loose dark waves with plasma-energy edges. Wearing: minimal solar-gold micro string bikini — plasma energy tendrils rising from skin surface, solar flare elements conforming to dramatic curves, gold stiletto thigh-high platform boots 5-inch heel with plasma orbiting, solar gold choker. Environment: solar atmosphere, plasma loops rising around figure, solar flare backdrop, intense solar energy. Lighting: solar plasma orange-gold from all plasma positions, warm caramel skin blazing in solar energy, plasma creating atmospheric depth. Style: hot glamour elemental plasma goddess editorial. Shot on Phase One XF IQ4, solar plasma grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "element_brazil_earth_goddess",
            "name": "Earth Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: Brazilian earth goddess, maximum dramatic hip ratio commanding earth elements — soil, roots, flowers responding to her generous curves. Body: extreme Brazilian hip physique, rich terra-cotta earth skin, voluminous dark waves entwined with living vines and flowers. Wearing: minimal tropical flower micro bikini — earth vines rising and wrapping around generous curves, tropical flowers blooming at hip line, terra-cotta platform wedge boots 5-inch heel in rich earth, flower crown forming naturally. Environment: lush tropical jungle floor, earth responding to her presence, roots parting, flowers blooming, green canopy above. Lighting: dappled jungle light, warm earth-gold filtering through canopy, terra-cotta skin warm in earth-filtered light. Style: Brazilian elemental earth goddess editorial. Shot on Hasselblad X2D, earth goddess grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "element_supermodel_aurora_goddess",
            "name": "Aurora Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: 185cm+ supermodel aurora goddess, extreme tall commanding northern lights — aurora elements responding and bending toward her tall figure. Body: extreme tall supermodel physique, alabaster skin, sleek dark hair absorbing aurora colors, expression ethereal-commanding. Wearing: minimal iridescent micro string bikini shifting aurora colors — aurora curtains bending toward and around extreme tall figure, aurora conforming to long silhouette, clear platform stiletto mules 6-inch heel, aurora crystal ear cuff. Environment: iceland aurora field, full aurora display bending toward figure, reflected in snow below, infinite arctic sky. Lighting: full aurora spectrum green-purple-blue from multiple sky positions, alabaster skin catching aurora color shifts, aurora responding to tall goddess presence. Style: supermodel elemental aurora goddess editorial. Shot on Phase One XF IQ4, aurora grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "element_powerlifter_volcano_goddess",
            "name": "Volcano Goddess",
            "prompt": "Professional fashion photograph, full body shot. Model: powerlifter muscle volcano goddess, extreme defined musculature with feminine power commanding volcanic eruption — volcanic elements responding to her iron strength. Body: extreme powerlifter physique, defined everywhere, bronze-iron skin glowing in volcanic light, severe warrior braid with volcanic ash. Wearing: minimal matte black micro sports bra + micro shorts — volcanic ash and embers orbiting powerful figure, volcanic energy rising from boot positions, matte black combat platform boots 5-inch heel on volcanic rock, iron cuff bracelets. Environment: active volcano crater rim, eruption behind her, volcanic ash cloud, lava below, power stance at eruption axis. Lighting: volcanic orange-red from eruption behind + lava below, iron skin in volcanic chiaroscuro, eruption creating dramatic silhouette edge-lighting. Style: powerlifter elemental volcano goddess editorial. Shot on Hasselblad X2D, volcanic eruption grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
    ],\
'''

# ── Body × Luxury Setting Glamour ────────────────────────────────────────
LUXURY_CATEGORY = '''\
    "💃 Body × Luxury Setting Glamour": [
        {
            "id": "luxury_super_glamour_versailles",
            "name": "Versailles",
            "prompt": "Professional fashion photograph, full body shot. Model: supreme hourglass goddess commanding Hall of Mirrors Versailles — perfect figure as living sculpture among gold and glass. Body: spectacular extreme hourglass, golden skin, voluminous champagne waves, expression regal-commanding. Wearing: ultra-minimal gold micro string bikini — barely there against Hall of Mirrors grandeur, gold stiletto thigh-high platform boots 6-inch heel on marble floor, diamond choker, long white opera gloves. Environment: Hall of Mirrors Versailles, gold and crystal chandeliers, infinite mirror reflections, perfect parquet floor, golden afternoon light through arched windows. Lighting: warm Versailles gold through arched windows + chandelier crystal diffusion, golden skin luminous in palace light, infinite mirror reflections of perfect figure. Style: super glamour luxury Versailles editorial. Shot on Hasselblad X2D, Versailles gold grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "luxury_bbw_monaco_yacht",
            "name": "Monaco Yacht",
            "prompt": "Professional fashion photograph, full body shot. Model: magnificent BBW goddess commanding Monaco superyacht deck — full magnificent figure owning the Mediterranean. Body: supremely full magnificent figure, deep mahogany skin, voluminous locs, expression owning-everything. Wearing: minimal deep navy micro string bikini — full figure against Monaco coastline backdrop, navy patent thigh-high platform boots 5-inch heel on teak deck, gold yacht anchor choker. Environment: Monaco superyacht deck, Monte Carlo visible behind, Mediterranean blue, other yachts, luxury deck furniture, champagne visible. Lighting: golden Mediterranean afternoon, warm mahogany skin in Mediterranean gold light, Monaco sparkle behind. Style: BBW luxury Monaco yacht editorial. Shot on Phase One XF IQ4, Mediterranean gold grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "luxury_amazon_dubai_penthouse",
            "name": "Dubai Penthouse",
            "prompt": "Professional fashion photograph, full body shot. Model: 185cm amazon goddess commanding Dubai penthouse — towering figure against Burj Khalifa skyline. Body: extreme tall powerful physique, copper skin, natural afro, expression commanding city below. Wearing: minimal gold metallic micro sports bra + micro thong — tall figure against full Dubai skyline, gold chrome thigh-high platform stiletto boots 6-inch heel on penthouse edge, gold cuff. Environment: Dubai penthouse top floor, floor-to-ceiling glass, Burj Khalifa visible, city lights below, infinity pool reflecting skyline. Lighting: golden Dubai sunset on copper skin, city lights beginning below, penthouse luxury atmosphere. Style: amazon luxury Dubai penthouse editorial. Shot on Hasselblad X2D, Dubai gold grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "luxury_latina_rio_carnival",
            "name": "Rio Carnival",
            "prompt": "Professional fashion photograph, full body shot. Model: Colombian extreme hourglass at Rio Carnival sambadrome — dramatic curves commanding carnival grandeur. Body: extreme Colombian hourglass, warm olive-bronze skin, massive carnival waves adorned with feathers. Wearing: minimal carnival gold micro samba bikini — dramatic curves in ultimate carnival setting, gold carnival platform boots 5-inch, full carnival feather headdress, carnival body jewels at waist. Environment: Rio Carnival sambadrome, parade floats, carnival performers, massive crowd, exploding carnival energy, fireworks above. Lighting: carnival flood lights + fireworks in sky, warm bronze skin in carnival gold light, carnival spectacle. Style: Colombian luxury Rio Carnival editorial. Shot on Phase One XF IQ4, carnival gold grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "luxury_bust_queen_milan_couture",
            "name": "Milan Couture",
            "prompt": "Professional fashion photograph, full body shot. Model: legendary bust goddess commanding Milan couture runway — legendary figure redefining haute couture. Body: legendary bust physique, cream skin, auburn waves, expression haute couture regal. Wearing: minimal deep cream micro corset — legendary figure on Milan white runway, cream patent thigh-high platform boots 5-inch heel, crystal choker, white runway atmosphere. Environment: Milan Fashion Week runway, front row visible, flashes, white runway lights, fashion world elite. Lighting: runway hard white overhead + fashion photography flash, cream skin luminous in couture light, fashion week grandeur. Style: bust queen luxury Milan couture editorial. Shot on Hasselblad X2D, couture white grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "luxury_vs_angel_paris_runway",
            "name": "Paris VS Runway",
            "prompt": "Professional fashion photograph, full body shot. Model: VS perfect angel on Paris runway — flawless proportions commanding fashion world attention. Body: VS perfect hourglass, golden skin, beach waves, expression angel-fierce. Wearing: minimal white micro lace VS Fantasy Bra — full VS angel runway look, white platform stiletto boots 5-inch heel, fantasy diamond bra statement piece, VS angel wings deployed. Environment: Paris runway, Eiffel Tower visible through venue windows, French fashion elite front row, explosion of flashbulbs, Paris runway energy. Lighting: Paris runway spot + flashbulb explosion, golden skin in runway light, Eiffel Tower Paris backdrop. Style: VS angel luxury Paris runway editorial. Shot on Phase One XF IQ4, Paris runway grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "luxury_black_glamour_nyc_rooftop",
            "name": "NYC Rooftop",
            "prompt": "Professional fashion photograph, full body shot. Model: extreme black glamour goddess commanding NYC rooftop — maximum ebony figure owning Manhattan skyline. Body: spectacular jet-black hourglass, deep ebony skin, voluminous natural coils, expression owning the night. Wearing: minimal all-black micro string bikini — jet figure against Manhattan night skyline, black patent thigh-high platform boots 6-inch heel on rooftop edge, diamond constellation choker. Environment: Manhattan rooftop, Empire State Building lit behind, Times Square glow below, helicopter lights, NYC night energy. Lighting: NYC ambient night light, diamond choker catching city light, ebony skin in Manhattan night atmosphere. Style: black glamour luxury NYC rooftop editorial. Shot on Hasselblad X2D, NYC night grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "luxury_hot_glamour_tokyo_penthouse",
            "name": "Tokyo Penthouse",
            "prompt": "Professional fashion photograph, full body shot. Model: hot glamour cinched-waist goddess commanding Tokyo penthouse — dramatic curves against neon Tokyo. Body: dramatic hot glamour hourglass, warm caramel skin, dark waves, expression sophisticated-commanding. Wearing: minimal black silk micro slip dress — dramatic figure against Tokyo neon backdrop, black stiletto thigh-high platform boots 5-inch heel, Tokyo neon colors catching on silk fabric, minimal gold jewelry. Environment: Tokyo penthouse, floor-to-ceiling glass, Shibuya crossing below, Tokyo Tower visible, neon city lights, Japanese luxury interior. Lighting: Tokyo neon ambient from cityscape, warm caramel skin in neon color shifts, luxury penthouse atmosphere. Style: hot glamour luxury Tokyo penthouse editorial. Shot on Phase One XF IQ4, Tokyo neon grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "luxury_brazil_maldives_overwater",
            "name": "Maldives Overwater",
            "prompt": "Professional fashion photograph, full body shot. Model: Brazilian booty goddess commanding Maldives overwater villa — maximum hip ratio against tropical paradise. Body: extreme Brazilian hip physique, rich warm skin, voluminous dark tropical waves. Wearing: minimal tropical micro string bikini — generous curves against infinite Indian Ocean, clear platform wedge boots 4-inch on overwater deck, tropical flower ear jewelry. Environment: Maldives overwater bungalow, crystal turquoise water below deck, tropical horizon, overwater villa luxury, tropical paradise. Lighting: golden Maldives tropical afternoon, warm skin in pure tropical paradise light, turquoise water reflection. Style: Brazilian luxury Maldives overwater editorial. Shot on Hasselblad X2D, tropical paradise grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "luxury_supermodel_london_couture",
            "name": "London Couture",
            "prompt": "Professional fashion photograph, full body shot. Model: 185cm+ supermodel goddess commanding London couture event — extreme tall figure in British high fashion. Body: extreme tall supermodel physique, alabaster skin, severe fashion updo, cheekbones, expression editorial-cold. Wearing: minimal white structured micro bandeau + micro skirt — tall figure at British Fashion Council event, white platform stiletto mules 6-inch heel, single architectural pearl ear cuff. Environment: London Royal Academy of Arts, grand British architecture, fashion elite, chandelier light, London couture grandeur. Lighting: British museum chandelier gold + architectural side light, alabaster skin in London couture light, grand architectural space. Style: supermodel luxury London couture editorial. Shot on Phase One XF IQ4, London couture grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "luxury_miniature_shanghai_skyline",
            "name": "Shanghai Skyline",
            "prompt": "Professional fashion photograph, full body shot. Model: petite miniature goddess commanding Shanghai Pudong skyline — ultra-tiny figure against massive modern Chinese architecture creating maximum scale contrast. Body: ultra-petite compact figure, porcelain skin, sleek black hair, expression confident-tiny-against-giant. Wearing: minimal red micro qipao-inspired string bikini — tiny figure against towering Pudong skyline, red platform stiletto ankle boots 4-inch heel, jade drop earrings. Environment: Shanghai Bund promenade, Pudong skyline across river, Oriental Pearl Tower, Shanghai Tower, gold hour, river reflections. Lighting: Shanghai golden hour on porcelain skin, Pudong towers glowing behind tiny figure, river reflection light below. Style: miniature luxury Shanghai skyline editorial, scale contrast goddess. Shot on Hasselblad X2D, Shanghai gold grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "luxury_powerlifter_greek_colosseum",
            "name": "Greek Colosseum",
            "prompt": "Professional fashion photograph, full body shot. Model: powerlifter muscle goddess commanding ancient Greek Colosseum ruins — iron physique against ancient stone power. Body: extreme powerlifter physique, defined everywhere, bronze-iron skin, severe warrior braid, expression warrior-commanding. Wearing: minimal dark battle-worn micro armor breastplate + micro shorts — iron physique at Colosseum ruin scale, matte black platform combat boots 5-inch heel on ancient stone, iron armband cuffs, minimal iron choker. Environment: Greek ancient Colosseum at golden dawn, ancient columns, Mediterranean morning light, ancient stone textures, warrior-goddess scale. Lighting: Greek golden dawn side light on iron skin, ancient stone warm gold, warrior goddess in ancient athlete domain. Style: powerlifter luxury Greek Colosseum editorial. Shot on Phase One XF IQ4, ancient dawn grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
    ],\
'''

# ══════════════════════════════════════════════════════════════════════════
# 2. HOF 추가 목록
# ══════════════════════════════════════════════════════════════════════════

NEW_HOF = [
    # Acoustic 확장 HOF 4종
    "acoustic_latina_silk_thread_web",
    "acoustic_amazon_lightning_arc",
    "acoustic_black_glamour_obsidian_float",
    "acoustic_brazil_petal_carnival",
    # Element HOF 4종
    "element_bbw_water_goddess",
    "element_latina_storm_goddess",
    "element_vs_angel_ice_goddess",
    "element_hot_glamour_plasma_goddess",
    # Luxury HOF 4종
    "luxury_super_glamour_versailles",
    "luxury_amazon_dubai_penthouse",
    "luxury_latina_rio_carnival",
    "luxury_vs_angel_paris_runway",
]

HOF_ANCHOR = '"acoustic_plus_size_ice_shard_armor",'

# ══════════════════════════════════════════════════════════════════════════
# STEP 1: presets_meta.py 패치
# ══════════════════════════════════════════════════════════════════════════

def patch_presets_meta():
    print("\n[ STEP 1 ] presets_meta.py 패치 중...")
    content = META_PATH.read_text(encoding="utf-8-sig")

    results = []

    # Acoustic 확장
    if "acoustic_latina_silk_thread_web" not in content:
        anchor = '"🔊 Acoustic Levitation Glamour"'
        if anchor not in content:
            print("  ❌ Acoustic 앵커 없음")
            results.append(False)
        else:
            idx = content.find(anchor)
            block_end = content.find("],", idx)
            insert_pos = block_end + 2
            content = content[:insert_pos] + "\n" + ACOUSTIC_EXPANSION + content[insert_pos:]
            print("  ✅ Acoustic 확장 12종 추가")
            results.append(True)
    else:
        print("  ⚠️  Acoustic 확장 이미 존재 — SKIP")
        results.append(True)

    # Element
    if "element_bbw_water_goddess" not in content:
        anchor = '"🔊 Acoustic Levitation Glamour 2"'
        if anchor not in content:
            # Acoustic 2 블록이 없으면 Acoustic 1 뒤에 삽입됐을 것
            # 다시 찾기
            anchor = '"🔊 Acoustic Levitation Glamour"'
            idx = content.rfind(anchor)  # 마지막 occurrence
            block_end = content.find("],", idx)
            insert_pos = block_end + 2
        else:
            idx = content.find(anchor)
            block_end = content.find("],", idx)
            insert_pos = block_end + 2
        content = content[:insert_pos] + "\n" + ELEMENT_CATEGORY + content[insert_pos:]
        print("  ✅ Body × Element Glamour 12종 추가")
        results.append(True)
    else:
        print("  ⚠️  Element 이미 존재 — SKIP")
        results.append(True)

    # Luxury
    if "luxury_super_glamour_versailles" not in content:
        anchor = '"🔥 Body × Element Glamour"'
        if anchor not in content:
            print("  ❌ Element 앵커 없음")
            results.append(False)
        else:
            idx = content.find(anchor)
            block_end = content.find("],", idx)
            insert_pos = block_end + 2
            content = content[:insert_pos] + "\n" + LUXURY_CATEGORY + content[insert_pos:]
            print("  ✅ Body × Luxury Setting Glamour 12종 추가")
            results.append(True)
    else:
        print("  ⚠️  Luxury 이미 존재 — SKIP")
        results.append(True)

    META_PATH.write_text(content, encoding="utf-8")

    # 검증
    verify = META_PATH.read_text(encoding="utf-8")
    check_ids = [
        "acoustic_latina_silk_thread_web",
        "acoustic_amazon_lightning_arc",
        "acoustic_black_glamour_obsidian_float",
        "acoustic_brazil_petal_carnival",
        "element_bbw_water_goddess",
        "element_latina_storm_goddess",
        "element_vs_angel_ice_goddess",
        "element_hot_glamour_plasma_goddess",
        "luxury_super_glamour_versailles",
        "luxury_amazon_dubai_penthouse",
        "luxury_latina_rio_carnival",
        "luxury_vs_angel_paris_runway",
    ]
    all_ok = True
    print("\n  검증:")
    for pid in check_ids:
        ok = pid in verify
        print(f"  {'✅' if ok else '❌'} {pid}")
        if not ok:
            all_ok = False
    print(f"\n  {'✅ 전체 검증 통과' if all_ok else '❌ 일부 누락'}")


# ══════════════════════════════════════════════════════════════════════════
# STEP 2: hof_tier.py HOF 12종 추가
# ══════════════════════════════════════════════════════════════════════════

def patch_hof():
    print("\n[ STEP 2 ] hof_tier.py — HOF 12종 추가 중...")
    content = HOF_PATH.read_text(encoding="utf-8")

    to_add = [pid for pid in NEW_HOF if pid not in content]
    if not to_add:
        print("  ⚠️  모두 이미 존재 — SKIP")
        return

    if HOF_ANCHOR not in content:
        print(f"  ❌ 앵커 없음: {HOF_ANCHOR}")
        return

    new_block = "\n\n    # ── 신규 카테고리 HOF (Acoustic 확장 + Element + Luxury) ──"
    for pid in to_add:
        new_block += f'\n    "{pid}",'

    new_content = content.replace(HOF_ANCHOR, HOF_ANCHOR + new_block)
    HOF_PATH.write_text(new_content, encoding="utf-8")

    verify = HOF_PATH.read_text(encoding="utf-8")
    all_ok = True
    for pid in NEW_HOF:
        ok = pid in verify
        print(f"  {'✅' if ok else '❌'} {pid}")
        if not ok:
            all_ok = False

    print(f"\n  {'✅ HOF 패치 완료' if all_ok else '❌ 일부 누락'}")


# ══════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("patch_new_categories.py 시작")
    print("=" * 60)

    if not META_PATH.exists():
        print(f"❌ 파일 없음: {META_PATH}")
        exit(1)
    if not HOF_PATH.exists():
        print(f"❌ 파일 없음: {HOF_PATH}")
        exit(1)

    patch_presets_meta()
    patch_hof()

    print("\n" + "=" * 60)
    print("패치 완료!")
    print("=" * 60)
    print("\n다음 단계:")
    print("  git add core/presets_meta.py core/hof_tier.py")
    print('  git commit -m "feat: Acoustic확장+Element+Luxury 36종 추가 HOF 12종"')
    print("  git push")
