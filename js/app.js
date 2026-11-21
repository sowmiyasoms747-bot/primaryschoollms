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
  initFlowFeatures();
  initChapterJourneyFlow();
  initQuizFlow();
  initAssignmentsFlow();
  initLiveClassesFlow();
  initProgressFlow();
  initAchievementsFlow();
  initAiBuddyFlow();
  switchView('home');
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
// 3. NAVIGATION & VIEW ROUTING CONTROLLER (12-SCREEN MASTER FLOW)
// ==========================================================================
function switchView(targetViewId) {
  const viewport = document.querySelector('.lms-screen-container') || document.querySelector('.dashboard-viewport');
  const allViews = document.querySelectorAll('.app-view');
  const navItems = document.querySelectorAll('.nav-item');

  let normalizedId = targetViewId;
  if (!normalizedId.startsWith('view-')) {
    normalizedId = 'view-' + normalizedId;
  }

  const targetEl = document.getElementById(normalizedId);
  if (!targetEl) return;

  // Toggle active view
  allViews.forEach(v => v.classList.remove('active'));
  targetEl.classList.add('active');

  // Handle right sidebar visibility & 2-column grid expansion (Right panel ONLY on Home Dashboard)
  const viewports = document.querySelectorAll('.lms-screen-container, .dashboard-viewport');
  viewports.forEach(vp => {
    if (normalizedId === 'view-home') {
      vp.classList.remove('subview-active');
    } else {
      vp.classList.add('subview-active');
    }
  });

  // Update Left Sidebar active nav item (adds green pill .active to the selected nav item)
  navItems.forEach(item => {
    const link = item.querySelector('a');
    if (!link) return;
    const href = link.getAttribute('href') || '';

    const isHome = (href === '#home' && normalizedId === 'view-home');
    const isLearning = (href === '#learning' && [
      'view-learning-subjects',
      'view-chapter-list',
      'view-chapter-journey',
      'view-theory-lesson',
      'view-video-lesson',
      'view-game-practice',
      'view-class-challenge'
    ].includes(normalizedId));
    const isQuizzes = (href === '#quizzes' && normalizedId === 'view-quiz');
    const isAssignments = (href === '#assignments' && normalizedId === 'view-assignments');
    const isLive = (href === '#live' && normalizedId === 'view-live-classes');
    const isProgress = (href === '#progress' && normalizedId === 'view-progress');
    const isAchievements = (href === '#achievements' && normalizedId === 'view-achievements');
    const isAiBuddy = (href === '#ai-buddy' && normalizedId === 'view-ai-buddy');

    if (isHome || isLearning || isQuizzes || isAssignments || isLive || isProgress || isAchievements || isAiBuddy) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  });

  const panel = document.querySelector('.main-dashboard-panel');
  if (panel) panel.scrollTop = 0;
}

function initNav() {
  // Delegated click handler on sidebar nav for 100% reliable clicks
  const sidebarNav = document.querySelector('.sidebar-nav');
  if (sidebarNav) {
    sidebarNav.addEventListener('click', (e) => {
      const item = e.target.closest('.nav-item');
      if (!item) return;
      const link = item.querySelector('a');
      if (!link) return;
      e.preventDefault();
      const href = link.getAttribute('href');
      playSound('pop');

      if (href === '#home') switchView('home');
      else if (href === '#learning') switchView('learning-subjects');
      else if (href === '#quizzes') switchView('quiz');
      else if (href === '#assignments') switchView('assignments');
      else if (href === '#live') switchView('live-classes');
      else if (href === '#progress') switchView('progress');
      else if (href === '#achievements') switchView('achievements');
      else if (href === '#ai-buddy') switchView('ai-buddy');
    });
  }

  // Direct click handler fallback on each nav link
  const navItems = document.querySelectorAll('.nav-item');
  navItems.forEach(item => {
    const link = item.querySelector('a');
    if (!link) return;
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const href = link.getAttribute('href');
      playSound('pop');

      if (href === '#home') switchView('home');
      else if (href === '#learning') switchView('learning-subjects');
      else if (href === '#quizzes') switchView('quiz');
      else if (href === '#assignments') switchView('assignments');
      else if (href === '#live') switchView('live-classes');
      else if (href === '#progress') switchView('progress');
      else if (href === '#achievements') switchView('achievements');
      else if (href === '#ai-buddy') switchView('ai-buddy');
    });
  });

  // Support elements with data-route attributes
  document.addEventListener('click', (e) => {
    const routeTrigger = e.target.closest('[data-route]');
    if (routeTrigger) {
      e.preventDefault();
      const route = routeTrigger.getAttribute('data-route');
      playSound('pop');
      if (route === 'chapter-journey') {
        if (currentJourneyStage % 2 === 0) {
          // If returning from lesson stage (2, 4, 6, 8), go to preceding map stage (1, 3, 5, 7)
          setJourneyStage(Math.max(1, currentJourneyStage - 1));
        } else {
          setJourneyStage(currentJourneyStage);
        }
      } else {
        switchView(route);
      }
    }
  });

  // Home Dashboard subject tiles navigate to Chapter List (Screen 3)
  const homeSubjectCards = document.querySelectorAll('.subject-card-box');
  homeSubjectCards.forEach(card => {
    card.addEventListener('click', () => {
      playSound('chime');
      switchView('chapter-list');
    });
  });

  // My Learning screen subject cards navigate to Chapter List (Screen 3)
  const learningSubjectCards = document.querySelectorAll('.subject-card-clay');
  learningSubjectCards.forEach(card => {
    card.addEventListener('click', () => {
      playSound('chime');
      switchView('chapter-list');
    });
  });

  // Hanging Wooden Signboard Ladder interactions
  const woodenPlanks = document.querySelectorAll('.wooden-plank-row');
  woodenPlanks.forEach(plank => {
    plank.addEventListener('click', (e) => {
      if (e.target.closest('.plank-btn-continue')) return;
      const ch = plank.getAttribute('data-chapter');
      if (ch === '1') {
        playSound('chime');
        showModal('✓ Chapter 1 Completed', 'Numbers and Place Value is 100% completed! 50 Stars earned. Review lessons anytime!');
      } else if (ch === '2') {
        playSound('pop');
        setJourneyStage(currentJourneyStage);
      } else {
        playSound('pop');
        showModal('🔒 Chapter Locked', `Chapter ${ch} is locked! Complete Chapter 2: Addition first to unlock this chapter.`);
      }
    });
  });
}

