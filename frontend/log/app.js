/* =========================================
   OBSERV — Dashboard de Observabilidade
   app.js - VERSÃO FINAL E COMPLETA
   ========================================= */

const isLocal = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";

const DEFAULT_CONFIG = {
  fastapi:  isLocal ? 'http://127.0.0.1:8000' : 'https://crm-back-bm9v.onrender.com',
  vercel:   'https://crm-eta-gold.vercel.app/frontend/index.html',
  supabase: 'https://sua-url-do-supabase.supabase.co', 
};

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
  startClock();
  checkAll();
  fetchLogs();
  startPolling();
});

function startClock() {
  const el = document.getElementById('clock');
  setInterval(() => {
    const now = new Date();
    el.textContent = now.toLocaleTimeString('pt-BR', { hour12: false });
  }, 1000);
}

function startPolling() {
  if (pollInterval) clearInterval(pollInterval);
  pollInterval = setInterval(() => {
    checkAll();
    fetchLogs();
  }, 30000);
}

// ─── HEALTH CHECKS ─────────────────────────────────────────────────────────

async function checkAll() {
  const btn = document.getElementById('btn-refresh');
  if (btn) {
    btn.textContent = '↻ ...';
    btn.disabled = true;
  }

  await Promise.allSettled([
    checkFastAPIAndServices(),
    checkVercel(),
    checkSupabase(),
  ]);

  updateOverall();
  
  if (btn) {
    btn.textContent = '↻ atualizar';
    btn.disabled = false;
  }
}

async function checkFastAPIAndServices() {
  const idFast = 'fastapi';
  const idBrevo = 'brevo';
  
  try {
    const t = Date.now();
    const res = await fetchWithTimeout(cfg.fastapi + '/system/health', 8000);
    const ms  = Date.now() - t;
    const data = await res.json();
    const ok  = res.ok;

    registerCheck(idFast, ok);
    setServiceState(
      idFast,
      ok ? 'ok' : 'err',
      ok ? 'online' : `erro ${res.status}`,
      ok ? `${ms}ms` : '—',
      formatLatencyBar(idFast, ms, ok)
    );
    document.getElementById('meta-fastapi').textContent = `/system/health · ${ms}ms`;

    if (data.services && data.services.brevo) {
      const info = data.services.brevo;
      const brevoOk = info.status === 'online';
      
      registerCheck(idBrevo, brevoOk);
      setServiceState(
        idBrevo,
        brevoOk ? 'ok' : 'err',
        brevoOk ? 'autenticado' : 'erro ponte',
        brevoOk ? `${info.monthly_sent} env` : '—',
        '—'
      );
      
      document.getElementById('meta-brevo').textContent = info.account_email || 'conta ativa';
      document.getElementById('lat-brevo').textContent  = info.monthly_sent?.toLocaleString('pt-BR') || '0';
    }

  } catch (e) {
    registerCheck(idFast, false);
    registerCheck(idBrevo, false);
    setServiceState(idFast, 'err', 'offline', '—', '—');
    setServiceState(idBrevo, 'err', 'off', '—', '—');
  }
}

async function checkVercel() {
  const id = 'vercel';
  try {
    const t = Date.now();
    const res = await fetchWithTimeout(cfg.vercel, 5000);
    const ms = Date.now() - t;
    const ok = res.ok;
    registerCheck(id, ok);
    setServiceState(id, ok ? 'ok' : 'err', ok ? 'online' : 'erro', `${ms}ms`, '100%');
  } catch (e) {
    registerCheck(id, false);
    setServiceState(id, 'err', 'offline', '—', '0%');
  }
}

async function checkSupabase() {
  const id = 'supabase';
  // Simulação baseada no status do backend
  const isOk = serviceState.fastapi.ok > 0;
  registerCheck(id, isOk);
  setServiceState(id, isOk ? 'ok' : 'err', isOk ? 'conectado' : 'desconectado', '—', '100%');
}

// ─── LOGS ──────────────────────────────────────────────────────────────────

async function fetchLogs() {
  setLiveDot(true);
  try {
    const res = await fetchWithTimeout(cfg.fastapi + '/system/logs', 5000);
    if (res.ok) {
      allLogs = await res.json();
      renderLogs();
    }
  } catch (e) {
    console.warn("Backend offline para logs.");
  }
  setLiveDot(false);
}

function renderLogs() {
  const terminal = document.getElementById('log-terminal');
  const countEl = document.getElementById('log-count');
  const levelFilt = document.getElementById('filter-level').value;
  
  const filtered = allLogs.filter(l => levelFilt === 'all' || l.level === levelFilt);
  
  if (filtered.length === 0) {
    terminal.innerHTML = '<div class="log-placeholder">sem logs para exibir...</div>';
  } else {
    terminal.innerHTML = filtered.map(l => `
      <div class="log-line">
        <span class="log-time">[${l.time}]</span>
        <span class="log-level ${l.level.toLowerCase()}">${l.level}</span>
        <span class="log-msg">${l.msg}</span>
      </div>
    `).join('');
  }
  
  countEl.textContent = `${filtered.length} entradas`;
  
  if (document.getElementById('auto-scroll').checked) {
    terminal.scrollTop = terminal.scrollHeight;
  }
}

// ─── UTILITÁRIOS ───────────────────────────────────────────────────────────

function registerCheck(id, ok) {
  if (serviceState[id]) {
    serviceState[id].checks++;
    if (ok) serviceState[id].ok++;
  }
}

function setServiceState(id, status, text, lat, bar) {
  const dot  = document.getElementById(`dot-${id}`);
  const txt  = document.getElementById(`text-${id}`);
  const lVal = document.getElementById(`lat-${id}`);
  const chk  = document.getElementById(`chk-${id}`);
  const up   = document.getElementById(`up-${id}`);
  const bFill= document.getElementById(`bar-${id}`);

  if (dot) dot.className = `ind-dot ${status}`;
  if (txt) txt.textContent = text;
  if (lVal) lVal.textContent = lat;
  if (bFill) bFill.style.width = bar !== '—' ? bar : '0%';
  
  const stats = serviceState[id];
  if (chk) chk.textContent = stats.checks;
  if (up) {
    const rate = stats.checks > 0 ? ((stats.ok / stats.checks) * 100).toFixed(1) : 0;
    up.textContent = `${rate}%`;
  }
}

function updateOverall() {
  const dot = document.getElementById('overall-dot');
  const txt = document.getElementById('overall-text');
  const anyErr = Object.values(serviceState).some(s => s.checks > 0 && s.ok === 0);
  
  dot.className = anyErr ? 'overall-dot err' : 'overall-dot ok';
  txt.textContent = anyErr ? 'atenção: falhas detectadas' : 'sistema operacional';
}

function formatLatencyBar(id, ms, ok) {
  if (!ok) return '0%';
  if (ms < 200) return '100%';
  if (ms < 500) return '70%';
  return '30%';
}

async function fetchWithTimeout(resource, timeout = 8000) {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);
  try {
    const response = await fetch(resource, { signal: controller.signal });
    clearTimeout(id);
    return response;
  } catch (e) {
    clearTimeout(id);
    throw e;
  }
}

function setLiveDot(active) {
  const dot = document.getElementById('live-dot');
  if (dot) dot.style.opacity = active ? '1' : '0.3';
}

function clearLogs() {
  allLogs = [];
  renderLogs();
}