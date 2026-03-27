document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("cadastroForm");
    const btnBuscarCep = document.getElementById("btn-buscar-cep");
    const submitBtn = form.querySelector('button[type="submit"]');

    // --- FUNÇÃO BUSCAR CEP ---
    async function buscarCep() {
        const cepInput = document.getElementById("person-cep");
        const cepValue = cepInput.value.replace(/\D/g, "");

        if (cepValue.length !== 8) {
            alert("Digite um CEP com 8 números.");
            return;
        }

        btnBuscarCep.textContent = "⌛...";
        btnBuscarCep.disabled = true;

        try {
            const response = await fetch(`https://viacep.com.br/ws/${cepValue}/json/`);
            const data = await response.json();

            if (data.erro) {
                alert("CEP não encontrado.");
            } else {
                // Mapeamento seguro de IDs -> Dados da API
                const campos = {
                    "person-street": data.logradouro,
                    "street-burgh": data.bairro,
                    "street-city": data.localidade,
                    "uf-state": data.uf,
                    "person-state": data.localidade // Fallback para nome do estado
                };

                // Só preenche se o campo existir no HTML, evitando o erro de 'null'
                Object.keys(campos).forEach(id => {
                    const el = document.getElementById(id);
                    if (el) el.value = campos[id] || "";
                });

                document.getElementById("street-number")?.focus();
            }
        } catch (error) {
            console.error("Erro na busca de CEP:", error);
            alert("Erro ao consultar serviço de CEP.");
        } finally {
            btnBuscarCep.textContent = "🔍 Buscar";
            btnBuscarCep.disabled = false;
        }
    }

    btnBuscarCep.addEventListener("click", buscarCep);

    // --- ENVIO DO FORMULÁRIO ---
    form.addEventListener("submit", async function (event) {
        event.preventDefault();

          // ===== BLOQUEIO PROFISSIONAL =====
        // 1. Desabilita o botão
        submitBtn.disabled = true;
        
        // 2. Muda o texto e adiciona spinner
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processando...';
        
        // 3. Adiciona classe de loading (opcional, para estilização)
        submitBtn.classList.add('btn-loading');
        // ==================================


        const selectedThemes = [];
        const themeCheckboxes = document.querySelectorAll('input[name="themes"]:checked');
        themeCheckboxes.forEach((cb) => selectedThemes.push(cb.value));

        const payload = {
            full_name: document.getElementById("person_full_name").value,
            email: document.getElementById("person_email").value,
            birth_date: document.getElementById("person_date").value,
            phone: document.getElementById("person-phone").value,
            consent: document.getElementById("themes-consent").checked,
            themes: selectedThemes,
            address: {
                cep: document.getElementById("person-cep").value,
                street: document.getElementById("person-street").value,
                number: document.getElementById("street-number").value,
                burgh: document.getElementById("street-burgh").value,
                city: document.getElementById("street-city").value,
                state_name: document.getElementById("person-state").value,
                state_uf: document.getElementById("uf-state").value,
                complement: document.getElementById("street-complement").value
            }
        };

        try {
            const response = await fetch("https://crm-back-bm9v.onrender.com/person/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const result = await response.json();

            if (response.ok) {
                alert("Cadastro realizado com sucesso 🚀");
                form.reset();
                window.location.href = "https://chat.whatsapp.com/HFrd79nQFG7HeQbLchvehW?mode=gi_t";
            } else {
                alert("Erro: " + (result.detail || "Falha no cadastro"));
                // ===== REATIVA O BOTÃO EM CASO DE ERRO =====
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
                submitBtn.classList.remove('btn-loading');
            }
        } catch (error) {
            console.error("Erro de conexão:", error);
            alert("Erro ao conectar com o servidor.");
            // ===== REATIVA O BOTÃO EM CASO DE ERRO =====
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalText;
            submitBtn.classList.remove('btn-loading');
        }
    });
});