// ==========================================================================
// 9. MULTI-SCREEN INTERACTIVE FLOW FEATURES
// ==========================================================================
function initFlowFeatures() {
  // 1. Quizzes 9-Screen Master Flow
  initQuizFlow();

  // 2. Achievements Tab Switcher (Screen 10 & 11)
  const achTabs = document.querySelectorAll('.ach-tab-btn');
  const tabContentMap = document.getElementById('tabContentMap');
  const tabContentBadges = document.getElementById('tabContentBadges');
  const achMainTitle = document.getElementById('achievementsMainTitle');

  achTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      achTabs.forEach(t => t.classList.remove('active-ach-tab'));
      tab.classList.add('active-ach-tab');
      playSound('pop');

      const viewMode = tab.getAttribute('data-ach-view');
      if (viewMode === 'map') {
        if (tabContentMap) tabContentMap.style.display = 'block';
        if (tabContentBadges) tabContentBadges.style.display = 'none';
        if (achMainTitle) achMainTitle.innerText = 'Achievements';
      } else if (viewMode === 'badges') {
        if (tabContentMap) tabContentMap.style.display = 'none';
        if (tabContentBadges) tabContentBadges.style.display = 'block';
        if (achMainTitle) achMainTitle.innerText = 'My Badges';
      } else if (viewMode === 'rewards') {
        playSound('celebration');
        showModal('🎁 Milestone Rewards', 'Aarav, you are 3 lessons away from unlocking the Diamond Star Trophy! 💎🏆');
      }
    });
  });

  // 3. Assignments Tab Switcher (Screen 7)
  const asgTabs = document.querySelectorAll('.asg-tab-btn');
  asgTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      asgTabs.forEach(t => t.classList.remove('active-tab'));
      tab.classList.add('active-tab');
      playSound('pop');
    });
  });

  const asgStartBtns = document.querySelectorAll('.btn-asg-start');
  asgStartBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const asgName = btn.getAttribute('data-assignment') || 'Assignment';
      playSound('chime');
      showModal(`📝 Starting: ${asgName}`, 'Your worksheet is loading... Remember to show your work step-by-step for full star bonus! ⭐');
    });
  });

  // 4. Live Classes Join Button (Screen 8)
  const liveJoinBtn = document.getElementById('btnJoinLiveClass');
  if (liveJoinBtn) {
    liveJoinBtn.addEventListener('click', () => {
      playSound('celebration');
      const rect = liveJoinBtn.getBoundingClientRect();
      triggerConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2);
      showModal('🔴 Connecting to Live Stream', 'Welcome to Maths - Addition with Ms. Nandhini! Your camera and microphone are connected. 👩‍🏫📐');
    });
  }

  const liveTabs = document.querySelectorAll('.live-tab-btn');
  liveTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      liveTabs.forEach(t => t.classList.remove('active-live-tab'));
      tab.classList.add('active-live-tab');
      playSound('pop');
    });
  });

  // 5. AI Study Buddy Chat (Screen 12)
  const chatForm = document.getElementById('chatInputForm');
  const chatInput = document.getElementById('chatInputField');
  const chatScroll = document.getElementById('aiChatMessages');
  const quickPills = document.querySelectorAll('.chat-quick-pill');

  function appendChat(role, text, isMath) {
    if (!chatScroll) return;
    const msgDiv = document.createElement('div');
    msgDiv.className = `chat-msg ${role}-msg`;

    if (role === 'user') {
      msgDiv.innerHTML = `
        <div class="chat-bubble user-bubble"><p>${escapeHtml(text)}</p></div>
        <img src="assets/characters/aarav_avatar.png" alt="Aarav" class="chat-avatar user-avatar">
      `;
    } else {
      let mathContent = isMath ? `<p class="chat-math-example">${isMath}</p>` : '';
      msgDiv.innerHTML = `
        <img src="assets/icons/nav_ai_buddy_3d.png" alt="Bot Avatar" class="chat-avatar bot-avatar">
        <div class="chat-bubble ai-bubble">
          <p>${escapeHtml(text)}</p>
          ${mathContent}
        </div>
      `;
    }
    chatScroll.appendChild(msgDiv);
    chatScroll.scrollTop = chatScroll.scrollHeight;
  }

  function escapeHtml(str) {
    return str.replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[m]);
  }

  if (chatForm && chatInput) {
    chatForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const val = chatInput.value.trim();
      if (!val) return;
      playSound('pop');
      appendChat('user', val);
      chatInput.value = '';

      setTimeout(() => {
        playSound('chime');
        appendChat('ai', `Great question about "${val}"! Remember, practice makes you a Maths Star! 🌟`, '3 + 4 = 7');
      }, 700);
    });
  }

  quickPills.forEach(pill => {
    pill.addEventListener('click', () => {
      const prompt = pill.getAttribute('data-prompt');
      playSound('pop');
      appendChat('user', prompt);

      setTimeout(() => {
        playSound('chime');
        if (prompt === 'Explain Again') {
          appendChat('ai', 'Sure! Addition is simply counting items from two sets into one big group. 🍎', '1 + 2 = 3');
        } else if (prompt === 'Give a Hint') {
          appendChat('ai', '💡 Hint: Count forward from the largest number! For 5 + 3, start at 5 and count 3 more: 6, 7, 8!', '');
        } else {
          appendChat('ai', 'Here is a quick practice question for you: What is 4 + 4 ? Can you solve it?', '4 + 4 = ?');
        }
      }, 700);
    });
  });
}


