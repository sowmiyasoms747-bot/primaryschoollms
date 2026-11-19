import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

os.makedirs('assets/subjects', exist_ok=True)
os.makedirs('assets/illustrations', exist_ok=True)
os.makedirs('assets/characters', exist_ok=True)

# 1. PROCESS AND ENHANCE EXTRACTED ASSETS INTO 512x512 / TRANSPARENT PNGs

def create_subject_maths():
    # 512x512 transparent PNG with vibrant 3D rounded tile and symbols
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Shadow
    draw.rounded_rectangle([60, 80, 452, 472], radius=110, fill=(109, 40, 217, 80))
    # Main rounded tile with gradient simulation
    for i in range(120):
        t = i / 120.0
        r = int(147 * (1 - t) + 109 * t)
        g = int(51 * (1 - t) + 40 * t)
        b = int(234 * (1 - t) + 217 * t)
        draw.rounded_rectangle([60 + i*0.2, 60 + i*0.4, 452 - i*0.2, 452], radius=int(100 - i*0.3), fill=(r, g, b, 255))
        
    # Top highlight
    draw.ellipse([110, 75, 400, 160], fill=(255, 255, 255, 60))
    
    # Mathematical symbols: ÷, ×, +, -
    # Draw Division ÷ (yellow)
    draw.ellipse([140, 125, 170, 155], fill=(255, 235, 59, 255))
    draw.rounded_rectangle([130, 175, 180, 195], radius=6, fill=(255, 235, 59, 255))
    draw.ellipse([140, 215, 170, 245], fill=(255, 235, 59, 255))
    
    # Draw Multiplication × (pink/coral)
    diag_w = 12
    # X lines
    for offset in range(-diag_w, diag_w):
        draw.line([305 + offset, 130, 395 + offset, 220], fill=(255, 64, 129, 255), width=3)
        draw.line([305 + offset, 220, 395 + offset, 130], fill=(255, 64, 129, 255), width=3)
        
    # Draw Addition + (cyan/white)
    draw.rounded_rectangle([145, 280, 165, 380], radius=8, fill=(0, 229, 255, 255))
    draw.rounded_rectangle([105, 320, 205, 340], radius=8, fill=(0, 229, 255, 255))
    
    # Draw Minus - (bright orange)
    draw.rounded_rectangle([305, 320, 400, 345], radius=8, fill=(255, 171, 0, 255))
    
    img.save('assets/subjects/maths.png', 'PNG')
    print('Maths subject icon created.')

def create_subject_english():
    # 512x512 transparent PNG: 3D open book on warm background
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Shadow
    draw.rounded_rectangle([60, 80, 452, 472], radius=110, fill=(217, 119, 6, 70))
    # Tile base: warm golden gradient
    for i in range(120):
        t = i / 120.0
        r = int(251 * (1 - t) + 217 * t)
        g = int(191 * (1 - t) + 119 * t)
        b = int(36 * (1 - t) + 6 * t)
        draw.rounded_rectangle([60 + i*0.2, 60 + i*0.4, 452 - i*0.2, 452], radius=int(100 - i*0.3), fill=(r, g, b, 255))
    draw.ellipse([110, 75, 400, 160], fill=(255, 255, 255, 70))
    
    # Open book cover (red/coral)
    draw.polygon([(100, 380), (256, 410), (412, 380), (405, 200), (256, 230), (107, 200)], fill=(225, 29, 72, 255))
    # Open book pages (white/cream)
    draw.polygon([(115, 365), (252, 395), (252, 195), (115, 180)], fill=(255, 255, 255, 255))
    draw.polygon([(260, 395), (397, 365), (397, 180), (260, 195)], fill=(248, 250, 252, 255))
    
    # Page text lines (soft blue/grey)
    for y in [220, 255, 290, 325]:
        draw.rounded_rectangle([140, y, 230, y+10], radius=5, fill=(148, 163, 184, 255))
        draw.rounded_rectangle([280, y, 370, y+10], radius=5, fill=(148, 163, 184, 255))
        
    # Golden ribbon bookmark
    draw.polygon([(250, 190), (262, 190), (262, 370), (256, 355), (250, 370)], fill=(250, 204, 21, 255))
    
    img.save('assets/subjects/english.png', 'PNG')
    print('English subject icon created.')

def create_subject_evs():
    # 512x512 transparent PNG: green seedling/sprout on soft green tile
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Shadow
    draw.rounded_rectangle([60, 80, 452, 472], radius=110, fill=(16, 185, 129, 70))
    # Tile base: lush mint/emerald green gradient
    for i in range(120):
        t = i / 120.0
        r = int(52 * (1 - t) + 16 * t)
        g = int(211 * (1 - t) + 185 * t)
        b = int(153 * (1 - t) + 129 * t)
        draw.rounded_rectangle([60 + i*0.2, 60 + i*0.4, 452 - i*0.2, 452], radius=int(100 - i*0.3), fill=(r, g, b, 255))
    draw.ellipse([110, 75, 400, 160], fill=(255, 255, 255, 70))
    
    # Sprout stem (dark green)
    draw.arc([230, 240, 330, 420], start=100, end=270, fill=(5, 150, 105, 255), width=24)
    # Left leaf
    draw.pieslice([110, 190, 280, 310], start=140, end=340, fill=(74, 222, 128, 255))
    # Right leaf
    draw.pieslice([240, 170, 410, 290], start=200, end=40, fill=(34, 197, 94, 255))
    # Dew drop highlight
    draw.ellipse([320, 205, 345, 230], fill=(255, 255, 255, 220))
    
    img.save('assets/subjects/evs.png', 'PNG')
    print('EVS subject icon created.')

