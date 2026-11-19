# Learning Universe LMS - Primary World

A responsive, gamified Learning Management System (LMS) website built for primary school learners using **HTML5**, **CSS3**, and **Vanilla JavaScript**.

Based faithfully on the approved design theme and character art style.

---

## 📁 Project Directory Structure

```
LMS Primary/
├── index.html                           # Main responsive LMS website
├── css/
│   └── style.css                        # Glassmorphism, animations & responsive grid
├── js/
│   └── app.js                           # Web Audio sound FX, confetti, interactive modals
├── assets/
│   ├── characters/
│   │   ├── fox_waving.png               # Fox mascot waving (1024x1024 transparent PNG)
│   │   ├── fox_reading.png              # Fox mascot reading book (1024x1024 transparent PNG)
│   │   ├── teacher_512.png              # Live class teacher avatar
│   │   └── aarav_avatar_clean.png       # Student profile avatar
│   ├── illustrations/
│   │   ├── treehouse.png                # "My Learning World" treehouse (1024x1024 transparent PNG)
│   │   ├── background-scenery.png       # Nature landscape scenery (1920x1080)
│   │   ├── leaderboard_podium_clean.png # 3D Class leaderboard podium
│   │   ├── island_theory_clean.png      # Journey step 1: Theory
│   │   ├── island_video_clean.png       # Journey step 2: Video
│   │   ├── island_game_clean.png        # Journey step 3: Game Practice
│   │   ├── island_challenge_clean.png   # Journey step 4: Class Challenge
│   │   └── island_treasure_clean.png    # Journey step 5: Treasure Chest
│   ├── subjects/
│   │   ├── maths.png                    # Maths (512x512 transparent PNG)
│   │   ├── english.png                  # English (512x512 transparent PNG)
│   │   ├── evs.png                      # EVS (512x512 transparent PNG)
│   │   ├── science.png                  # Science (512x512 transparent PNG)
│   │   ├── tamil.png                    # Tamil (512x512 transparent PNG)
│   │   └── art.png                      # Art & Craft (512x512 transparent PNG)
│   └── icons/
│       ├── icon-logo.svg                # Colorful open book logo
│       ├── icon-home.svg                # Sidebar Home
│       ├── icon-my-learning.svg         # Sidebar My Learning
│       ├── icon-quizzes.svg             # Sidebar Quizzes
│       ├── icon-assignments.svg         # Sidebar Assignments
│       ├── icon-live-classes.svg        # Sidebar Live Classes
│       ├── icon-progress.svg            # Sidebar Progress
│       ├── icon-achievements.svg        # Sidebar Achievements
│       ├── icon-ai-buddy.svg            # Sidebar AI Study Buddy
│       ├── icon-star-badge.svg          # 3D Glossy Star
│       ├── icon-streak-flame.svg        # 3D Glossy Flame
│       ├── icon-crown-badge.svg         # 3D Gold Crown
│       ├── icon-medal-badge.svg         # Quiz Champ Medal
│       ├── icon-bell.svg                # Notification Bell
│       ├── icon-check.svg               # Green checkmark
│       └── icon-lock.svg                # Silver lock
└── scripts/                             # Utility build scripts
```

---

## 🚀 How to Run the Website

You can open the project in any modern web browser in either of two ways:

### Option 1: Direct File Open
Double click `index.html` or open `c:\Users\Admin\Downloads\LMS Primary\index.html` directly in your browser (Chrome, Edge, Firefox, Safari).

### Option 2: Local HTTP Server (Recommended)
Open a terminal in the project directory and run:
```powershell
python -m http.server 8080
```
Then visit [http://localhost:8080](http://localhost:8080) in your browser.

---

## 🎮 Interactive Features
- **Synthesized Audio System**: Built with the native Web Audio API (no external sound files required). Produces chimes, pops, and celebration chords on clicks.
- **Confetti Engine**: Particle confetti blast on clicking the Treasure Chest, Fox mascots, or Treehouse.
- **Fox Mascot Dialogue**: Click either the waving fox or reading fox to receive encouraging tips and quotes.
- **Interactive Journey Path**: Click on stepping stone islands to preview lessons or unlock quests.
- **Class Live Session**: Click "Join Class" to simulate connecting to the live virtual classroom.