// ==========================================================================
// 4. JOURNEY STEPPING PATH
// ==========================================================================
function initJourneyPath() {
  const steps = document.querySelectorAll('#view-home .stepping-island');
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
      showModal('🦊 Friendly Fox Mascot', 'Ready to write, learn, and explore exciting new adventures today! ✏️🎒🌟');
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

// ==========================================================================
// 10. DYNAMIC 9-STAGE MY LEARNING CHAPTER JOURNEY FLOW CONTROLLER
// ==========================================================================
let currentJourneyStage = 1;

function initChapterJourneyFlow() {
  // Initial render at Stage 1 (Start)
  renderJourneyStage(1);

  // Fast-jump stage pills (1 to 9)
  const stagePills = document.querySelectorAll('.stage-nav-pill');
  stagePills.forEach(pill => {
    pill.addEventListener('click', () => {
      const stage = parseInt(pill.getAttribute('data-set-stage'), 10);
      playSound('pop');
      setJourneyStage(stage);
    });
  });

  // Reset button
  const resetBtn = document.getElementById('btnResetJourney');
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      playSound('pop');
      setJourneyStage(1);
      showModal('↺ Journey Reset', 'Chapter Addition has been reset to Step 1 (Start). Have fun learning!');
    });
  }

  // Interactive Chapter Islands (Theory, Video, Game, Challenge, Treasure)
  const journeyNodes = document.querySelectorAll('#journeySteppingStonesContainer .stepping-island, #journeySteppingStonesContainer .journey-node');
  journeyNodes.forEach(node => {
    node.addEventListener('click', () => {
      const station = node.getAttribute('data-station');
      const rect = node.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;

      if (station === 'theory') {
        playSound('chime');
        setJourneyStage(2); // Jump into Theory Lesson
      } else if (station === 'video') {
        if (currentJourneyStage < 3) {
          playSound('pop');
          showModal('🔒 Video Lesson Locked', 'Please complete the Theory lesson first to unlock this video lesson!');
        } else {
          playSound('chime');
          setJourneyStage(4); // Jump into Video Lesson
        }
      } else if (station === 'game') {
        if (currentJourneyStage < 5) {
          playSound('pop');
          showModal('🔒 Game Practice Locked', 'Watch and complete the Video lesson first to unlock Game Practice!');
        } else {
          playSound('chime');
          setJourneyStage(6); // Jump into Game Practice
        }
      } else if (station === 'challenge') {
        if (currentJourneyStage < 7) {
          playSound('pop');
          showModal('🔒 Class Challenge Locked', 'Complete the Game Practice first to unlock the Class Challenge!');
        } else {
          playSound('chime');
          setJourneyStage(8); // Jump into Class Challenge Quiz
        }
      } else if (station === 'treasure') {
        if (currentJourneyStage < 9) {
          playSound('pop');
          showModal('🔒 Magical Treasure Locked', 'Complete all chapter stages (Theory, Video, Game Practice & Challenge) to unlock the Treasure Chest!');
        } else {
          playSound('celebration');
          triggerConfetti(cx, cy);
          triggerConfetti(cx - 80, cy - 50);
          triggerConfetti(cx + 80, cy - 50);
          openTreasureChestReward();
        }
      }
    });
  });

  // Step 2 (Theory): "Complete & Continue >"
  const btnCompleteTheory = document.getElementById('btnCompleteTheory');
  if (btnCompleteTheory) {
    btnCompleteTheory.addEventListener('click', () => {
      playSound('celebration');
      const rect = btnCompleteTheory.getBoundingClientRect();
      triggerConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2);
      setJourneyStage(3);
    });
  }

  // Step 4 (Video): Center Play button toggle
  const btnVideoPlayToggle = document.getElementById('btnVideoPlayToggle');
  const videoPlayIcon = document.getElementById('videoPlayIcon');
  let isVideoPlaying = false;
  let videoProgressTimer = null;
  if (btnVideoPlayToggle) {
    btnVideoPlayToggle.addEventListener('click', () => {
      isVideoPlaying = !isVideoPlaying;
      playSound(isVideoPlaying ? 'pop' : 'click');
      if (videoPlayIcon) videoPlayIcon.innerText = isVideoPlaying ? '❚❚' : '▶';

      const progressFill = document.getElementById('videoProgressFill');
      const timeDisplay = document.getElementById('videoTimeDisplay');
      if (isVideoPlaying) {
        let p = 51;
        videoProgressTimer = setInterval(() => {
          if (p < 100) {
            p += 2;
            if (progressFill) progressFill.style.width = p + '%';
            const totalSecs = 300;
            const curSecs = Math.floor((p / 100) * totalSecs);
            const m = Math.floor(curSecs / 60);
            const s = curSecs % 60;
            if (timeDisplay) timeDisplay.innerText = `0${m}:${s.toString().padStart(2, '0')} / 05:00`;
          } else {
            clearInterval(videoProgressTimer);
          }
        }, 300);
      } else {
        if (videoProgressTimer) clearInterval(videoProgressTimer);
      }
    });
  }

  // Step 4 (Video): "Mark as Completed"
  const btnCompleteVideo = document.getElementById('btnCompleteVideo');
  if (btnCompleteVideo) {
    btnCompleteVideo.addEventListener('click', () => {
      playSound('celebration');
      const rect = btnCompleteVideo.getBoundingClientRect();
      triggerConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2);
      setJourneyStage(5);
    });
  }

  // Step 6 (Game Practice): Interactive Answer Cards 5, 6, 7
  const gameOptCards = document.querySelectorAll('.game-opt-card');
  const btnContinueGame = document.getElementById('btnContinueGame');
  const gameScoreEl = document.getElementById('gamePracticeScore');
  gameOptCards.forEach(card => {
    card.addEventListener('click', () => {
      const ans = card.getAttribute('data-ans');
      if (ans === '6') {
        playSound('celebration');
        const rect = card.getBoundingClientRect();
        triggerConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2);
        card.classList.add('opt-correct-glow');
        if (gameScoreEl) gameScoreEl.innerText = 'Score: 3 / 5';
        if (btnContinueGame) {
          btnContinueGame.style.display = 'inline-block';
        }
      } else {
        playSound('pop');
        card.classList.add('opt-shake');
        setTimeout(() => card.classList.remove('opt-shake'), 400);
      }
    });
  });

  if (btnContinueGame) {
    btnContinueGame.addEventListener('click', () => {
      playSound('chime');
      setJourneyStage(7);
    });
  }

  // Step 8 (Class Challenge): Interactive Options 8, 9, 10, 11
  const challengeOptBtns = document.querySelectorAll('.challenge-opt-btn');
  let challengeAnswerSelected = false;
  challengeOptBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const ans = btn.getAttribute('data-ans');
      if (ans === '10') {
        playSound('celebration');
        const rect = btn.getBoundingClientRect();
        triggerConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2);
        btn.classList.add('opt-correct-glow');
        challengeAnswerSelected = true;
      } else {
        playSound('pop');
        btn.classList.add('opt-shake');
        setTimeout(() => btn.classList.remove('opt-shake'), 400);
      }
    });
  });

  const btnFinishChallenge = document.getElementById('btnFinishChallenge');
  if (btnFinishChallenge) {
    btnFinishChallenge.addEventListener('click', () => {
      playSound('celebration');
      const rect = btnFinishChallenge.getBoundingClientRect();
      triggerConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2);
      setJourneyStage(9);
    });
  }

  // Step 9 (Chapter Completed): Claim Reward Button
  const btnClaimChest = document.getElementById('btnClaimChest');
  if (btnClaimChest) {
    btnClaimChest.addEventListener('click', () => {
      playSound('celebration');
      const rect = btnClaimChest.getBoundingClientRect();
      triggerConfetti(rect.left + rect.width / 2, rect.top + rect.height / 2);
      triggerConfetti(window.innerWidth / 2, window.innerHeight / 2);
      openTreasureChestReward();
    });
  }
}