def create_subject_science():
    # 512x512 transparent PNG: chemistry flask with glowing pink bubbling potion
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Shadow
    draw.rounded_rectangle([60, 80, 452, 472], radius=110, fill=(2, 132, 199, 70))
    # Tile base: vibrant cyan/blue gradient
    for i in range(120):
        t = i / 120.0
        r = int(56 * (1 - t) + 2 * t)
        g = int(189 * (1 - t) + 132 * t)
        b = int(248 * (1 - t) + 199 * t)
        draw.rounded_rectangle([60 + i*0.2, 60 + i*0.4, 452 - i*0.2, 452], radius=int(100 - i*0.3), fill=(r, g, b, 255))
    draw.ellipse([110, 75, 400, 160], fill=(255, 255, 255, 70))
    
    # Flask neck & rim
    draw.rounded_rectangle([220, 150, 292, 170], radius=8, fill=(224, 242, 254, 255))
    draw.rounded_rectangle([236, 170, 276, 260], radius=4, fill=(186, 230, 253, 200))
    
    # Conical body
    draw.polygon([(240, 250), (130, 390), (382, 390), (272, 250)], fill=(224, 242, 254, 180))
    
    # Glowing magenta/pink bubbling liquid
    draw.polygon([(200, 305), (145, 385), (367, 385), (312, 305)], fill=(244, 63, 94, 240))
    # Liquid surface
    draw.ellipse([195, 295, 317, 320], fill=(251, 113, 133, 255))
    
    # Bubbles
    draw.ellipse([230, 255, 260, 285], fill=(255, 255, 255, 220))
    draw.ellipse([275, 225, 295, 245], fill=(255, 255, 255, 200))
    draw.ellipse([215, 195, 230, 210], fill=(255, 255, 255, 180))
    
    img.save('assets/subjects/science.png', 'PNG')
    print('Science subject icon created.')

def create_subject_tamil():
    # 512x512 transparent PNG: pink/magenta tile with bold white Tamil letter அ
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Shadow
    draw.rounded_rectangle([60, 80, 452, 472], radius=110, fill=(217, 70, 239, 70))
    # Tile base: vibrant fuchsia/pink gradient
    for i in range(120):
        t = i / 120.0
        r = int(244 * (1 - t) + 217 * t)
        g = int(114 * (1 - t) + 70 * t)
        b = int(182 * (1 - t) + 239 * t)
        draw.rounded_rectangle([60 + i*0.2, 60 + i*0.4, 452 - i*0.2, 452], radius=int(100 - i*0.3), fill=(r, g, b, 255))
    draw.ellipse([110, 75, 400, 160], fill=(255, 255, 255, 70))
    
    # Draw Tamil 'அ' character with smooth curves
    # Loop of 'அ'
    draw.ellipse([140, 200, 230, 290], outline=(255, 255, 255, 255), width=28)
    draw.line([185, 290, 280, 290], fill=(255, 255, 255, 255), width=28)
    draw.line([280, 170, 280, 370], fill=(255, 255, 255, 255), width=28)
    draw.arc([280, 170, 390, 370], start=270, end=90, fill=(255, 255, 255, 255), width=28)
    draw.line([335, 370, 385, 370], fill=(255, 255, 255, 255), width=28)
    
    img.save('assets/subjects/tamil.png', 'PNG')
    print('Tamil subject icon created.')

def create_subject_art():
    # 512x512 transparent PNG: painter's palette with paint splatters and brush
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Shadow
    draw.rounded_rectangle([60, 80, 452, 472], radius=110, fill=(245, 158, 11, 70))
    # Tile base: warm amber/orange gradient
    for i in range(120):
        t = i / 120.0
        r = int(251 * (1 - t) + 245 * t)
        g = int(191 * (1 - t) + 158 * t)
        b = int(36 * (1 - t) + 11 * t)
        draw.rounded_rectangle([60 + i*0.2, 60 + i*0.4, 452 - i*0.2, 452], radius=int(100 - i*0.3), fill=(r, g, b, 255))
    draw.ellipse([110, 75, 400, 160], fill=(255, 255, 255, 70))
    
    # Wooden palette base
    draw.ellipse([115, 160, 400, 370], fill=(254, 243, 199, 255), outline=(217, 119, 6, 255), width=6)
    # Thumb hole
    draw.ellipse([320, 260, 365, 315], fill=(245, 158, 11, 255))
    
    # Colorful paint drops
    draw.ellipse([160, 210, 205, 255], fill=(239, 68, 68, 255))  # Red
    draw.ellipse([215, 185, 260, 230], fill=(59, 130, 246, 255))  # Blue
    draw.ellipse([275, 185, 320, 230], fill=(34, 197, 94, 255))  # Green
    draw.ellipse([160, 275, 205, 320], fill=(234, 179, 8, 255))  # Yellow
    draw.ellipse([225, 305, 270, 350], fill=(168, 85, 247, 255)) # Purple
    
    # Paintbrush
    draw.line([130, 390, 360, 150], fill=(180, 83, 9, 255), width=18)
    draw.line([340, 170, 370, 140], fill=(156, 163, 175, 255), width=22)
    draw.line([365, 145, 395, 115], fill=(59, 130, 246, 255), width=24) # Blue bristles
    
    img.save('assets/subjects/art.png', 'PNG')
    print('Art & Craft subject icon created.')

