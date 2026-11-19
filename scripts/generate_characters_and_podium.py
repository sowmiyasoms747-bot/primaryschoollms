import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

os.makedirs('assets/characters', exist_ok=True)
os.makedirs('assets/illustrations', exist_ok=True)

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


# 1. Cute Teacher Avatar (512x512)
def create_teacher():
    w, h = 512, 512
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = w // 2, h // 2
    
    # Soft background circle glow
    draw.ellipse([cx - 200, cy - 200, cx + 200, cy + 200], fill=(224, 242, 254, 255))
    
    # Purple Blouse / Shoulders
    draw.ellipse([cx - 160, cy + 110, cx + 160, cy + 320], fill=(147, 51, 234, 255))
    draw.polygon([(cx - 140, cy + 180), (cx + 140, cy + 180), (cx + 120, h), (cx - 120, h)], fill=(126, 34, 206, 255))
    
    # Neck
    draw.rounded_rectangle([cx - 36, cy + 70, cx + 36, cy + 130], radius=10, fill=(254, 215, 170, 255))
    
    # Head & Face
    draw.ellipse([cx - 100, cy - 100, cx + 100, cy + 100], fill=(255, 237, 213, 255))
    
    # Dark brown hair (styled hair with cute side bangs)
    draw.ellipse([cx - 125, cy - 135, cx + 125, cy + 50], fill=(67, 40, 24, 255))
    draw.ellipse([cx - 100, cy - 90, cx + 100, cy + 90], fill=(255, 237, 213, 255)) # face
    draw.pieslice([cx - 120, cy - 140, cx + 120, cy + 10], start=180, end=0, fill=(67, 40, 24, 255))
    draw.ellipse([cx - 110, cy - 40, cx - 75, cy + 60], fill=(67, 40, 24, 255))
    draw.ellipse([cx + 75, cy - 40, cx + 110, cy + 60], fill=(67, 40, 24, 255))
    
    # Cute round glasses (black frames)
    draw.ellipse([cx - 75, cy - 20, cx - 15, cy + 40], outline=(30, 41, 59, 255), width=7)
    draw.ellipse([cx + 15, cy - 20, cx + 75, cy + 40], outline=(30, 41, 59, 255), width=7)
    draw.line([(cx - 15, cy + 10), (cx + 15, cy + 10)], fill=(30, 41, 59, 255), width=6)
    
    # Eyes & Smile
    draw.ellipse([cx - 52, cy, cx - 38, cy + 20], fill=(30, 41, 59, 255))
    draw.ellipse([cx + 38, cy, cx + 52, cy + 20], fill=(30, 41, 59, 255))
    draw.arc([cx - 28, cy + 30, cx + 28, cy + 65], start=0, end=180, fill=(225, 29, 72, 255), width=6)
    
    # Blushing pink cheeks
    draw.ellipse([cx - 82, cy + 28, cx - 60, cy + 45], fill=(251, 113, 133, 120))
    draw.ellipse([cx + 60, cy + 28, cx + 82, cy + 45], fill=(251, 113, 133, 120))
    
    # Wooden pointer stick held in hand
    draw.line([(cx + 110, cy + 170), (cx + 175, cy - 40)], fill=(180, 83, 9, 255), width=8)
    draw.ellipse([cx + 170, cy - 45, cx + 180, cy - 35], fill=(245, 158, 11, 255))
    
    img.save('assets/characters/teacher.png', 'PNG')
    print('Teacher avatar saved.')