function openTreasureChestReward() {
  playSound('celebration');
  // Update user score displays to 370 Points
  const userPointsEls = document.querySelectorAll('.user-points-val, #userScoreDisplay, .points-display');
  userPointsEls.forEach(el => {
    el.innerText = '370 Points';
  });
  showModal(
    '🎉 Addition Chapter Mastered! 🏆',
    'Congratulations Aarav! You have successfully completed Theory, Video, Game Practice, and Class Challenge! 🌟\n\n' +
    '🎁 Rewards Claimed:\n' +
    '• +50 Bonus Stars (Total: 370 Points)\n' +
    '• Chapter Badge: Addition Expert 👑\n' +
    '• Unlocked Chapter 3: Subtraction! 🚀'
  );
}

function setJourneyStage(stageNum) {
  currentJourneyStage = stageNum;

  // Highlight active stage pill
  document.querySelectorAll('.stage-nav-pill').forEach(pill => {
    const s = parseInt(pill.getAttribute('data-set-stage'), 10);
    if (s === stageNum) {
      pill.classList.add('active-stage');
    } else {
      pill.classList.remove('active-stage');
    }
  });

  if ([1, 3, 5, 7, 9].includes(stageNum)) {
    switchView('chapter-journey');
    renderJourneyStage(stageNum);
  } else if (stageNum === 2) {
    switchView('theory-lesson');
  } else if (stageNum === 4) {
    switchView('video-lesson');
  } else if (stageNum === 6) {
    switchView('game-practice');
  } else if (stageNum === 8) {
    switchView('class-challenge');
  }
}

