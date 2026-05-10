/* ============================================================
   LOGIN.JS - Autenticação Administrativa
   ============================================================ */

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const togglePassword = document.getElementById('togglePassword');
    const errorMessage = document.getElementById('error-message');
    const submitBtn = document.getElementById('submit-btn');
    const rememberCheckbox = document.getElementById('remember');

    // Verifica se já está logado
    const token = Auth.getToken();
    if (token) {
        Auth.validateToken(token).then(valid => {
            if (valid) {
                window.location.href = 'dashboard.html';
            } else {
                Auth.clearToken();
            }
        });
    }

    // Toggle senha
    togglePassword.addEventListener('click', function() {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        const icon = this.querySelector('i');
        icon.classList.toggle('fa-eye');
        icon.classList.toggle('fa-eye-slash');
    });

    // Login
    loginForm.addEventListener('submit', async function(event) {
        event.preventDefault();

        if (!emailInput.value || !passwordInput.value) {
            showError('Por favor, preencha todos os campos.');
            return;
        }

        setLoading(true);
        hideError();

        try {
            const response = await fetch(`${CONFIG.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'apikey': CONFIG.SUPABASE_ANON_KEY
                },
                body: JSON.stringify({
                    email: emailInput.value.trim(),
                    password: passwordInput.value
                })
            });

            const data = await response.json();

            if (response.ok && data.access_token) {
                const userRole = data.user?.app_metadata?.role || data.user?.role;

                if (userRole !== 'admin') {
                    showError('Acesso negado. Esta área é restrita a administradores.');
                    setLoading(false);
                    return;
                }

                Auth.setToken(data.access_token, rememberCheckbox.checked);
                window.location.href = 'dashboard.html';
            } else {
                showError(data.msg || data.error_description || 'Credenciais inválidas.');
            }
        } catch (error) {
            console.error('Erro ao fazer login:', error);
            showError('Erro de conexão. Verifique sua internet e tente novamente.');
        } finally {
            setLoading(false);
        }
    });

    function showError(message) {
        errorMessage.querySelector('span').textContent = message;
        errorMessage.classList.remove('hidden');
    }

    function hideError() {
        errorMessage.classList.add('hidden');
    }

    function setLoading(isLoading) {
        if (isLoading) {
            submitBtn.disabled = true;
            submitBtn.querySelector('.btn-text').textContent = 'Entrando...';
            submitBtn.querySelector('i').className = 'fas fa-spinner fa-spin';
        } else {
            submitBtn.disabled = false;
            submitBtn.querySelector('.btn-text').textContent = 'Entrar';
            submitBtn.querySelector('i').className = 'fas fa-arrow-right';
        }
    }

    emailInput.addEventListener('input', hideError);
    passwordInput.addEventListener('input', hideError);
});
