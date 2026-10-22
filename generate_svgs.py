"""
GitHub Profile Animation Generator for Siddharth Kumar (siddharthskyhub)
Creates animated SVGs for GitHub profile READMEs inspired by modern developer designs.
"""

import os
import sys

def get_theme_palette(theme_name="ocean"):
    themes = {
        "ocean": {
            "name": "Ocean Breeze (Reference Exact)",
            "card_grad_start": "#03396c",
            "card_grad_mid1": "#005b96",
            "card_grad_mid2": "#017dbb",
            "card_grad_end": "#00a8cc",
            "wave_back": "#001a33",
            "wave_mid": "#002b4d",
            "wave_front": "#00406c",
            "shimmer_opacity": "0.16",
            "title_color": "#FFFFFF",
            "subtitle_color": "#E0F2FE",
            "tagline_color": "#FF758F",
            "portfolio_bg": "#C4B5FD",
            "portfolio_text": "#3B0764",
            "linkedin_bg": "#93C5FD",
            "linkedin_text": "#1E3A8A",
            "email_bg": "#FDA4AF",
            "email_text": "#881337",
            "location_bg": "#86EFAC",
            "location_text": "#064E3B",
        }
    }
    return themes.get(theme_name, themes["ocean"])

def create_banner_complete_svg(
    name="Siddharth Kumar",
    subtitle="GenAI & LLM Enthusiast • Full-Stack Crafter",
    breadcrumb="siddharthskyhub / README.md",
    tagline="Turning coffee and chai into clean code",
    portfolio_url="siddharth.dev",
    linkedin_text="Let's Connect",
    email_text="Say Hello",
    location_text="India",
    theme="ocean"
):
    t = get_theme_palette(theme)

    char_count = max(len(tagline), 1)
    char_width = 11.9
    text_total_width = char_count * char_width
    center_x = 460
    start_x = int(center_x - (text_total_width / 2))

    p_val_w = max(70, int(len(portfolio_url) * 7.5 + 18))
    l_val_w = max(70, int(len(linkedin_text) * 7.5 + 18))
    e_val_w = max(60, int(len(email_text) * 7.5 + 18))
    loc_val_w = max(55, int(len(location_text) * 7.5 + 18))

    p_badge_w = 78 + p_val_w
    l_badge_w = 78 + l_val_w
    e_badge_w = 68 + e_val_w
    loc_badge_w = 74 + loc_val_w

    gap = 14
    total_badges_w = p_badge_w + l_badge_w + e_badge_w + loc_badge_w + (gap * 3)
    badges_start_x = int(center_x - (total_badges_w / 2))

    b1_x = badges_start_x
    b2_x = b1_x + p_badge_w + gap
    b3_x = b2_x + l_badge_w + gap
    b4_x = b3_x + e_badge_w + gap

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 405" width="100%" height="100%">
  <defs>
    <!-- Card Gradient -->
    <linearGradient id="cardGrad" x1="0%" y1="15%" x2="100%" y2="85%">
      <stop offset="0%" stop-color="{t['card_grad_start']}" />
      <stop offset="42%" stop-color="{t['card_grad_mid1']}" />
      <stop offset="78%" stop-color="{t['card_grad_mid2']}" />
      <stop offset="100%" stop-color="{t['card_grad_end']}" />
    </linearGradient>

    <!-- Diagonal Shimmer Light Sweep -->
    <linearGradient id="shimmerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(255,255,255,0)" />
      <stop offset="45%" stop-color="rgba(255,255,255,{t['shimmer_opacity']})" />
      <stop offset="55%" stop-color="rgba(255,255,255,{t['shimmer_opacity']})" />
      <stop offset="100%" stop-color="rgba(255,255,255,0)" />
    </linearGradient>

    <!-- Clip Path for Rounded Card Corners -->
    <clipPath id="cardClip">
      <rect x="20" y="44" width="880" height="215" rx="14" ry="14" />
    </clipPath>

    <!-- Clip Path for Precise Typewriter Mask -->
    <clipPath id="typeClip">
      <rect class="type-mask" x="{start_x}" y="275" width="0" height="45" />
    </clipPath>

    <style>
      .font-mono {{
        font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, 'Courier New', monospace;
      }}
      .font-sans {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
      }}

      @keyframes waveFlowA {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-880px); }}
      }}
      @keyframes waveFlowB {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(880px); }}
      }}
      @keyframes waveGentle {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(6px); }}
      }}

      .wave-1 {{
        animation: waveFlowA 24s linear infinite;
      }}
      .wave-2 {{
        animation: waveFlowB 18s linear infinite;
        opacity: 0.65;
      }}
      .wave-3 {{
        animation: waveGentle 7s ease-in-out infinite;
        opacity: 0.85;
      }}

      @keyframes twinkle {{
        0%, 100% {{ opacity: 0.15; transform: scale(0.75); }}
        50% {{ opacity: 0.95; transform: scale(1.25); }}
      }}
      .star {{
        transform-origin: center;
        animation: twinkle 3.8s ease-in-out infinite;
      }}
      .s1 {{ animation-delay: 0.3s; }}
      .s2 {{ animation-delay: 1.2s; }}
      .s3 {{ animation-delay: 2.1s; }}
      .s4 {{ animation-delay: 3.0s; }}

      @keyframes shimmer {{
        0% {{ transform: translateX(-650px) skewX(-20deg); }}
        35% {{ transform: translateX(950px) skewX(-20deg); }}
        100% {{ transform: translateX(950px) skewX(-20deg); }}
      }}
      .shimmer-bar {{
        animation: shimmer 8s ease-in-out infinite;
      }}

      @keyframes softBreath {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-1.5px); }}
      }}
      .hero-title {{
        animation: softBreath 4.5s ease-in-out infinite;
      }}

      @keyframes typeTyping {{
        0% {{ width: 0; }}
        42% {{ width: {int(text_total_width + 12)}px; }}
        78% {{ width: {int(text_total_width + 12)}px; }}
        92% {{ width: 0; }}
        100% {{ width: 0; }}
      }}

      @keyframes cursorTranslate {{
        0% {{ transform: translateX(0); }}
        42% {{ transform: translateX({int(text_total_width + 4)}px); }}
        78% {{ transform: translateX({int(text_total_width + 4)}px); }}
        92% {{ transform: translateX(0); }}
        100% {{ transform: translateX(0); }}
      }}

      @keyframes cursorBlink {{
        0%, 48% {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}

      .type-mask {{
        animation: typeTyping 9s steps({char_count + 4}, end) infinite;
      }}
      .cursor-tracker {{
        animation: cursorTranslate 9s steps({char_count + 4}, end) infinite;
      }}
      .cursor-bar {{
        animation: cursorBlink 0.75s infinite;
      }}

      .badge-item {{
        transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), filter 0.25s ease;
        cursor: pointer;
      }}
      .badge-item:hover {{
        filter: brightness(1.15) drop-shadow(0 4px 10px rgba(0,0,0,0.3));
        transform: translateY(-2px);
      }}
    </style>
  </defs>

  <rect width="920" height="405" fill="#0D1117" rx="16" />

  <!-- 1. Breadcrumb Top Bar -->
  <g class="font-mono" transform="translate(24, 28)">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5v-9zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8V1.5z"
          fill="#7D8590" transform="translate(0, -11) scale(0.9)" />
    <text x="20" y="0" font-size="13" font-weight="500" letter-spacing="0.2">
      <tspan fill="#C9D1D9">{breadcrumb.split('/')[0].strip()} </tspan>
      <tspan fill="#484F58">/</tspan>
      <tspan fill="#8B949E"> {breadcrumb.split('/')[1].strip() if '/' in breadcrumb else 'README.md'}</tspan>
    </text>
  </g>

  <!-- 2. Main Header Banner Card -->
  <g clip-path="url(#cardClip)">
    <rect x="20" y="44" width="880" height="215" fill="url(#cardGrad)" />

    <!-- Twinkling Ambient Stars -->
    <circle cx="85" cy="85" r="1.5" fill="#FFFFFF" class="star s1" />
    <circle cx="215" cy="70" r="2.0" fill="#E0F2FE" class="star s3" />
    <circle cx="340" cy="100" r="1.2" fill="#FFFFFF" class="star s2" />
    <circle cx="585" cy="75" r="2.2" fill="#BAE6FD" class="star s4" />
    <circle cx="725" cy="90" r="1.5" fill="#FFFFFF" class="star s1" />
    <circle cx="825" cy="80" r="2.0" fill="#E0F2FE" class="star s3" />
    <circle cx="155" cy="120" r="1.3" fill="#FFFFFF" class="star s2" />
    <circle cx="785" cy="125" r="1.5" fill="#FFFFFF" class="star s4" />

    <!-- Shimmer Beam -->
    <rect class="shimmer-bar" x="20" y="44" width="350" height="215" fill="url(#shimmerGrad)" />

    <!-- Wave 1 (Deep Navy, Left) -->
    <g class="wave-1" transform="translate(20, 0)">
      <path d="M 0,165 C 220,140 220,190 440,165 C 660,140 660,190 880,165 C 1100,140 1100,190 1320,165 C 1540,140 1540,190 1760,165 L 1760,265 L 0,265 Z"
            fill="{t['wave_back']}" />
    </g>

    <!-- Wave 2 (Middle Layer, Right) -->
    <g class="wave-2" transform="translate(-880, 0)">
      <path d="M 0,180 C 220,200 220,158 440,180 C 660,200 660,158 880,180 C 1100,200 1100,158 1320,180 C 1540,200 1540,158 1760,180 L 1760,265 L 0,265 Z"
            fill="{t['wave_mid']}" />
    </g>

    <!-- Wave 3 (Foreground Organic Crest) -->
    <g class="wave-3">
      <path d="M 20,190 C 200,175 380,210 560,190 C 720,174 810,205 900,188 L 900,265 L 20,265 Z"
            fill="{t['wave_front']}" />
    </g>

    <!-- Polished Border -->
    <rect x="20" y="44" width="880" height="215" rx="14" ry="14" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" />

    <!-- Hero Title & Subtitle -->
    <g class="hero-title">
      <text class="font-sans" x="460" y="138" text-anchor="middle"
            font-size="44" font-weight="800" fill="{t['title_color']}" letter-spacing="-0.5"
            filter="drop-shadow(0 4px 14px rgba(0,0,0,0.45))">
        {name}
      </text>

      <text class="font-sans" x="460" y="176" text-anchor="middle"
            font-size="18" font-weight="500" fill="{t['subtitle_color']}" letter-spacing="0.4"
            filter="drop-shadow(0 2px 6px rgba(0,0,0,0.3))">
        {subtitle}
      </text>
    </g>
  </g>

  <!-- 3. Animated Typewriter Quote -->
  <g>
    <g clip-path="url(#typeClip)">
      <text class="font-mono" x="460" y="303" text-anchor="middle"
            font-size="19" font-weight="600" fill="{t['tagline_color']}" letter-spacing="0.5"
            filter="drop-shadow(0 0 10px {t['tagline_color']}55)">
        {tagline}
      </text>
    </g>

    <g transform="translate({start_x}, 0)">
      <g class="cursor-tracker">
        <rect class="cursor-bar" x="0" y="287" width="2.8" height="20" rx="1.4" fill="{t['tagline_color']}" />
      </g>
    </g>
  </g>

  <!-- 4. Modern Badge Pill Row -->
  <g transform="translate(0, 338)">
    
    <!-- Badge 1: Portfolio -->
    <g class="badge-item" transform="translate({b1_x}, 0)">
      <rect x="0" y="0" width="78" height="28" rx="6" fill="#161B22" stroke="#30363D" stroke-width="1" />
      <g transform="translate(10, 6) scale(0.68)">
        <circle cx="12" cy="12" r="10" stroke="#38BDF8" stroke-width="2" fill="none" />
        <line x1="2" y1="12" x2="22" y2="12" stroke="#38BDF8" stroke-width="2" />
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" stroke="#38BDF8" stroke-width="2" fill="none" />
      </g>
      <text class="font-sans" x="35" y="18" font-size="11.5" font-weight="600" fill="#E6EDF3">Portfolio</text>
      
      <rect x="74" y="0" width="{p_val_w}" height="28" rx="6" fill="{t['portfolio_bg']}" />
      <text class="font-sans" x="{74 + p_val_w/2}" y="18" text-anchor="middle" font-size="11.5" font-weight="700" fill="{t['portfolio_text']}">{portfolio_url}</text>
    </g>

    <!-- Badge 2: LinkedIn -->
    <g class="badge-item" transform="translate({b2_x}, 0)">
      <rect x="0" y="0" width="78" height="28" rx="6" fill="#161B22" stroke="#30363D" stroke-width="1" />
      <g transform="translate(11, 6) scale(0.68)">
        <rect x="0" y="1" width="22" height="22" rx="4" fill="#0A66C2" />
        <text class="font-sans" x="11" y="17" text-anchor="middle" font-size="15" font-weight="bold" fill="#FFFFFF">in</text>
      </g>
      <text class="font-sans" x="34" y="18" font-size="11.5" font-weight="600" fill="#E6EDF3">LinkedIn</text>
      
      <rect x="74" y="0" width="{l_val_w}" height="28" rx="6" fill="{t['linkedin_bg']}" />
      <text class="font-sans" x="{74 + l_val_w/2}" y="18" text-anchor="middle" font-size="11.5" font-weight="700" fill="{t['linkedin_text']}">{linkedin_text}</text>
    </g>

    <!-- Badge 3: Email -->
    <g class="badge-item" transform="translate({b3_x}, 0)">
      <rect x="0" y="0" width="68" height="28" rx="6" fill="#161B22" stroke="#30363D" stroke-width="1" />
      <g transform="translate(10, 6) scale(0.65)">
        <rect x="2" y="4" width="20" height="16" rx="2" stroke="#F43F5E" stroke-width="2" fill="none" />
        <polyline points="2,6 12,14 22,6" stroke="#F43F5E" stroke-width="2" fill="none" />
      </g>
      <text class="font-sans" x="31" y="18" font-size="11.5" font-weight="600" fill="#E6EDF3">Email</text>
      
      <rect x="64" y="0" width="{e_val_w}" height="28" rx="6" fill="{t['email_bg']}" />
      <text class="font-sans" x="{64 + e_val_w/2}" y="18" text-anchor="middle" font-size="11.5" font-weight="700" fill="{t['email_text']}">{email_text}</text>
    </g>

    <!-- Badge 4: Location -->
    <g class="badge-item" transform="translate({b4_x}, 0)">
      <rect x="0" y="0" width="74" height="28" rx="6" fill="#161B22" stroke="#30363D" stroke-width="1" />
      <g transform="translate(11, 6) scale(0.68)">
        <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z" fill="#EF4444" />
        <circle cx="12" cy="9" r="2.5" fill="#FFFFFF" />
      </g>
      <text class="font-sans" x="31" y="18" font-size="11.5" font-weight="600" fill="#E6EDF3">Location</text>
      
      <rect x="70" y="0" width="{loc_val_w}" height="28" rx="6" fill="{t['location_bg']}" />
      <text class="font-sans" x="{70 + loc_val_w/2}" y="18" text-anchor="middle" font-size="11.5" font-weight="700" fill="{t['location_text']}">{location_text}</text>
    </g>

  </g>
</svg>"""
    return svg

def create_banner_only_svg(
    name="Siddharth Kumar",
    subtitle="GenAI & LLM Enthusiast • Full-Stack Crafter",
    theme="ocean"
):
    t = get_theme_palette(theme)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 215" width="100%" height="100%">
  <defs>
    <linearGradient id="cardGradStandalone" x1="0%" y1="15%" x2="100%" y2="85%">
      <stop offset="0%" stop-color="{t['card_grad_start']}" />
      <stop offset="42%" stop-color="{t['card_grad_mid1']}" />
      <stop offset="78%" stop-color="{t['card_grad_mid2']}" />
      <stop offset="100%" stop-color="{t['card_grad_end']}" />
    </linearGradient>

    <linearGradient id="shimmerGradStandalone" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(255,255,255,0)" />
      <stop offset="45%" stop-color="rgba(255,255,255,{t['shimmer_opacity']})" />
      <stop offset="55%" stop-color="rgba(255,255,255,{t['shimmer_opacity']})" />
      <stop offset="100%" stop-color="rgba(255,255,255,0)" />
    </linearGradient>

    <clipPath id="cardClipStandalone">
      <rect x="0" y="0" width="880" height="215" rx="14" ry="14" />
    </clipPath>

    <style>
      .font-sans {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
      }}
      @keyframes waveFlowA {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-880px); }}
      }}
      @keyframes waveFlowB {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(880px); }}
      }}
      @keyframes waveGentle {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(6px); }}
      }}
      .wave-1 {{ animation: waveFlowA 24s linear infinite; }}
      .wave-2 {{ animation: waveFlowB 18s linear infinite; opacity: 0.65; }}
      .wave-3 {{ animation: waveGentle 7s ease-in-out infinite; opacity: 0.85; }}

      @keyframes twinkle {{
        0%, 100% {{ opacity: 0.15; transform: scale(0.75); }}
        50% {{ opacity: 0.95; transform: scale(1.25); }}
      }}
      .star {{ transform-origin: center; animation: twinkle 3.8s ease-in-out infinite; }}
      .s1 {{ animation-delay: 0.3s; }}
      .s2 {{ animation-delay: 1.2s; }}
      .s3 {{ animation-delay: 2.1s; }}
      .s4 {{ animation-delay: 3.0s; }}

      @keyframes shimmer {{
        0% {{ transform: translateX(-650px) skewX(-20deg); }}
        35% {{ transform: translateX(950px) skewX(-20deg); }}
        100% {{ transform: translateX(950px) skewX(-20deg); }}
      }}
      .shimmer-bar {{ animation: shimmer 8s ease-in-out infinite; }}

      @keyframes softBreath {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-1.5px); }}
      }}
      .hero-title {{ animation: softBreath 4.5s ease-in-out infinite; }}
    </style>
  </defs>

  <g clip-path="url(#cardClipStandalone)">
    <rect x="0" y="0" width="880" height="215" fill="url(#cardGradStandalone)" />

    <circle cx="65" cy="45" r="1.5" fill="#FFFFFF" class="star s1" />
    <circle cx="195" cy="30" r="2.0" fill="#E0F2FE" class="star s3" />
    <circle cx="320" cy="60" r="1.2" fill="#FFFFFF" class="star s2" />
    <circle cx="565" cy="35" r="2.2" fill="#BAE6FD" class="star s4" />
    <circle cx="705" cy="50" r="1.5" fill="#FFFFFF" class="star s1" />
    <circle cx="805" cy="40" r="2.0" fill="#E0F2FE" class="star s3" />

    <rect class="shimmer-bar" x="0" y="0" width="350" height="215" fill="url(#shimmerGradStandalone)" />

    <g class="wave-1">
      <path d="M 0,165 C 220,140 220,190 440,165 C 660,140 660,190 880,165 C 1100,140 1100,190 1320,165 C 1540,140 1540,190 1760,165 L 1760,265 L 0,265 Z"
            fill="{t['wave_back']}" />
    </g>
    <g class="wave-2" transform="translate(-880, 0)">
      <path d="M 0,180 C 220,200 220,158 440,180 C 660,200 660,158 880,180 C 1100,200 1100,158 1320,180 C 1540,200 1540,158 1760,180 L 1760,265 L 0,265 Z"
            fill="{t['wave_mid']}" />
    </g>
    <g class="wave-3">
      <path d="M 0,190 C 180,175 360,210 540,190 C 700,174 790,205 880,188 L 880,265 L 0,265 Z"
            fill="{t['wave_front']}" />
    </g>

    <rect x="0" y="0" width="880" height="215" rx="14" ry="14" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" />

    <g class="hero-title">
      <text class="font-sans" x="440" y="96" text-anchor="middle"
            font-size="44" font-weight="800" fill="{t['title_color']}" letter-spacing="-0.5"
            filter="drop-shadow(0 4px 14px rgba(0,0,0,0.45))">
        {name}
      </text>
      <text class="font-sans" x="440" y="136" text-anchor="middle"
            font-size="18" font-weight="500" fill="{t['subtitle_color']}" letter-spacing="0.4"
            filter="drop-shadow(0 2px 6px rgba(0,0,0,0.3))">
        {subtitle}
      </text>
    </g>
  </g>
</svg>"""
    return svg

def create_tagline_svg(tagline="Turning coffee and chai into clean code", color="#FF758F"):
    char_count = max(len(tagline), 1)
    char_width = 11.9
    text_total_width = char_count * char_width
    center_x = 440
    start_x = int(center_x - (text_total_width / 2))

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 50" width="100%" height="100%">
  <defs>
    <clipPath id="taglineClip">
      <rect class="type-mask" x="{start_x}" y="0" width="0" height="50" />
    </clipPath>
    <style>
      .font-mono {{
        font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, 'Courier New', monospace;
      }}
      @keyframes typeTyping {{
        0% {{ width: 0; }}
        42% {{ width: {int(text_total_width + 12)}px; }}
        78% {{ width: {int(text_total_width + 12)}px; }}
        92% {{ width: 0; }}
        100% {{ width: 0; }}
      }}
      @keyframes cursorTranslate {{
        0% {{ transform: translateX(0); }}
        42% {{ transform: translateX({int(text_total_width + 4)}px); }}
        78% {{ transform: translateX({int(text_total_width + 4)}px); }}
        92% {{ transform: translateX(0); }}
        100% {{ transform: translateX(0); }}
      }}
      @keyframes cursorBlink {{
        0%, 48% {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}
      .type-mask {{
        animation: typeTyping 9s steps({char_count + 4}, end) infinite;
      }}
      .cursor-tracker {{
        animation: cursorTranslate 9s steps({char_count + 4}, end) infinite;
      }}
      .cursor-bar {{
        animation: cursorBlink 0.75s infinite;
      }}
    </style>
  </defs>

  <g clip-path="url(#taglineClip)">
    <text class="font-mono" x="440" y="32" text-anchor="middle"
          font-size="19" font-weight="600" fill="{color}" letter-spacing="0.5"
          filter="drop-shadow(0 0 10px {color}55)">
      {tagline}
    </text>
  </g>

  <g transform="translate({start_x}, 0)">
    <g class="cursor-tracker">
      <rect class="cursor-bar" x="0" y="16" width="2.8" height="20" rx="1.4" fill="{color}" />
    </g>
  </g>
</svg>"""
    return svg

def main():
    print("Regenerating tailored profile SVGs for Siddharth Kumar...")
    with open("banner-complete.svg", "w", encoding="utf-8") as f:
        f.write(create_banner_complete_svg())
    with open("banner.svg", "w", encoding="utf-8") as f:
        f.write(create_banner_only_svg())
    with open("tagline.svg", "w", encoding="utf-8") as f:
        f.write(create_tagline_svg())
    print("Done!")

if __name__ == "__main__":
    main()
