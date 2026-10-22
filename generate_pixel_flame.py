"""
6-Frame Coordinated 8-Bit Pixel Flame Generator
Features:
  - 8px fine pixel grid (115 columns x 20 rows)
  - Strict Harmonic Wave Physics ensuring 100% pixel coordination across adjacent columns
  - Authentic 5-tier thermal color mapping from reference image
  - Coordinated floating spark embers
  - Discrete 6-frame retro arcade sprite cycle (100ms per frame)
  - Zero column-tearing, fully cohesive flame tongues
"""
import math
import xml.etree.ElementTree as ET

def generate_pixel_flame_banner():
    width = 920
    height = 160
    px = 8
    cols = width // px   # 115 columns
    num_frames = 6
    duration = 0.60      # 100ms per frame = 10 FPS arcade timing

    # Authentic Thermal Palette from Reference Image
    C_YELLOW = "#FFE24A"  # Hot core golden yellow
    C_AMBER  = "#FFA71A"  # Warm amber
    C_ORANGE = "#FF5500"  # Vibrant flame orange
    C_RED    = "#D81820"  # Fiery red
    C_DARK   = "#7A0A10"  # Deep crimson boundary
    STROKE   = "rgba(10, 2, 2, 0.45)"

    svg_lines = []
    svg_lines.append(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <style>
      /* 6-Frame Coordinated Retro Pixel Sprite Cycle (100ms/frame) */
      @keyframes showFrame0 {{
        0% {{ opacity: 1; }}
        16.65% {{ opacity: 1; }}
        16.66% {{ opacity: 0; }}
        100% {{ opacity: 0; }}
      }}
      @keyframes showFrame1 {{
        0% {{ opacity: 0; }}
        16.65% {{ opacity: 0; }}
        16.66% {{ opacity: 1; }}
        33.32% {{ opacity: 1; }}
        33.33% {{ opacity: 0; }}
        100% {{ opacity: 0; }}
      }}
      @keyframes showFrame2 {{
        0% {{ opacity: 0; }}
        33.32% {{ opacity: 0; }}
        33.33% {{ opacity: 1; }}
        49.99% {{ opacity: 1; }}
        50.00% {{ opacity: 0; }}
        100% {{ opacity: 0; }}
      }}
      @keyframes showFrame3 {{
        0% {{ opacity: 0; }}
        49.99% {{ opacity: 0; }}
        50.00% {{ opacity: 1; }}
        66.65% {{ opacity: 1; }}
        66.66% {{ opacity: 0; }}
        100% {{ opacity: 0; }}
      }}
      @keyframes showFrame4 {{
        0% {{ opacity: 0; }}
        66.65% {{ opacity: 0; }}
        66.66% {{ opacity: 1; }}
        83.32% {{ opacity: 1; }}
        83.33% {{ opacity: 0; }}
        100% {{ opacity: 0; }}
      }}
      @keyframes showFrame5 {{
        0% {{ opacity: 0; }}
        83.32% {{ opacity: 0; }}
        83.33% {{ opacity: 1; }}
        100% {{ opacity: 1; }}
      }}

      .frame-0 {{ animation: showFrame0 {duration}s infinite; }}
      .frame-1 {{ animation: showFrame1 {duration}s infinite; }}
      .frame-2 {{ animation: showFrame2 {duration}s infinite; }}
      .frame-3 {{ animation: showFrame3 {duration}s infinite; }}
      .frame-4 {{ animation: showFrame4 {duration}s infinite; }}
      .frame-5 {{ animation: showFrame5 {duration}s infinite; }}

      .px-cell {{
        stroke: {STROKE};
        stroke-width: 0.5;
      }}
    </style>
  </defs>

  <!-- Deep Canvas Background (Jet Black #0A0A0A) -->
  <rect width="{width}" height="{height}" fill="#0A0A0A" rx="8" />
""")

    # Generate each frame with harmonic traveling wave physics
    for f in range(num_frames):
        t = f * (2 * math.pi / num_frames)
        svg_lines.append(f'  <!-- Frame {f} -->\n  <g class="frame-{f}">')

        # Calculate coordinated heights for all 115 columns
        heights = []
        for c in range(cols):
            # Smooth harmonic traveling waves across the columns
            # Gives 8-10 distinct cohesive flame tongues across the 920px width
            w1 = math.sin(c * 0.16 + t) * 3.8
            w2 = math.cos(c * 0.32 - t * 1.4) * 2.2
            w3 = math.sin(c * 0.07 + t * 0.8) * 2.8
            w4 = math.sin(c * 0.52 + t * 2.1) * 1.4
            # Flame base height + wave offset
            h = int(7.0 + w1 + w2 + w3 + w4)
            h = max(3, min(17, h))
            heights.append(h)

        # Render coordinated pixel blocks for this frame
        for c in range(cols):
            x = c * px
            h = heights[c]

            for r in range(h):
                y = height - ((r + 1) * px)
                
                # Height ratio within this flame column (0.0 = base, 1.0 = top tip)
                ratio = r / max(h - 1, 1)

                # Thermal color banding matching reference
                if ratio < 0.25:
                    color = C_YELLOW
                elif ratio < 0.48:
                    color = C_AMBER
                elif ratio < 0.70:
                    color = C_ORANGE
                elif ratio < 0.88:
                    color = C_RED
                else:
                    color = C_DARK

                svg_lines.append(f'    <rect class="px-cell" x="{x}" y="{y}" width="{px}" height="{px}" fill="{color}" />')

        # Add coordinated floating spark embers for this frame
        # Embers rise from local flame peaks
        for c in range(2, cols - 2, 4):
            # If this is a local peak
            if heights[c] > heights[c-1] and heights[c] > heights[c+1] and heights[c] >= 8:
                h = heights[c]
                ember_y_offset = ((f + (c % 3)) % 4) + 1
                ember_r = h + ember_y_offset
                ey = height - ((ember_r + 1) * px)
                if ey > 10:
                    ex = c * px
                    ember_color = C_AMBER if ember_y_offset == 1 else (C_ORANGE if ember_y_offset == 2 else C_DARK)
                    svg_lines.append(f'    <rect class="px-cell" x="{ex}" y="{ey}" width="{px}" height="{px}" fill="{ember_color}" />')

        svg_lines.append('  </g>\n')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)

def main():
    print("Generating strictly validated 8px Coordinated Pixel Flame SVG...")
    svg_code = generate_pixel_flame_banner()
    filename = "pixel-flame.svg"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_code)

    # Validate XML
    tree = ET.parse(filename)
    print(f"VERIFIED VALID: {filename}! Root: {tree.getroot().tag}, Total elements: {len(list(tree.getroot().iter()))}")

if __name__ == "__main__":
    main()
