import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import numpy as np

src_path = r'C:\Users\Admin\.gemini\antigravity\brain\d5322e7a-ec00-4506-83e6-576f8ff335d2\.user_uploaded\media_1795076758054_3b35560c.jpg'
src_img = Image.open(src_path).convert('RGBA')

# 1. PRECISE EXTRACTION OF THE 5 ISLANDS FROM APPROVED REFERENCE
def extract_island_with_contour(src, box, polygon_pts, out_path, target_size=(512, 512)):
    # Crop region
    crop = src.crop(box)
    cw, ch = crop.size
    
    # Create mask with smooth anti-aliased polygon
    # Oversample mask 4x for super smooth anti-aliasing
    scale = 4
    mask_large = Image.new('L', (cw * scale, ch * scale), 0)
    draw_l = ImageDraw.Draw(mask_large)
    
    scaled_pts = [(int(p[0] * scale), int(p[1] * scale)) for p in polygon_pts]
    draw_l.polygon(scaled_pts, fill=255)
    
    # Smooth with slight blur
    mask_large = mask_large.filter(ImageFilter.GaussianBlur(radius=scale * 0.75))
    mask = mask_large.resize((cw, ch), Image.Resampling.LANCZOS)
    
    crop.putalpha(mask)
    
    # Square canvas with transparent padding
    max_dim = max(cw, ch)
    sq_img = Image.new('RGBA', (max_dim + 20, max_dim + 20), (0, 0, 0, 0))
    paste_x = (sq_img.width - cw) // 2
    paste_y = (sq_img.height - ch) // 2
    sq_img.paste(crop, (paste_x, paste_y), crop)
    
    # Resize to target 512x512
    final_img = sq_img.resize(target_size, Image.Resampling.LANCZOS)
    enhancer = ImageEnhance.Sharpness(final_img)
    final_img = enhancer.enhance(1.25)
    final_img.save(out_path, 'PNG')
    print('Saved:', out_path)

# --- ISLAND 1: THEORY ---
# Box: (108, 80, 258, 226) -> size (150, 146)
# Badge on top-right: x ~ 100..130, y ~ 4..34
# Book on top: x ~ 25..120, y ~ 15..80
# Moss island: x ~ 5..145, y ~ 65..140
pts_i1 = [
    (15, 80), (10, 95), (20, 115), (45, 138), (80, 144), (115, 138), 
    (140, 115), (145, 95), (135, 75), (138, 45), (132, 10), (108, 4), 
    (96, 12), (90, 16), (40, 18), (25, 28), (20, 55), (15, 75)
]
extract_island_with_contour(src_img, (108, 80, 258, 226), pts_i1, 'assets/illustrations/island_theory.png')

# --- ISLAND 2: VIDEO ---
# Box: (266, 80, 416, 226) -> size (150, 146)
# Badge top-right: x ~ 100..130, y ~ 4..34
# Monitor: x ~ 30..115, y ~ 16..78
# Moss island: x ~ 6..145, y ~ 65..140
pts_i2 = [
    (15, 80), (8, 98), (18, 118), (42, 138), (76, 144), (112, 138),
    (138, 118), (145, 96), (136, 75), (138, 45), (132, 10), (108, 4),
    (96, 12), (92, 16), (36, 16), (28, 30), (22, 55), (15, 75)
]
extract_island_with_contour(src_img, (266, 80, 416, 226), pts_i2, 'assets/illustrations/island_video.png')

# --- ISLAND 3: GAME PRACTICE ---
# Box: (426, 88, 572, 230) -> size (146, 142)
# Lock badge top-right: x ~ 98..126, y ~ 4..32
# Controller: x ~ 35..110, y ~ 18..75
# Grey rock island: x ~ 8..140, y ~ 60..138
pts_i3 = [
    (18, 75), (10, 95), (20, 116), (48, 136), (75, 140), (105, 136),
    (132, 118), (140, 96), (132, 75), (132, 40), (126, 8), (104, 4),
    (92, 14), (88, 18), (42, 18), (32, 30), (26, 52), (18, 75)
]
extract_island_with_contour(src_img, (426, 88, 572, 230), pts_i3, 'assets/illustrations/island_game.png')

# --- ISLAND 4: CLASS CHALLENGE ---
# Box: (580, 88, 726, 230) -> size (146, 142)
# Lock badge top-right: x ~ 98..126, y ~ 4..32
# Trophy: x ~ 35..110, y ~ 16..78
# Grey rock island: x ~ 8..140, y ~ 60..138
pts_i4 = [
    (18, 75), (10, 95), (20, 116), (48, 136), (75, 140), (105, 136),
    (132, 118), (140, 96), (132, 75), (132, 40), (126, 8), (104, 4),
    (92, 14), (88, 18), (40, 16), (32, 30), (26, 52), (18, 75)
]
extract_island_with_contour(src_img, (580, 88, 726, 230), pts_i4, 'assets/illustrations/island_challenge.png')

# --- ISLAND 5: TREASURE REWARD ---
# Box: (730, 80, 890, 238) -> size (160, 158)
# Lock badge top-right: x ~ 118..148, y ~ 8..38
# Treasure chest & light rays: x ~ 25..145, y ~ 12..85
# Purple crystal island: x ~ 10..152, y ~ 70..152
pts_i5 = [
    (18, 80), (10, 105), (25, 132), (55, 152), (85, 156), (118, 150),
    (145, 130), (155, 105), (145, 80), (148, 48), (142, 12), (118, 6),
    (105, 14), (95, 16), (45, 14), (32, 28), (24, 52), (18, 80)
]
extract_island_with_contour(src_img, (730, 80, 890, 238), pts_i5, 'assets/illustrations/island_treasure.png')

# 2. EXTRACT THE EXACT ROLLED SCROLL BANNER (Parchment background with rollers & internal meadow)
# From media_1795076758054_3b35560c.jpg:
# The entire scroll is from x: 0 to 1002, y: 32 to 266
scroll_full = src_img.crop((0, 32, 1002, 266))
scroll_full.save('assets/illustrations/scroll_banner_exact.png')
print('Saved scroll_banner_exact.png')

# Also crop just the left roller and right roller with high fidelity
left_roller = src_img.crop((0, 32, 80, 266))
left_roller.save('assets/illustrations/scroll_roller_left.png')

right_roller = src_img.crop((922, 32, 1002, 266))
right_roller.save('assets/illustrations/scroll_roller_right.png')
print('Saved left and right rollers.')

# Extract Target bullseye icon with cyan dart
target_icon = src_img.crop((92, 48, 146, 100))
target_icon.save('assets/icons/target_bullseye_dart.png')
print('Saved target_bullseye_dart.png')