# Run all subject creators
create_subject_maths()
create_subject_english()
create_subject_evs()
create_subject_science()
create_subject_tamil()
create_subject_art()

# 2. CREATE 1920x1080 BACKGROUND SCENERY
# A vibrant, enchanting learning landscape matching the reference image:
# Sky blue with sunbursts, rolling grassy green hills, colorful daisies, foliage framing.
def create_background_scenery():
    w, h = 1920, 1080
    img = Image.new('RGBA', (w, h), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    
    # Sky gradient: top #bce6ff to horizon #eef9ff
    for y in range(h):
        t = y / float(h)
        # soft sky blue to warm white/greenish horizon
        if t < 0.6:
            st = t / 0.6
            r = int(185 * (1 - st) + 235 * st)
            g = int(225 * (1 - st) + 248 * st)
            b = int(255 * (1 - st) + 255 * st)
        else:
            gt = (t - 0.6) / 0.4
            r = int(235 * (1 - gt) + 120 * gt)
            g = int(248 * (1 - gt) + 195 * gt)
            b = int(255 * (1 - gt) + 85 * gt)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
        
    # Soft background distant hills (misty green)
    draw.ellipse([-200, 480, 900, 950], fill=(180, 225, 155, 255))
    draw.ellipse([600, 450, 1800, 920], fill=(160, 215, 140, 255))
    draw.ellipse([1400, 480, 2200, 960], fill=(175, 220, 150, 255))
    
    # Midground rolling hill (fresh vibrant green)
    draw.ellipse([-100, 560, 1300, 1150], fill=(115, 195, 75, 255))
    draw.ellipse([800, 530, 2100, 1120], fill=(95, 180, 60, 255))
    
    # Foreground rolling meadow (lush rich green)
    draw.ellipse([-50, 650, 2050, 1300], fill=(85, 168, 50, 255))
    
    # Sun flare / soft warm glow near top center
    glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([700, -100, 1300, 400], fill=(255, 255, 220, 90))
    glow_draw.ellipse([850, -50, 1150, 250], fill=(255, 255, 255, 120))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=60))
    img = Image.alpha_composite(img, glow)
    
    # Add scattered cute pink and white daisy flowers at bottom
    np.random.seed(42)
    draw = ImageDraw.Draw(img)
    for _ in range(85):
        fx = np.random.randint(40, w - 40)
        fy = np.random.randint(h - 130, h - 15)
        # Flower petals
        petal_color = (255, 182, 193, 230) if np.random.rand() > 0.4 else (255, 255, 255, 230)
        r = np.random.randint(6, 12)
        for angle in range(0, 360, 60):
            rad = np.radians(angle)
            px = fx + int(r * np.cos(rad))
            py = fy + int(r * np.sin(rad))
            draw.ellipse([px-4, py-4, px+4, py+4], fill=petal_color)
        draw.ellipse([fx-3, fy-3, fx+3, fy+3], fill=(255, 215, 0, 255))
        
    # Lush foliage framing in top-left, top-right, bottom corners
    # Leaves top-left
    for lx, ly, lr in [(40, 20, 110), (120, -10, 130), (-20, 80, 120), (90, 90, 80)]:
        draw.ellipse([lx-lr, ly-lr, lx+lr, ly+lr], fill=(56, 142, 60, 220))
        draw.ellipse([lx-lr+10, ly-lr+10, lx+lr-10, ly+lr-10], fill=(76, 175, 80, 220))
        
    # Leaves top-right
    for lx, ly, lr in [(w-50, 20, 130), (w-130, -20, 140), (w, 90, 120), (w-100, 80, 90)]:
        draw.ellipse([lx-lr, ly-lr, lx+lr, ly+lr], fill=(46, 125, 50, 220))
        draw.ellipse([lx-lr+10, ly-lr+10, lx+lr-10, ly+lr-10], fill=(67, 160, 71, 220))
        
    img.save('assets/illustrations/background-scenery.png', 'PNG')
    print('Background scenery 1920x1080 created.')

create_background_scenery()
