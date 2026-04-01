/* =========================================
   OBSERV — Dashboard de Observabilidade
   app.js
   ========================================= */

// ─── CONFIG ────────────────────────────────────────────────────────────────
// Edite aqui ou use o painel de configuração na tela.
// As URLs salvas via UI ficam no localStorage.

const DEFAULT_CONFIG = {
  fastapi:  '',   // ex: https://meu-app.onrender.com
  vercel:   '',   // ex: https://meu-app.vercel.app
  supabase: '',   // ex: https://xxxx.supabase.co
  brevoKey: '',   // chave de API do Brevo
};

// ─── ESTADO ────────────────────────────────────────────────────────────────

let cfg = { ...DEFAULT_CONFIG };
let serviceState = {
  fastapi:  { checks: 0, ok: 0 },
  vercel:   { checks: 0, ok: 0 },
  supabase: { checks: 0, ok: 0 },
  brevo:    { checks: 0, ok: 0 },
};

let allLogs = [];
let pollInterval = null;

// ─── INICIALIZAÇÃO ─────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  loadConfig();
  startClock();
  checkAll();
  fetchLogs();
  startPolling();
});

// ─── RELÓGIO ───────────────────────────────────────────────────────────────

function startClock() {
  const el = document.getElementById('clock');
  function tick() {
    const now = new Date();
    el.textContent = now.toLocaleTimeString('pt-BR', { hour12: false });
  }
  tick();
  setInterval(tick, 1000);
}

// ─── POLLING ───────────────────────────────────────────────────────────────

function startPolling() {
  if (pollInterval) clearInterval(pollInterval);
  pollInterval = setInterval(() => {
    checkAll();
    fetchLogs();
  }, 30_000);
}

// ─── CONFIG UI ─────────────────────────────────────────────────────────────

function loadConfig() {
  try {
    const saved = JSON.parse(localStorage.getItem('observ_cfg') || '{}');
    cfg = { ...DEFAULT_CONFIG, ...saved };
  } catch {
    cfg = { ...DEFAULT_CONFIG };
  }
  document.getElementById('cfg-fastapi').value  = cfg.fastapi  || '';
  document.getElementById('cfg-vercel').value   = cfg.vercel   || '';
  document.getElementById('cfg-supabase').value = cfg.supabase || '';
  document.getElementById('cfg-brevo').value    = cfg.brevoKey || '';
}

function saveConfig() {
  cfg.fastapi  = document.getElementById('cfg-fastapi').value.trim().replace(/\/$/, '');
  cfg.vercel   = document.getElementById('cfg-vercel').value.trim().replace(/\/$/, '');
  cfg.supabase = document.getElementById('cfg-supabase').value.trim().replace(/\/$/, '');
  cfg.brevoKey = document.getElementById('cfg-brevo').value.trim();
  localStorage.setItem('observ_cfg', JSON.stringify(cfg));

  const el = document.getElementById('config-saved');
  el.textContent = '✓ salvo';
  el.classList.add('visible');
  setTimeout(() => el.classList.remove('visible'), 2500);

  checkAll();
  fetchLogs();
}

// ─── HEALTH CHECKS ─────────────────────────────────────────────────────────

async function checkAll() {
  const btn = document.getElementById('btn-refresh');
  btn.textContent = '↻ ...';
  btn.disabled = true;

  await Promise.allSettled([
    checkFastAPI(),
    checkVercel(),
    checkSupabase(),
    checkBrevo(),
  ]);

  updateOverall();
  btn.textContent = '↻ atualizar';
  btn.disabled = false;
}

async function checkFastAPI() {
  const id = 'fastapi';
  if (!cfg.fastapi) {
    setServiceState(id, 'warn', 'não configurado', '—', '—');
    return;
  }
  try {
    const t = Date.now();
    const res = await fetchWithTimeout(cfg.fastapi + '/health', 8000);
    const ms  = Date.now() - t;
    const ok  = res.ok;
    registerCheck(id, ok);
    setServiceState(
      id,
      ok ? 'ok' : 'err',
      ok ? 'online' : `erro ${res.status}`,
      ok ? `${ms}ms` : '—',
      formatLatencyBar(id, ms, ok),
    );
    document.getElementById('meta-fastapi').textContent = `/health · ${ms}ms`;
  } catch (e) {
    registerCheck(id, false);
    setServiceState(id, 'err', 'inacessível', '—', '—');
  }
}

