# -*- coding: utf-8 -*-
# Regenerates index.html from ranking_data.json (updated daily by the
# GitHub Action / scraper) + the static format-card content below.
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "index.html")

with open(os.path.join(BASE, "ranking_data.json"), encoding="utf-8") as f:
    RANKING = json.load(f)

RANK_TYPES = RANKING["rank_types"]
CATEGORIES = RANKING["categories"]
RANKINGS = RANKING["rankings"]
LAST_UPDATED = RANKING["last_updated"]

VIDS = {
    "ugc_celular": "videos/lib_ugc_celular.mp4",
    "ugc_pacote": "videos/lib_ugc_pacote.mp4",
    "ugc_blusa": "videos/lib_ugc_blusa.mp4",
    "ugc_giro360": "videos/lib_ugc_giro360.mp4",
    "ugc_posefofa": "videos/lib_ugc_posefofa.mp4",
    "ugc_look": "videos/lib_ugc_mostrandolook.mp4",
    "ugc_cta": "videos/lib_ugc_cta.mp4",
    "mirror1": "videos/fmt_mirror1_hq.mp4",
    "mirror_cabelo": "videos/lib_mirror_cabelo.mp4",
    "pov1": "videos/fmt_pov1_hq.mp4",
    "pov_colocar": "videos/lib_pov_colocar.mp4",
    "pov_esticar": "videos/lib_pov_esticar.mp4",
    "story1": "videos/fmt_story1_hq.mp4",
    "story_cores": "videos/lib_story_cores.mp4",
}

SCENE_DIR = "images/scenes"

PROPS = {
    "ugc_pacote": {
        "label": "Pacote TikTok Shop (2ª imagem de referência) — já pronto, copie e use:",
        "img": f"{SCENE_DIR}/package_tiktokshop_web.jpg",
    },
}

REQS_ICONS = {
    "model": ("\U0001f9cd‍♀️", "Foto da modelo"),
    "scene": ("\U0001f5bc️", "Foto do cenário"),
    "screenshot": ("\U0001f4f1", "Print do TikTok Shop (pra aparecer no celular)"),
    "package": ("\U0001f4e6", "Foto do pacote TikTok Shop (fornecida abaixo)"),
    "clothing": ("\U0001f455", "Foto da roupa/peça"),
}

SCENES = {
    "ugc1": [f"{SCENE_DIR}/scene_ugc_web.jpg", f"{SCENE_DIR}/scene_ugc_var1_web.jpg",
              f"{SCENE_DIR}/scene_ugc_var2_web.jpg", f"{SCENE_DIR}/scene_ugc_var3_web.jpg"],
    "mirror1": [f"{SCENE_DIR}/scene_mirror1_web.jpg", f"{SCENE_DIR}/scene_mirror2_web.jpg",
                 f"{SCENE_DIR}/scene_mirror1_var1_web.jpg", f"{SCENE_DIR}/scene_mirror1_var2_web.jpg"],
    "pov1": [f"{SCENE_DIR}/scene_pov_web.jpg", f"{SCENE_DIR}/scene_pov_table_web.jpg",
              f"{SCENE_DIR}/scene_pov_bed_web.jpg", f"{SCENE_DIR}/scene_pov_sofa_web.jpg"],
    "story1": [f"{SCENE_DIR}/scene_story1_web.jpg", f"{SCENE_DIR}/scene_story2_web.jpg",
                f"{SCENE_DIR}/scene_story1_var1_web.jpg", f"{SCENE_DIR}/scene_story1_var2_web.jpg"],
}
for _alias, _base in [
    ("ugc_celular", "ugc1"), ("ugc_pacote", "ugc1"), ("ugc_blusa", "ugc1"),
    ("ugc_giro360", "ugc1"), ("ugc_posefofa", "ugc1"), ("ugc_look", "ugc1"),
    ("ugc_cta", "ugc1"), ("mirror_cabelo", "mirror1"),
    ("pov_colocar", "pov1"), ("pov_esticar", "pov1"), ("story_cores", "story1"),
]:
    SCENES[_alias] = SCENES[_base]

