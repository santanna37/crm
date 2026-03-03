document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("cadastroForm");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const selectedThemes = [];
        const themeCheckboxes = document.querySelectorAll('input[name="themes"]:checked');

        themeCheckboxes.forEach((checkbox) => {
            selectedThemes.push(checkbox.value);
        });

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
            const response = await fetch("http://localhost:8000/person/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            });

            const result = await response.json();

            // ✅ Só mostra sucesso se for 200 ou 201
            if (response.ok) {
                alert("Cadastro realizado com sucesso 🚀");
                console.log("Sucesso:", result);

                // limpa o formulário
                form.reset();

            } else {
                // mostra erro real do backend
                alert("Erro: " + result.error);
                console.error("Erro do backend:", result);
            }

        } catch (error) {
            console.error("Erro de conexão:", error);
            alert("Erro ao conectar com o servidor");
        }
    });

});