async function checkVercel() {
  const id = 'vercel';
  if (!cfg.vercel) {
    setServiceState(id, 'warn', 'não configurado', '—', '—');
    return;
  }
  try {
    const t   = Date.now();
    const res = await fetchWithTimeout(cfg.vercel, 10000);
    const ms  = Date.now() - t;
    const ok  = res.ok || res.status === 304;
    registerCheck(id, ok);
    setServiceState(id, ok ? 'ok' : 'err', ok ? 'online' : `erro ${res.status}`, ok ? `${ms}ms` : '—', formatLatencyBar(id, ms, ok));
    document.getElementById('meta-vercel').textContent = `raiz · ${ms}ms`;
  } catch {
    registerCheck(id, false);
    setServiceState(id, 'err', 'inacessível', '—', '—');
  }
}

async function checkSupabase() {
  const id = 'supabase';
  if (!cfg.supabase) {
    setServiceState(id, 'warn', 'não configurado', '—', '—');
    return;
  }
  try {
    const t   = Date.now();
    const res = await fetchWithTimeout(cfg.supabase + '/rest/v1/', 8000);
    const ms  = Date.now() - t;
    // Supabase retorna 401 quando não há anon key — API está de pé mesmo assim
    const ok  = res.ok || res.status === 401;
    registerCheck(id, ok);
    setServiceState(id, ok ? 'ok' : 'err', ok ? 'online' : `erro ${res.status}`, ok ? `${ms}ms` : '—', formatLatencyBar(id, ms, ok));
    document.getElementById('meta-supabase').textContent = `/rest/v1 · ${ms}ms`;
  } catch {
    registerCheck(id, false);
    setServiceState(id, 'err', 'inacessível', '—', '—');
  }
}

async function checkBrevo() {
  const id = 'brevo';
  if (!cfg.brevoKey) {
    setServiceState(id, 'warn', 'não configurado', '—', '—');
    return;
  }
  try {
    const res = await fetchWithTimeout('https://api.brevo.com/v3/account', 8000, {
      headers: { 'api-key': cfg.brevoKey }
    });
    if (res.ok) {
      const data = await res.json();
      registerCheck(id, true);
      const emailsSent = data.statistics?.monthlyEmailSent ?? '—';
      setServiceState(id, 'ok', 'autenticado', typeof emailsSent === 'number' ? `${emailsSent} este mês` : '—', '—');
      document.getElementById('meta-brevo').textContent = data.email || 'conta ativa';
      document.getElementById('lat-brevo').textContent  = typeof emailsSent === 'number' ? emailsSent.toLocaleString('pt-BR') : '—';
    } else {
      registerCheck(id, false);
      setServiceState(id, 'err', res.status === 401 ? 'api key inválida' : `erro ${res.status}`, '—', '—');
    }
  } catch {
    registerCheck(id, false);
    setServiceState(id, 'err', 'inacessível', '—', '—');
  }
}

// ─── DOM: SERVIÇOS ─────────────────────────────────────────────────────────

function setServiceState(id, state, text, latency, _) {
  const card = document.getElementById(`card-${id}`);
  const dot  = document.getElementById(`dot-${id}`);
  const txt  = document.getElementById(`text-${id}`);
  const latEl = document.getElementById(`lat-${id}`);

  card.className = `service-card state-${state}`;
  dot.className  = `ind-dot ${state}`;
  txt.className  = `ind-text ${state}`;
  txt.textContent = text;

  if (id !== 'brevo' && latency !== '—') {
    latEl.textContent = latency;
  }

  // uptime %
  const s = serviceState[id];
  if (s.checks > 0) {
    const pct = Math.round((s.ok / s.checks) * 100);
    document.getElementById(`up-${id}`).textContent  = `${pct}%`;
    document.getElementById(`chk-${id}`).textContent = s.checks;
  }

  // latency bar
  const bar = document.getElementById(`bar-${id}`);
  if (state === 'err' || latency === '—') {
    bar.style.width = '0%';
    bar.className   = 'bar-fill dead';
  } else {
    const ms  = parseInt(latency);
    const pct = Math.min(100, Math.round((ms / 2000) * 100));
    bar.style.width = `${pct}%`;
    bar.className   = `bar-fill${ms > 800 ? ' slow' : ''}`;
  }
}

function registerCheck(id, success) {
  serviceState[id].checks++;
  if (success) serviceState[id].ok++;
}

function formatLatencyBar(id, ms, ok) {
  return ok ? `${ms}ms` : '—';
}

// ─── OVERALL BADGE ─────────────────────────────────────────────────────────

