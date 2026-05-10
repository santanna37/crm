/* ============================================================
   APP.JS - Módulos Compartilhados
   Auth, API, Utils
   ============================================================ */

const CONFIG = {
    API_BASE_URL: 'https://back-claudinho.onrender.com',
    SUPABASE_URL: 'https://lipajeykqlitxzooxjza.supabase.co',
    SUPABASE_ANON_KEY: 'sb_publishable__-e1dxqLKevQ6Lga5YmJWQ_7o3Q56UN'
};

/* ===== AUTH ===== */
const Auth = {
    getToken() {
        return localStorage.getItem('admin_token') || sessionStorage.getItem('admin_token');
    },

    isAuthenticated() {
        return !!this.getToken();
    },

    setToken(token, remember = false) {
        if (remember) {
            localStorage.setItem('admin_token', token);
        } else {
            sessionStorage.setItem('admin_token', token);
        }
    },

    clearToken() {
        localStorage.removeItem('admin_token');
        sessionStorage.removeItem('admin_token');
        localStorage.removeItem('admin_email');
        sessionStorage.removeItem('admin_email');
    },

    logout() {
        if (confirm('Tem certeza que deseja sair?')) {
            this.clearToken();
            window.location.href = '/frontend/login.html';
        }
    },

    requireAuth() {
        if (!this.isAuthenticated()) {
            alert('Sessão expirada. Por favor, faça login novamente.');
            window.location.href = '/frontend/login.html';
            return false;
        }
        return true;
    },

    async validateToken(token) {
        try {
            const response = await fetch(`${CONFIG.SUPABASE_URL}/auth/v1/user`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'apikey': CONFIG.SUPABASE_ANON_KEY
                }
            });
            return response.ok;
        } catch {
            return false;
        }
    },

    setupLogoutButton() {
        const btn = document.getElementById('logout-btn');
        if (btn) {
            btn.addEventListener('click', () => this.logout());
        }
    }
};

/* ===== API ===== */
const API = {
    async request(endpoint, options = {}) {
        const token = Auth.getToken();
        const url = `${CONFIG.API_BASE_URL}${endpoint}`;

        const defaults = {
            headers: {
                'Content-Type': 'application/json',
                ...(token && { 'Authorization': `Bearer ${token}` })
            }
        };

        const response = await fetch(url, { ...defaults, ...options });

        if (response.status === 401) {
            Auth.clearToken();
            alert('Sessão inválida. Por favor, faça login novamente.');
            window.location.href = '/frontend/login.html';
            return null;
        }

        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(error.detail || `Erro ${response.status}`);
        }

        return response.json();
    },

    get(endpoint) {
        return this.request(endpoint, { method: 'GET' });
    },

    post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }
};

/* ===== UTILS ===== */
const Utils = {
    formatDate(dateStr) {
        if (!dateStr) return '-';
        const [year, month, day] = dateStr.split('-');
        return `${day}/${month}/${year}`;
    },

    formatPhone(phone) {
        if (!phone) return '-';
        const cleaned = phone.replace(/\D/g, '');
        if (cleaned.length === 11) {
            return `(${cleaned.slice(0,2)}) ${cleaned.slice(2,7)}-${cleaned.slice(7)}`;
        }
        return phone;
    },

    formatCEP(cep) {
        if (!cep) return '-';
        const cleaned = cep.replace(/\D/g, '');
        if (cleaned.length === 8) {
            return `${cleaned.slice(0,5)}-${cleaned.slice(5)}`;
        }
        return cep;
    },

    showLoading(elementId) {
        const el = document.getElementById(elementId);
        if (el) el.classList.remove('hidden');
    },

    hideLoading(elementId) {
        const el = document.getElementById(elementId);
        if (el) el.classList.add('hidden');
    },

    showAlert(message, type = 'error') {
        const existing = document.querySelector('.alert');
        if (existing) existing.remove();

        const alert = document.createElement('div');
        alert.className = `alert alert-${type}`;
        alert.innerHTML = `<i class="fas fa-${type === 'error' ? 'exclamation-circle' : 'check-circle'}"></i> <span>${message}</span>`;

        const container = document.querySelector('.main-content') || document.body;
        container.insertBefore(alert, container.firstChild);

        setTimeout(() => alert.remove(), 5000);
    },

    debounce(fn, delay) {
        let timeout;
        return (...args) => {
            clearTimeout(timeout);
            timeout = setTimeout(() => fn(...args), delay);
        };
    }
};

/* ===== CEP ===== */
const CEP = {
    async buscar(cepValue) {
        const cleaned = cepValue.replace(/\D/g, '');
        if (cleaned.length !== 8) {
            throw new Error('Digite um CEP com 8 números.');
        }

        const response = await fetch(`https://viacep.com.br/ws/${cleaned}/json/`);
        const data = await response.json();

        if (data.erro) {
            throw new Error('CEP não encontrado.');
        }

        return {
            logradouro: data.logradouro,
            bairro: data.bairro,
            localidade: data.localidade,
            uf: data.uf
        };
    }
};

// Exportar para uso global
window.CONFIG = CONFIG;
window.Auth = Auth;
window.API = API;
window.Utils = Utils;
window.CEP = CEP;
