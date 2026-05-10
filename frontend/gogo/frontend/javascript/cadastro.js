/* ============================================================
   CADASTRO.JS - Formulário de Apoiadores
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('cadastroForm');
    const btnBuscarCep = document.getElementById('btn-buscar-cep');
    const submitBtn = document.getElementById('submit-btn');
    const cepHelp = document.getElementById('cep-help');

    // --- BUSCAR CEP ---
    btnBuscarCep.addEventListener('click', async function () {
        const cepInput = document.getElementById('person-cep');
        const cepValue = cepInput.value;

        btnBuscarCep.disabled = true;
        btnBuscarCep.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Buscando...';
        cepHelp.classList.remove('hidden');

        try {
            const data = await CEP.buscar(cepValue);

            const campos = {
                'person-street': data.logradouro,
                'street-burgh': data.bairro,
                'street-city': data.localidade,
                'uf-state': data.uf,
                'person-state': data.localidade
            };

            Object.keys(campos).forEach(id => {
                const el = document.getElementById(id);
                if (el) el.value = campos[id] || '';
            });

            document.getElementById('street-number')?.focus();

        } catch (error) {
            alert(error.message);
        } finally {
            btnBuscarCep.disabled = false;
            btnBuscarCep.innerHTML = '<i class="fas fa-search"></i> Buscar';
            cepHelp.classList.add('hidden');
        }
    });

    // --- ENVIO DO FORMULÁRIO ---
    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        // Bloqueia botão
        const originalHTML = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processando...';

        const selectedThemes = [];
        document.querySelectorAll('input[name="themes"]:checked').forEach(cb => {
            selectedThemes.push(cb.value);
        });

        const payload = {
            full_name: document.getElementById('person_full_name').value,
            email: document.getElementById('person_email').value,
            birth_date: document.getElementById('person_date').value,
            phone: document.getElementById('person-phone').value,
            consent: document.getElementById('themes-consent').checked,
            themes: selectedThemes,
            address: {
                cep: document.getElementById('person-cep').value,
                street: document.getElementById('person-street').value,
                number: document.getElementById('street-number').value,
                burgh: document.getElementById('street-burgh').value,
                city: document.getElementById('street-city').value,
                state_name: document.getElementById('person-state').value,
                state_uf: document.getElementById('uf-state').value,
                complement: document.getElementById('street-complement').value
            }
        };

        try {
            const result = await API.post('/person/', payload);

            alert('Cadastro realizado com sucesso! 🚀');
            form.reset();
            window.location.href = 'https://chat.whatsapp.com/HFrd79nQFG7HeQbLchvehW';

        } catch (error) {
            alert('Erro: ' + error.message);
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalHTML;
        }
    });
});
