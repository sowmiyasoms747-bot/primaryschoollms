import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import numpy as np

os.makedirs('assets/illustrations', exist_ok=True)
os.makedirs('assets/subjects', exist_ok=True)
os.makedirs('assets/characters', exist_ok=True)

# Helper for font loading
def get_font(size, bold=True):
    font_paths = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/comicbd.ttf" if bold else "C:/Windows/Fonts/comic.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

# ==============================================================================
# 1. GENERATE THE 5 FLOATING LEARNING ISLANDS (512x512 with transparent background)
# ==============================================================================

def draw_island_base(draw, w, h, island_type="moss"):
    # Draws the 3D floating island rock
    cx = w // 2
    # Bottom rocky cone/taper
    rock_top_y = int(h * 0.48)
    rock_bot_y = int(h * 0.82)
    
    if island_type == "moss":
        # Earthy stone bottom
        pts = [
            (int(w * 0.18), rock_top_y),
            (int(w * 0.28), int(h * 0.65)),
            (int(w * 0.42), int(h * 0.78)),
            (cx, rock_bot_y),
            (int(w * 0.58), int(h * 0.78)),
            (int(w * 0.72), int(h * 0.65)),
            (int(w * 0.82), rock_top_y)
        ]
        draw.polygon(pts, fill=(94, 76, 56, 255))
        # Rocky facets
        draw.polygon([(int(w * 0.28), int(h * 0.65)), (int(w * 0.42), int(h * 0.78)), (cx, rock_bot_y), (cx, int(h * 0.62))], fill=(116, 96, 74, 255))
        draw.polygon([(cx, rock_bot_y), (int(w * 0.58), int(h * 0.78)), (int(w * 0.72), int(h * 0.65)), (int(w * 0.52), int(h * 0.60))], fill=(75, 58, 42, 255))
        
        # Lush Green Mossy Top
        moss_pts = [
            (int(w * 0.12), int(h * 0.45)),
            (int(w * 0.22), int(h * 0.38)),
            (int(w * 0.50), int(h * 0.36)),
            (int(w * 0.78), int(h * 0.38)),
            (int(w * 0.88), int(h * 0.45)),
            (int(w * 0.84), int(h * 0.58)),
            (int(w * 0.68), int(h * 0.64)),
            (int(w * 0.50), int(h * 0.66)),
            (int(w * 0.32), int(h * 0.64)),
            (int(w * 0.16), int(h * 0.58))
        ]
        draw.polygon(moss_pts, fill=(76, 175, 80, 255))
        # Moss highlights
        draw.polygon([
            (int(w * 0.18), int(h * 0.43)),
            (int(w * 0.50), int(h * 0.38)),
            (int(w * 0.82), int(h * 0.43)),
            (int(w * 0.76), int(h * 0.52)),
            (int(w * 0.50), int(h * 0.54)),
            (int(w * 0.24), int(h * 0.52))
        ], fill=(129, 199, 132, 255))
        
    elif island_type == "rock":
        # Grey Stone Island with slate crystals
        pts = [
            (int(w * 0.18), rock_top_y),
            (int(w * 0.26), int(h * 0.66)),
            (int(w * 0.40), int(h * 0.80)),
            (cx, rock_bot_y),
            (int(w * 0.60), int(h * 0.80)),
            (int(w * 0.74), int(h * 0.66)),
            (int(w * 0.82), rock_top_y)
        ]
        draw.polygon(pts, fill=(100, 116, 139, 255))
        draw.polygon([(int(w * 0.26), int(h * 0.66)), (int(w * 0.40), int(h * 0.80)), (cx, rock_bot_y), (cx, int(h * 0.62))], fill=(148, 163, 184, 255))
        draw.polygon([(cx, rock_bot_y), (int(w * 0.60), int(h * 0.80)), (int(w * 0.74), int(h * 0.66)), (int(w * 0.52), int(h * 0.60))], fill=(71, 85, 105, 255))
        
        # Slate/cyan crystal plate top
        plate_pts = [
            (int(w * 0.14), int(h * 0.45)),
            (int(w * 0.25), int(h * 0.38)),
            (int(w * 0.50), int(h * 0.36)),
            (int(w * 0.75), int(h * 0.38)),
            (int(w * 0.86), int(h * 0.45)),
            (int(w * 0.80), int(h * 0.58)),
            (int(w * 0.50), int(h * 0.64)),
            (int(w * 0.20), int(h * 0.58))
        ]
        draw.polygon(plate_pts, fill=(186, 230, 253, 255))
        draw.polygon([
            (int(w * 0.20), int(h * 0.43)),
            (int(w * 0.50), int(h * 0.38)),
            (int(w * 0.80), int(h * 0.43)),
            (int(w * 0.74), int(h * 0.50)),
            (int(w * 0.50), int(h * 0.52)),
            (int(w * 0.26), int(h * 0.50))
        ], fill=(224, 242, 254, 255))

    elif island_type == "crystal":
        # Magical purple crystal island
        pts = [
            (int(w * 0.18), rock_top_y),
            (int(w * 0.28), int(h * 0.68)),
            (int(w * 0.42), int(h * 0.82)),
            (cx, int(h * 0.86)),
            (int(w * 0.58), int(h * 0.82)),
            (int(w * 0.72), int(h * 0.68)),
            (int(w * 0.82), rock_top_y)
        ]
        draw.polygon(pts, fill=(107, 33, 168, 255))
        draw.polygon([(int(w * 0.28), int(h * 0.68)), (int(w * 0.42), int(h * 0.82)), (cx, int(h * 0.86)), (cx, int(h * 0.64))], fill=(147, 51, 234, 255))
        draw.polygon([(cx, int(h * 0.86)), (int(w * 0.58), int(h * 0.82)), (int(w * 0.72), int(h * 0.68)), (int(w * 0.52), int(h * 0.62))], fill=(88, 28, 135, 255))
        
        # Faceted violet top
        plate_pts = [
            (int(w * 0.14), int(h * 0.45)),
            (int(w * 0.26), int(h * 0.38)),
            (int(w * 0.50), int(h * 0.36)),
            (int(w * 0.74), int(h * 0.38)),
            (int(w * 0.86), int(h * 0.45)),
            (int(w * 0.80), int(h * 0.60)),
            (int(w * 0.50), int(h * 0.66)),
            (int(w * 0.20), int(h * 0.60))
        ]
        draw.polygon(plate_pts, fill=(168, 85, 247, 255))
        draw.polygon([
            (int(w * 0.20), int(h * 0.43)),
            (int(w * 0.50), int(h * 0.38)),
            (int(w * 0.80), int(h * 0.43)),
            (int(w * 0.74), int(h * 0.52)),
            (int(w * 0.50), int(h * 0.54)),
            (int(w * 0.26), int(h * 0.52))
        ], fill=(216, 180, 254, 255))

