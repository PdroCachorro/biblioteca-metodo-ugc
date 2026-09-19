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
    ("pov", "POV", ["pov_colocar", "pov_esticar"]),
    ("story", "Storyboard", ["story1", "story_cores"]),
]
PLACEHOLDER_COUNTS = {"ugc": 0, "mirror": 0, "pov": 0, "story": 0}


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


MODEL_PROMPTS = [
    {
        "title": "Modelo em fundo branco",
        "note": "Retrato de cintura pra cima, fundo branco liso &mdash; sua refer&ecirc;ncia clara antes de colocar a modelo em qualquer cen&aacute;rio.",
        "prompt": (
            "Using the uploaded reference photo as the identity source, generate a clean waist-up portrait of the same woman on a seamless pure white background (#ffffff).\n"
            "The subject must face the camera directly in a fully front-facing position. Keep the camera at eye level. Her head, face, shoulders, chest, and torso should be square to the camera, with both shoulders equally visible and no noticeable body rotation. Avoid 3/4 views, side angles, profile views, turned shoulders, or a tilted torso.\n"
            "Pose: neutral standing posture, shoulders relaxed, body centered, natural relaxed expression, looking directly into the camera. No forced smile.\n"
            "Wardrobe: keep the exact same outfit worn in the uploaded reference photo - same garment, color, fabric, and fit, unchanged.\n"
            "Lighting: soft, even studio lighting from the front-left with gentle fill from the opposite side. Balanced exposure, no harsh shadows, no dramatic contrast, and no color cast.\n"
            "Realism: preserve the identity, facial structure, and natural proportions from the reference image. Show realistic skin texture, visible pores, subtle imperfections, and natural asymmetry. No beauty filter, no excessive retouching, no AI smoothing, and no plastic or waxy skin.\n"
            "Composition: vertical waist-up portrait, centered subject, straightforward frontal composition, seamless pure white background, 4:5 aspect ratio, no text, no watermark."
        ),
    },
    {
        "title": "Ficha de referência (4 ângulos)",
        "note": "Frente, perfil e costas numa composi&ccedil;&atilde;o s&oacute; &mdash; trava a identidade antes de gerar qualquer coisa nova.",
        "prompt": (
            "Using the uploaded reference photo as the identity and outfit source, create a hyper-realistic UGC model reference sheet designed as a neutral identity matrix for future TikTok Shop and ecommerce content. Show the same person consistently across multiple angles in one clean composition. Include a full-body front view on the left, a centered close-up front portrait, a right-facing side profile, and a rear three-quarter or back-angle profile. The goal is to establish a strong visual identity anchor for future image and video generation in any angle.\n"
            "The person should have a broadly marketable, relatable UGC creator look with natural commercial appeal, visually neutral and adaptable across many ecommerce niches. Do not stylize the subject too much. Keep the appearance balanced, versatile, and realistic. Natural skin texture with visible pores and subtle imperfections, natural unstyled hair, realistic facial proportions, realistic body proportions. Wardrobe: keep the exact same outfit worn in the uploaded reference photo - same garment, color, fabric, and fit, identical across all four angles - no logos added, no accessories that dominate the look, no extreme fashion elements.\n"
            "Expression should be neutral and calm, with a slight natural closed-mouth expression. Maintain strong identity consistency across every angle, preserving the exact same face, hair, body shape, and outfit. Pose should be stable and reference-like, similar to a professional model turnaround sheet. Background should be plain light gray or soft neutral studio backdrop, clean and minimal. No text, no captions, no UI, no phone frame, no Instagram story elements, no iPhone HUD, no watermarks.\n"
            "Style: modern iPhone camera quality, unedited realism, zero bokeh, zero depth of field, sharp focus across the entire frame, soft even lighting, subtle studio realism, highly detailed, clean composition, reference-sheet aesthetic, 16:9 aspect ratio."
        ),
    },
]


def model_prompt_card_html(i, item):
    return f'''<div class="modal-block model-prompt-card">
      <div class="modal-block-head">
        <span class="modal-step">{i}</span>
        <h3>{esc(item["title"])}</h3>
      </div>
      <p class="modal-note">{item["note"]}</p>
      <textarea readonly>{esc(item["prompt"])}</textarea>
      <button class="btn-copy">Copiar Prompt</button>
    </div>'''


model_prompts_html = "\n".join(model_prompt_card_html(i + 1, item) for i, item in enumerate(MODEL_PROMPTS))


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


RANK_MEDALS = {1: ("#ffd257", "\U0001f947"), 2: ("#d7dde3", "\U0001f948"), 3: ("#e3a15f", "\U0001f949")}
RANK_TYPE_ICONS = {"vendas": "\U0001f4c8", "novos": "\U0001f195", "video": "\U0001f3ac"}
CATEGORY_ICONS = {"todos": "\U0001f6cd️", "roupas": "\U0001f457", "beleza": "\U0001f484"}


