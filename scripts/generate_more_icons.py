import os

additional_icons = {
'icon-chevron-right.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path d="M9 18 L15 12 L9 6" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',

'icon-chevron-down.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path d="M6 9 L12 15 L18 9" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',

'icon-calendar.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <rect x="3" y="4" width="18" height="18" rx="4" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="3" y1="9" x2="21" y2="9" stroke="currentColor" stroke-width="2"/>
  <line x1="8" y1="2" x2="8" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <line x1="16" y1="2" x2="16" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <circle cx="8" cy="14" r="1.5" fill="currentColor"/>
  <circle cx="12" cy="14" r="1.5" fill="currentColor"/>
  <circle cx="16" cy="14" r="1.5" fill="currentColor"/>
</svg>''',

'icon-medal-badge.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <circle cx="32" cy="28" r="20" fill="#FFC107" stroke="#FFA000" stroke-width="3"/>
  <circle cx="32" cy="28" r="14" fill="#FFE082"/>
  <polygon points="32,18 35,25 42,26 37,31 38,38 32,34 26,38 27,31 22,26 29,25" fill="#FF8F00"/>
  <path d="M22 42 L16 58 L26 52 L32 58 L28 44" fill="#E91E63"/>
  <path d="M42 42 L48 58 L38 52 L32 58 L36 44" fill="#C2185B"/>
</svg>''',

'icon-scroll-pin.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <circle cx="12" cy="12" r="10" fill="#FF5252"/>
  <circle cx="12" cy="12" r="6" fill="#FFFFFF"/>
  <circle cx="12" cy="12" r="3" fill="#FF5252"/>
</svg>'''
}

for name, svg in additional_icons.items():
    with open(f'assets/icons/{name}', 'w', encoding='utf-8') as f:
        f.write(svg.strip())

print('Additional icons generated.')