def draw_badge(draw, cx, cy, radius, badge_type="check"):
    # Draw circular badge
    if badge_type == "check":
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=(34, 197, 94, 255), outline=(255, 255, 255, 255), width=int(radius * 0.18))
        # White checkmark
        cw = int(radius * 0.2)
        draw.line([cx - radius*0.45, cy, cx - radius*0.1, cy + radius*0.35], fill=(255, 255, 255, 255), width=cw)
        draw.line([cx - radius*0.1, cy + radius*0.35, cx + radius*0.45, cy - radius*0.35], fill=(255, 255, 255, 255), width=cw)
    else: # lock
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=(148, 163, 184, 255), outline=(255, 255, 255, 255), width=int(radius * 0.18))
        # White padlock
        lw = int(radius * 0.45)
        lh = int(radius * 0.4)
        draw.rounded_rectangle([cx - lw, cy - lh*0.2, cx + lw, cy + lh], radius=4, fill=(255, 255, 255, 255))
        draw.arc([cx - lw*0.7, cy - lh*1.1, cx + lw*0.7, cy + lh*0.2], start=180, end=0, fill=(255, 255, 255, 255), width=int(radius*0.16))

def draw_island_label(draw, text, cx, cy, font, text_color=(255, 255, 255), shadow_color=(0, 0, 0)):
    # Draw crisp drop-shadowed label text directly on the island
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = cx - tw // 2
    ty = cy - th // 2
    
    # Shadow
    for sx, sy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (1, 1), (-1, 1), (1, -1), (0, 3)]:
        draw.text((tx + sx, ty + sy), text, font=font, fill=shadow_color)
    draw.text((tx, ty), text, font=font, fill=text_color)