# 2. Leaderboard Podium (800x400)
def create_leaderboard():
    w, h = 800, 400
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Podium pedestals:
    # Rank 2 (Silver, left): x: 120 to 300, y: 220 to 360
    # Rank 1 (Gold, center): x: 310 to 490, y: 160 to 360
    # Rank 3 (Bronze, right): x: 500 to 680, y: 250 to 360
    
    # Silver Pedestal (2)
    draw.rounded_rectangle([120, 220, 300, 360], radius=16, fill=(203, 213, 225, 255), outline=(148, 163, 184, 255), width=4)
    draw.ellipse([185, 260, 235, 310], fill=(255, 255, 255, 255))
    # Number 2
    # Gold Pedestal (1)
    draw.rounded_rectangle([310, 160, 490, 360], radius=16, fill=(251, 191, 36, 255), outline=(217, 119, 6, 255), width=4)
    draw.ellipse([375, 220, 425, 270], fill=(255, 255, 255, 255))
    # Bronze Pedestal (3)
    draw.rounded_rectangle([500, 250, 680, 360], radius=16, fill=(251, 146, 60, 255), outline=(194, 65, 12, 255), width=4)
    draw.ellipse([565, 280, 615, 330], fill=(255, 255, 255, 255))
    
    # Numbers
    font_lg = get_font(38, bold=True)
    draw.text((200, 265), "2", font=font_lg, fill=(71, 85, 105, 255))
    draw.text((390, 225), "1", font=font_lg, fill=(180, 83, 9, 255))
    draw.text((580, 285), "3", font=font_lg, fill=(154, 52, 18, 255))
    
    # Kid 2 (Ananya, left): girl with dark pigtails
    draw.ellipse([160, 110, 260, 210], fill=(255, 237, 213, 255)) # face
    draw.ellipse([145, 95, 275, 170], fill=(30, 41, 59, 255)) # hair
    draw.ellipse([165, 115, 255, 205], fill=(255, 237, 213, 255)) # inner face
    draw.ellipse([185, 145, 197, 160], fill=(30, 41, 59, 255))
    draw.ellipse([223, 145, 235, 160], fill=(30, 41, 59, 255))
    draw.arc([195, 165, 225, 185], start=0, end=180, fill=(225, 29, 72, 255), width=4)
    
    # Kid 1 (Rohan, center): boy with golden crown & laurels
    # Laurel sparks
    for offset in [-65, 65]:
        draw.ellipse([400 + offset - 10, 80, 400 + offset + 10, 100], fill=(250, 204, 21, 200))
    # Face
    draw.ellipse([350, 60, 450, 160], fill=(255, 237, 213, 255))
    draw.ellipse([345, 45, 455, 110], fill=(120, 53, 15, 255)) # hair
    draw.ellipse([355, 65, 445, 155], fill=(255, 237, 213, 255)) # inner face
    draw.ellipse([375, 95, 387, 110], fill=(30, 41, 59, 255))
    draw.ellipse([413, 95, 425, 110], fill=(30, 41, 59, 255))
    draw.arc([385, 115, 415, 135], start=0, end=180, fill=(225, 29, 72, 255), width=4)
    # Golden Crown on Rohan
    draw.polygon([(365, 45), (375, 15), (390, 30), (400, 10), (410, 30), (425, 15), (435, 45)], fill=(250, 204, 21, 255), outline=(217, 119, 6, 255), width=3)
    
    # Kid 3 (Aarav, right): boy smiling
    draw.ellipse([540, 140, 640, 240], fill=(255, 237, 213, 255))
    draw.ellipse([535, 125, 645, 190], fill=(30, 41, 59, 255)) # hair
    draw.ellipse([545, 145, 635, 235], fill=(255, 237, 213, 255)) # inner face
    draw.ellipse([565, 175, 577, 190], fill=(30, 41, 59, 255))
    draw.ellipse([603, 175, 615, 190], fill=(30, 41, 59, 255))
    draw.arc([575, 195, 605, 215], start=0, end=180, fill=(225, 29, 72, 255), width=4)
    
    img.save('assets/illustrations/leaderboard_podium.png', 'PNG')
    print('Leaderboard podium saved.')

# 3. Aarav Avatar (128x128)
def create_aarav_avatar():
    w, h = 128, 128
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Circle outline
    draw.ellipse([4, 4, 124, 124], fill=(224, 242, 254, 255), outline=(59, 130, 246, 255), width=4)
    # Head & hair
    draw.ellipse([28, 20, 100, 92], fill=(255, 237, 213, 255))
    draw.ellipse([24, 14, 104, 62], fill=(30, 41, 59, 255))
    draw.ellipse([30, 24, 98, 90], fill=(255, 237, 213, 255))
    # Eyes & Smile
    draw.ellipse([46, 48, 54, 60], fill=(30, 41, 59, 255))
    draw.ellipse([74, 48, 82, 60], fill=(30, 41, 59, 255))
    draw.arc([52, 62, 76, 78], start=0, end=180, fill=(225, 29, 72, 255), width=3)
    # Shoulders
    draw.ellipse([20, 95, 108, 150], fill=(37, 99, 235, 255))
    
    img.save('assets/characters/aarav_avatar.png', 'PNG')
    print('Aarav avatar saved.')

create_teacher()
create_leaderboard()
create_aarav_avatar()