def rank_feat_card_html(modal_id, i, row):
    color, medal = RANK_MEDALS[i]
    metrics = "".join(f'<span class="rank-metric"><b>{esc(l)}</b> {esc(v)}</span>' for l, v in row["metrics"][:2])
    return f'''<button class="rank-card rank-feat" data-rank-modal="{modal_id}" type="button" style="--feat-color:{color};background:linear-gradient(165deg,{color}2e,var(--bg-card) 55%);border-color:{color}55;">
        <span class="rank-feat-badge">{medal} #{i}</span>
        <div class="rank-feat-media">
          <img src="{row["img"]}" alt="{esc(row["title"])}" loading="lazy">
          <div class="rank-feat-shade"></div>
          <div class="rank-feat-overlay">
            <h4>{esc(row["title"])}</h4>
            <div class="rank-feat-price">{esc(row["price"])}</div>
          </div>
        </div>
        <div class="rank-feat-footer">
          <div class="rank-metrics">{metrics}</div>
        </div>
      </button>'''


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


def parse_metric_num(s):
    s = (s or "").strip()
    neg = s.startswith("-")
    s2 = s.lstrip("+-").replace("R$", "").replace("%", "").strip()
    mult = 1
    if "milhão" in s2:
        mult = 1_000_000
        s2 = s2.split("milh")[0].strip()
    elif "mil" in s2:
        mult = 1_000
        s2 = s2.split("mil")[0].strip()
    s2 = s2.replace(".", "").replace(",", ".") if s2.count(",") else s2
    try:
        val = float(s2) * mult
    except ValueError:
        return 0.0
    return -val if neg else val


def short_title(t, maxlen=26):
    t = t.strip()
    return t if len(t) <= maxlen else t[: maxlen - 1].rstrip() + "…"


def compare_chart_html(rows, current_row):
    label = current_row["metrics"][0][0]
    parsed = [(r, parse_metric_num(r["metrics"][0][1])) for r in rows]
    max_val = max((v for _, v in parsed), default=1) or 1
    bars = "".join(
        f'''<div class="cmp-row{" current" if r is current_row else ""}">
          <span class="cmp-label">{esc(short_title(r["title"]))}</span>
          <div class="cmp-track"><div class="cmp-fill" style="width:{max(4, v / max_val * 100):.0f}%"></div></div>
          <span class="cmp-val">{esc(r["metrics"][0][1])}</span>
        </div>'''
        for r, v in parsed
    )
    return f'''<div class="modal-block">
      <div class="modal-block-head"><h3>Compara&ccedil;&atilde;o no Top 5 ({esc(label)})</h3></div>
      <div class="cmp-chart">{bars}</div>
    </div>'''


def popularity_bar_html(d):
    if not d or not d.get("popularityIndex"):
        return ""
    try:
        val = max(0.0, min(100.0, float(str(d["popularityIndex"]).replace(",", "."))))
    except ValueError:
        return ""
    return f'''<div class="modal-block">
      <div class="modal-block-head"><h3>Índice de popularidade</h3></div>
      <div class="pop-gauge">
        <div class="pop-track"><div class="pop-fill" style="width:{val:.0f}%"></div></div>
        <span class="pop-val">{val:.0f}/100</span>
      </div>
    </div>'''