function renderJourneyStage(stageNum) {
  const bannerSlot = document.getElementById('journeyBannerSlot');
  const rewardCard = document.getElementById('chapterRewardCard');
  const progressLabel = document.getElementById('journeyProgressLabel');

  const imgTheory = document.getElementById('imgIslandTheory');
  const haloTheory = document.getElementById('haloTheory');

  const imgVideo = document.getElementById('imgIslandVideo');
  const haloVideo = document.getElementById('haloVideo');

  const imgGame = document.getElementById('imgIslandGame');
  const haloGame = document.getElementById('haloGame');

  const imgChallenge = document.getElementById('imgIslandChallenge');
  const haloChallenge = document.getElementById('haloChallenge');

  const imgTreasure = document.getElementById('imgIslandTreasure');
  const haloTreasure = document.getElementById('haloTreasure');
  const sparkleTreasure = document.getElementById('treasureSparkleFx');

  if (!bannerSlot) return;

  // Reset pulsing halos and sparkle fx
  if (haloTheory) haloTheory.style.display = 'none';
  if (haloVideo) haloVideo.style.display = 'none';
  if (haloGame) haloGame.style.display = 'none';
  if (haloChallenge) haloChallenge.style.display = 'none';
  if (haloTreasure) haloTreasure.style.display = 'none';
  if (sparkleTreasure) sparkleTreasure.style.display = 'none';

  if (rewardCard) rewardCard.style.display = 'none';

  if (stageNum === 1) {
    // 1. Chapter Journey - Start
    bannerSlot.innerHTML = `
      <div class="journey-notice-capsule">
        <span class="notice-icon">ℹ️</span>
        <span class="notice-text">Start the chapter! Only Theory is available now.</span>
      </div>
    `;
    if (progressLabel) progressLabel.innerText = '0 of 4 Completed';

    if (imgTheory) imgTheory.src = 'assets/illustrations/island_theory_active.png';
    if (haloTheory) haloTheory.style.display = 'block';

    if (imgVideo) imgVideo.src = 'assets/illustrations/island_video_locked.png';
    if (imgGame) imgGame.src = 'assets/illustrations/island_game_locked.png';
    if (imgChallenge) imgChallenge.src = 'assets/illustrations/island_challenge_locked.png';
    if (imgTreasure) imgTreasure.src = 'assets/illustrations/island_treasure_locked.png';

  } else if (stageNum === 3) {
    // 3. Theory Completed - Video Unlocked
    bannerSlot.innerHTML = `
      <div class="journey-success-capsule">
        <span class="success-check-badge">✓</span>
        <span class="success-text">Theory Completed! Video Unlocked!</span>
      </div>
    `;
    if (progressLabel) progressLabel.innerText = '1 of 4 Completed';

    if (imgTheory) imgTheory.src = 'assets/illustrations/island_theory_done.png';
    if (imgVideo) imgVideo.src = 'assets/illustrations/island_video_active.png';
    if (haloVideo) haloVideo.style.display = 'block';

    if (imgGame) imgGame.src = 'assets/illustrations/island_game_locked.png';
    if (imgChallenge) imgChallenge.src = 'assets/illustrations/island_challenge_locked.png';
    if (imgTreasure) imgTreasure.src = 'assets/illustrations/island_treasure_locked.png';

  } else if (stageNum === 5) {
    // 5. Video Completed - Game Practice Unlocked
    bannerSlot.innerHTML = `
      <div class="journey-success-capsule">
        <span class="success-check-badge">✓</span>
        <span class="success-text">Video Completed! Game Practice Unlocked!</span>
      </div>
    `;
    if (progressLabel) progressLabel.innerText = '2 of 4 Completed';

    if (imgTheory) imgTheory.src = 'assets/illustrations/island_theory_done.png';
    if (imgVideo) imgVideo.src = 'assets/illustrations/island_video_done.png';
    if (imgGame) imgGame.src = 'assets/illustrations/island_game_active.png';
    if (haloGame) haloGame.style.display = 'block';

    if (imgChallenge) imgChallenge.src = 'assets/illustrations/island_challenge_locked.png';
    if (imgTreasure) imgTreasure.src = 'assets/illustrations/island_treasure_locked.png';

  } else if (stageNum === 7) {
    // 7. Game Practice Completed - Class Challenge Unlocked
    bannerSlot.innerHTML = `
      <div class="journey-success-capsule">
        <span class="success-check-badge">✓</span>
        <span class="success-text">Game Practice Completed! Class Challenge Unlocked!</span>
      </div>
    `;
    if (progressLabel) progressLabel.innerText = '3 of 4 Completed';

    if (imgTheory) imgTheory.src = 'assets/illustrations/island_theory_done.png';
    if (imgVideo) imgVideo.src = 'assets/illustrations/island_video_done.png';
    if (imgGame) imgGame.src = 'assets/illustrations/island_game_done.png';
    if (imgChallenge) imgChallenge.src = 'assets/illustrations/island_challenge_active.png';
    if (haloChallenge) haloChallenge.style.display = 'block';

    if (imgTreasure) imgTreasure.src = 'assets/illustrations/island_treasure_locked.png';

  } else if (stageNum === 9) {
    // 9. Chapter Completed - Treasure Unlocked
    bannerSlot.innerHTML = `
      <div class="chapter-completed-ribbon-wrap">
        <div class="celebration-ribbon-tail left-tail"></div>
        <div class="celebration-ribbon-body">
          <span class="ribbon-sparkle">✨</span>
          <span class="ribbon-text">Chapter Completed!</span>
          <span class="ribbon-sparkle">🎉</span>
        </div>
        <div class="celebration-ribbon-tail right-tail"></div>
      </div>
    `;
    if (progressLabel) progressLabel.innerText = '4 of 4 Completed';

    if (imgTheory) imgTheory.src = 'assets/illustrations/island_theory_done.png';
    if (imgVideo) imgVideo.src = 'assets/illustrations/island_video_done.png';
    if (imgGame) imgGame.src = 'assets/illustrations/island_game_done.png';
    if (imgChallenge) imgChallenge.src = 'assets/illustrations/island_challenge_done.png';
    if (imgTreasure) imgTreasure.src = 'assets/illustrations/island_treasure_done.png';

    if (haloTreasure) haloTreasure.style.display = 'block';
    if (sparkleTreasure) sparkleTreasure.style.display = 'block';

    if (rewardCard) rewardCard.style.display = 'flex';
  }
}