function updateOverall() {
  const badge = document.getElementById('overall-badge');
  const txt   = document.getElementById('overall-text');

  const cards = ['fastapi', 'vercel', 'supabase', 'brevo'];
  const states = cards.map(id => document.getElementById(`card-${id}`).className);

  const hasErr  = states.some(c => c.includes('state-err'));
  const hasWarn = states.some(c => c.includes('state-warn'));

  if (hasErr) {
    badge.className = 'overall-badge err';
    txt.textContent = 'erro detectado';
  } else if (hasWarn) {
    badge.className = 'overall-badge warn';
    txt.textContent = 'config pendente';
  } else {
    badge.className = 'overall-badge ok';
    txt.textContent = 'tudo ok';
  }
}

// ─── LOGS ──────────────────────────────────────────────────────────────────

const MOCK_LOGS = [
  { time: nowTime(-0),  level: 'INFO',  service: 'fastapi', msg: 'GET /health → 200 [2ms]' },
  { time: nowTime(-3),  level: 'INFO',  service: 'fastapi', msg: 'POST /api/users/register → 201 [34ms]' },
  { time: nowTime(-6),  level: 'WARN',  service: 'fastapi', msg: 'Token expirando em menos de 5min para user_id=42' },
  { time: nowTime(-9),  level: 'INFO',  service: 'brevo',   msg: 'Email enviado: confirmação de cadastro → user@email.com' },
  { time: nowTime(-14), level: 'INFO',  service: 'fastapi', msg: 'GET /api/products → 200 [18ms]' },
  { time: nowTime(-17), level: 'ERROR', service: 'fastapi', msg: 'DB timeout na query users.find_by_email [502ms]' },
  { time: nowTime(-22), level: 'INFO',  service: 'brevo',   msg: 'Campanha "Bem-vindo" despachada (12 destinatários)' },
  { time: nowTime(-26), level: 'INFO',  service: 'fastapi', msg: 'GET /api/orders?user=9 → 200 [22ms]' },
  { time: nowTime(-30), level: 'WARN',  service: 'fastapi', msg: '3 tentativas falhas de login para user_id=7' },
  { time: nowTime(-35), level: 'INFO',  service: 'fastapi', msg: 'POST /api/checkout → 201 [61ms]' },
  { time: nowTime(-38), level: 'INFO',  service: 'brevo',   msg: 'Email enviado: recibo pedido #881 → cliente@mail.com' },
  { time: nowTime(-42), level: 'ERROR', service: 'fastapi', msg: "Unhandled exception: KeyError 'price' em checkout.py:88" },
];

function nowTime(offsetSeconds) {
  const d = new Date(Date.now() + offsetSeconds * 1000);
  return d.toLocaleTimeString('pt-BR', { hour12: false });
}

async function fetchLogs() {
  setLiveDot(true);
  if (cfg.fastapi) {
    try {
      const res  = await fetchWithTimeout(cfg.fastapi + '/logs', 5000);
      if (res.ok) {
        const data = await res.json();
        if (Array.isArray(data) && data.length) {
          allLogs = data;
          renderLogs();
          return;
        }
      }
    } catch {
      // fallback para mock
    }
  }
  // usa mock quando não há backend configurado
  allLogs = [...MOCK_LOGS];
  renderLogs();
}

function renderLogs() {
  const level = document.getElementById('filter-level').value;
  const svc   = document.getElementById('filter-service').value;

  const filtered = allLogs.filter(l =>
    (level === 'all' || l.level === level) &&
    (svc   === 'all' || l.service === svc)
  );

  const container = document.getElementById('log-terminal');
  document.getElementById('log-count').textContent =
    `${filtered.length} entrada${filtered.length !== 1 ? 's' : ''}`;

  if (!filtered.length) {
    container.innerHTML = '<div class="log-placeholder">nenhum log encontrado.</div>';
    return;
  }

  container.innerHTML = filtered.map(l => `
    <div class="log-row level-${l.level}">
      <span class="log-time">${escHtml(l.time)}</span>
      <span class="log-level ${l.level}">${l.level}</span>
      <span class="log-svc">${escHtml(l.service)}</span>
      <span class="log-msg">${escHtml(l.msg)}</span>
    </div>
  `).join('');

  const autoScroll = document.getElementById('auto-scroll').checked;
  if (autoScroll) {
    container.scrollTop = 0; // logs mais recentes no topo
  }
}

function clearLogs() {
  allLogs = [];
  renderLogs();
}

function setLiveDot(active) {
  const dot = document.getElementById('live-dot');
  dot.className = active ? 'live-dot active' : 'live-dot';
}

// ─── UTILITÁRIOS ───────────────────────────────────────────────────────────

function fetchWithTimeout(url, timeout = 8000, options = {}) {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);
  return fetch(url, { ...options, signal: controller.signal, mode: 'cors' })
    .finally(() => clearTimeout(id));
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