# Titles from FastMoss are keyword-stuffed for SEO (color/style/model list
# first, real product type often buried at the end, e.g. "...p/ iPhone 18 17
# 16..., shell suave alto nível"), so we can't just slice the first N words.
# Beyond naming the product right, generic one-size-fits-all headline templates
# read as forced -- a perfume and a phone case don't share a pain point or
# social angle. Each keyword below also carries the grammatical gender (for
# "esse/essa", "o/a" agreement) and an archetype that picks which headline
# angle bank fits how people actually talk about that kind of product.
# Longest keyword wins so specific phrases ("calça jeans") beat generic ones
# ("calça") -- see PRODUCT_TYPES_SORTED.
PRODUCT_TYPES = [
    # beauty / personal care -- angle: resultado, cheiro, autoestima, elogio
    ("body splash", "body splash", "m", "beauty"),
    ("protetor solar", "protetor solar", "m", "beauty"),
    ("perfume", "perfume", "m", "beauty"),
    ("hidratante", "hidratante", "m", "beauty"),
    ("sérum", "sérum", "m", "beauty"), ("serum", "sérum", "m", "beauty"),
    ("máscara ultra hidratante", "máscara capilar", "f", "beauty"),
    ("máscara capilar", "máscara capilar", "f", "beauty"), ("mascara capilar", "máscara capilar", "f", "beauty"),
    ("máscara facial", "máscara facial", "f", "beauty"),
    ("reparador de pontas", "reparador de pontas", "m", "beauty"),
    ("spray defrizante", "spray defrizante", "m", "beauty"), ("defrizante", "spray defrizante", "m", "beauty"),
    ("shampoo", "shampoo", "m", "beauty"), ("condicionador", "condicionador", "m", "beauty"),
    ("kit capilar", "kit capilar", "m", "beauty"),
    ("sabonete", "sabonete", "m", "beauty"),
    ("caneta sobrancelha", "caneta de sobrancelha", "f", "beauty"),
    ("giz de cabelo", "giz de cabelo colorido", "m", "beauty"),
    ("gloss", "gloss labial", "m", "beauty"), ("batom", "batom", "m", "beauty"),
    # fashion / acessórios -- angle: caimento, elogio, "parece caro"
    ("calça jeans", "calça jeans", "f", "fashion"), ("calça legging", "calça legging", "f", "fashion"),
    ("calça wide leg", "calça wide leg", "f", "fashion"), ("calça", "calça", "f", "fashion"),
    ("blusa", "blusa", "f", "fashion"), ("camisola", "camisola", "f", "fashion"),
    ("vestido", "vestido", "m", "fashion"),
    ("macacão", "macacão", "m", "fashion"), ("macacao", "macacão", "m", "fashion"),
    ("conjunto de terno", "conjunto", "m", "fashion"), ("conjunto alfaiataria", "conjunto", "m", "fashion"),
    ("conjunto", "conjunto", "m", "fashion"),
    ("jaqueta", "jaqueta", "f", "fashion"), ("casaco", "casaco", "m", "fashion"), ("moletom", "moletom", "m", "fashion"),
    ("saia", "saia", "f", "fashion"),
    ("sutiã", "sutiã", "m", "fashion"), ("sutia", "sutiã", "m", "fashion"), ("top sutiã", "top", "m", "fashion"),
    ("calcinha", "calcinha", "f", "fashion"),
    ("adesivos para o peito", "adesivo de peito", "m", "fashion"),
    ("bolsa", "bolsa", "f", "fashion"),
    ("óculos de sol", "óculos de sol", "m", "fashion"), ("oculos de sol", "óculos de sol", "m", "fashion"),
    ("capa roupa chuva", "capa de chuva", "f", "fashion"),
    ("biquíni", "biquíni", "m", "fashion"), ("biquini", "biquíni", "m", "fashion"),
    ("tênis", "tênis", "m", "fashion"), ("tenis", "tênis", "m", "fashion"),
    ("sandália", "sandália", "f", "fashion"), ("sandalia", "sandália", "f", "fashion"),
    ("relógio", "relógio", "m", "fashion"), ("relogio", "relógio", "m", "fashion"),
    ("pulseira", "pulseira", "f", "fashion"), ("colar", "colar", "m", "fashion"), ("brinco", "brinco", "m", "fashion"),
    # casa / utilidades -- angle: resolve um perrengue, praticidade, custo-benefício
    ("cortina", "cortina", "f", "home"), ("cabide", "cabide", "m", "home"),
    ("saco de lixo", "saco de lixo", "m", "home"),
    ("guarda-chuva", "guarda-chuva", "m", "home"), ("guarda chuva", "guarda-chuva", "m", "home"),
    ("cortador", "cortador de legumes", "m", "home"),
    ("esmerilhadeira", "esmerilhadeira", "f", "home"),
    ("organizador", "organizador", "m", "home"), ("umidificador", "umidificador", "m", "home"),
    ("luminária", "luminária", "f", "home"), ("luminaria", "luminária", "f", "home"),
    ("almofada", "almofada", "f", "home"),
    # infantil -- angle: diversão dos filhos, verão, os pais aprovam
    ("squishy", "brinquedo squishy", "m", "kids"),
    ("tapete de sprinkler", "tapete de água", "m", "kids"), ("brinquedo de água", "tapete de água", "m", "kids"),
    ("brinquedo", "brinquedo", "m", "kids"),
    # tech / celular -- angle: proteção, praticidade, combina com tudo
    ("capa de celular", "capinha de celular", "f", "tech"), ("capinha", "capinha de celular", "f", "tech"),
    ("shell", "capinha de celular", "f", "tech"),
    ("fone de ouvido", "fone de ouvido", "m", "tech"), ("fone", "fone de ouvido", "m", "tech"),
    ("carregador", "carregador", "m", "tech"), ("suporte", "suporte", "m", "tech"),
]
PRODUCT_TYPES_SORTED = sorted(PRODUCT_TYPES, key=lambda x: -len(x[0]))


def classify_product(title):
    t = title.lower()
    for kw, noun, gender, archetype in PRODUCT_TYPES_SORTED:
        if kw in t:
            return noun, gender, archetype
    return " ".join(title.split()[:3]), None, None


def cap(s):
    return s[:1].upper() + s[1:] if s else s


def esse(g):
    return "essa" if g == "f" else "esse"


def desse(g):
    return "dessa" if g == "f" else "desse"


def art(g):
    return "a" if g == "f" else "o"


def prep_in(g):
    return "nessa" if g == "f" else "nesse"


def fit(s, limit=72):
    s = s.strip()
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


# The user wants the headline emojis to always look like iPhone (Apple) emoji,
# regardless of what OS/browser renders the page -- a plain unicode emoji
# character is drawn by the visitor's own emoji font (e.g. Segoe UI Emoji on
# Windows), which looks nothing like Apple's. Rendering the known emoji as
# <img> pulled from the emoji-datasource-apple asset set (Apple-style PNGs,
# used the same way by Slack/emoji-mart) forces the Apple look everywhere.
# The literal unicode character is kept in data-copy-inline so pasting the
# headline elsewhere still carries a real emoji, rendered by whatever device
# the person pastes it on.
APPLE_EMOJI_CDN = "https://cdn.jsdelivr.net/npm/emoji-datasource-apple@15.1.2/img/apple/64"
EMOJI_CODEPOINTS = {"\U0001f633": "1f633", "\U0001f60d": "1f60d", "\U0001f440": "1f440"}