// ==========================================================================
// QUIZZES 9-SCREEN MASTER FLOW CONTROLLER
// ==========================================================================
let currentQuizScreen = 1;
let quizTimerInterval = null;
let quizTimeRemaining = 504; // 08:24

function initQuizFlow() {
  // Navigation pill strip clicks
  const pills = document.querySelectorAll('.quiz-nav-pill');
  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      const step = parseInt(pill.getAttribute('data-quiz-step'), 10);
      playSound('pop');
      setQuizScreen(step);
    });
  });

  // Reset button
  const btnReset = document.getElementById('btnResetQuizFlow');
  if (btnReset) {
    btnReset.addEventListener('click', () => {
      playSound('pop');
      setQuizScreen(1);
    });
  }

  // Delegated clicks for all elements with [data-quiz-nav]
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-quiz-nav]');
    if (trigger) {
      e.preventDefault();
      const targetScreen = parseInt(trigger.getAttribute('data-quiz-nav'), 10);
      playSound('pop');
      setQuizScreen(targetScreen);
    }
  });

  // Screen 5: Answer Card selection
  const ansCards = document.querySelectorAll('.quiz-answer-card');
  ansCards.forEach(card => {
    card.addEventListener('click', () => {
      playSound('pop');
      ansCards.forEach(c => {
        c.classList.remove('selected-answer');
        const badge = c.querySelector('.ans-check-badge');
        if (badge) badge.remove();
      });
      card.classList.add('selected-answer');
      const badge = document.createElement('span');
      badge.className = 'ans-check-badge';
      badge.innerText = '✓';
      card.appendChild(badge);
    });
  });

  // Screen 5: Submit & Proceed
  const btnProceed = document.getElementById('btnQuizProceed');
  if (btnProceed) {
    btnProceed.addEventListener('click', () => {
      const selected = document.querySelector('.quiz-answer-card.selected-answer');
      const val = selected ? selected.getAttribute('data-answer-val') : '7';
      if (val === '7') {
        playSound('celebration');
        setQuizScreen(6); // Correct Answer
      } else {
        playSound('pop');
        setQuizScreen(7); // Incorrect Answer
      }
    });
  }

  // Start Live Timer
  startQuizTimer();
}

function setQuizScreen(screenNum) {
  currentQuizScreen = screenNum;

  // Update nav pills
  document.querySelectorAll('.quiz-nav-pill').forEach(pill => {
    const s = parseInt(pill.getAttribute('data-quiz-step'), 10);
    if (s === screenNum) {
      pill.classList.add('active-quiz-stage');
    } else {
      pill.classList.remove('active-quiz-stage');
    }
  });

  // Toggle active screen panel
  document.querySelectorAll('.quiz-screen-panel').forEach(panel => {
    const s = parseInt(panel.getAttribute('data-quiz-screen'), 10);
    if (s === screenNum) {
      panel.classList.add('active-quiz-screen');
    } else {
      panel.classList.remove('active-quiz-screen');
    }
  });

  // Screen-specific triggers
  if (screenNum === 6) {
    // Correct feedback: celebration confetti!
    playSound('celebration');
    triggerConfetti(window.innerWidth / 2, window.innerHeight / 2 - 50);
  } else if (screenNum === 8) {
    // Quiz completed: big celebration!
    playSound('celebration');
    triggerConfetti(window.innerWidth / 2 - 100, window.innerHeight / 2);
    triggerConfetti(window.innerWidth / 2 + 100, window.innerHeight / 2);
  }

  // Scroll main panel to top smoothly
  const panel = document.querySelector('.main-dashboard-panel');
  if (panel) panel.scrollTop = 0;
}

function startQuizTimer() {
  if (quizTimerInterval) clearInterval(quizTimerInterval);
  quizTimeRemaining = 504; // 08:24
  const timerEl = document.getElementById('quizLiveTimer');

  quizTimerInterval = setInterval(() => {
    if (quizTimeRemaining > 0) {
      quizTimeRemaining--;
      const mins = Math.floor(quizTimeRemaining / 60);
      const secs = quizTimeRemaining % 60;
      if (timerEl) {
        timerEl.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
      }
    }
  }, 1000);
}

// ==========================================================================
// UNIFIED FLOW CONTROLLERS: ASSIGNMENTS, LIVE CLASSES, PROGRESS, ACHIEVEMENTS, AI BUDDY
// ==========================================================================

// 1. ASSIGNMENTS FLOW
let currentAsgScreen = 1;
function setAssignmentsScreen(screenNum) {
  currentAsgScreen = screenNum;
  document.querySelectorAll('[data-asg-step]').forEach(pill => {
    const s = parseInt(pill.getAttribute('data-asg-step'), 10);
    pill.classList.toggle('active-pill', s === screenNum);
  });
  document.querySelectorAll('[data-asg-screen]').forEach(panel => {
    const s = parseInt(panel.getAttribute('data-asg-screen'), 10);
    panel.classList.toggle('active-screen', s === screenNum);
  });
  if (screenNum === 8) {
    if (typeof playSound === 'function') playSound('celebration');
    if (typeof triggerConfetti === 'function') triggerConfetti(window.innerWidth / 2, window.innerHeight / 2 - 50);
  }
}

