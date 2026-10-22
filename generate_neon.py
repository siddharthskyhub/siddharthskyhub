"""
Generate Neon Trio Banner for Siddharth Kumar
Colors:
  - Jet Black: #0A0A0A
  - Cerulean Blue: #007BA7
  - Neon Rose: #FF2095
"""

import xml.sax.saxutils as saxutils
import xml.etree.ElementTree as ET

def xml_escape(text):
    return saxutils.escape(str(text))

def generate_neon_banner(
    name="Siddharth Kumar",
    subtitle="GenAI &amp; LLM Enthusiast &#8226; Full-Stack Crafter",
    breadcrumb="siddharthskyhub / README.md",
    tagline="Turning coffee and chai into clean code",
    portfolio_url="siddharth.dev",
    linkedin_text="Let's Connect",
    email_text="Say Hello",
    location_text="Bangalore"
):
    clean_tagline = tagline.replace("&amp;", "&").replace("&#8226;", "•")
    char_count = max(len(clean_tagline), 1)
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

    b_parts = breadcrumb.split('/')
    repo_user = xml_escape(b_parts[0].strip() if len(b_parts) > 0 else 'siddharthskyhub')
    repo_file = xml_escape(b_parts[1].strip() if len(b_parts) > 1 else 'README.md')

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 405" width="100%" height="100%">
  <defs>
    <!-- Background Card Gradient: Jet Black #0A0A0A blending with Cerulean #007BA7 and Neon Rose #FF2095 -->
    <linearGradient id="neonCardGrad" x1="0%" y1="10%" x2="100%" y2="90%">
      <stop offset="0%" stop-color="#0A0A0A" />
      <stop offset="35%" stop-color="#041E28" />
      <stop offset="68%" stop-color="#007BA7" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#FF2095" stop-opacity="0.85" />
    </linearGradient>

    <!-- Glowing Border Gradient -->
    <linearGradient id="neonBorderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#007BA7" />
      <stop offset="50%" stop-color="#0A0A0A" />
      <stop offset="100%" stop-color="#FF2095" />
    </linearGradient>

    <!-- Diagonal Shimmer Beam -->
    <linearGradient id="neonShimmerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(0,123,167,0)" />
      <stop offset="50%" stop-color="rgba(255,32,149,0.3)" />
      <stop offset="100%" stop-color="rgba(0,123,167,0)" />
    </linearGradient>

    <!-- Rounded Corner Clip -->
    <clipPath id="neonCardClip">
      <rect x="20" y="44" width="880" height="215" rx="14" ry="14" />
    </clipPath>

    <!-- Typewriter Mask -->
    <clipPath id="neonTypeClip">
      <rect class="type-mask" x="{start_x}" y="275" width="0" height="45" />
    </clipPath>

    <style>
      .font-mono {{
        font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
      }}
      .font-sans {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
      }}

      /* --- Fluid Wave Oscillations --- */
      @keyframes waveScrollA {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-880px); }}
      }}
      @keyframes waveScrollB {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(880px); }}
      }}
      @keyframes waveGentle {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(6px); }}
      }}

      .wave-neon-1 {{
        animation: waveScrollA 20s linear infinite;
      }}
      .wave-neon-2 {{
        animation: waveScrollB 15s linear infinite;
        opacity: 0.7;
      }}
      .wave-neon-3 {{
        animation: waveGentle 6s ease-in-out infinite;
        opacity: 0.9;
      }}

      /* --- Twinkle Stars (Cerulean and Neon Rose) --- */
      @keyframes twinkleNeon {{
        0%, 100% {{ opacity: 0.2; transform: scale(0.8); }}
        50% {{ opacity: 1; transform: scale(1.3); }}
      }}
      .star-neon {{
        transform-origin: center;
        animation: twinkleNeon 3.6s ease-in-out infinite;
      }}
      .s1 {{ animation-delay: 0.2s; }}
      .s2 {{ animation-delay: 1.1s; }}
      .s3 {{ animation-delay: 2.0s; }}
      .s4 {{ animation-delay: 2.9s; }}

      /* --- Shimmer Beam Sweep --- */
      @keyframes shimmerNeon {{
        0% {{ transform: translateX(-650px) skewX(-20deg); }}
        35% {{ transform: translateX(950px) skewX(-20deg); }}
        100% {{ transform: translateX(950px) skewX(-20deg); }}
      }}
      .shimmer-neon {{
        animation: shimmerNeon 7.5s ease-in-out infinite;
      }}

      /* --- Hero Title Dual Neon Breathing --- */
      @keyframes softBreath {{
        0%, 100% {{ transform: translateY(0); filter: drop-shadow(0 0 12px rgba(255,32,149,0.55)) drop-shadow(0 0 24px rgba(0,123,167,0.45)); }}
        50% {{ transform: translateY(-2px); filter: drop-shadow(0 0 20px rgba(255,32,149,0.75)) drop-shadow(0 0 32px rgba(0,123,167,0.65)); }}
      }}
      .hero-title-neon {{
        animation: softBreath 4s ease-in-out infinite;
      }}

      /* --- Typewriter &amp; Blinking Cursor --- */
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
        transition: transform 0.25s ease, filter 0.25s ease;
        cursor: pointer;
      }}
      .badge-item:hover {{
        filter: brightness(1.2) drop-shadow(0 0 12px #FF2095);
        transform: translateY(-2px);
      }}
    </style>
  </defs>

  <!-- Deep Canvas: Jet Black #0A0A0A -->
  <rect width="920" height="405" fill="#0A0A0A" rx="16" />

  <!-- 1. Breadcrumb Top Bar -->
  <g class="font-mono" transform="translate(24, 28)">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5v-9zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8V1.5z"
          fill="#007BA7" transform="translate(0, -11) scale(0.9)" />
    <text x="20" y="0" font-size="13" font-weight="500" letter-spacing="0.2">
      <tspan fill="#E6EDF3">{repo_user} </tspan>
      <tspan fill="#FF2095">/</tspan>
      <tspan fill="#007BA7"> {repo_file}</tspan>
    </text>
  </g>

  <!-- 2. Main Header Banner Card -->
  <g clip-path="url(#neonCardClip)">
    <!-- Base Jet Black &amp; Neon Gradient -->
    <rect x="20" y="44" width="880" height="215" fill="url(#neonCardGrad)" />

    <!-- Twinkling Ambient Stars: Cerulean Blue &amp; Neon Rose -->
    <circle cx="85" cy="85" r="1.5" fill="#007BA7" class="star-neon s1" />
    <circle cx="215" cy="70" r="2.0" fill="#FF2095" class="star-neon s3" />
    <circle cx="340" cy="100" r="1.2" fill="#FFFFFF" class="star-neon s2" />
    <circle cx="585" cy="75" r="2.2" fill="#007BA7" class="star-neon s4" />
    <circle cx="725" cy="90" r="1.5" fill="#FF2095" class="star-neon s1" />
    <circle cx="825" cy="80" r="2.0" fill="#007BA7" class="star-neon s3" />
    <circle cx="155" cy="120" r="1.3" fill="#FF2095" class="star-neon s2" />
    <circle cx="785" cy="125" r="1.5" fill="#007BA7" class="star-neon s4" />

    <!-- Shimmer Beam -->
    <rect class="shimmer-neon" x="20" y="44" width="350" height="215" fill="url(#neonShimmerGrad)" />

    <!-- Wave 1: Jet Black #0A0A0A base layer (moving left) -->
    <g class="wave-neon-1" transform="translate(20, 0)">
      <path d="M 0,165 C 220,135 220,195 440,165 C 660,135 660,195 880,165 C 1100,135 1100,195 1320,165 C 1540,135 1540,195 1760,165 L 1760,265 L 0,265 Z"
            fill="#0A0A0A" />
    </g>

    <!-- Wave 2: Cerulean Blue #007BA7 (moving right) -->
    <g class="wave-neon-2" transform="translate(-880, 0)">
      <path d="M 0,180 C 220,205 220,155 440,180 C 660,205 660,155 880,180 C 1100,205 1100,155 1320,180 C 1540,205 1540,155 1760,180 L 1760,265 L 0,265 Z"
            fill="#007BA7" />
    </g>

    <!-- Wave 3: Neon Rose #FF2095 Crest (gentle vertical float) -->
    <g class="wave-neon-3">
      <path d="M 20,192 C 200,175 380,212 560,192 C 720,174 810,208 900,190 L 900,265 L 20,265 Z"
            fill="#FF2095" />
    </g>

    <!-- Glowing Dual Neon Border Stroke -->
    <rect x="20" y="44" width="880" height="215" rx="14" ry="14" fill="none" stroke="url(#neonBorderGrad)" stroke-width="2" />

    <!-- Hero Title &amp; Subtitle -->
    <g class="hero-title-neon">
      <text class="font-sans" x="460" y="138" text-anchor="middle"
            font-size="44" font-weight="800" fill="#FFFFFF" letter-spacing="-0.5">
        {name}
      </text>

      <text class="font-sans" x="460" y="176" text-anchor="middle"
            font-size="18" font-weight="600" fill="#007BA7" letter-spacing="0.5"
            filter="drop-shadow(0 0 6px #007BA788)">
        {subtitle}
      </text>
    </g>
  </g>

  <!-- 3. Animated Typewriter Quote: Neon Rose #FF2095 -->
  <g>
    <g clip-path="url(#neonTypeClip)">
      <text class="font-mono" x="460" y="303" text-anchor="middle"
            font-size="19" font-weight="700" fill="#FF2095" letter-spacing="0.5"
            filter="drop-shadow(0 0 12px #FF2095)">
        {xml_escape(clean_tagline)}
      </text>
    </g>

    <g transform="translate({start_x}, 0)">
      <g class="cursor-tracker">
        <rect class="cursor-bar" x="0" y="287" width="3" height="20" rx="1.5" fill="#007BA7" filter="drop-shadow(0 0 6px #007BA7)" />
      </g>
    </g>
  </g>

  <!-- 4. Badges: Strictly Jet Black #0A0A0A, Cerulean Blue #007BA7, and Neon Rose #FF2095 -->
  <g transform="translate(0, 338)">
    
    <!-- Badge 1: Portfolio (Cerulean Accent) -->
    <g class="badge-item" transform="translate({b1_x}, 0)">
      <rect x="0" y="0" width="78" height="28" rx="6" fill="#0A0A0A" stroke="#007BA7" stroke-width="1.2" />
      <g transform="translate(10, 6) scale(0.68)">
        <circle cx="12" cy="12" r="10" stroke="#007BA7" stroke-width="2" fill="none" />
        <line x1="2" y1="12" x2="22" y2="12" stroke="#007BA7" stroke-width="2" />
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" stroke="#007BA7" stroke-width="2" fill="none" />
      </g>
      <text class="font-sans" x="35" y="18" font-size="11.5" font-weight="600" fill="#FFFFFF">Portfolio</text>
      
      <rect x="74" y="0" width="{p_val_w}" height="28" rx="6" fill="#007BA7" />
      <text class="font-sans" x="{74 + p_val_w/2}" y="18" text-anchor="middle" font-size="11.5" font-weight="800" fill="#0A0A0A">{xml_escape(portfolio_url)}</text>
    </g>

    <!-- Badge 2: LinkedIn (Neon Rose Accent) -->
    <g class="badge-item" transform="translate({b2_x}, 0)">
      <rect x="0" y="0" width="78" height="28" rx="6" fill="#0A0A0A" stroke="#FF2095" stroke-width="1.2" />
      <g transform="translate(11, 6) scale(0.68)">
        <rect x="0" y="1" width="22" height="22" rx="4" fill="#FF2095" />
        <text class="font-sans" x="11" y="17" text-anchor="middle" font-size="15" font-weight="bold" fill="#0A0A0A">in</text>
      </g>
      <text class="font-sans" x="34" y="18" font-size="11.5" font-weight="600" fill="#FFFFFF">LinkedIn</text>
      
      <rect x="74" y="0" width="{l_val_w}" height="28" rx="6" fill="#FF2095" />
      <text class="font-sans" x="{74 + l_val_w/2}" y="18" text-anchor="middle" font-size="11.5" font-weight="800" fill="#0A0A0A">{xml_escape(linkedin_text)}</text>
    </g>

    <!-- Badge 3: Email (Cerulean Accent) -->
    <g class="badge-item" transform="translate({b3_x}, 0)">
      <rect x="0" y="0" width="68" height="28" rx="6" fill="#0A0A0A" stroke="#007BA7" stroke-width="1.2" />
      <g transform="translate(10, 6) scale(0.65)">
        <rect x="2" y="4" width="20" height="16" rx="2" stroke="#007BA7" stroke-width="2" fill="none" />
        <polyline points="2,6 12,14 22,6" stroke="#007BA7" stroke-width="2" fill="none" />
      </g>
      <text class="font-sans" x="31" y="18" font-size="11.5" font-weight="600" fill="#FFFFFF">Email</text>
      
      <rect x="64" y="0" width="{e_val_w}" height="28" rx="6" fill="#007BA7" />
      <text class="font-sans" x="{64 + e_val_w/2}" y="18" text-anchor="middle" font-size="11.5" font-weight="800" fill="#0A0A0A">{xml_escape(email_text)}</text>
    </g>

    <!-- Badge 4: Location (Neon Rose Accent) -->
    <g class="badge-item" transform="translate({b4_x}, 0)">
      <rect x="0" y="0" width="74" height="28" rx="6" fill="#0A0A0A" stroke="#FF2095" stroke-width="1.2" />
      <g transform="translate(11, 6) scale(0.68)">
        <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z" fill="#FF2095" />
        <circle cx="12" cy="9" r="2.5" fill="#0A0A0A" />
      </g>
      <text class="font-sans" x="31" y="18" font-size="11.5" font-weight="600" fill="#FFFFFF">Location</text>
      
      <rect x="70" y="0" width="{loc_val_w}" height="28" rx="6" fill="#FF2095" />
      <text class="font-sans" x="{70 + loc_val_w/2}" y="18" text-anchor="middle" font-size="11.5" font-weight="800" fill="#0A0A0A">{xml_escape(location_text)}</text>
    </g>

  </g>
</svg>"""
    return svg

def main():
    print("Generating Neon Palette SVG (Jet Black #0A0A0A, Cerulean Blue #007BA7, Neon Rose #FF2095)...")
    svg_content = generate_neon_banner()
    filename = "banner-neon.svg"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    # Strict validation
    tree = ET.parse(filename)
    print(f"VERIFIED: {filename} is 100% strictly valid XML! Elements: {len(list(tree.getroot().iter()))}")

if __name__ == "__main__":
    main()