def apple_emoji_html(text):
    text = text.rstrip()
    if text and text[-1] in EMOJI_CODEPOINTS:
        emoji = text[-1]
        rest = text[:-1].rstrip()
        cp = EMOJI_CODEPOINTS[emoji]
        return f'{esc(rest)} <img class="hl-emoji" src="{APPLE_EMOJI_CDN}/{cp}.png" alt="{emoji}">'
    return esc(text)


def gen_headlines_beauty(noun, g, price, metric_val):
    return [
        (fit(f"Como assim {esse(g)} {noun} custa só {price}? \U0001f60d"), "Hook de curiosidade"),
        (fit(f"{cap(noun)} que todo mundo tá comentando o resultado"), "Prova social"),
        (fit(f"Gente, {metric_val} pessoas já compraram {esse(g)} {noun} \U0001f440"), "Prova social"),
        (fit(f"Achei {esse(g)} {noun} incrível por {price}"), "Benefício direto"),
        (fit(f"POV: elogiaram você e era {esse(g)} {noun}"), "Formato POV"),
    ]


def gen_headlines_fashion(noun, g, price, metric_val):
    return [
        (fit(f"Como assim {esse(g)} {noun} por só {price}? \U0001f633"), "Hook de curiosidade"),
        (fit(f"{cap(noun)} tem cara de caro e custa {price}"), "Percepção de valor"),
        (fit(f"Gente, {metric_val} vendidos {prep_in(g)} {noun} \U0001f440"), "Prova social"),
        (fit(f"Achei {esse(g)} {noun} incrível quase de graça"), "Benefício direto"),
        (fit(f"POV: você achou {art(g)} {noun} perfeit{'a' if g == 'f' else 'o'} por menos de {price}"), "Formato POV"),
    ]


def gen_headlines_home(noun, g, price, metric_val):
    return [
        (fit(f"Como assim {esse(g)} {noun} resolve isso por só {price}? \U0001f633"), "Hook de curiosidade"),
        (fit(f"{cap(noun)} que eu não sabia que precisava"), "Hook de curiosidade"),
        (fit(f"Gente, {metric_val} pessoas já compraram {esse(g)} {noun} \U0001f440"), "Prova social"),
        (fit(f"Achei {esse(g)} {noun} que resolveu meu perrengue por {price}"), "Benefício direto"),
        (fit(f"POV: você parou de sofrer com isso depois {desse(g)} {noun}"), "Formato POV"),
    ]


def gen_headlines_kids(noun, g, price, metric_val):
    return [
        (fit(f"Como assim {esse(g)} {noun} custa só {price}? \U0001f633"), "Hook de curiosidade"),
        (fit(f"As crianças não largam {art(g)} {noun} nem um minuto"), "Prova social"),
        (fit(f"Gente, {metric_val} pais já compraram {esse(g)} {noun} \U0001f440"), "Prova social"),
        (fit(f"Achei {esse(g)} {noun} que salvou minhas férias por {price}"), "Benefício direto"),
        (fit(f"POV: seu filho pediu {esse(g)} {noun} e valeu cada centavo"), "Formato POV"),
    ]


def gen_headlines_tech(noun, g, price, metric_val):
    return [
        (fit(f"Como assim {esse(g)} {noun} custa só {price}? \U0001f633"), "Hook de curiosidade"),
        (fit(f"{cap(noun)} que deixa tudo mais bonito e ainda protege"), "Benefício direto"),
        (fit(f"Gente, {metric_val} pessoas já compraram {esse(g)} {noun} \U0001f440"), "Prova social"),
        (fit(f"Achei {esse(g)} {noun} que combina com tudo por {price}"), "Benefício direto"),
        (fit(f"POV: parou de se preocupar depois {desse(g)} {noun}"), "Formato POV"),
    ]


def gen_headlines_generic(noun, price, metric_val):
    return [
        (fit(f"Como assim {noun} custa só {price}? \U0001f633"), "Hook de curiosidade"),
        (fit(f"{cap(noun)} tá bombando no TikTok Shop"), "Prova social"),
        (fit(f"Gente, {metric_val} pessoas comprando {noun} agora"), "Prova social"),
        (fit(f"Achei {noun} quase de graça"), "Benefício direto"),
        (fit(f"POV: você achou {noun} perfeito por menos de {price}"), "Formato POV"),
    ]


ARCHETYPE_GENERATORS = {
    "beauty": gen_headlines_beauty, "fashion": gen_headlines_fashion, "home": gen_headlines_home,
    "kids": gen_headlines_kids, "tech": gen_headlines_tech,
}


def generate_headlines(row):
    price = row["price"]
    _, metric_val = row["metrics"][0]
    noun, gender, archetype = classify_product(row["title"])
    gen_fn = ARCHETYPE_GENERATORS.get(archetype)
    if gen_fn is None:
        return gen_headlines_generic(noun, price, metric_val)
    return gen_fn(noun, gender, price, metric_val)