function initAssignmentsFlow() {
  document.querySelectorAll('[data-asg-step]').forEach(pill => {
    pill.addEventListener('click', () => {
      const step = parseInt(pill.getAttribute('data-asg-step'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setAssignmentsScreen(step);
    });
  });
  const btnReset = document.getElementById('btnResetAsgFlow');
  if (btnReset) {
    btnReset.addEventListener('click', () => {
      if (typeof playSound === 'function') playSound('pop');
      setAssignmentsScreen(1);
    });
  }
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-asg-nav]');
    if (trigger) {
      e.preventDefault();
      const targetScreen = parseInt(trigger.getAttribute('data-asg-nav'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setAssignmentsScreen(targetScreen);
    }
  });
}

// 2. LIVE CLASSES FLOW
let currentLiveScreen = 1;
function setLiveClassesScreen(screenNum) {
  currentLiveScreen = screenNum;
  document.querySelectorAll('[data-live-step]').forEach(pill => {
    const s = parseInt(pill.getAttribute('data-live-step'), 10);
    pill.classList.toggle('active-pill', s === screenNum);
  });
  document.querySelectorAll('[data-live-screen]').forEach(panel => {
    const s = parseInt(panel.getAttribute('data-live-screen'), 10);
    panel.classList.toggle('active-screen', s === screenNum);
  });
  if (screenNum === 7) {
    if (typeof playSound === 'function') playSound('celebration');
    if (typeof triggerConfetti === 'function') triggerConfetti(window.innerWidth / 2, window.innerHeight / 2 - 50);
  }
}

function initLiveClassesFlow() {
  document.querySelectorAll('[data-live-step]').forEach(pill => {
    pill.addEventListener('click', () => {
      const step = parseInt(pill.getAttribute('data-live-step'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setLiveClassesScreen(step);
    });
  });
  const btnReset = document.getElementById('btnResetLiveFlow');
  if (btnReset) {
    btnReset.addEventListener('click', () => {
      if (typeof playSound === 'function') playSound('pop');
      setLiveClassesScreen(1);
    });
  }
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-live-nav]');
    if (trigger) {
      e.preventDefault();
      const targetScreen = parseInt(trigger.getAttribute('data-live-nav'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setLiveClassesScreen(targetScreen);
    }
  });
}

// 3. PROGRESS FLOW
let currentProgScreen = 1;
function setProgressScreen(screenNum) {
  currentProgScreen = screenNum;
  document.querySelectorAll('[data-prog-step]').forEach(pill => {
    const s = parseInt(pill.getAttribute('data-prog-step'), 10);
    pill.classList.toggle('active-pill', s === screenNum);
  });
  document.querySelectorAll('[data-prog-screen]').forEach(panel => {
    const s = parseInt(panel.getAttribute('data-prog-screen'), 10);
    panel.classList.toggle('active-screen', s === screenNum);
  });
  if (screenNum === 9) {
    if (typeof playSound === 'function') playSound('celebration');
    if (typeof triggerConfetti === 'function') triggerConfetti(window.innerWidth / 2, window.innerHeight / 2 - 50);
  }
}

function initProgressFlow() {
  document.querySelectorAll('[data-prog-step]').forEach(pill => {
    pill.addEventListener('click', () => {
      const step = parseInt(pill.getAttribute('data-prog-step'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setProgressScreen(step);
    });
  });
  const btnReset = document.getElementById('btnResetProgFlow');
  if (btnReset) {
    btnReset.addEventListener('click', () => {
      if (typeof playSound === 'function') playSound('pop');
      setProgressScreen(1);
    });
  }
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-prog-nav]');
    if (trigger) {
      e.preventDefault();
      const targetScreen = parseInt(trigger.getAttribute('data-prog-nav'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setProgressScreen(targetScreen);
    }
  });
}

// 4. ACHIEVEMENTS FLOW
let currentAchScreen = 1;
function setAchievementsScreen(screenNum) {
  currentAchScreen = screenNum;
  document.querySelectorAll('[data-ach-step]').forEach(pill => {
    const s = parseInt(pill.getAttribute('data-ach-step'), 10);
    pill.classList.toggle('active-pill', s === screenNum);
  });
  document.querySelectorAll('[data-ach-screen]').forEach(panel => {
    const s = parseInt(panel.getAttribute('data-ach-screen'), 10);
    panel.classList.toggle('active-screen', s === screenNum);
  });
  if (screenNum === 9) {
    if (typeof playSound === 'function') playSound('celebration');
    if (typeof triggerConfetti === 'function') triggerConfetti(window.innerWidth / 2, window.innerHeight / 2 - 50);
  }
}

function initAchievementsFlow() {
  document.querySelectorAll('[data-ach-step]').forEach(pill => {
    pill.addEventListener('click', () => {
      const step = parseInt(pill.getAttribute('data-ach-step'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setAchievementsScreen(step);
    });
  });
  const btnReset = document.getElementById('btnResetAchFlow');
  if (btnReset) {
    btnReset.addEventListener('click', () => {
      if (typeof playSound === 'function') playSound('pop');
      setAchievementsScreen(1);
    });
  }
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-ach-nav]');
    if (trigger) {
      e.preventDefault();
      const targetScreen = parseInt(trigger.getAttribute('data-ach-nav'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setAchievementsScreen(targetScreen);
    }
  });

  // Badge Filter Pills (All / Earned / Locked)
  document.querySelectorAll('[data-ach-filter]').forEach(pill => {
    pill.addEventListener('click', (e) => {
      e.preventDefault();
      document.querySelectorAll('[data-ach-filter]').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      const filter = pill.getAttribute('data-ach-filter');
      document.querySelectorAll('#achScreen3 .badge-item-card').forEach(card => {
        if (filter === 'all') {
          card.style.display = 'flex';
        } else if (filter === 'earned') {
          card.style.display = card.classList.contains('earned-badge') ? 'flex' : 'none';
        } else if (filter === 'locked') {
          card.style.display = card.classList.contains('locked-badge') ? 'flex' : 'none';
        }
      });
      if (typeof playSound === 'function') playSound('pop');
    });
  });

  // Leaderboard Scope Tabs
  document.querySelectorAll('.lb-scope-tabs .lb-tab').forEach(tab => {
    tab.addEventListener('click', (e) => {
      e.preventDefault();
      document.querySelectorAll('.lb-scope-tabs .lb-tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      if (typeof playSound === 'function') playSound('pop');
    });
  });

  // Certificate View Modal & Download
  document.querySelectorAll('.btn-cert-view').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const title = btn.getAttribute('data-cert-title') || 'Certificate of Completion';
      const date = btn.getAttribute('data-cert-date') || '19 Nov 2026';
      const modalBackdrop = document.getElementById('modalBackdrop');
      const modalBody = document.getElementById('modalBody');
      if (modalBackdrop && modalBody) {
        modalBody.innerHTML = `
          <div style="text-align:center; padding: 10px;">
            <img src="assets/illustrations/certificate_large.png" alt="Certificate" style="width: 100%; max-width: 320px; height: auto; margin-bottom: 16px;">
            <h3 style="font-family: var(--font-display); font-size: 1.3rem; color: #1e1b4b; margin-bottom: 6px;">${title}</h3>
            <p style="font-size: 0.9rem; color: #64748b; margin-bottom: 12px;">Awarded to <strong>Kavin S.</strong> • Issued on ${date}</p>
            <button class="btn-primary" id="btnCloseCertModal" style="padding: 8px 24px; border-radius: 999px;">Close</button>
          </div>
        `;
        modalBackdrop.classList.add('active');
        document.getElementById('btnCloseCertModal')?.addEventListener('click', () => {
          modalBackdrop.classList.remove('active');
        });
        if (typeof playSound === 'function') playSound('celebration');
      }
    });
  });

  document.querySelectorAll('.btn-cert-download').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (typeof playSound === 'function') playSound('celebration');
      alert('Certificate downloaded successfully!');
    });
  });
}

