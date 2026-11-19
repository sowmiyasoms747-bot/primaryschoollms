/* ==========================================================================
   Learning Universe LMS - Interactive Vanilla JavaScript
   Web Audio Synthesizer, Confetti FX, Modals, Progress Tracking
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initAudio();
  initNav();
  initJourneyPath();
  initSubjects();
  initFoxInteractions();
  initModals();
  initLiveClass();
});

// ==========================================================================
// 1. WEB AUDIO API SYNTHESIZER
// ==========================================================================
let audioCtx = null;

function initAudio() {
  const startAudio = () => {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
  };
  window.addEventListener('click', startAudio, { once: true });
}

function playSound(type) {
  if (!audioCtx) {
    try {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    } catch (e) {
      return;
    }
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }

  const now = audioCtx.currentTime;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  osc.connect(gain);
  gain.connect(audioCtx.destination);

  if (type === 'chime') {
    osc.type = 'sine';
    osc.frequency.setValueAtTime(587.33, now); // D5
    osc.frequency.exponentialRampToValueAtTime(880, now + 0.15); // A5
    osc.frequency.exponentialRampToValueAtTime(1174.66, now + 0.3); // D6
    gain.gain.setValueAtTime(0.2, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
    osc.start(now);
    osc.stop(now + 0.5);
  } else if (type === 'celebration') {
    const freqs = [523.25, 659.25, 783.99, 1046.50]; // C Major
    freqs.forEach((freq, idx) => {
      const o = audioCtx.createOscillator();
      const g = audioCtx.createGain();
      o.connect(g);
      g.connect(audioCtx.destination);
      o.type = 'triangle';
      o.frequency.setValueAtTime(freq, now + idx * 0.08);
      g.gain.setValueAtTime(0.18, now + idx * 0.08);
      g.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.6);
      o.start(now + idx * 0.08);
      o.stop(now + idx * 0.08 + 0.6);
    });
  } else if (type === 'pop') {
    osc.type = 'sine';
    osc.frequency.setValueAtTime(320, now);
    osc.frequency.exponentialRampToValueAtTime(640, now + 0.08);
    gain.gain.setValueAtTime(0.25, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
    osc.start(now);
    osc.stop(now + 0.12);
  } else if (type === 'click') {
    osc.type = 'sine';
    osc.frequency.setValueAtTime(440, now);
    gain.gain.setValueAtTime(0.1, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.06);
    osc.start(now);
    osc.stop(now + 0.06);
  }
}

// ==========================================================================
// 2. CONFETTI PARTICLE SYSTEM
// ==========================================================================
function triggerConfetti(originX, originY) {
  const colors = ['#f43f5e', '#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899', '#facc15'];
  const count = 40;

  for (let i = 0; i < count; i++) {
    const confetti = document.createElement('div');
    confetti.style.position = 'fixed';
    confetti.style.pointerEvents = 'none';
    confetti.style.zIndex = '9999';
    confetti.style.left = (originX || window.innerWidth / 2) + 'px';
    confetti.style.top = (originY || window.innerHeight / 2) + 'px';
    confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];

    const angle = Math.random() * Math.PI * 2;
    const velocity = 80 + Math.random() * 200;
    const vx = Math.cos(angle) * velocity;
    const vy = Math.sin(angle) * velocity - 90;

    const size = 6 + Math.random() * 8;
    confetti.style.width = size + 'px';
    confetti.style.height = (size * (Math.random() > 0.5 ? 1 : 2)) + 'px';
    confetti.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';

    document.body.appendChild(confetti);

    let posX = originX || window.innerWidth / 2;
    let posY = originY || window.innerHeight / 2;
    let currentVx = vx;
    let currentVy = vy;
    let opacity = 1;

    const startTime = performance.now();
    function animate(time) {
      const elapsed = (time - startTime) / 1000;
      currentVy += 500 * 0.016;
      posX += currentVx * 0.016;
      posY += currentVy * 0.016;
      opacity = Math.max(0, 1 - elapsed / 2);

      confetti.style.transform = `translate3d(${posX - (originX || window.innerWidth / 2)}px, ${posY - (originY || window.innerHeight / 2)}px, 0) rotate(${elapsed * 400}deg)`;
      confetti.style.opacity = opacity;

      if (opacity > 0) {
        requestAnimationFrame(animate);
      } else {
        confetti.remove();
      }
    }
    requestAnimationFrame(animate);
  }
}

// ==========================================================================
// 3. NAVIGATION INTERACTIONS
// ==========================================================================
function initNav() {
  const navItems = document.querySelectorAll('.nav-item');
  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      navItems.forEach(i => i.classList.remove('active'));
      item.classList.add('active');
      playSound('pop');
    });
  });
}

// ==========================================================================
// 4. JOURNEY STEPPING PATH
// ==========================================================================
function initJourneyPath() {
  const steps = document.querySelectorAll('.stepping-island');
  steps.forEach(step => {
    step.addEventListener('click', () => {
      const stepType = step.getAttribute('data-step');
      const rect = step.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;

      if (stepType === 'theory') {
        playSound('chime');
        showModal('📚 Lesson Theory: Addition Facts', 'You have mastered basic addition! 3-digit addition rules are unlocked. Review questions anytime!');
      } else if (stepType === 'video') {
        playSound('chime');
        showModal('▶️ Video Lesson Completed', 'You watched "Maths Adventure: Adding with Carrots & Apples"! 20 Stars earned.');
      } else if (stepType === 'game') {
        playSound('pop');
        showModal('🎮 Practice Game Locked', 'Complete the video lesson review to unlock Math Blaster 3000!');
      } else if (stepType === 'challenge') {
        playSound('pop');
        showModal('🏆 Class Challenge Locked', 'Upcoming weekend tournament against Class 3-B!');
      } else if (stepType === 'treasure') {
        playSound('celebration');
        triggerConfetti(centerX, centerY);
        showModal('✨ Magical Treasure Reward!', '🎉 You unlocked the Mystery Chest! Inside: 50 Bonus Gold Stars & New Wizard Hat for your Fox Avatar! 🦊⭐');
      }
    });
  });
}

// ==========================================================================
// 5. SUBJECT CARDS
// ==========================================================================
function initSubjects() {
  const subjectCards = document.querySelectorAll('.subject-card-box');
  subjectCards.forEach(card => {
    card.addEventListener('click', () => {
      const title = card.querySelector('.subject-card-title').innerText;
      playSound('pop');
      showModal(`📖 ${title} Subject`, `Welcome to ${title}! You have completed 65% of the syllabus. Ready for today's exercises?`);
    });
  });
}

// ==========================================================================
// 6. FOX MASCOT INTERACTIONS
// ==========================================================================
const foxQuotes = [
  "Hi Aarav! Ready for our maths adventure today? 🌟",
  "You're on a 5-day streak! Don't let the fire go out! 🔥",
  "Reading books is like discovering secret worlds! 📚✨",
  "320 Stars! We're almost ready to unlock the Golden Trophy! 🏆",
  "Maths addition class is at 4:00 PM today! See you there! ⏰"
];

function initFoxInteractions() {
  const wavingFox = document.querySelector('.waving-fox-graphic');
  const readingFox = document.querySelector('.reading-fox-img');
  const treehouse = document.querySelector('.treehouse-anchor');

  if (wavingFox) {
    wavingFox.addEventListener('click', () => {
      const rect = wavingFox.getBoundingClientRect();
      playSound('chime');
      triggerConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2);
      const quote = foxQuotes[Math.floor(Math.random() * foxQuotes.length)];
      showModal('🦊 Friendly Fox Mascot Says:', quote);
    });
  }

  if (readingFox) {
    readingFox.addEventListener('click', () => {
      playSound('chime');
      showModal('🦊 Reading Fox', 'Shh! I am reading "The Secret of the Treehouse"! Want to join our book club? 📖✨');
    });
  }

  if (treehouse) {
    treehouse.addEventListener('click', () => {
      const rect = treehouse.getBoundingClientRect();
      playSound('celebration');
      triggerConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2);
      showModal('🏡 My Learning World Treehouse', 'Welcome to the clubhouse! Here you can trade your badges, visit friend treehouses, and customize your study room!');
    });
  }
}

// ==========================================================================
// 7. MODAL DIALOG SYSTEM
// ==========================================================================
function initModals() {
  const overlay = document.getElementById('lms-modal');
  const closeBtn = document.querySelector('.modal-close-cross');

  if (closeBtn && overlay) {
    closeBtn.addEventListener('click', () => {
      overlay.classList.remove('active');
      playSound('click');
    });
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        overlay.classList.remove('active');
      }
    });
  }

  const notifBtn = document.querySelector('.bell-btn');
  if (notifBtn) {
    notifBtn.addEventListener('click', () => {
      playSound('pop');
      showModal('🔔 Notifications', '1. Maths Worksheet due tomorrow at 5 PM.\n2. EVS project submission open.\n3. Aarav moved up to 3rd place on leaderboard!');
    });
  }

  const badges = document.querySelectorAll('.badge-capsule-card');
  badges.forEach(badge => {
    badge.addEventListener('click', () => {
      const name = badge.querySelector('.badge-caption').innerText;
      playSound('chime');
      showModal(`🏆 Badge: ${name}`, `Congratulations! You unlocked the '${name}' badge for active classroom participation and quiz excellence!`);
    });
  });
}

function showModal(title, message) {
  const overlay = document.getElementById('lms-modal');
  const modalTitle = document.getElementById('modal-header-title');
  const modalMsg = document.getElementById('modal-body-desc');

  if (overlay && modalTitle && modalMsg) {
    modalTitle.innerText = title;
    modalMsg.innerText = message;
    overlay.classList.add('active');
  }
}

// ==========================================================================
// 8. LIVE CLASS INTERACTION
// ==========================================================================
function initLiveClass() {
  const joinBtn = document.querySelector('.join-class-btn-pill');
  if (joinBtn) {
    joinBtn.addEventListener('click', () => {
      playSound('celebration');
      showModal('🎥 Joining Live Class', 'Connecting to Maths – Addition with Ms. Priya... Please ensure your camera and microphone are ready! 👩‍🏫📐');
    });
  }
}