def headlines_html(row):
    items = "".join(
        f'''<div class="hl-item">
          <span class="hl-angle">{esc(angle)}</span>
          <div class="hl-mock">
            <span class="hl-mock-text">{apple_emoji_html(h)}</span>
            <button class="btn-copy hl-copy" data-copy-inline="{esc(h)}" title="Copiar">&#128203;</button>
          </div>
        </div>'''
        for h, angle in generate_headlines(row)
    )
    return f'''<div class="modal-block">
      <div class="modal-block-head"><h3>5 headlines pra queimar na tela</h3></div>
      <p class="modal-note">Mesmo estilo da edi&ccedil;&atilde;o de v&iacute;deo: branco bold com contorno preto, centralizado, sem anima&ccedil;&atilde;o.</p>
      <div class="hl-list">{items}</div>
    </div>'''


def rank_modal_html(modal_id, row, rows):
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
    tiktok_url = row.get("tiktok_url")
    tiktok_btn = (
        f'<a class="btn-tiktok" href="{tiktok_url}" target="_blank" rel="noopener">Ver na TikTok Shop &rarr;</a>'
        if tiktok_url else ""
    )
    return f'''<div class="modal" id="{modal_id}">
  <div class="modal-inner rank-modal-inner">
    <button class="modal-close" data-close>&times;</button>
    <span class="modal-tag">{esc(row["store"])}</span>
    <h2>{esc(row["title"])}</h2>
    <div class="rank-report" style="margin-bottom:14px;"><div class="rank-report-row"><span>Loja</span><b>{esc(row["store"])}</b></div><div class="rank-report-row"><span>Pre&ccedil;o de venda</span><b>{esc(row["price"])}</b></div></div>
    {tiktok_btn}
    <div class="modal-block" style="margin-top:22px;">
      <div class="modal-block-head"><h3>Imagens liberadas &mdash; clique pra copiar</h3></div>
      <div class="rank-gallery">{gallery}</div>
    </div>
    <div class="modal-block">
      <div class="modal-block-head"><h3>Métricas do ranking</h3></div>
      <div class="rank-metrics">{list_metrics}</div>
    </div>
    {compare_chart_html(rows, row)}
    {popularity_bar_html(d)}
    {headlines_html(row)}
    <div class="modal-block">
      <div class="modal-block-head"><h3>Relatório do produto</h3></div>
      <div class="rank-report">{report_rows}</div>
    </div>
  </div>
</div>'''


rank_type_tabs_html = "\n      ".join(
    f'<button class="fmt-tab{" active" if i == 0 else ""}" data-rank="{rid}">{RANK_TYPE_ICONS.get(rid, "")} {label}</button>'
    for i, (rid, label) in enumerate(RANK_TYPES)
)
rank_cat_tabs_html = "\n      ".join(
    f'<button class="fmt-tab{" active" if i == 0 else ""}" data-cat="{cid}">{CATEGORY_ICONS.get(cid, "")} {label}</button>'
    for i, (cid, label) in enumerate(CATEGORIES)
)