// 5. AI STUDY BUDDY FLOW
let currentAiScreen = 1;
function setAiBuddyScreen(screenNum) {
  currentAiScreen = screenNum;
  document.querySelectorAll('[data-ai-step]').forEach(pill => {
    const s = parseInt(pill.getAttribute('data-ai-step'), 10);
    pill.classList.toggle('active-pill', s === screenNum);
  });
  document.querySelectorAll('[data-ai-screen]').forEach(panel => {
    const s = parseInt(panel.getAttribute('data-ai-screen'), 10);
    panel.classList.toggle('active-screen', s === screenNum);
  });
}

function initAiBuddyFlow() {
  document.querySelectorAll('[data-ai-step]').forEach(pill => {
    pill.addEventListener('click', () => {
      const step = parseInt(pill.getAttribute('data-ai-step'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setAiBuddyScreen(step);
    });
  });
  const btnReset = document.getElementById('btnResetAiFlow');
  if (btnReset) {
    btnReset.addEventListener('click', () => {
      if (typeof playSound === 'function') playSound('pop');
      setAiBuddyScreen(1);
    });
  }
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-ai-nav]');
    if (trigger) {
      e.preventDefault();
      const targetScreen = parseInt(trigger.getAttribute('data-ai-nav'), 10);
      if (typeof playSound === 'function') playSound('pop');
      setAiBuddyScreen(targetScreen);
    }
  });

  // Chat message sending
  const chatInput = document.querySelector('.ai-chat-input');
  const sendBtn = document.querySelector('.ai-send-btn');
  const chatContainer = document.getElementById('aiChatMsgContainer');

  function sendAiMessage() {
    if (!chatInput || !chatContainer) return;
    const text = chatInput.value.trim();
    if (!text) return;
    if (typeof playSound === 'function') playSound('pop');

    // Append user message
    const userRow = document.createElement('div');
    userRow.className = 'chat-bubble-row user-row';
    userRow.innerHTML = `
      <div class="chat-speech-bubble user-bubble">${text}</div>
      <div class="chat-avatar-circ user-avatar">👦</div>
    `;
    chatContainer.appendChild(userRow);
    chatInput.value = '';
    chatContainer.scrollTop = chatContainer.scrollHeight;

    // Simulate smart AI response
    setTimeout(() => {
      if (typeof playSound === 'function') playSound('pop');
      const botRow = document.createElement('div');
      botRow.className = 'chat-bubble-row bot-row';
      botRow.innerHTML = `
        <div class="chat-avatar-circ">🤖</div>
        <div class="chat-speech-bubble bot-bubble">
          Super question! 🌟 Let's solve it step-by-step together! You can click "Show Visual Steps" or "Practice a Problem" above to master it!
        </div>
      `;
      chatContainer.appendChild(botRow);
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }, 700);
  }

  if (sendBtn) {
    sendBtn.addEventListener('click', sendAiMessage);
  }
  if (chatInput) {
    chatInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        sendAiMessage();
      }
    });
  }
}
