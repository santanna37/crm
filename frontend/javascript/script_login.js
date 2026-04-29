// Configuração da API Supabase
const SUPABASE_URL = 'https://lipajeykqlitxzooxjza.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxpcGFqZXlrcWxpdHh6b294emp6YSIsInJvbGUiOiJhbm9uIiwiaWF0IjoxNzMwMzY2NzQ4LCJleHAiOjE4NDYxNDI3NDh9.m3M-yrI8JZ9EeSDUJ0GJB5Q1X4j5F6zT4Xl2CXLr6ME';

// Elementos do DOM
const loginForm = document.getElementById('loginForm');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const togglePassword = document.getElementById('togglePassword');
const errorMessage = document.getElementById('error-message');
const submitBtn = loginForm.querySelector('button[type="submit"]');
const rememberCheckbox = document.getElementById('remember');

// Verifica se usuário já está logado
document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('admin_token') || sessionStorage.getItem('admin_token');
    if (token) {
        // Tenta validar o token fazendo uma requisição de teste
        validateToken(token);
    }
});

// Toggle de visibilidade da senha
togglePassword.addEventListener('click', function() {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    
    // Muda o ícone
    const icon = this.querySelector('i');
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
});

// Submissão do formulário
loginForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    
    // Validação básica
    if (!emailInput.value || !passwordInput.value) {
        showError('Por favor, preencha todos os campos.');
        return;
    }
    
    // Desabilita botão durante o login
    setLoadingState(true);
    hideError();
    
    try {
        const response = await fetch(`${SUPABASE_URL}/auth/v1/token?grant_type=password`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'apikey': SUPABASE_ANON_KEY
            },
            body: JSON.stringify({
                email: emailInput.value.trim(),
                password: passwordInput.value
            })
        });
        
        const data = await response.json();
        
        if (response.ok && data.access_token) {
            // Sucesso no login
            const token = data.access_token;
            
            // Verifica se o usuário tem role 'admin'
            const userRole = data.user?.app_metadata?.role || data.user?.role;
            
            if (userRole !== 'admin') {
                showError('Acesso negado. Esta área é restrita a administradores.');
                setLoadingState(false);
                return;
            }
            
            // Armazena o token
            if (rememberCheckbox.checked) {
                localStorage.setItem('admin_token', token);
                localStorage.setItem('admin_email', data.user.email);
            } else {
                sessionStorage.setItem('admin_token', token);
                sessionStorage.setItem('admin_email', data.user.email);
            }
            
            // Redireciona para a lista
            window.location.href = '/frontend/html/lista.html';
            
        } else {
            // Erro de autenticação
            const errorMsg = data.msg || data.error_description || 'Credenciais inválidas.';
            showError(errorMsg);
        }
        
    } catch (error) {
        console.error('Erro ao fazer login:', error);
        showError('Erro de conexão. Verifique sua internet e tente novamente.');
    } finally {
        setLoadingState(false);
    }
});

// Função para validar token existente
async function validateToken(token) {
    try {
        const response = await fetch(`${SUPABASE_URL}/auth/v1/user`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'apikey': SUPABASE_ANON_KEY
            }
        });
        
        if (response.ok) {
            const userData = await response.json();
            const userRole = userData.app_metadata?.role || userData.role;
            
            if (userRole === 'admin') {
                window.location.href = '/frontend/html/lista.html';
            }
        }
    } catch (error) {
        console.error('Erro ao validar token:', error);
        // Token inválido, remove do storage
        localStorage.removeItem('admin_token');
        sessionStorage.removeItem('admin_token');
    }
}

// Função para mostrar erro
function showError(message) {
    errorMessage.querySelector('span').textContent = message;
    errorMessage.classList.remove('hidden');
}

// Função para esconder erro
function hideError() {
    errorMessage.classList.add('hidden');
}

// Função para controlar estado de loading do botão
function setLoadingState(isLoading) {
    if (isLoading) {
        submitBtn.disabled = true;
        submitBtn.classList.add('btn-loading');
        submitBtn.querySelector('.btn-text').textContent = 'Entrando...';
        submitBtn.querySelector('i').className = 'fas fa-spinner fa-spin';
    } else {
        submitBtn.disabled = false;
        submitBtn.classList.remove('btn-loading');
        submitBtn.querySelector('.btn-text').textContent = 'Entrar';
        submitBtn.querySelector('i').className = 'fas fa-arrow-right';
    }
}

// Limpar mensagem de erro ao digitar
emailInput.addEventListener('input', hideError);
passwordInput.addEventListener('input', hideError);
