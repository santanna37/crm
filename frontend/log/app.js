/* =========================================
   OBSERV — Dashboard de Observabilidade
   app.js - VERSÃO INTEGRADA (HEXAGONAL)
   ========================================= */

const isLocal = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";

const DEFAULT_CONFIG = {
  fastapi:  isLocal ? 'http://127.0.0.1:8000' : 'https://crm-back-bm9v.onrender.com',
  vercel:   'https://crm-eta-gold.vercel.app',
  supabase: 'https://sua-url-do-supabase.supabase.co', 
  // brevoKey removida: agora o backend cuida disso com segurança.
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

// ─── HEALTH CHECKS ─────────────────────────────────────────────────────────

async function checkAll() {
  const btn = document.getElementById('btn-refresh');
  btn.textContent = '↻ ...';
  btn.disabled = true;

  // MODIFICADO: Chamamos as checagens. Note que a Brevo agora depende da resposta da FastAPI
  await Promise.allSettled([
    checkFastAPIAndServices(), // Esta função agora cuida de FastAPI E Brevo
    checkVercel(),
    checkSupabase(),
  ]);

  updateOverall();
  btn.textContent = '↻ atualizar';
  btn.disabled = false;
}

async function checkFastAPIAndServices() {
  const idFast = 'fastapi';
  const idBrevo = 'brevo';
  
  try {
    const t = Date.now();
    // Chamada única para o seu adapter_person.system_check_health
    const res = await fetchWithTimeout(cfg.fastapi + '/system/health', 8000);
    const ms  = Date.now() - t;
    const data = await res.json();
    const ok  = res.ok;

    // 1. ATUALIZA CARD FASTAPI (O que já fazia)
    registerCheck(idFast, ok);
    setServiceState(
      idFast,
      ok ? 'ok' : 'err',
      ok ? 'online' : `erro ${res.status}`,
      ok ? `${ms}ms` : '—',
      formatLatencyBar(idFast, ms, ok),
    );
    document.getElementById('meta-fastapi').textContent = `/system/health · ${ms}ms`;

    // 2. ATUALIZA CARD BREVO (Lendo o JSON unificado do seu Backend)
    // MODIFICADO: Acessando data.services.brevo (conforme montamos no Python)
    if (data.services && data.services.brevo) {
      const info = data.services.brevo;
      const brevoOk = info.status === 'online';
      
      registerCheck(idBrevo, brevoOk);
      setServiceState(
        idBrevo,
        brevoOk ? 'ok' : 'err',
        brevoOk ? 'autenticado' : 'erro na ponte',
        brevoOk ? `${info.monthly_sent} envios` : '—',
        '—'
      );
      
      // Preenche os campos de texto no card da Brevo
      document.getElementById('meta-brevo').textContent = info.account_email || 'conta ativa';
      document.getElementById('lat-brevo').textContent  = info.monthly_sent?.toLocaleString('pt-BR') || '0';
    }

  } catch (e) {
    registerCheck(idFast, false);
    registerCheck(idBrevo, false);
    setServiceState(idFast, 'err', 'inacessível', '—', '—');
    setServiceState(idBrevo, 'err', 'backend offline', '—', '—');
  }
}

// ... (Funções checkVercel e checkSupabase permanecem como estavam)
// ... (Função fetchLogs e renderLogs permanecem como estavam)