CARDS = {
    "mirror1": {"tag": "MOVIMENTO NATURAL", "title": "Showcase completo", "tool": "Kling 3 / Veo 3", "reqs": ["model", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity and image reference 2 (the scenario photo below) for the room — she is photographing her own reflection in that exact mirror, matching its real position, framing, and ambient light. Her iPhone's camera flash is turned on, held clearly in her hand overlapping her torso in the reflection, and the flash's light is visible reflecting off the mirror glass as a small bright flare. Full outfit visible knees to head, casual fit (fitted top, denim shorts). Slight natural rotation of the hips, imperfect off-center framing like a real handheld mirror shot — not tripod-centered. Visible skin texture, no studio lighting, no beauty filter added on top of the scenario's real light. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. She holds the phone steady with the flash lit, tilts her head slightly and touches her hair/shoulder with her free hand as she adjusts her pose, small natural repositioning of the phone angle, and settles into a warm genuine smile by the end. Slight natural rotation of the hips, imperfect handheld mirror-shot wobble — no cuts, no zoom. ~9-10 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "pov1": {"tag": "POV", "title": "Produto visto de cima", "tool": "Seedance 2", "reqs": ["model", "scene"],
        "image_prompt": "Use image reference 1 (the model) to match her real hand/skin tone and image reference 2 (the scenario photo below) for the exact rug, plant, and light — a top-down POV flat-lay photo, shot from directly above, of her hands arranging a clothing item on that rug, a pair of sunglasses and a thin belt placed next to the garment as styling props. Hands have visible skin texture and natural nail polish, casual bracelets. Authentic phone-camera top-down framing, slightly imperfect angle, matching the scenario's real shadows. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. The hands slowly slide the garment slightly to re-center it, then one hand places the sunglasses down beside it while the other smooths a wrinkle out of the fabric — calm, deliberate top-down product-styling motion, camera locked directly overhead with no movement. ~4-5 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "story1": {"tag": "STORYBOARD", "title": "Apenas uma cor", "tool": "Kling 3 / Veo 3", "reqs": ["model", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity and image reference 2 (the scenario photo below) for the room — a frontal portrait UGC photo of her standing centered inside that exact room, matching its real light and camera height, facing the camera directly, knee-to-head framing, wearing a fitted solid-color slip dress. Relaxed confident stance, one hand resting near her hip. Visible skin texture, no studio lighting, no beauty filter added on top of the scenario's real light. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. She runs one hand through her hair and lets it settle back down, gives a slight confident shift of weight and turn of the shoulders, fabric of the dress moving naturally with the motion. Camera locked, no zoom, no cuts. ~4-5 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "ugc_celular": {"tag": "GANCHO", "title": "Print no celular", "tool": "Kling 3 / Veo 3", "reqs": ["model", "screenshot", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity, image reference 2 (the TikTok Shop screenshot below) to display on her phone screen, and image reference 3 (the scenario photo below) for the background — place her inside that exact room, matching its real lighting, perspective, and camera height. She holds her phone up with one arm extended toward the camera so the framing captures her from the knees up, the TikTok Shop screenshot clearly readable on the phone screen. Casual white tank top, denim shorts, natural everyday makeup, visible skin texture — no studio lighting, no beauty filter added on top of the scenario's real light. Front-facing phone-camera framing, knee-up, natural phone-camera color and grain. No on-screen text, no captions, no watermarks — the phone's own screen content is the only text element.",
        "motion_prompt": "Animate this exact photo. She holds the phone steady with a warm confident smile, raises her free hand and points at the screen to highlight the product, glances back at the camera with a playful head tilt and briefly touches her collarbone, then brings her free hand up covering the lens like a wipe transition. Natural handheld phone-camera motion, subtle wobble. ~5-6 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "ugc_pacote": {"tag": "TIKTOK SHOP", "title": "Segurando pacote", "tool": "Kling 3 / Veo 3", "reqs": ["model", "package", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity, image reference 2 (the TikTok Shop package below) held in her hands, and image reference 3 (the scenario photo below) for the background — place her inside that exact room, matching its real lighting, perspective, and camera height. She holds the black TikTok Shop mailer package with both hands at chest height, framing captures her from the knees up. Casual white tank top, denim shorts, natural everyday makeup, visible skin texture — no studio lighting, no beauty filter added on top of the scenario's real light. Front-facing phone-camera framing, knee-up, natural phone-camera color and grain. No on-screen text, no captions, no watermarks other than the package's own real label.",
        "motion_prompt": "Animate this exact photo. She holds the package at chest height with her eyes closed for a beat of anticipation, then excitedly shakes/flips it up near her face in a quick playful blur, and settles back into a big genuine smile holding the package steady at chest height, looking at the camera. Natural handheld phone-camera motion, subtle wobble. ~5-6 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "ugc_blusa": {"tag": "DETALHE", "title": "Segurando blusa", "tool": "Kling 3 / Veo 3", "reqs": ["model", "clothing", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity, image reference 2 (the clothing item below) held up against her torso, and image reference 3 (the scenario photo below) for the background — place her inside that exact room, matching its real lighting, perspective, and camera height. She holds the garment up by the shoulders against her chest with both hands, framing captures her from the knees up. Denim shorts, natural everyday makeup, visible skin texture — no studio lighting, no beauty filter added on top of the scenario's real light. Front-facing phone-camera framing, knee-up, natural phone-camera color and grain. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. She gently sways the garment side to side while holding it up against her chest, glancing down to check the print then back up at the camera with a soft satisfied smile. Natural handheld phone-camera motion, subtle wobble, no cuts. ~5-6 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "ugc_giro360": {"tag": "MOVIMENTO NATURAL", "title": "Giro 360°", "tool": "Kling 3 / Veo 3", "reqs": ["model", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity and image reference 2 (the scenario photo below) for the background — place her standing centered inside that exact room, matching its real lighting, perspective, and camera height, facing the camera directly, knee-to-head framing, wearing a casual halter top and denim mini skirt. Relaxed confident stance. Visible skin texture, no studio lighting, no beauty filter added on top of the scenario's real light. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. She does a slow full 360° turn to show the outfit from every angle, hair and fabric moving naturally with the motion, ending back facing the camera with a big smile. Camera locked, no zoom, no cuts. ~5-6 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "ugc_posefofa": {"tag": "GANCHO", "title": "Ligar a câmera e pose fofa", "tool": "Kling 3 / Veo 3", "reqs": ["model", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity and image reference 2 (the scenario photo below) for the background — place her standing centered inside that exact room, matching its real lighting, perspective, and camera height, facing the camera directly, knee-to-head framing, wearing a casual halter top and denim mini skirt, hands resting near her back pockets in a cute relaxed pose. Visible skin texture, no studio lighting, no beauty filter added on top of the scenario's real light. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo, as if she just turned the camera on. She gives a playful hair flip/toss with one hand, smiles warmly at the camera, then settles into a cute relaxed pose with her hands near her back pockets. Camera locked, subtle natural sway, no cuts. ~5-6 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "ugc_look": {"tag": "MOVIMENTO NATURAL", "title": "Mostrando o look", "tool": "Kling 3 / Veo 3", "reqs": ["model", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity and image reference 2 (the scenario photo below) for the background — place her standing centered inside that exact room, matching its real lighting, perspective, and camera height, facing the camera directly, knee-to-head framing, wearing a casual halter top and denim mini skirt, confident relaxed stance. Visible skin texture, no studio lighting, no beauty filter added on top of the scenario's real light. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. She shifts her weight and leans slightly side to side to show off the outfit, runs a hand through her hair and tucks it back, smiling confidently at the camera throughout. Camera locked, no zoom, no cuts. ~5-6 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "ugc_cta": {"tag": "CTA", "title": "CTA", "tool": "Kling 3 / Veo 3", "reqs": ["model", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity and image reference 2 (the scenario photo below) for the background — place her standing centered inside that exact room, matching its real lighting, perspective, and camera height, facing the camera directly, knee-to-head framing, wearing a casual halter top and denim mini skirt, warm inviting smile, direct eye contact with the camera. Visible skin texture, no studio lighting, no beauty filter added on top of the scenario's real light. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. She leans in closer toward the camera with a warm genuine smile, pointing downward with a repeated beckoning finger motion as if directing viewers to a link or button below, maintaining direct eye contact throughout. Natural handheld phone-camera motion, subtle wobble. ~5-6 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "mirror_cabelo": {"tag": "MOVIMENTO NATURAL", "title": "Cabelo e aponta pra baixo", "tool": "Kling 3 / Veo 3", "reqs": ["model", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity and image reference 2 (the scenario photo below) for the room — she is photographing her own reflection in that exact mirror, matching its real position, framing, and ambient light. Her iPhone's camera flash is turned on, held in one hand, and the flash's light is visible reflecting off the mirror glass as a bright flare/starburst. Her other hand is raised, running through her hair. Full outfit visible knees to head, casual fit. Visible skin texture, no studio lighting, no beauty filter added on top of the scenario's real light. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. She runs her free hand through her hair, fluffing her curls, then glides that hand down along her neck and collarbone, phone with the flash lit staying steady in her other hand, subtle natural mirror-shot wobble. ~9-10 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "pov_colocar": {"tag": "TIKTOK SHOP", "title": "Colocando roupa no cenário", "tool": "Seedance 2", "reqs": ["clothing", "scene"],
        "note": "O último frame do vídeo de referência é a composição final (flat-lay pronto) — gere a imagem mirando nesse resultado.",
        "image_prompt": "Use image reference 1 (the clothing photo below) and image reference 2 (the scenario photo below) for the exact rug, plant, and light — a top-down POV flat-lay photo, shot from directly above, of the clothing item neatly arranged on that rug (matching the final arranged layout, not mid-placement), a thin belt and a pair of sunglasses placed next to it as styling props, one hand entering the frame from the bottom corner holding the sunglasses. Natural skin texture and nail polish on the hand. Authentic phone-camera top-down framing, slightly imperfect angle, matching the scenario's real shadows. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. The hand slowly slides the sunglasses into their final position beside the garment, then smooths a small wrinkle out of the fabric — calm, deliberate top-down product-styling motion, camera locked directly overhead with no movement. ~5-6 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "pov_esticar": {"tag": "DETALHE", "title": "Esticar tecido", "tool": "Seedance 2", "reqs": ["clothing", "scene"],
        "image_prompt": "Use image reference 1 (the clothing photo below) and image reference 2 (the scenario photo below) for the exact rug, plant, and light — a top-down POV flat-lay photo, shot from directly above, of the clothing item neatly arranged on that rug next to a thin belt and a pair of sunglasses, with both hands entering the frame from the bottom corners gripping the garment's waistband. Natural skin texture and nail polish on the hands. Authentic phone-camera top-down framing, slightly imperfect angle, matching the scenario's real shadows. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo. Both hands gently pull the garment's waistband taut to show the fabric's stretch and quality, then release it back to its relaxed shape — calm, deliberate top-down product motion, camera locked directly overhead with no movement. ~5-6 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
    "story_cores": {"tag": "STORYBOARD", "title": "Cores diferentes", "tool": "Kling 3 / Veo 3", "reqs": ["model", "scene"],
        "image_prompt": "Use image reference 1 (the model) for identity and image reference 2 (the scenario photo below) for the room — a frontal portrait UGC photo of her standing centered inside that exact room, matching its real light and camera height, facing the camera directly, knee-to-head framing, wearing a fitted halter-neck slip dress with a ruched center front and a thigh-high slit, in a soft pastel yellow. Relaxed confident stance, hands at her sides. Visible skin texture, no studio lighting, no beauty filter added on top of the scenario's real light. No on-screen text, no captions, no watermarks.",
        "motion_prompt": "Animate this exact photo, keeping her pose and the camera completely locked. The dress color snap-transitions through 3 solid colors in rhythm — pastel yellow, then chocolate brown, then deep burgundy wine — like a quick outfit-color-swap trend edit, same exact dress design and fit each time, ending on the burgundy version. ~4-5 seconds. No on-screen text, no captions, no subtitles, no watermarks."},
}

TABS = [
    ("ugc", "UGC", ["ugc_celular", "ugc_pacote", "ugc_blusa", "ugc_giro360", "ugc_posefofa", "ugc_look", "ugc_cta"]),
    ("mirror", "Mirror Selfie", ["mirror1", "mirror_cabelo"]),
    ("pov", "POV", ["pov1", "pov_colocar", "pov_esticar"]),
    ("story", "Storyboard", ["story1", "story_cores"]),
]
PLACEHOLDER_COUNTS = {"ugc": 0, "mirror": 0, "pov": 1, "story": 0}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def card_html(key):
    c = CARDS[key]
    return f'''<div class="fmt-card">
    <div class="fmt-thumb">
      <video autoplay muted loop playsinline preload="auto" src="{VIDS[key]}"></video>
      <span class="fmt-tag">{c["tag"]}</span>
    </div>
    <div class="fmt-cap">
      <h3>{esc(c["title"])}</h3>
      <button class="btn-formato" data-card="{key}">Fazer esse formato!</button>
    </div>
  </div>'''


def placeholder_html(i):
    return f'''<div class="fmt-card placeholder">
    <div class="fmt-thumb placeholder"><span class="soon">EM BREVE</span></div>
    <div class="fmt-cap">
      <h3>Formato #{i}</h3>
      <button class="btn-formato" disabled>Fazer esse formato!</button>
    </div>
  </div>'''


panels = []
for tab_id, label, real_keys in TABS:
    cards = "\n  ".join(card_html(k) for k in real_keys)
    n_placeholders = PLACEHOLDER_COUNTS[tab_id]
    placeholders = "\n  ".join(placeholder_html(i + 1) for i in range(n_placeholders))
    active = "active" if tab_id == "ugc" else ""
    panels.append(f'''<div class="fmt-panel {active}" data-panel="{tab_id}">
  <div class="fmt-row-wrap">
    <button class="fmt-arrow fmt-arrow-left" data-scroll="-1" aria-label="Voltar">&#8249;</button>
    <div class="fmt-row">
    {cards}
    {placeholders}
    </div>
    <button class="fmt-arrow fmt-arrow-right" data-scroll="1" aria-label="Avan&ccedil;ar">&#8250;</button>
  </div>
</div>''')
panels_html = "\n\n".join(panels)

tabs_html = "\n      ".join(
    f'<button class="fmt-tab{" active" if i == 0 else ""}" data-tab="{tid}">{label}</button>'
    for i, (tid, label, _) in enumerate(TABS)
)


def scene_thumb_html(src, alt):
    return f'''<div class="scene-thumb-wrap">
          <img class="scene-thumb" src="{src}" alt="{alt}" loading="lazy">
          <button class="btn-copy-img" data-copy-img title="Copiar imagem">&#128203;</button>
        </div>'''


def scene_preview_html(key):
    variants = SCENES.get(key)
    if not variants:
        return ""
    row = "".join(scene_thumb_html(v, "Variação de cenário") for v in variants)
    return f'''<div class="scene-preview">
        <span class="scene-preview-label">Cen&aacute;rio (2&ordm; imagem de refer&ecirc;ncia, junto com a foto da sua modelo) &mdash; escolha uma varia&ccedil;&atilde;o:</span>
        <div class="scene-row">{row}</div>
      </div>'''


def prop_preview_html(key):
    prop = PROPS.get(key)
    if not prop:
        return ""
    return f'''<div class="scene-preview">
        <span class="scene-preview-label">{prop["label"]}</span>
        {scene_thumb_html(prop["img"], "Imagem pronta pra usar")}
      </div>'''


def reqs_html(c):
    chips = "".join(
        f'<span class="reqs-chip"><span class="reqs-icon">{REQS_ICONS[r][0]}</span>{REQS_ICONS[r][1]}</span>'
        for r in c.get("reqs", [])
    )
    if not chips:
        return ""
    return f'''<div class="modal-reqs">
      <span class="modal-reqs-label">O que voc&ecirc; precisa:</span>
      <div class="modal-reqs-row">{chips}</div>
    </div>'''


CLOTHING_SWAP_PROMPT = (
    "Using the photo above as the base image, change ONLY her outfit: "
    "dress her in the exact clothing item from the product photo you "
    "attach as a second reference — match its color, fabric, print, cut, "
    "and length precisely, fitting it naturally to her pose and body. "
    "Keep her identity, face, pose, expression, hair, the background, and "
    "the lighting completely unchanged. Photorealistic, seamless edit, no "
    "other changes, no on-screen text, no watermarks."
)


def modal_block_html(step_num, title, text, copy_target, extra=""):
    return f'''<div class="modal-block">
      <div class="modal-block-head">
        <span class="modal-step">{step_num}</span>
        <h3>{title}</h3>
      </div>
      <textarea readonly>{esc(text)}</textarea>
      <button class="btn-copy" data-copy-target="{copy_target}">Copiar Prompt</button>
      {extra}
    </div>'''


def modal_html(key, c):
    has_model = "model" in c.get("reqs", [])
    note = f'<p class="modal-note">{c["note"]}</p>' if c.get("note") else ""
    step1_extra = note + prop_preview_html(key) + scene_preview_html(key)
    blocks = [modal_block_html(1, "Prompt de imagem &mdash; gera sua modelo nesse cen&aacute;rio", c["image_prompt"], f"img-{key}", step1_extra)]
    step = 2
    if has_model:
        blocks.append(modal_block_html(step, "Prompt para vestir sua modelo com uma pe&ccedil;a do TikTok Shop", CLOTHING_SWAP_PROMPT, f"swap-{key}"))
        step += 1
    blocks.append(modal_block_html(step, f"Prompt de v&iacute;deo ({c['tool']}) &mdash; anima ela se movendo assim", c["motion_prompt"], f"mov-{key}"))
    blocks_html = "\n".join(blocks)
    return f'''<div class="modal" id="modal-{key}">
  <div class="modal-inner">
    <button class="modal-close" data-close>&times;</button>
    <span class="modal-tag">{c["tag"]} &middot; {esc(c["title"])}</span>
    <h2>Fazer esse formato</h2>
    {reqs_html(c)}
    {blocks_html}
  </div>
</div>'''


modals_html = "\n".join(modal_html(key, c) for key, c in CARDS.items())


def rank_card_html(modal_id, i, row):
    metrics = "".join(f'<span class="rank-metric"><b>{esc(l)}</b> {esc(v)}</span>' for l, v in row["metrics"])
    return f'''<button class="rank-card" data-rank-modal="{modal_id}" type="button">
        <span class="rank-num">{i}</span>
        <img class="rank-img" src="{row["img"]}" alt="{esc(row["title"])}" loading="lazy">
        <div class="rank-info">
          <h4>{esc(row["title"])}</h4>
          <div class="rank-price">{esc(row["price"])} &middot; {esc(row["store"])}</div>
          <div class="rank-metrics">{metrics}</div>
        </div>
      </button>'''


REPORT_FIELDS = [
    ("rankRange", "Ranking (faixa)"), ("popularityIndex", "Índice de popularidade"),
    ("vendasTotais", "Vendas totais"), ("gmvTotal", "GMV total"),
    ("numInfluencers", "N° de influenciadores"), ("price", "Preço"),
    ("frete", "Frete"), ("tipoLogistica", "Tipo de logística"),
    ("comissao", "Taxa de comissão"), ("dataUpload", "Data estimada de upload"),
]


def rank_modal_html(modal_id, row):
    d = row.get("detail")
    imgs = (d["imgs"] if d else None) or [row["img"]]
    gallery = "".join(
        f'''<div class="rank-gallery-item">
          <img src="{src}" alt="{esc(row["title"])}" loading="lazy">
          <button class="btn-copy-img small" data-copy-img title="Copiar imagem">&#128203;</button>
        </div>''' for src in imgs
    )
    if d:
        report_rows = "".join(
            f'<div class="rank-report-row"><span>{esc(label)}</span><b>{esc(d.get(key) or "-")}</b></div>'
            for key, label in REPORT_FIELDS
        )
    else:
        report_rows = '<p class="modal-note">Relatório detalhado indisponível pra este produto no momento.</p>'
    list_metrics = "".join(f'<span class="rank-metric"><b>{esc(l)}</b> {esc(v)}</span>' for l, v in row["metrics"])
    return f'''<div class="modal" id="{modal_id}">
  <div class="modal-inner rank-modal-inner">
    <button class="modal-close" data-close>&times;</button>
    <span class="modal-tag">{esc(row["store"])}</span>
    <h2>{esc(row["title"])}</h2>
    <div class="rank-report" style="margin-bottom:18px;"><div class="rank-report-row"><span>Loja</span><b>{esc(row["store"])}</b></div><div class="rank-report-row"><span>Pre&ccedil;o de venda</span><b>{esc(row["price"])}</b></div></div>
    <div class="modal-block">
      <div class="modal-block-head"><h3>Imagens liberadas &mdash; clique pra copiar</h3></div>
      <div class="rank-gallery">{gallery}</div>
    </div>
    <div class="modal-block">
      <div class="modal-block-head"><h3>Métricas do ranking</h3></div>
      <div class="rank-metrics">{list_metrics}</div>
    </div>
    <div class="modal-block">
      <div class="modal-block-head"><h3>Relatório do produto</h3></div>
      <div class="rank-report">{report_rows}</div>
    </div>
  </div>
</div>'''


rank_type_tabs_html = "\n      ".join(
    f'<button class="fmt-tab{" active" if i == 0 else ""}" data-rank="{rid}">{label}</button>'
    for i, (rid, label) in enumerate(RANK_TYPES)
)
rank_cat_tabs_html = "\n      ".join(
    f'<button class="fmt-tab{" active" if i == 0 else ""}" data-cat="{cid}">{label}</button>'
    for i, (cid, label) in enumerate(CATEGORIES)
)

rank_panels = []
rank_modals = []
for rid, _ in RANK_TYPES:
    for cid, _ in CATEGORIES:
        rows = RANKINGS[rid][cid]
        cards = []
        for i, r in enumerate(rows):
            modal_id = f"rank-modal-{rid}-{cid}-{i}"
            cards.append(rank_card_html(modal_id, i + 1, r))
            rank_modals.append(rank_modal_html(modal_id, r))
        cards_html = "\n    ".join(cards)
        active = "active" if (rid == RANK_TYPES[0][0] and cid == CATEGORIES[0][0]) else ""
        rank_panels.append(f'''<div class="rank-panel {active}" data-rank="{rid}" data-cat="{cid}">
    <div class="rank-grid">
    {cards_html}
    </div>
  </div>''')
rank_panels_html = "\n".join(rank_panels)
rank_modals_html = "\n".join(rank_modals)


BODY = f"""<div class="top-nav">
  <button class="top-nav-btn active" data-section="formats">Criar formatos de IA</button>
  <button class="top-nav-btn" data-section="ranking">Ranking Top 5</button>
</div>

<div class="section active" data-section="formats">
<div class="wrap">
  <div class="head">
    <span class="eyebrow">Aula 2 &middot; Biblioteca TikTok Shop</span>
    <h1>Formatos validados, prontos pra usar</h1>
    <p>Escolha um formato, clique em "Fazer esse formato!" e copie os prompts &mdash; gerar sua modelo no cen&aacute;rio, vestir a pe&ccedil;a do TikTok Shop e anim&aacute;-la se movendo igual no v&iacute;deo.</p>
  </div>
  <div class="fmt-tabs">
      {tabs_html}
  </div>
  <div class="fmt-panels">
{panels_html}
  </div>
</div>
{modals_html}
</div>

<div class="section" data-section="ranking">
<div class="wrap">
  <div class="head">
    <span class="eyebrow">Aula 2 &middot; Radar de produtos</span>
    <h1>Ranking Top 5 &mdash; TikTok Shop Brasil</h1>
    <p>Os produtos que mais vendem, mais recentes e mais promovidos em v&iacute;deo agora no TikTok Shop, direto do FastMoss.</p>
  </div>
  <div class="rank-meta">
    <span>&Uacute;ltima coleta: {LAST_UPDATED}</span>
    <span>Pr&oacute;xima atualiza&ccedil;&atilde;o em <span class="rank-countdown" id="rank-countdown">--:--:--</span></span>
  </div>
  <div class="fmt-tabs rank-type-tabs">
      {rank_type_tabs_html}
  </div>
  <div class="fmt-tabs rank-cat-tabs">
      {rank_cat_tabs_html}
  </div>
  <div class="rank-panels">
{rank_panels_html}
  </div>
</div>
</div>

{rank_modals_html}
"""

CSS = """
  :root{--bg:#0a0c09;--bg-raised:#12160f;--bg-card:#171c13;--line:#2a3122;--line-soft:#1d2317;--ink:#f3f5ee;--ink-dim:#a7ae9c;--ink-faint:#6f7566;--green:#35e17e;--green-ink:#04120a;--amber:#ffc845;--amber-ink:#241a02;}
  *{box-sizing:border-box;}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:'Plus Jakarta Sans',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}
  h1,h2,h3{font-family:'Unbounded','Plus Jakarta Sans',sans-serif;margin:0;}
  .eyebrow{font-family:'JetBrains Mono',monospace;font-size:12.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--green);}
  .wrap{max-width:1080px;margin:0 auto;padding:48px 24px;}
  .head{max-width:640px;margin:0 auto 40px;text-align:center;}
  .head h1{font-size:clamp(26px,4vw,36px);font-weight:800;margin-top:12px;}
  .head p{color:var(--ink-dim);margin-top:12px;font-size:15.5px;line-height:1.6;}
  .fmt-tabs{display:flex;justify-content:center;gap:8px;flex-wrap:wrap;margin:0 auto 30px;}
  .fmt-tab{appearance:none;border:1px solid var(--line);cursor:pointer;background:var(--bg-card);color:var(--ink-dim);font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-size:13.5px;padding:10px 18px;border-radius:100px;transition:all .15s ease;}
  .fmt-tab.active{background:var(--green);color:var(--green-ink);border-color:var(--green);}
  .fmt-panel{display:none;}
  .fmt-panel.active{display:block;}
  .fmt-row-wrap{display:flex;align-items:center;gap:8px;}
  .fmt-row{display:flex;gap:16px;overflow-x:auto;padding:4px 4px 12px;scroll-snap-type:x proximity;scroll-behavior:smooth;flex:1 1 auto;min-width:0;scrollbar-width:none;-ms-overflow-style:none;}
  .fmt-row::-webkit-scrollbar{display:none;}
  .fmt-arrow{flex:none;width:36px;height:36px;border-radius:50%;border:1px solid var(--line);background:var(--bg-card);color:var(--ink);font-size:20px;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .15s ease,border-color .15s ease;}
  .fmt-arrow:hover{background:var(--green);color:var(--green-ink);border-color:var(--green);}
  @media (max-width:640px){ .fmt-arrow{width:30px;height:30px;font-size:17px;} }
  .fmt-card{flex:none;width:220px;scroll-snap-align:start;border:1px solid var(--line);border-radius:16px;overflow:hidden;background:var(--bg-card);}
  .fmt-thumb{aspect-ratio:9/16;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;}
  .fmt-thumb video{width:100%;height:100%;object-fit:cover;background:#000;}
  .fmt-thumb.placeholder{background:radial-gradient(circle at 50% 30%,rgba(255,200,69,.10),transparent 60%),#0f1310;}
  .fmt-thumb .soon{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;letter-spacing:.08em;color:var(--ink-faint);border:1px dashed var(--line);padding:8px 14px;border-radius:100px;}
  .fmt-tag{position:absolute;left:10px;top:10px;z-index:2;font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);background:rgba(0,0,0,.55);border:1px solid rgba(255,255,255,.15);padding:4px 9px;border-radius:100px;}
  .fmt-cap{padding:14px;}
  .fmt-cap h3{font-size:14px;font-weight:700;font-family:'Plus Jakarta Sans',sans-serif;margin-bottom:10px;}
  .btn-formato{appearance:none;border:none;cursor:pointer;width:100%;font-family:'Unbounded',sans-serif;font-weight:700;font-size:12.5px;background:var(--amber);color:var(--amber-ink);padding:11px 10px;border-radius:100px;transition:transform .15s ease,filter .15s ease;}
  .btn-formato:hover{transform:translateY(-1px);filter:brightness(1.06);}
  .btn-formato:disabled{background:var(--bg-raised);color:var(--ink-faint);cursor:not-allowed;}
  .modal{display:none;position:fixed;inset:0;z-index:100;background:rgba(5,6,4,.82);align-items:center;justify-content:center;padding:24px;}
  .modal.open{display:flex;}
  .modal-inner{position:relative;max-width:640px;width:100%;max-height:86vh;overflow-y:auto;background:var(--bg-raised);border:1px solid var(--line);border-radius:20px;padding:32px;}
  .modal-close{position:absolute;top:16px;right:16px;background:none;border:none;color:var(--ink-dim);font-size:26px;line-height:1;cursor:pointer;}
  .modal-tag{font-family:'JetBrains Mono',monospace;font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--green);}
  .modal-inner h2{font-size:22px;font-weight:800;margin:8px 0 16px;}
  .modal-reqs{background:var(--bg-card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin-bottom:22px;}
  .modal-reqs-label{display:block;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-faint);margin-bottom:10px;}
  .modal-reqs-row{display:flex;gap:8px;flex-wrap:wrap;}
  .reqs-chip{display:inline-flex;align-items:center;gap:6px;background:var(--bg-raised);border:1px solid var(--line);border-radius:100px;padding:6px 12px 6px 8px;font-size:12.5px;color:var(--ink-dim);}
  .reqs-icon{font-size:15px;line-height:1;}
  .modal-note{font-size:12.5px;color:var(--amber);background:rgba(255,200,69,.08);border:1px dashed var(--amber);border-radius:10px;padding:9px 12px;margin-bottom:10px;}
  .modal-block{margin-bottom:22px;}
  .modal-block-head{display:flex;align-items:center;gap:10px;margin-bottom:10px;}
  .modal-step{flex:none;width:22px;height:22px;border-radius:50%;background:var(--green);color:var(--green-ink);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:12px;}
  .modal-block-head h3{font-size:14.5px;font-weight:700;font-family:'Plus Jakarta Sans',sans-serif;}
  .modal-block textarea{width:100%;min-height:130px;resize:vertical;background:var(--bg-card);color:var(--ink-dim);border:1px solid var(--line);border-radius:12px;padding:14px;font-size:13px;line-height:1.55;font-family:'JetBrains Mono',monospace;margin-bottom:10px;}
  .btn-copy{appearance:none;border:none;cursor:pointer;font-family:'Unbounded',sans-serif;font-weight:700;font-size:12.5px;background:var(--green);color:var(--green-ink);padding:10px 18px;border-radius:100px;}
  .btn-copy.copied{background:var(--amber);}
  .scene-preview{margin-top:16px;padding-top:16px;border-top:1px dashed var(--line);}
  .scene-preview-label{display:block;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-faint);margin-bottom:10px;}
  .scene-row{display:flex;gap:10px;flex-wrap:wrap;}
  .scene-thumb{display:block;width:104px;aspect-ratio:9/16;object-fit:cover;border-radius:10px;border:1px solid var(--line);}
  .scene-thumb-wrap{position:relative;display:inline-block;}
  .btn-copy-img{position:absolute;bottom:6px;right:6px;width:26px;height:26px;border-radius:50%;border:1px solid rgba(255,255,255,.18);background:rgba(5,6,4,.72);color:var(--ink);font-size:12px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .15s ease;}
  .btn-copy-img.copied{background:var(--amber);color:var(--amber-ink);border-color:var(--amber);}
  .top-nav{display:flex;justify-content:center;gap:10px;padding:40px 24px 0;}
  .top-nav-btn{appearance:none;border:1px solid var(--line);cursor:pointer;background:var(--bg-card);color:var(--ink-dim);font-family:'Unbounded',sans-serif;font-weight:700;font-size:13px;padding:12px 22px;border-radius:100px;transition:all .15s ease;}
  .top-nav-btn.active{background:var(--amber);color:var(--amber-ink);border-color:var(--amber);}
  .section{display:none;}
  .section.active{display:block;}
  .rank-meta{display:flex;justify-content:center;align-items:center;gap:18px;flex-wrap:wrap;margin:-8px 0 26px;font-size:13px;color:var(--ink-dim);}
  .rank-countdown{color:#ff4949;font-weight:800;font-family:'JetBrains Mono',monospace;font-size:15px;background:rgba(255,73,73,.1);border:1px solid rgba(255,73,73,.35);border-radius:8px;padding:3px 9px;}
  .rank-type-tabs,.rank-cat-tabs{margin-bottom:16px;}
  .rank-cat-tabs .fmt-tab{font-size:12px;padding:8px 14px;}
  .rank-cat-tabs{margin-bottom:26px;}
  .rank-panel{display:none;}
  .rank-panel.active{display:block;}
  .rank-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px;}
  .rank-card{appearance:none;font-family:inherit;text-align:left;cursor:pointer;display:flex;gap:12px;background:var(--bg-card);border:1px solid var(--line);border-radius:14px;padding:12px;position:relative;transition:border-color .15s ease,transform .15s ease;}
  .rank-card:hover{border-color:var(--green);transform:translateY(-1px);}
  .rank-num{position:absolute;top:8px;left:8px;background:var(--green);color:var(--green-ink);width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;z-index:2;}
  .rank-img{width:64px;height:64px;object-fit:cover;border-radius:10px;flex:none;background:#0f1310;display:block;}
  .btn-copy-img.small{width:18px;height:18px;font-size:9px;bottom:3px;right:3px;}
  .rank-info{min-width:0;}
  .rank-info h4{font-size:12.5px;font-weight:700;margin:0 0 5px;line-height:1.32;color:var(--ink);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
  .rank-price{font-size:11.5px;color:var(--ink-dim);margin-bottom:7px;}
  .rank-metrics{display:flex;flex-wrap:wrap;gap:5px;}
  .rank-metric{font-size:10px;color:var(--ink-faint);background:var(--bg-raised);border:1px solid var(--line-soft);border-radius:100px;padding:3px 8px;}
  .rank-metric b{color:var(--ink-dim);font-weight:700;}
  .rank-modal-inner{max-width:560px;}
  .rank-gallery{display:flex;gap:10px;flex-wrap:wrap;}
  .rank-gallery-item{position:relative;flex:none;}
  .rank-gallery-item img{width:96px;height:96px;object-fit:cover;border-radius:10px;border:1px solid var(--line);display:block;}
  .rank-report{display:flex;flex-direction:column;gap:0;border:1px solid var(--line);border-radius:12px;overflow:hidden;}
  .rank-report-row{display:flex;justify-content:space-between;gap:12px;padding:9px 14px;font-size:12.5px;border-bottom:1px solid var(--line-soft);background:var(--bg-card);}
  .rank-report-row:last-child{border-bottom:none;}
  .rank-report-row span{color:var(--ink-faint);}
  .rank-report-row b{color:var(--ink);font-weight:700;text-align:right;}
"""

JS = """
(function(){
  var tabs = document.querySelectorAll('.fmt-tab');
  var panels = document.querySelectorAll('.fmt-panel');
  function playVideosIn(el){ el.querySelectorAll('video').forEach(function(v){ var p=v.play(); if(p&&p.catch) p.catch(function(){}); }); }
  tabs.forEach(function(tab){
    tab.addEventListener('click', function(){
      var name = tab.getAttribute('data-tab');
      tabs.forEach(function(t){ t.classList.toggle('active', t===tab); });
      panels.forEach(function(p){
        var isActive = p.getAttribute('data-panel')===name;
        p.classList.toggle('active', isActive);
        if(isActive) playVideosIn(p);
      });
    });
  });
  function playAllAutoplay(){ document.querySelectorAll('video[autoplay]').forEach(function(v){ var p=v.play(); if(p&&p.catch) p.catch(function(){}); }); }
  playAllAutoplay();
  ['click','touchstart','scroll'].forEach(function(evt){ document.addEventListener(evt, playAllAutoplay, {once:true, passive:true}); });

  document.querySelectorAll('.rank-card[data-rank-modal]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var modal = document.getElementById(btn.getAttribute('data-rank-modal'));
      if(modal) modal.classList.add('open');
    });
  });

  document.querySelectorAll('.top-nav-btn').forEach(function(btn){
    btn.addEventListener('click', function(){
      var name = btn.getAttribute('data-section');
      document.querySelectorAll('.top-nav-btn').forEach(function(b){ b.classList.toggle('active', b===btn); });
      document.querySelectorAll('.section').forEach(function(s){ s.classList.toggle('active', s.getAttribute('data-section')===name); });
    });
  });

  var currentRank='vendas', currentCat='todos';
  function showRankPanel(){
    document.querySelectorAll('.rank-panel').forEach(function(p){
      p.classList.toggle('active', p.getAttribute('data-rank')===currentRank && p.getAttribute('data-cat')===currentCat);
    });
  }
  document.querySelectorAll('.rank-type-tabs .fmt-tab').forEach(function(btn){
    btn.addEventListener('click', function(){
      currentRank = btn.getAttribute('data-rank');
      document.querySelectorAll('.rank-type-tabs .fmt-tab').forEach(function(b){ b.classList.toggle('active', b===btn); });
      showRankPanel();
    });
  });
  document.querySelectorAll('.rank-cat-tabs .fmt-tab').forEach(function(btn){
    btn.addEventListener('click', function(){
      currentCat = btn.getAttribute('data-cat');
      document.querySelectorAll('.rank-cat-tabs .fmt-tab').forEach(function(b){ b.classList.toggle('active', b===btn); });
      showRankPanel();
    });
  });

  function updateCountdown(){
    var el = document.getElementById('rank-countdown');
    if(!el) return;
    var fmt = new Intl.DateTimeFormat('en-US', {timeZone:'America/Sao_Paulo', hour12:false, year:'numeric', month:'2-digit', day:'2-digit', hour:'2-digit', minute:'2-digit', second:'2-digit'});
    var parts = fmt.formatToParts(new Date());
    function get(t){ var p = parts.find(function(x){ return x.type===t; }); return p?parseInt(p.value,10):0; }
    var y=get('year'), mo=get('month')-1, d=get('day'), h=get('hour'), mi=get('minute'), s=get('second');
    var nowSP = Date.UTC(y,mo,d,h,mi,s);
    var target = Date.UTC(y,mo,d,18,0,0);
    if(nowSP>=target){ target = Date.UTC(y,mo,d+1,18,0,0); }
    var diff = target-nowSP;
    var hh=Math.floor(diff/3600000), mm=Math.floor((diff%3600000)/60000), ss=Math.floor((diff%60000)/1000);
    function pad(n){ return (n<10?'0':'')+n; }
    el.textContent = pad(hh)+':'+pad(mm)+':'+pad(ss);
  }
  updateCountdown();
  setInterval(updateCountdown, 1000);

  document.querySelectorAll('.fmt-arrow').forEach(function(btn){
    btn.addEventListener('click', function(){
      var row = btn.parentElement.querySelector('.fmt-row');
      if(!row) return;
      var dir = parseInt(btn.getAttribute('data-scroll'),10)||1;
      var cardEl = row.querySelector('.fmt-card');
      var step = (cardEl?cardEl.getBoundingClientRect().width:220)+16;
      row.scrollBy({left: dir*step*2, behavior:'smooth'});
    });
  });
  document.querySelectorAll('.btn-formato[data-card]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var modal = document.getElementById('modal-'+btn.getAttribute('data-card'));
      if(modal) modal.classList.add('open');
    });
  });
  document.querySelectorAll('.modal').forEach(function(modal){
    modal.addEventListener('click', function(e){
      if(e.target===modal || e.target.hasAttribute('data-close')) modal.classList.remove('open');
    });
  });
  document.querySelectorAll('.btn-copy-img').forEach(function(btn){
    btn.addEventListener('click', function(){
      var wrap = btn.parentElement;
      var img = wrap.querySelector('img');
      function flash(symbol){
        var old = btn.innerHTML;
        btn.innerHTML = symbol;
        btn.classList.add('copied');
        setTimeout(function(){ btn.innerHTML = old; btn.classList.remove('copied'); }, 1600);
      }
      fetch(img.src).then(function(r){ return r.blob(); }).then(function(blob){
        return navigator.clipboard.write([new ClipboardItem({ [blob.type]: blob })]);
      }).then(function(){ flash('&#10003;'); }).catch(function(){
        navigator.clipboard.writeText(img.src).then(function(){ flash('&#128279;'); }).catch(function(err){ console.error('copy image failed', err); });
      });
    });
  });
  document.querySelectorAll('.btn-copy').forEach(function(btn){
    btn.addEventListener('click', function(){
      var block = btn.closest('.modal-block');
      var text = block.querySelector('textarea').value;
      navigator.clipboard.writeText(text).then(function(){
        btn.classList.add('copied');
        var old = btn.textContent;
        btn.textContent = 'Copiado!';
        setTimeout(function(){ btn.classList.remove('copied'); btn.textContent = old; }, 1600);
      });
    });
  });
})();
"""

HTML = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Biblioteca TikTok Shop &mdash; M&eacute;todo UGC</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap">
<style>{CSS}</style>
</head>
<body>
{BODY}
<script>{JS}</script>
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print("wrote", OUT, "size", len(HTML))
