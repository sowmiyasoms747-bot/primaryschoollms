import os
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

def make_island_transparent(input_path, output_path, parchment_rgb=(254, 248, 230), tol=45):
    img = Image.open(input_path).convert('RGBA')
    arr = np.array(img, dtype=float)
    
    # Distance to parchment yellow/cream color
    diff = np.sqrt(
        (arr[:, :, 0] - parchment_rgb[0])**2 +
        (arr[:, :, 1] - parchment_rgb[1])**2 +
        (arr[:, :, 2] - parchment_rgb[2])**2
    )
    
    alpha = np.clip((diff - 20) / (tol - 20) * 255, 0, 255).astype(np.uint8)
    
    # Keep solid colors fully opaque
    solid_mask = (diff > tol)
    alpha[solid_mask] = 255
    
    alpha_img = Image.fromarray(alpha, mode='L')
    alpha_img = alpha_img.filter(ImageFilter.GaussianBlur(radius=0.8))
    
    img.putalpha(alpha_img)
    # Resize nicely to 256x256
    img = img.resize((256, 256), Image.Resampling.LANCZOS)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.2)
    img.save(output_path, 'PNG')
    print('Cleaned island saved:', output_path)

# Clean all 5 islands
for name in ['island_theory', 'island_video', 'island_game', 'island_challenge', 'island_treasure']:
    src = f'assets/illustrations/{name}.png'
    if os.path.exists(src):
        make_island_transparent(src, f'assets/illustrations/{name}_clean.png')

# Clean teacher
if os.path.exists('assets/characters/teacher.png'):
    t_img = Image.open('assets/characters/teacher.png').convert('RGBA')
    # Resize to 512x512
    t_img = t_img.resize((512, 512), Image.Resampling.LANCZOS)
    t_img.save('assets/characters/teacher_512.png')

# Clean leaderboard
if os.path.exists('assets/illustrations/leaderboard_podium.png'):
    lb_img = Image.open('assets/illustrations/leaderboard_podium.png').convert('RGBA')
    lb_img = lb_img.resize((800, 360), Image.Resampling.LANCZOS)
    lb_img.save('assets/illustrations/leaderboard_podium_clean.png')

# Clean Aarav avatar
if os.path.exists('assets/characters/aarav_avatar.png'):
    a_img = Image.open('assets/characters/aarav_avatar.png').convert('RGBA')
    a_img = a_img.resize((128, 128), Image.Resampling.LANCZOS)
    a_img.save('assets/characters/aarav_avatar_clean.png')

print('All extracted assets polished successfully!')