rank_panels = []
rank_modals = []
for rid, _ in RANK_TYPES:
    for cid, _ in CATEGORIES:
        rows = RANKINGS[rid][cid]
        feat_cards, rest_cards = [], []
        for i, r in enumerate(rows):
            modal_id = f"rank-modal-{rid}-{cid}-{i}"
            n = i + 1
            if n in RANK_MEDALS:
                feat_cards.append(rank_feat_card_html(modal_id, n, r))
            else:
                rest_cards.append(rank_card_html(modal_id, n, r))
            rank_modals.append(rank_modal_html(modal_id, r, rows))
        feat_html = "\n    ".join(feat_cards)
        rest_html = "\n    ".join(rest_cards)
        rest_block = f'''<div class="rank-list-label">Tamb&eacute;m no Top 5</div>
    <div class="rank-grid">
    {rest_html}
    </div>''' if rest_cards else ""
        active = "active" if (rid == RANK_TYPES[0][0] and cid == CATEGORIES[0][0]) else ""
        rank_panels.append(f'''<div class="rank-panel {active}" data-rank="{rid}" data-cat="{cid}">
    <div class="rank-featured-row">
    {feat_html}
    </div>
    {rest_block}
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
  <div class="model-prompts-section">
    <div class="head" style="margin-bottom:24px;">
      <span class="eyebrow">Antes de tudo</span>
      <h2>Criando sua modelo</h2>
      <p>Prompts prontos pra gerar a base da sua modelo antes de aplicar qualquer formato.</p>
    </div>
    <div class="model-prompts-grid">
{model_prompts_html}
    </div>
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
    <span class="rank-next-pill">&#128337; Atualiza em <span class="rank-countdown" id="rank-countdown">--:--:--</span></span>
  </div>
  <div class="rank-filter-group">
    <span class="rank-filter-label">1. Escolha o ranking</span>
    <div class="fmt-tabs rank-type-tabs">
        {rank_type_tabs_html}
    </div>
  </div>
  <div class="rank-filter-group">
    <span class="rank-filter-label">2. Filtre por categoria</span>
    <div class="fmt-tabs rank-cat-tabs">
        {rank_cat_tabs_html}
    </div>
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
  html{scrollbar-width:thin;scrollbar-color:var(--line) var(--bg);}
  ::-webkit-scrollbar{width:11px;height:11px;}
  ::-webkit-scrollbar-track{background:var(--bg);}
  ::-webkit-scrollbar-thumb{background:var(--line);border-radius:100px;border:2px solid var(--bg);}
  ::-webkit-scrollbar-thumb:hover{background:var(--green);}
  ::-webkit-scrollbar-corner{background:var(--bg);}
  .modal-inner{scrollbar-width:thin;scrollbar-color:var(--line-soft) var(--bg-raised);}
  .modal-inner::-webkit-scrollbar-track{background:var(--bg-raised);}
  .modal-inner::-webkit-scrollbar-thumb{background:var(--line-soft);border:2px solid var(--bg-raised);}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:'Plus Jakarta Sans',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}
  h1,h2,h3{font-family:'Unbounded','Plus Jakarta Sans',sans-serif;margin:0;}
  .eyebrow{font-family:'JetBrains Mono',monospace;font-size:12.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--green);}
  .wrap{max-width:1080px;margin:0 auto;padding:48px 24px;}
  .head{max-width:640px;margin:0 auto 40px;text-align:center;}
  .head h1{font-size:clamp(26px,4vw,36px);font-weight:800;margin-top:12px;}
  .head h2{font-size:clamp(20px,3vw,26px);font-weight:800;margin-top:10px;}
  .head p{color:var(--ink-dim);margin-top:12px;font-size:15.5px;line-height:1.6;}
  .fmt-tabs{display:flex;justify-content:center;gap:8px;flex-wrap:wrap;margin:0 auto 30px;}
  .fmt-tab{appearance:none;border:1px solid var(--line);cursor:pointer;background:var(--bg-card);color:var(--ink-dim);font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-size:13.5px;padding:10px 18px;border-radius:100px;transition:all .15s ease;}
  .fmt-tab.active{background:var(--green);color:var(--green-ink);border-color:var(--green);}
  .fmt-panel{display:none;}
  .fmt-panel.active{display:block;}
  .fmt-row-wrap{position:relative;max-width:920px;margin:0 auto;}
  .fmt-row{display:flex;gap:16px;overflow-x:auto;padding:4px 4px 12px;scroll-snap-type:x proximity;width:max-content;max-width:100%;margin:0 auto;scrollbar-width:none;-ms-overflow-style:none;}
  .fmt-row::-webkit-scrollbar{display:none;}
  .fmt-arrow{
    position:absolute;top:50%;transform:translateY(-50%);z-index:3;width:38px;height:38px;border-radius:50%;
    border:1px solid var(--line);background:rgba(10,12,9,.85);color:var(--ink);font-size:20px;line-height:1;cursor:pointer;
    display:flex;align-items:center;justify-content:center;box-shadow:0 8px 20px -8px rgba(0,0,0,.6);
    transition:background .15s ease,border-color .15s ease;
  }
  .fmt-arrow:hover{background:var(--green);color:var(--green-ink);border-color:var(--green);}
  .fmt-arrow-left{left:-6px;}
  .fmt-arrow-right{right:-6px;}
  @keyframes rowNudge{0%{transform:translateX(0);}40%{transform:translateX(28px);}75%{transform:translateX(0);}100%{transform:translateX(0);}}
  .fmt-row.nudge{animation:rowNudge 1600ms ease-in-out;}
  .fmt-card{flex:none;width:220px;scroll-snap-align:start;border:1px solid var(--line);border-radius:16px;overflow:hidden;background:var(--bg-card);}
  @media (max-width:640px){
    .fmt-arrow{display:none;}
    .fmt-card{width:250px;}
  }
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
  .modal-block textarea{width:100%;resize:none;overflow:hidden;background:var(--bg-card);color:var(--ink-dim);border:1px solid var(--line);border-radius:12px;padding:14px;font-size:13px;line-height:1.55;font-family:'JetBrains Mono',monospace;margin-bottom:10px;}
  .btn-copy{appearance:none;border:none;cursor:pointer;font-family:'Unbounded',sans-serif;font-weight:700;font-size:12.5px;background:var(--green);color:var(--green-ink);padding:10px 18px;border-radius:100px;}
  .model-prompts-section{max-width:920px;margin:44px auto 0;}
  .model-prompts-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;}
  @media (max-width:760px){ .model-prompts-grid{grid-template-columns:1fr;} }
  .model-prompt-card{background:var(--bg-card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin-bottom:0;}
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
  .rank-meta{
    display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;
    margin:-8px 0 26px;font-size:13px;color:var(--ink-dim);background:linear-gradient(90deg,var(--bg-card),var(--bg-raised));
    border:1px solid var(--line);border-radius:16px;padding:14px 22px;
  }
  .rank-next-pill{
    display:inline-flex;align-items:center;gap:10px;background:rgba(255,73,73,.12);
    border:1px solid rgba(255,73,73,.4);border-radius:100px;padding:8px 18px;
  }
  .rank-countdown{color:#ff5c5c;font-weight:900;font-family:'JetBrains Mono',monospace;font-size:20px;letter-spacing:.02em;animation:rankPulse 2s ease-in-out infinite;}
  @keyframes rankPulse{0%,100%{opacity:1;}50%{opacity:.55;}}
  .rank-filter-group{margin-bottom:22px;}
  .rank-filter-label{
    display:block;text-align:center;font-family:'JetBrains Mono',monospace;font-size:10.5px;
    font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-faint);margin-bottom:12px;
  }
  .rank-type-tabs .fmt-tab{font-size:14px;padding:12px 22px;}
  .rank-cat-tabs .fmt-tab{
    font-size:12px;padding:8px 16px;background:transparent;border-style:dashed;color:var(--ink-faint);
  }
  .rank-cat-tabs .fmt-tab.active{background:var(--amber);color:var(--amber-ink);border-color:var(--amber);border-style:solid;}
  .rank-panel{display:none;}
  .rank-panel.active{display:block;}
  .rank-featured-row{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:26px;}
  @media (max-width:760px){ .rank-featured-row{grid-template-columns:1fr;} }
  .rank-feat{
    appearance:none;font-family:inherit;text-align:left;cursor:pointer;padding:0;
    display:flex;flex-direction:column;border:1px solid var(--line);border-radius:18px;overflow:hidden;
    position:relative;transition:transform .18s ease,box-shadow .18s ease;
  }
  .rank-feat:hover{transform:translateY(-5px);box-shadow:0 16px 34px rgba(0,0,0,.4),0 0 0 1px var(--feat-color, var(--green));}
  .rank-feat-badge{
    position:absolute;top:12px;left:12px;z-index:2;background:var(--feat-color,var(--amber));color:#241a02;
    font-weight:900;font-size:12px;padding:5px 12px;border-radius:100px;box-shadow:0 3px 10px rgba(0,0,0,.45);
    font-family:'JetBrains Mono',monospace;letter-spacing:.02em;
  }
  .rank-feat-media{position:relative;aspect-ratio:1/1;overflow:hidden;background:#0f1310;}
  .rank-feat-media img{width:100%;height:100%;object-fit:cover;display:block;}
  .rank-feat-shade{position:absolute;inset:0;background:linear-gradient(180deg,transparent 38%,rgba(0,0,0,.9) 100%);}
  .rank-feat-overlay{position:absolute;left:0;right:0;bottom:0;padding:14px 16px;}
  .rank-feat-overlay h4{
    font-size:14px;font-weight:800;color:#fff;margin:0 0 5px;line-height:1.28;
    display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;
  }
  .rank-feat-price{font-family:'JetBrains Mono',monospace;font-weight:800;font-size:15px;color:var(--feat-color,var(--amber));}
  .rank-feat-footer{padding:12px 16px 16px;}
  .rank-list-label{
    font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
    color:var(--ink-faint);margin:0 0 12px;
  }
  .rank-grid{display:flex;flex-direction:column;gap:10px;}
  .rank-card{
    appearance:none;font-family:inherit;text-align:left;cursor:pointer;width:100%;
    display:flex;align-items:center;gap:16px;background:var(--bg-card);border:1px solid var(--line);
    border-radius:14px;padding:12px 16px;position:relative;transition:border-color .15s ease,transform .15s ease;
  }
  .rank-card:hover{border-color:var(--green);transform:translateY(-1px);}
  .rank-num{
    flex:none;background:var(--green);color:var(--green-ink);width:28px;height:28px;border-radius:50%;
    display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;
  }
  .rank-img{width:56px;height:56px;object-fit:cover;border-radius:10px;flex:none;background:#0f1310;display:block;}
  .btn-copy-img.small{width:18px;height:18px;font-size:9px;bottom:3px;right:3px;}
  .rank-info{min-width:0;flex:1;}
  .rank-info h4{font-size:13.5px;font-weight:700;margin:0 0 5px;line-height:1.32;color:var(--ink);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
  .rank-price{font-size:11.5px;color:var(--ink-dim);margin-bottom:7px;}
  .rank-metrics{display:flex;flex-wrap:wrap;gap:5px;}
  .rank-metric{font-size:10px;color:var(--ink-faint);background:var(--bg-raised);border:1px solid var(--line-soft);border-radius:100px;padding:3px 8px;}
  .rank-metric b{color:var(--ink-dim);font-weight:700;}
  .rank-modal-inner{max-width:640px;}
  .rank-gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
  .rank-gallery-item{position:relative;}
  .rank-gallery-item img{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:12px;border:1px solid var(--line);display:block;}
  .rank-gallery-item .btn-copy-img{width:28px;height:28px;font-size:13px;bottom:8px;right:8px;}
  .rank-report{display:flex;flex-direction:column;gap:0;border:1px solid var(--line);border-radius:12px;overflow:hidden;}
  .rank-report-row{display:flex;justify-content:space-between;gap:12px;padding:9px 14px;font-size:12.5px;border-bottom:1px solid var(--line-soft);background:var(--bg-card);}
  .rank-report-row:last-child{border-bottom:none;}
  .rank-report-row span{color:var(--ink-faint);}
  .rank-report-row b{color:var(--ink);font-weight:700;text-align:right;}
  .btn-tiktok{
    display:inline-flex;align-items:center;gap:8px;font-family:'Unbounded',sans-serif;font-weight:700;
    font-size:12.5px;text-decoration:none;background:var(--amber);color:var(--amber-ink);
    padding:11px 20px;border-radius:100px;transition:transform .15s ease,filter .15s ease;
  }
  .btn-tiktok:hover{transform:translateY(-1px);filter:brightness(1.06);}
  .cmp-chart{display:flex;flex-direction:column;gap:8px;}
  .cmp-row{display:grid;grid-template-columns:110px 1fr auto;align-items:center;gap:10px;font-size:11.5px;}
  .cmp-label{color:var(--ink-dim);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
  .cmp-track{height:10px;border-radius:100px;background:var(--bg-card);border:1px solid var(--line-soft);overflow:hidden;}
  .cmp-fill{height:100%;background:var(--green);border-radius:100px;}
  .cmp-row.current .cmp-label{color:var(--amber);font-weight:700;}
  .cmp-row.current .cmp-fill{background:var(--amber);}
  .cmp-val{color:var(--ink-faint);font-family:'JetBrains Mono',monospace;font-size:10.5px;white-space:nowrap;}
  .pop-gauge{display:flex;align-items:center;gap:12px;}
  .pop-track{flex:1;height:14px;border-radius:100px;background:var(--bg-card);border:1px solid var(--line-soft);overflow:hidden;}
  .pop-fill{height:100%;background:linear-gradient(90deg,var(--green),var(--amber));border-radius:100px;}
  .pop-val{font-family:'JetBrains Mono',monospace;font-size:12.5px;font-weight:700;color:var(--ink);}
  .hl-list{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;}
  @media (max-width:560px){ .hl-list{grid-template-columns:1fr;} }
  .hl-item{display:flex;flex-direction:column;gap:6px;}
  .hl-angle{
    font-family:'JetBrains Mono',monospace;font-size:9.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
    color:var(--amber);
  }
  .hl-mock{
    position:relative;display:flex;align-items:center;justify-content:center;text-align:center;
    aspect-ratio:16/8;border-radius:12px;padding:10px 34px 10px 12px;overflow:hidden;
    background:
      radial-gradient(120% 140% at 15% 15%, rgba(53,225,126,.16), transparent 55%),
      radial-gradient(120% 140% at 85% 85%, rgba(255,200,69,.14), transparent 55%),
      linear-gradient(160deg,#1c2117,#0d100b);
    border:1px solid var(--line);
  }
  .hl-mock-text{
    font-family:'Unbounded','Plus Jakarta Sans',sans-serif;font-weight:800;font-size:14px;line-height:1.3;color:#fff;
    text-shadow:-1.5px -1.5px 0 #000,1.5px -1.5px 0 #000,-1.5px 1.5px 0 #000,1.5px 1.5px 0 #000,0 0 10px rgba(0,0,0,.5);
  }
  .hl-emoji{width:1.15em;height:1.15em;vertical-align:-0.2em;display:inline-block;}
  .hl-copy{
    position:absolute;top:8px;right:8px;width:24px;height:24px;padding:0;font-size:11px;flex:none;
    border-radius:8px;background:rgba(10,12,9,.7);border:1px solid rgba(255,255,255,.18);
  }
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

  function autoSizeTextareas(modal){
    modal.querySelectorAll('textarea').forEach(function(ta){
      ta.style.height = 'auto';
      ta.style.height = ta.scrollHeight + 'px';
    });
  }
  document.querySelectorAll('.rank-card[data-rank-modal]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var modal = document.getElementById(btn.getAttribute('data-rank-modal'));
      if(modal){ modal.classList.add('open'); autoSizeTextareas(modal); }
    });
  });
  var modelPromptsSection = document.querySelector('.model-prompts-section');
  if(modelPromptsSection) autoSizeTextareas(modelPromptsSection);

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

  function animateScrollLeft(row, delta){
    var startX = row.scrollLeft;
    var maxX = row.scrollWidth - row.clientWidth;
    var endX = Math.max(0, Math.min(maxX, startX + delta));
    var dist = endX - startX;
    var duration = 380;
    var startTime = null;
    function ease(t){ return 1 - Math.pow(1 - t, 3); }
    function step(ts){
      if(!startTime) startTime = ts;
      var progress = Math.min((ts - startTime) / duration, 1);
      row.scrollLeft = startX + dist * ease(progress);
      if(progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  document.querySelectorAll('.fmt-arrow').forEach(function(btn){
    btn.addEventListener('click', function(){
      var row = btn.parentElement.querySelector('.fmt-row');
      if(!row) return;
      var dir = parseInt(btn.getAttribute('data-scroll'),10)||1;
      var cardEl = row.querySelector('.fmt-card');
      var step = (cardEl?cardEl.getBoundingClientRect().width:220)+16;
      animateScrollLeft(row, dir*step*2);
    });
  });
  function nudgeActivePanel(){
    if(window.matchMedia('(max-width:640px)').matches){
      var row = document.querySelector('.fmt-panel.active .fmt-row');
      if(row){
        row.classList.remove('nudge');
        void row.offsetWidth;
        row.classList.add('nudge');
      }
    }
  }
  setTimeout(nudgeActivePanel, 900);
  setInterval(nudgeActivePanel, 4500);
  tabs.forEach(function(tab){
    tab.addEventListener('click', function(){ setTimeout(nudgeActivePanel, 150); });
  });
  document.querySelectorAll('.btn-formato[data-card]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var modal = document.getElementById('modal-'+btn.getAttribute('data-card'));
      if(modal){ modal.classList.add('open'); autoSizeTextareas(modal); }
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
      var inline = btn.getAttribute('data-copy-inline');
      var text;
      if(inline !== null){
        text = inline;
      } else {
        var block = btn.closest('.modal-block');
        text = block.querySelector('textarea').value;
      }
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
