import os
from PIL import Image, ImageOps, ImageFilter
import numpy as np

os.makedirs('assets/icons', exist_ok=True)
os.makedirs('assets/characters', exist_ok=True)
os.makedirs('assets/illustrations', exist_ok=True)
os.makedirs('assets/subjects', exist_ok=True)

# 1. GENERATE ALL CRISP SVG ICONS
icons = {
'icon-home.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <path d="M32 8 L8 28 L14 28 L14 54 C14 56.2 15.8 58 18 58 L46 58 C48.2 58 50 56.2 50 54 L50 28 L56 28 Z" fill="currentColor"/>
  <path d="M26 58 L26 38 C26 35.8 27.8 34 30 34 L34 34 C36.2 34 38 35.8 38 38 L38 58 Z" fill="#ffffff" opacity="0.4"/>
</svg>''',

'icon-my-learning.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <path d="M32 16 C26 12 14 12 8 16 L8 50 C14 46 26 46 32 50 C38 46 50 46 56 50 L56 16 C50 12 38 12 32 16 Z" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="32" y1="16" x2="32" y2="50" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
  <path d="M14 26 C20 23 27 23 30 25" stroke="currentColor" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
  <path d="M34 25 C37 23 44 23 50 26" stroke="currentColor" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
</svg>''',

'icon-quizzes.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <circle cx="32" cy="32" r="24" fill="none" stroke="currentColor" stroke-width="4.5"/>
  <circle cx="32" cy="32" r="16" fill="none" stroke="currentColor" stroke-width="4"/>
  <circle cx="32" cy="32" r="8" fill="none" stroke="currentColor" stroke-width="3.5"/>
  <circle cx="32" cy="32" r="3.5" fill="currentColor"/>
  <path d="M48 16 L35 29" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
  <path d="M44 14 L50 20" stroke="currentColor" stroke-width="3.5" stroke-linecap="round"/>
</svg>''',

'icon-assignments.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect x="12" y="14" width="40" height="44" rx="8" fill="none" stroke="currentColor" stroke-width="4.5"/>
  <rect x="24" y="8" width="16" height="10" rx="3" fill="currentColor"/>
  <line x1="24" y1="26" x2="44" y2="26" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
  <line x1="24" y1="36" x2="44" y2="36" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
  <line x1="24" y1="46" x2="36" y2="46" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
  <circle cx="18" cy="26" r="2.5" fill="currentColor"/>
  <circle cx="18" cy="36" r="2.5" fill="currentColor"/>
  <circle cx="18" cy="46" r="2.5" fill="currentColor"/>
</svg>''',

'icon-live-classes.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect x="8" y="16" width="34" height="32" rx="8" fill="none" stroke="currentColor" stroke-width="4.5"/>
  <polygon points="42,27 56,18 56,46 42,37" fill="currentColor"/>
  <polygon points="22,25 32,32 22,39" fill="currentColor"/>
</svg>''',

'icon-progress.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect x="10" y="38" width="8" height="18" rx="3" fill="currentColor"/>
  <rect x="24" y="26" width="8" height="30" rx="3" fill="currentColor"/>
  <rect x="38" y="18" width="8" height="38" rx="3" fill="currentColor"/>
  <rect x="52" y="10" width="8" height="46" rx="3" fill="currentColor"/>
</svg>''',

'icon-achievements.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <polygon points="32,6 39,22 56,24 43,36 47,53 32,44 17,53 21,36 8,24 25,22" fill="currentColor"/>
</svg>''',

'icon-ai-buddy.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect x="12" y="20" width="40" height="32" rx="10" fill="none" stroke="currentColor" stroke-width="4.5"/>
  <line x1="32" y1="8" x2="32" y2="20" stroke="currentColor" stroke-width="4.5" stroke-linecap="round"/>
  <circle cx="32" cy="8" r="4" fill="currentColor"/>
  <circle cx="24" cy="34" r="4" fill="currentColor"/>
  <circle cx="40" cy="34" r="4" fill="currentColor"/>
  <path d="M26 44 C28 47 36 47 38 44" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" fill="none"/>
  <line x1="6" y1="33" x2="12" y2="33" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
  <line x1="52" y1="33" x2="58" y2="33" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
</svg>''',

'icon-bell.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <path d="M32 10 C23.2 10 16 17.2 16 26 L16 38 L10 46 L54 46 L48 38 L48 26 C48 17.2 40.8 10 32 10 Z" fill="#FFC107"/>
  <path d="M27 49 C27 51.8 29.2 54 32 54 C34.8 54 37 51.8 37 49 Z" fill="#FF9800"/>
  <circle cx="46" cy="14" r="7" fill="#FF3B30"/>
</svg>''',

'icon-star-badge.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <radialGradient id="starGlow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#FFF176"/>
      <stop offset="60%" stop-color="#FFB300"/>
      <stop offset="100%" stop-color="#FF8F00"/>
    </radialGradient>
  </defs>
  <polygon points="32,6 39.5,21.5 56.5,23.5 44,35 47.5,52 32,43.5 16.5,52 20,35 7.5,23.5 24.5,21.5" fill="url(#starGlow)"/>
  <ellipse cx="32" cy="20" rx="8" ry="4" fill="#FFF9C4" opacity="0.6"/>
</svg>''',

'icon-streak-flame.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="flameOuter" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FF7043"/>
      <stop offset="50%" stop-color="#FF5722"/>
      <stop offset="100%" stop-color="#E64A19"/>
    </linearGradient>
    <linearGradient id="flameInner" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFEE58"/>
      <stop offset="100%" stop-color="#FFA726"/>
    </linearGradient>
  </defs>
  <path d="M32 4 C32 4 48 18 48 36 C48 48 39 58 32 60 C25 58 16 48 16 36 C16 26 22 16 32 4 Z" fill="url(#flameOuter)"/>
  <path d="M32 24 C32 24 40 32 40 42 C40 48 36 53 32 54 C28 53 24 48 24 42 C24 35 28 30 32 24 Z" fill="url(#flameInner)"/>
</svg>''',

'icon-crown-badge.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="crownGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFD54F"/>
      <stop offset="100%" stop-color="#FF8F00"/>
    </linearGradient>
  </defs>
  <path d="M8 48 L14 18 L25 32 L32 14 L39 32 L50 18 L56 48 Z" fill="url(#crownGrad)"/>
  <rect x="8" y="46" width="48" height="8" rx="3" fill="#FFA000"/>
  <circle cx="14" cy="18" r="3.5" fill="#FFF9C4"/>
  <circle cx="32" cy="14" r="4" fill="#FFF9C4"/>
  <circle cx="50" cy="18" r="3.5" fill="#FFF9C4"/>
</svg>''',

'icon-logo.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 70 70" width="70" height="70">
  <defs>
    <linearGradient id="pageL" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF2A6D"/>
      <stop offset="50%" stop-color="#FF5E36"/>
      <stop offset="100%" stop-color="#FFAA00"/>
    </linearGradient>
    <linearGradient id="pageR" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="50%" stop-color="#00B0FF"/>
      <stop offset="100%" stop-color="#7C4DFF"/>
    </linearGradient>
  </defs>
  <path d="M35 56 C26 48 10 50 6 54 L6 20 C10 16 26 14 35 22 C44 14 60 16 64 20 L64 54 C60 50 44 48 35 56 Z" fill="#3F51B5" opacity="0.2"/>
  <path d="M35 52 C26 45 12 47 8 50 L8 22 C12 18 26 16 35 24 Z" fill="url(#pageL)"/>
  <path d="M35 52 C44 45 58 47 62 50 L62 22 C58 18 44 16 35 24 Z" fill="url(#pageR)"/>
  <circle cx="35" cy="12" r="3" fill="#FFD700"/>
  <circle cx="48" cy="14" r="2" fill="#FFEB3B"/>
  <circle cx="22" cy="14" r="2" fill="#FF69B4"/>
</svg>''',

'icon-check.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <circle cx="32" cy="32" r="28" fill="#4CAF50"/>
  <path d="M20 32 L28 40 L44 24" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',

'icon-lock.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect x="16" y="28" width="32" height="26" rx="6" fill="#90A4AE"/>
  <path d="M22 28 L22 18 C22 12.5 26.5 8 32 8 C37.5 8 42 12.5 42 18 L42 28" fill="none" stroke="#90A4AE" stroke-width="5" stroke-linecap="round"/>
  <circle cx="32" cy="39" r="3" fill="#FFFFFF"/>
  <line x1="32" y1="41" x2="32" y2="47" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
</svg>'''
}

for name, svg in icons.items():
    with open(f'assets/icons/{name}', 'w', encoding='utf-8') as f:
        f.write(svg.strip())

print(f"Successfully generated {len(icons)} SVG icons.")
