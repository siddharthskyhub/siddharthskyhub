"""
Pixel Flame Banner Generator
Generates a stunning 8-bit retro pixel art animated flame banner matching pixel_flame_ref.png.
"""
import xml.etree.ElementTree as ET

def generate_pixel_flame_banner():
    # 58 columns, 16px cell width = 928px width, 180px height
    width = 928
    height = 180
    px = 16

    # Palette
    C_YELLOW = "#FFD000"   # Core bright yellow
    C_AMBER  = "#FF9E00"   # Warm gold / amber
    C_ORANGE = "#FF6000"   # Vibrant orange
    C_RED    = "#D82020"   # Fiery red
    C_DARK   = "#8E0E18"   # Deep crimson outline
    STROKE   = "#1A0505"   # Pixel grid stroke

    # Heights of flame tongues for each column (0 to 57)
    # Heights in number of blocks (from bottom up, total 11 rows max)
    # Base height is around 4-5 blocks, peaks reach 8-10 blocks
    peak_pattern = [
        4, 5, 5, 7, 8, 7, 5, 4, 6, 8, 10, 9, 7, 5, 4, 6, 7, 5, 
        4, 6, 8, 9, 8, 6, 5, 7, 9, 11, 10, 8, 6, 4, 5, 7, 6, 4,
        6, 8, 10, 9, 7, 5, 4, 6, 8, 7, 5, 4, 5, 7, 9, 8, 7, 5, 4, 5, 6, 5
    ]

    # Assign each column to a flicker group: 0 = base, 1 = flicker-a, 2 = flicker-b, 3 = flicker-c
    # Alternating groups create organic chaotic fire flickering
    group_pattern = [
        1, 1, 1, 2, 2, 2, 1, 3, 3, 3, 1, 1, 1, 2, 2, 3, 3, 3,
        1, 1, 2, 2, 2, 1, 1, 3, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1,
        2, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 1
    ]

    svg_parts = []
    svg_parts.append(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <style>
      /* Retro 8-bit Stepped Arcade Fire Animation */
      @keyframes flameFlickerA {{
        0%, 100% {{ transform: translateY(0); }}
        33% {{ transform: translateY(-16px); }}
        66% {{ transform: translateY(16px); }}
      }}
      @keyframes flameFlickerB {{
        0%, 100% {{ transform: translateY(-16px); }}
        40% {{ transform: translateY(0); }}
        80% {{ transform: translateY(16px); }}
      }}
      @keyframes flameFlickerC {{
        0%, 100% {{ transform: translateY(16px); }}
        50% {{ transform: translateY(-16px); }}
        75% {{ transform: translateY(0); }}
      }}

      /* Rising Embers &amp; Sparks */
      @keyframes emberAscend1 {{
        0% {{ transform: translate(0, 0); opacity: 1; }}
        40% {{ transform: translate(16px, -32px); opacity: 0.9; }}
        80% {{ transform: translate(0, -64px); opacity: 0.5; }}
        100% {{ transform: translate(16px, -80px); opacity: 0; }}
      }}
      @keyframes emberAscend2 {{
        0% {{ transform: translate(0, 0); opacity: 1; }}
        35% {{ transform: translate(-16px, -24px); opacity: 0.95; }}
        70% {{ transform: translate(0, -56px); opacity: 0.6; }}
        100% {{ transform: translate(-16px, -76px); opacity: 0; }}
      }}
      @keyframes emberAscend3 {{
        0% {{ transform: translate(0, 0); opacity: 1; }}
        50% {{ transform: translate(16px, -40px); opacity: 0.8; }}
        100% {{ transform: translate(32px, -88px); opacity: 0; }}
      }}

      .flicker-1 {{ animation: flameFlickerA 0.45s steps(2, start) infinite; }}
      .flicker-2 {{ animation: flameFlickerB 0.55s steps(2, start) infinite; }}
      .flicker-3 {{ animation: flameFlickerC 0.50s steps(2, start) infinite; }}

      .ember-a {{ animation: emberAscend1 1.4s steps(5, start) infinite; }}
      .ember-b {{ animation: emberAscend2 1.7s steps(6, start) infinite 0.3s; }}
      .ember-c {{ animation: emberAscend3 1.5s steps(5, start) infinite 0.7s; }}
      .ember-d {{ animation: emberAscend1 1.6s steps(5, start) infinite 1.0s; }}
      .ember-e {{ animation: emberAscend2 1.8s steps(6, start) infinite 0.5s; }}
      .ember-f {{ animation: emberAscend3 1.3s steps(5, start) infinite 0.2s; }}

      .px-cell {{
        stroke: {STROKE};
        stroke-width: 0.8;
      }}
    </style>
  </defs>

  <!-- Deep Canvas Background (Jet Black #0A0A0A) -->
  <rect width="{width}" height="{height}" fill="#0A0A0A" rx="8" />
""")

    # Bottom 2 rows are always solid base (y = 148 and y = 164)
    svg_parts.append('  <!-- Solid Fire Bed Base (Anchored) -->\n  <g>')
    for col in range(len(peak_pattern)):
        x = col * px
        # Row 0 (Bottom)
        svg_parts.append(f'    <rect class="px-cell" x="{x}" y="{height - px}" width="{px}" height="{px}" fill="{C_YELLOW}" />')
        # Row 1
        svg_parts.append(f'    <rect class="px-cell" x="{x}" y="{height - (px*2)}" width="{px}" height="{px}" fill="{C_AMBER}" />')
        # Row 2
        svg_parts.append(f'    <rect class="px-cell" x="{x}" y="{height - (px*3)}" width="{px}" height="{px}" fill="{C_ORANGE}" />')
    svg_parts.append('  </g>\n')

    # Upper Flame Tongues separated into 3 flicker groups
    group_rects = {1: [], 2: [], 3: []}

    for col in range(len(peak_pattern)):
        x = col * px
        h = peak_pattern[col]
        grp = group_pattern[col]

        # Blocks from row 3 up to h
        for r in range(3, h):
            y = height - ((r + 1) * px)
            # Determine color based on height from top of this tongue
            dist_from_top = h - 1 - r

            if dist_from_top == 0:
                color = C_DARK    # Outermost dark crimson tip
            elif dist_from_top == 1:
                color = C_RED     # Fiery red
            elif dist_from_top == 2:
                color = C_ORANGE  # Orange
            elif dist_from_top == 3:
                color = C_AMBER   # Amber
            else:
                color = C_YELLOW  # Core yellow

            group_rects[grp].append(
                f'    <rect class="px-cell" x="{x}" y="{y}" width="{px}" height="{px}" fill="{color}" />'
            )

    # Output Flicker Groups
    for g_id in [1, 2, 3]:
        svg_parts.append(f'  <!-- Animated Tongue Group {g_id} -->\n  <g class="flicker-{g_id}">')
        svg_parts.extend(group_rects[g_id])
        svg_parts.append('  </g>\n')

    # Floating Embers / Sparks (1x1 pixel blocks floating above flame peaks)
    embers = [
        (4, 9, "ember-a", C_DARK),
        (10, 11, "ember-b", C_RED),
        (11, 12, "ember-c", C_ORANGE),
        (21, 10, "ember-d", C_DARK),
        (27, 12, "ember-e", C_RED),
        (28, 13, "ember-f", C_AMBER),
        (38, 11, "ember-a", C_RED),
        (39, 12, "ember-b", C_DARK),
        (44, 9, "ember-c", C_ORANGE),
        (50, 10, "ember-d", C_RED),
        (51, 11, "ember-e", C_DARK),
        (16, 8, "ember-f", C_RED),
        (33, 8, "ember-a", C_ORANGE),
    ]

    svg_parts.append('  <!-- Floating Rising Pixel Embers -->\n  <g>')
    for col, r, cls, colr in embers:
        x = col * px
        y = height - ((r + 1) * px)
        svg_parts.append(f'    <g class="{cls}">')
        svg_parts.append(f'      <rect class="px-cell" x="{x}" y="{y}" width="{px}" height="{px}" fill="{colr}" />')
        svg_parts.append('    </g>')
    svg_parts.append('  </g>\n')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)

def main():
    print("Generating pixel flame SVG...")
    svg_content = generate_pixel_flame_banner()
    filename = "pixel-flame.svg"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)

    tree = ET.parse(filename)
    print(f"VERIFIED: {filename} is strictly valid XML! Total elements: {len(list(tree.getroot().iter()))}")

if __name__ == "__main__":
    main()
