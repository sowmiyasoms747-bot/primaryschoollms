import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

os.makedirs('assets/learning_plan', exist_ok=True)
os.makedirs('assets/illustrations', exist_ok=True)

def get_font(size, bold=True):
    font_paths = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def create_composed_island(island_type, icon_name, badge_type, label_text, out_path, is_purple=False, is_dark_text=False):
    # Load base images from assets/learning_plan
    base_island = Image.open(f'assets/learning_plan/{island_type}.png').convert('RGBA')
    icon = Image.open(f'assets/learning_plan/{icon_name}.png').convert('RGBA')
    badge = Image.open(f'assets/learning_plan/{badge_type}.png').convert('RGBA')
    
    # Target canvas size: 512 x 512
    canvas = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    
    # 1. Scale and position base island
    # Island width ~ 380, height ~ 240, placed at center bottom
    iw, ih = 390, int(390 * (base_island.height / base_island.width))
    island_scaled = base_island.resize((iw, ih), Image.Resampling.LANCZOS)
    ix = (512 - iw) // 2
    iy = 230
    canvas.paste(island_scaled, (ix, iy), island_scaled)
    
    # 2. Scale and position top icon
    # Icon width ~ 240, placed on top of island
    icon_w = 230
    icon_h = int(icon_w * (icon.height / icon.width))
    icon_scaled = icon.resize((icon_w, icon_h), Image.Resampling.LANCZOS)
    icon_x = (512 - icon_w) // 2
    # Adjust y position so it sits cleanly on top of the island surface
    icon_y = iy - int(icon_h * 0.72)
    canvas.paste(icon_scaled, (icon_x, icon_y), icon_scaled)
    
    # 3. Scale and position badge (checkmark or lock)
    # Badge width ~ 100, placed at top-right of icon
    bw, bh = 96, int(96 * (badge.height / badge.width))
    badge_scaled = badge.resize((bw, bh), Image.Resampling.LANCZOS)
    badge_x = icon_x + icon_w - 45
    badge_y = icon_y - 10
    canvas.paste(badge_scaled, (badge_x, badge_y), badge_scaled)
    
    # 4. Draw bold label text on front face of island
    draw = ImageDraw.Draw(canvas)
    font_size = 36 if len(label_text) <= 8 else 28
    font = get_font(font_size, bold=True)
    
    bbox = font.getbbox(label_text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    tx = (512 - tw) // 2
    ty = iy + int(ih * 0.46)
    
    if is_dark_text:
        text_color = (24, 30, 42, 255)
        # White outer glow
        for ox in range(-3, 4):
            for oy in range(-3, 4):
                if ox != 0 or oy != 0:
                    draw.text((tx + ox, ty + oy), label_text, font=font, fill=(255, 255, 255, 255))
        draw.text((tx, ty), label_text, font=font, fill=text_color)
    else:
        text_color = (255, 255, 255, 255)
        shadow_color = (18, 56, 26, 255) if not is_purple else (74, 20, 110, 255)
        # Dark shadow
        for ox in [-2, -1, 0, 1, 2]:
            for oy in [-2, -1, 0, 1, 2, 3]:
                if ox != 0 or oy != 0:
                    draw.text((tx + ox, ty + oy), label_text, font=font, fill=shadow_color)
        draw.text((tx, ty), label_text, font=font, fill=text_color)
        
    canvas.save(out_path, 'PNG')
    print('Composed island saved:', out_path)

# Create all 5 islands
# Island 1: Theory
create_composed_island('island_green', 'icon_book', 'badge_check', 'Theory', 'assets/illustrations/island_theory.png', is_purple=False, is_dark_text=False)

# Island 2: Video
create_composed_island('island_green', 'icon_video', 'badge_check', 'Video', 'assets/illustrations/island_video.png', is_purple=False, is_dark_text=False)

# Island 3: Game Practice
create_composed_island('island_grey', 'icon_gamepad', 'badge_lock', 'Game Practice', 'assets/illustrations/island_game.png', is_purple=False, is_dark_text=True)

# Island 4: Class Challenge
create_composed_island('island_grey', 'icon_trophy', 'badge_lock', 'Class Challenge', 'assets/illustrations/island_challenge.png', is_purple=False, is_dark_text=True)

# Island 5: Treasure Reward
create_composed_island('island_purple', 'icon_chest', 'badge_lock', 'Treasure Reward', 'assets/illustrations/island_treasure.png', is_purple=True, is_dark_text=False)