# 1. Island 1: Theory
def create_theory_island():
    w, h = 512, 512
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_island_base(draw, w, h, "moss")
    
    # 3D Open Textbook on top
    bx, by = w // 2, int(h * 0.28)
    # Red/orange cover
    draw.polygon([(bx - 90, by + 45), (bx, by + 65), (bx + 90, by + 45), (bx + 85, by - 40), (bx, by - 20), (bx - 85, by - 40)], fill=(225, 29, 72, 255))
    # Pages
    draw.polygon([(bx - 80, by + 35), (bx - 4, by + 52), (bx - 4, by - 28), (bx - 80, by - 45)], fill=(255, 255, 255, 255))
    draw.polygon([(bx + 4, by + 52), (bx + 80, by + 35), (bx + 80, by - 45), (bx + 4, by - 28)], fill=(248, 250, 252, 255))
    # Text lines
    for ly in [by - 25, by - 5, by + 15]:
        draw.line([(bx - 70, ly), (bx - 12, ly + 14)], fill=(148, 163, 184, 255), width=5)
        draw.line([(bx + 12, ly + 14), (bx + 70, ly)], fill=(148, 163, 184, 255), width=5)
    # Golden bookmark
    draw.polygon([(bx - 4, by - 32), (bx + 4, by - 32), (bx + 4, by + 62), (bx, by + 54), (bx - 4, by + 62)], fill=(245, 158, 11, 255))
    
    # Label "Theory" on moss front
    font = get_font(36, bold=True)
    draw_island_label(draw, "Theory", w // 2, int(h * 0.58), font, (255, 255, 255, 255), (20, 83, 45, 255))
    
    # Badge (Checkmark) at top right
    draw_badge(draw, int(w * 0.78), int(h * 0.15), 36, "check")
    
    img.save('assets/illustrations/island_theory.png', 'PNG')
    print('Saved island_theory.png')

# 2. Island 2: Video
def create_video_island():
    w, h = 512, 512
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_island_base(draw, w, h, "moss")
    
    # 3D Purple Tablet / Screen on top
    bx, by = w // 2, int(h * 0.28)
    draw.rounded_rectangle([bx - 75, by - 55, bx + 75, by + 45], radius=16, fill=(109, 40, 217, 255), outline=(237, 233, 254, 255), width=6)
    # Inner display
    draw.rounded_rectangle([bx - 63, by - 43, bx + 63, by + 33], radius=10, fill=(147, 51, 234, 255))
    # Play triangle (white)
    draw.polygon([(bx - 18, by - 24), (bx - 18, by + 24), (bx + 26, by)], fill=(255, 255, 255, 255))
    
    # Label "Video" on moss front
    font = get_font(36, bold=True)
    draw_island_label(draw, "Video", w // 2, int(h * 0.58), font, (255, 255, 255, 255), (20, 83, 45, 255))
    
    # Badge (Checkmark)
    draw_badge(draw, int(w * 0.78), int(h * 0.15), 36, "check")
    
    img.save('assets/illustrations/island_video.png', 'PNG')
    print('Saved island_video.png')

# 3. Island 3: Game Practice
def create_game_island():
    w, h = 512, 512
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_island_base(draw, w, h, "rock")
    
    # 3D Yellow Gamepad on top
    bx, by = w // 2, int(h * 0.28)
    draw.rounded_rectangle([bx - 75, by - 40, bx + 75, by + 40], radius=32, fill=(250, 204, 21, 255), outline=(202, 138, 4, 255), width=6)
    # D-pad (left)
    draw.rounded_rectangle([bx - 55, by - 18, bx - 35, by + 18], radius=4, fill=(51, 65, 85, 255))
    draw.rounded_rectangle([bx - 64, by - 9, bx - 26, by + 9], radius=4, fill=(51, 65, 85, 255))
    # Buttons (right)
    draw.ellipse([bx + 40, by - 18, bx + 54, by - 4], fill=(239, 68, 68, 255))
    draw.ellipse([bx + 26, by - 4, bx + 40, by + 10], fill=(59, 130, 246, 255))
    draw.ellipse([bx + 54, by - 4, bx + 68, by + 10], fill=(34, 197, 94, 255))
    draw.ellipse([bx + 40, by + 10, bx + 54, by + 24], fill=(168, 85, 247, 255))
    
    # Label "Game Practice" on rock front
    font = get_font(30, bold=True)
    draw_island_label(draw, "Game Practice", w // 2, int(h * 0.58), font, (255, 255, 255, 255), (15, 23, 42, 255))
    
    # Badge (Lock)
    draw_badge(draw, int(w * 0.78), int(h * 0.15), 36, "lock")
    
    img.save('assets/illustrations/island_game.png', 'PNG')
    print('Saved island_game.png')

# 4. Island 4: Class Challenge
def create_challenge_island():
    w, h = 512, 512
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_island_base(draw, w, h, "rock")
    
    # 3D Golden Trophy on top
    bx, by = w // 2, int(h * 0.28)
    # Cup body
    draw.polygon([(bx - 45, by - 45), (bx + 45, by - 45), (bx + 35, by + 15), (bx - 35, by + 15)], fill=(245, 158, 11, 255), outline=(217, 119, 6, 255), width=4)
    draw.polygon([(bx - 35, by - 40), (bx + 35, by - 40), (bx + 28, by + 10), (bx - 28, by + 10)], fill=(251, 191, 36, 255))
    # Handles
    draw.arc([bx - 68, by - 40, bx - 30, by + 5], start=90, end=270, fill=(245, 158, 11, 255), width=8)
    draw.arc([bx + 30, by - 40, bx + 68, by + 5], start=270, end=90, fill=(245, 158, 11, 255), width=8)
    # Stem & base
    draw.rounded_rectangle([bx - 10, by + 15, bx + 10, by + 35], radius=2, fill=(217, 119, 6, 255))
    draw.rounded_rectangle([bx - 32, by + 35, bx + 32, by + 48], radius=4, fill=(180, 83, 9, 255))
    # Red star on trophy
    draw.ellipse([bx - 10, by - 18, bx + 10, by + 2], fill=(239, 68, 68, 255))
    
    # Label "Class Challenge" on rock front
    font = get_font(28, bold=True)
    draw_island_label(draw, "Class Challenge", w // 2, int(h * 0.58), font, (255, 255, 255, 255), (15, 23, 42, 255))
    
    # Badge (Lock)
    draw_badge(draw, int(w * 0.78), int(h * 0.15), 36, "lock")
    
    img.save('assets/illustrations/island_challenge.png', 'PNG')
    print('Saved island_challenge.png')

# 5. Island 5: Treasure Reward
def create_treasure_island():
    w, h = 512, 512
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Sparkling rays behind chest
    cx, cy = w // 2, int(h * 0.28)
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x2 = cx + int(110 * math.cos(rad))
        y2 = cy + int(110 * math.sin(rad))
        draw.line([(cx, cy), (x2, y2)], fill=(255, 255, 255, 90), width=6)
        
    draw_island_base(draw, w, h, "crystal")
    
    # 3D Treasure Chest on top
    # Chest base (red velvet & wood)
    draw.rounded_rectangle([cx - 55, cy - 10, cx + 55, cy + 45], radius=8, fill=(185, 28, 28, 255), outline=(245, 158, 11, 255), width=6)
    # Lid (curved dome)
    draw.pieslice([cx - 55, cy - 50, cx + 55, cy + 10], start=180, end=0, fill=(220, 38, 38, 255), outline=(245, 158, 11, 255), width=6)
    # Gold straps & lock
    draw.line([(cx - 28, cy - 42), (cx - 28, cy + 42)], fill=(251, 191, 36, 255), width=8)
    draw.line([(cx + 28, cy - 42), (cx + 28, cy + 42)], fill=(251, 191, 36, 255), width=8)
    draw.rounded_rectangle([cx - 12, cy - 5, cx + 12, cy + 20], radius=4, fill=(251, 191, 36, 255), outline=(180, 83, 9, 255), width=3)
    draw.ellipse([cx - 4, cy + 2, cx + 4, cy + 10], fill=(30, 41, 59, 255))
    
    # Label "Treasure Reward" on crystal front
    font = get_font(28, bold=True)
    draw_island_label(draw, "Treasure Reward", w // 2, int(h * 0.58), font, (255, 255, 255, 255), (88, 28, 135, 255))
    
    # Badge (Lock)
    draw_badge(draw, int(w * 0.78), int(h * 0.15), 36, "lock")
    
    img.save('assets/illustrations/island_treasure.png', 'PNG')
    print('Saved island_treasure.png')

# Generate all 5 islands
create_theory_island()
create_video_island()
create_game_island()
create_challenge_island()
create_treasure_island()

# ==============================================================================
# 2. GENERATE WOODEN SCROLL ENDS (for realistic 3D rolled parchment)
# ==============================================================================
def create_scroll_rollers():
    # Left roller
    img_l = Image.new('RGBA', (48, 280), (0, 0, 0, 0))
    draw_l = ImageDraw.Draw(img_l)
    # Wooden rod
    for y in range(280):
        # Top and bottom knobs
        if y < 35 or y > 245:
            r, g, b = 245, 158, 11 # Golden knob
        else:
            r, g, b = 180, 83, 9   # Warm wood
        draw_l.line([(8, y), (40, y)], fill=(r, g, b, 255))
    # Highlights
    draw_l.line([(14, 0), (14, 280)], fill=(255, 255, 255, 120), width=4)
    img_l.save('assets/illustrations/scroll_roller_left.png', 'PNG')
    
    # Right roller (mirror)
    img_r = img_l.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    img_r.save('assets/illustrations/scroll_roller_right.png', 'PNG')
    print('Saved scroll rollers.')

create_scroll_rollers()

# ==============================================================================
# 3. GENERATE CRISP 3D SUBJECT TILES (512x512 with transparent background)
# ==============================================================================
def create_3d_subject_tile(name, base_color_top, base_color_bot, border_color, icon_drawer):
    w, h = 512, 512
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Soft drop shadow
    draw.rounded_rectangle([48, 68, 464, 464], radius=110, fill=(0, 0, 0, 45))
    
    # Gradient rounded tile
    for i in range(100):
        t = i / 100.0
        r = int(base_color_top[0] * (1 - t) + base_color_bot[0] * t)
        g = int(base_color_top[1] * (1 - t) + base_color_bot[1] * t)
        b = int(base_color_top[2] * (1 - t) + base_color_bot[2] * t)
        draw.rounded_rectangle([48 + i*0.2, 48 + i*0.4, 464 - i*0.2, 448], radius=int(100 - i*0.25), fill=(r, g, b, 255))
        
    # Top glossy highlight
    draw.ellipse([90, 60, 420, 150], fill=(255, 255, 255, 75))
    
    # Custom 3D Icon inside
    icon_drawer(draw, w // 2, h // 2)
    
    img.save(f'assets/subjects/{name}.png', 'PNG')
    print(f'Saved subject {name}.png')

# Maths
def draw_maths_icon(draw, cx, cy):
    # Purple cube with math symbols
    draw.rounded_rectangle([cx - 100, cy - 90, cx + 100, cy + 90], radius=32, fill=(124, 58, 237, 255), outline=(221, 214, 254, 255), width=8)
    # Division ÷ (yellow)
    draw.ellipse([cx - 65, cy - 65, cx - 45, cy - 45], fill=(253, 224, 71, 255))
    draw.rounded_rectangle([cx - 75, cy - 35, cx - 35, cy - 23], radius=4, fill=(253, 224, 71, 255))
    draw.ellipse([cx - 65, cy - 13, cx - 45, cy + 7], fill=(253, 224, 71, 255))
    # Multiplication × (pink)
    draw.line([(cx + 35, cy - 60), (cx + 75, cy - 20)], fill=(244, 114, 182, 255), width=12)
    draw.line([(cx + 75, cy - 60), (cx + 35, cy - 20)], fill=(244, 114, 182, 255), width=12)
    # Addition + (cyan)
    draw.line([(cx - 55, cy + 30), (cx - 55, cy + 70)], fill=(56, 189, 248, 255), width=12)
    draw.line([(cx - 75, cy + 50), (cx - 35, cy + 50)], fill=(56, 189, 248, 255), width=12)
    # Minus - (orange)
    draw.line([(cx + 35, cy + 50), (cx + 75, cy + 50)], fill=(251, 146, 60, 255), width=12)

# English
def draw_english_icon(draw, cx, cy):
    # Red open storybook
    draw.polygon([(cx - 100, cy + 45), (cx, cy + 70), (cx + 100, cy + 45), (cx + 90, cy - 50), (cx, cy - 25), (cx - 90, cy - 50)], fill=(225, 29, 72, 255))
    draw.polygon([(cx - 90, cy + 35), (cx - 4, cy + 58), (cx - 4, cy - 35), (cx - 90, cy - 55)], fill=(255, 255, 255, 255))
    draw.polygon([(cx + 4, cy + 58), (cx + 90, cy + 35), (cx + 90, cy - 55), (cx + 4, cy - 35)], fill=(248, 250, 252, 255))
    draw.polygon([(cx - 4, cy - 40), (cx + 4, cy - 40), (cx + 4, cy + 65), (cx, cy + 55), (cx - 4, cy + 65)], fill=(245, 158, 11, 255))

# EVS
def draw_evs_icon(draw, cx, cy):
    # Plant seedling sprout
    draw.ellipse([cx - 85, cy + 45, cx + 85, cy + 95], fill=(120, 53, 15, 255))
    draw.arc([cx - 15, cy - 45, cx + 75, cy + 65], start=100, end=270, fill=(22, 101, 52, 255), width=24)
    draw.pieslice([cx - 105, cy - 70, cx + 15, cy + 25], start=140, end=340, fill=(74, 222, 128, 255))
    draw.pieslice([cx - 5, cy - 90, cx + 115, cy + 5], start=200, end=40, fill=(34, 197, 94, 255))
    draw.ellipse([cx + 40, cy - 65, cx + 58, cy - 47], fill=(255, 255, 255, 220))

# Science
def draw_science_icon(draw, cx, cy):
    # Chemistry conical flask with pink bubbling liquid
    draw.rounded_rectangle([cx - 28, cy - 95, cx + 28, cy - 80], radius=6, fill=(224, 242, 254, 255))
    draw.rounded_rectangle([cx - 18, cy - 80, cx + 18, cy - 10], radius=4, fill=(186, 230, 253, 200))
    draw.polygon([(cx - 18, cy - 10), (cx - 95, cy + 85), (cx + 95, cy + 85), (cx + 18, cy - 10)], fill=(224, 242, 254, 180))
    draw.polygon([(cx - 65, cy + 25), (cx - 90, cy + 82), (cx + 90, cy + 82), (cx + 65, cy + 25)], fill=(244, 63, 94, 240))
    draw.ellipse([cx - 65, cy + 15, cx + 65, cy + 35], fill=(251, 113, 133, 255))
    draw.ellipse([cx - 15, cy - 25, cx + 10, cy], fill=(255, 255, 255, 220))
    draw.ellipse([cx + 20, cy - 45, cx + 38, cy - 27], fill=(255, 255, 255, 180))

# Tamil
def draw_tamil_icon(draw, cx, cy):
    # Magenta tile with white Tamil calligraphy 'அ'
    draw.ellipse([cx - 85, cy - 50, cx - 15, cy + 20], outline=(255, 255, 255, 255), width=24)
    draw.line([(cx - 50, cy + 20), (cx + 20, cy + 20)], fill=(255, 255, 255, 255), width=24)
    draw.line([(cx + 20, cy - 75), (cx + 20, cy + 75)], fill=(255, 255, 255, 255), width=24)
    draw.arc([cx + 20, cy - 75, cx + 95, cy + 75], start=270, end=90, fill=(255, 255, 255, 255), width=24)
    draw.line([(cx + 55, cy + 75), (cx + 95, cy + 75)], fill=(255, 255, 255, 255), width=24)

# Art & Craft
def draw_art_icon(draw, cx, cy):
    # Palette with paint blobs & brush
    draw.ellipse([cx - 105, cy - 75, cx + 95, cy + 75], fill=(254, 243, 199, 255), outline=(217, 119, 6, 255), width=6)
    draw.ellipse([cx + 45, cy - 5, cx + 75, cy + 35], fill=(245, 158, 11, 255))
    draw.ellipse([cx - 65, cy - 45, cx - 35, cy - 15], fill=(239, 68, 68, 255))
    draw.ellipse([cx - 20, cy - 65, cx + 10, cy - 35], fill=(59, 130, 246, 255))
    draw.ellipse([cx + 25, cy - 60, cx + 55, cy - 30], fill=(34, 197, 94, 255))
    draw.ellipse([cx - 70, cy + 10, cx - 40, cy + 40], fill=(234, 179, 8, 255))
    draw.line([(cx - 95, cy + 90), (cx + 80, cy - 85)], fill=(180, 83, 9, 255), width=16)
    draw.line([(cx + 65, cy - 70), (cx + 95, cy - 100)], fill=(59, 130, 246, 255), width=20)

create_3d_subject_tile("maths", (168, 85, 247), (126, 34, 206), (192, 132, 252), draw_maths_icon)
create_3d_subject_tile("english", (251, 146, 60), (234, 88, 12), (253, 186, 116), draw_english_icon)
create_3d_subject_tile("evs", (74, 222, 128), (22, 163, 74), (134, 239, 172), draw_evs_icon)
create_3d_subject_tile("science", (56, 189, 248), (2, 132, 199), (125, 211, 252), draw_science_icon)
create_3d_subject_tile("tamil", (244, 114, 182), (219, 39, 119), (249, 168, 212), draw_tamil_icon)
create_3d_subject_tile("art", (250, 204, 21), (217, 119, 6), (253, 224, 71), draw_art_icon)

# ==============================================================================
# 4. GENERATE 1920x1080 BACKGROUND WITH OAK TREE TRUNK ON RIGHT & SUNBURST
# ==============================================================================
def create_lush_background():
    w, h = 1920, 1080
    img = Image.new('RGBA', (w, h), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    
    # Sky gradient: top #bfe7fe to horizon #eefaff
    for y in range(h):
        t = y / float(h)
        if t < 0.55:
            st = t / 0.55
            r = int(180 * (1 - st) + 230 * st)
            g = int(225 * (1 - st) + 248 * st)
            b = int(255 * (1 - st) + 255 * st)
        else:
            gt = (t - 0.55) / 0.45
            r = int(230 * (1 - gt) + 115 * gt)
            g = int(248 * (1 - gt) + 195 * gt)
            b = int(255 * (1 - gt) + 80 * gt)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
        
    # Sunburst / Sun rays from upper-middle
    sun_glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(sun_glow)
    cx, cy = int(w * 0.45), int(h * 0.05)
    for angle in range(0, 360, 15):
        rad = math.radians(angle)
        x2 = cx + int(1400 * math.cos(rad))
        y2 = cy + int(1400 * math.sin(rad))
        glow_draw.line([(cx, cy), (x2, y2)], fill=(255, 255, 230, 45), width=28)
    glow_draw.ellipse([cx - 280, cy - 280, cx + 280, cy + 280], fill=(255, 255, 255, 110))
    sun_glow = sun_glow.filter(ImageFilter.GaussianBlur(radius=40))
    img = Image.alpha_composite(img, sun_glow)
    
    draw = ImageDraw.Draw(img)
    
    # Distant hills
    draw.ellipse([-150, 480, 950, 950], fill=(175, 222, 150, 255))
    draw.ellipse([650, 450, 1750, 920], fill=(158, 212, 138, 255))
    draw.ellipse([1350, 480, 2150, 960], fill=(170, 218, 148, 255))
    
    # Midground rolling hill
    draw.ellipse([-80, 560, 1350, 1150], fill=(110, 192, 70, 255))
    draw.ellipse([780, 530, 2150, 1120], fill=(90, 176, 55, 255))
    
    # Foreground meadow
    draw.ellipse([-40, 660, 2060, 1300], fill=(78, 164, 44, 255))
    
    # Ancient Oak Tree Trunk & Branches on the right (where the treehouse perches!)
    tree_x = int(w * 0.72)
    # Sturdy wooden trunk rising up
    draw.polygon([
        (tree_x, h), (tree_x + 40, int(h * 0.45)), 
        (tree_x + 120, int(h * 0.20)), (tree_x + 220, 0),
        (tree_x + 320, 0), (tree_x + 240, int(h * 0.35)),
        (tree_x + 180, int(h * 0.55)), (tree_x + 160, h)
    ], fill=(120, 75, 42, 255))
    # Horizontal branch supporting treehouse
    draw.polygon([
        (tree_x + 30, int(h * 0.32)), (int(w * 0.54), int(h * 0.22)),
        (int(w * 0.54), int(h * 0.16)), (tree_x + 60, int(h * 0.26))
    ], fill=(108, 66, 36, 255))
    
    # Lush leafy canopy in top-right
    for lx, ly, lr in [(int(w*0.82), 60, 240), (int(w*0.72), 40, 220), (int(w*0.92), 120, 260), (int(w*0.62), 80, 180), (w - 20, 40, 250)]:
        draw.ellipse([lx - lr, ly - lr, lx + lr, ly + lr], fill=(46, 125, 50, 235))
        draw.ellipse([lx - lr + 15, ly - lr + 15, lx + lr - 15, ly + lr - 15], fill=(67, 160, 71, 235))
        
    # Foliage top-left
    for lx, ly, lr in [(60, 20, 140), (160, -20, 150), (-20, 80, 130), (120, 90, 100)]:
        draw.ellipse([lx - lr, ly - lr, lx + lr, ly + lr], fill=(56, 142, 60, 235))
        draw.ellipse([lx - lr + 12, ly - lr + 12, lx + lr - 12, ly + lr - 12], fill=(76, 175, 80, 235))
        
    # Foreground flowers (pink and white daisies) & pebbles
    np.random.seed(101)
    for _ in range(75):
        fx = np.random.randint(30, w - 30)
        fy = np.random.randint(h - 120, h - 15)
        # Daisy
        petal_col = (255, 182, 193, 240) if np.random.rand() > 0.45 else (255, 255, 255, 240)
        r = np.random.randint(6, 12)
        for angle in range(0, 360, 60):
            rad = math.radians(angle)
            px = fx + int(r * math.cos(rad))
            py = fy + int(r * math.sin(rad))
            draw.ellipse([px-4, py-4, px+4, py+4], fill=petal_col)
        draw.ellipse([fx-3, fy-3, fx+3, fy+3], fill=(255, 215, 0, 255))
        
    # Pebbles
    for _ in range(25):
        px = np.random.randint(50, w - 50)
        py = np.random.randint(h - 80, h - 10)
        pw, ph = np.random.randint(12, 28), np.random.randint(8, 16)
        draw.ellipse([px - pw//2, py - ph//2, px + pw//2, py + ph//2], fill=(148, 163, 184, 220))
        draw.ellipse([px - pw//2 + 2, py - ph//2 + 2, px + pw//2 - 2, py + ph//2 - 2], fill=(203, 213, 225, 220))

    img.save('assets/illustrations/background-scenery.png', 'PNG')
    print('Saved background-scenery.png')

create_lush_background()
