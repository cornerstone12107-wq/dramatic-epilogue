/* =============================================
   script.js — 드라마틱 에필로그 : 케노시스
   빌립보서 2:5-11
   ============================================= */

// ─── 카카오 JavaScript 키 (발급받은 키로 교체하세요) ───
const KAKAO_APP_KEY = 'YOUR_KAKAO_JAVASCRIPT_KEY';

// ─── 전체 씬 수 (scene-0 ~ scene-14) ───
const TOTAL_SCENES = 15;

let currentScene = 0;
let soundOn = false;
let sliderMoved = false;

const bgm = document.getElementById('bgm');
const soundBtn = document.getElementById('sound-btn');

// ─── 초기화 ─────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  // 카카오 SDK 초기화
  if (KAKAO_APP_KEY && KAKAO_APP_KEY !== 'YOUR_KAKAO_JAVASCRIPT_KEY') {
    try { Kakao.init(KAKAO_APP_KEY); } catch (e) { console.warn('Kakao init 실패:', e); }
  }

  showScene(0);

  // 첫 터치 시 BGM 자동 시작
  document.addEventListener('touchstart', tryAutoPlay, { once: true });
});

function tryAutoPlay() {
  if (!soundOn) {
    bgm.volume = 0.42;
    bgm.play().then(() => {
      soundOn = true;
      soundBtn.textContent = '🔊';
    }).catch(() => {});
  }
}

function startApp() {
  tryAutoPlay();
  goNext(0);
}

// ─── 씬 이동 ─────────────────────────────────
function showScene(index) {
  document.querySelectorAll('.scene').forEach(s => s.classList.remove('active'));
  const target = document.getElementById('scene-' + index);
  if (target) {
    target.classList.add('active');
    target.scrollTop = 0;
  }
  currentScene = index;
}

function goNext(from) {
  const next = from + 1;
  if (next < TOTAL_SCENES) showScene(next);
}

function goPrev(from) {
  const prev = from - 1;
  if (prev >= 0) showScene(prev);
}

// ─── 슬라이더 ─────────────────────────────────
function onSliderChange(value) {
  if (!sliderMoved && parseInt(value) >= 20) {
    sliderMoved = true;
    setTimeout(() => goNext(1), 350);
  }
}

// ─── 사운드 ──────────────────────────────────
function toggleSound() {
  if (soundOn) {
    bgm.pause(); soundOn = false; soundBtn.textContent = '🔇';
  } else {
    bgm.volume = 0.42;
    bgm.play().then(() => {
      soundOn = true; soundBtn.textContent = '🔊';
    }).catch(() => {});
  }
}

// ─── 카카오 공유 ─────────────────────────────
function shareKakao() {
  let pageUrl = window.location.href.split('?')[0];
  if (pageUrl.endsWith('index.html')) {
    pageUrl = pageUrl.replace('index.html', '');
  }
  if (!pageUrl.endsWith('/')) {
    pageUrl += '/';
  }

  if (!KAKAO_APP_KEY || KAKAO_APP_KEY === 'YOUR_KAKAO_JAVASCRIPT_KEY'
      || typeof Kakao === 'undefined' || !Kakao.isInitialized()) {
    copyLink(pageUrl); return;
  }

  try {
    Kakao.Share.sendDefault({
      objectType: 'feed',
      content: {
        title: '드라마틱 에필로그 — 케노시스',
        description: '나를 위해 가장 낮은 곳까지 비우신 위대한 왕의 사랑.',
        imageUrl: pageUrl + 'images/0.jpeg?v=new2',
        link: { mobileWebUrl: pageUrl, webUrl: pageUrl },
      },
      buttons: [{
        title: '에필로그 보기',
        link: { mobileWebUrl: pageUrl, webUrl: pageUrl },
      }],
    });
  } catch (e) {
    console.warn('카카오 공유 실패:', e);
    copyLink(pageUrl);
  }
}

// 링크 복사 fallback
function copyLink(url) {
  const copy = () => showToast('링크가 복사됐어요! 카카오톡에 붙여넣기 해주세요 🌸');
  if (navigator.clipboard) {
    navigator.clipboard.writeText(url).then(copy);
  } else {
    const ta = document.createElement('textarea');
    ta.value = url;
    document.body.appendChild(ta); ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta); copy();
  }
}

// 토스트 메시지
function showToast(msg) {
  let toast = document.getElementById('toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast';
    toast.style.cssText = [
      'position:fixed', 'bottom:110px', 'left:50%', 'transform:translateX(-50%)',
      'background:rgba(40,25,15,0.9)', 'color:white', 'padding:12px 22px',
      'border-radius:50px', 'font-size:13px', "font-family:'Noto Sans KR',sans-serif",
      'z-index:9999', 'white-space:nowrap', 'box-shadow:0 4px 16px rgba(0,0,0,0.25)',
      'backdrop-filter:blur(8px)', 'transition:opacity 0.4s', 'letter-spacing:0.03em',
    ].join(';');
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.style.display = 'block';
  toast.style.opacity = '1';
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => { toast.style.display = 'none'; }, 400);
  }, 2800);
}
