// 1. CONFIGURAÇÕES: Endereço do seu servidor FastAPI
const API_BASE_URL = 'https://back-claudinho.onrender.com';
const ENDPOINT_LIST = '/person/list';

// 2. MAPEAMENTO DO DOM: Conectando o JS aos IDs do seu HTML
const elements = {
    filterName: document.getElementById('filter-name'),
    filterEmail: document.getElementById('filter-email'),
    filterTheme: document.getElementById('filter-theme'),
    filterPhone: document.getElementById('filter-phone'),
    filterCep: document.getElementById('filter-cep'),
    filterCity: document.getElementById('filter-city'),
    btnSearch: document.getElementById('btn-search'),
    btnClear: document.getElementById('btn-clear'),
    btnExport: document.getElementById('btn-export'),
    btnLogout: document.getElementById('logout-btn'),
    tableBody: document.getElementById('table-body'),
    recordCount: document.getElementById('record-count'),
    loading: document.getElementById('loading'),
    personsTable: document.getElementById('persons-table')
};

// Variável para guardar os dados da última busca (usada na exportação)
let currentData = [];

// 3. INICIALIZAÇÃO: Executa assim que a página carrega
document.addEventListener('DOMContentLoaded', () => {
    // Verifica autenticação antes de carregar dados
    if (!checkAuthentication()) {
        return;
    }
    
    // Configura os cliques dos botões
    elements.btnSearch.addEventListener('click', loadData);
    elements.btnClear.addEventListener('click', handleClear);
    elements.btnExport.addEventListener('click', handleExport);
    elements.btnLogout.addEventListener('click', handleLogout);
    
    // Carrega os dados iniciais
    loadData();
});

// Função para verificar autenticação
function checkAuthentication() {
    const token = localStorage.getItem('admin_token') || sessionStorage.getItem('admin_token');
    
    if (!token) {
        // Redireciona para login se não houver token
        alert('Sessão expirada. Por favor, faça login novamente.');
        window.location.href = '/frontend/html/login.html';
        return false;
    }
    
    // Armazena o token para uso nas requisições
    window.adminToken = token;
    return true;
}

// Função de logout
function handleLogout() {
    if (confirm('Tem certeza que deseja sair?')) {
        localStorage.removeItem('admin_token');
        sessionStorage.removeItem('admin_token');
        window.location.href = '/frontend/html/login.html';
    }
}

// 4. CONSTRUÇÃO DA URL: Monta a rota com filtros (ex: ?full_name=Luiz)
function buildUrlWithParams() {
    const params = new URLSearchParams();
    
    if (elements.filterName.value) params.append('full_name', elements.filterName.value.trim());
    if (elements.filterEmail.value) params.append('email', elements.filterEmail.value.trim());
    if (elements.filterTheme.value) params.append('themes', elements.filterTheme.value.trim());
    if (elements.filterPhone.value) params.append('phone', elements.filterPhone.value.trim());
    if (elements.filterCep.value) params.append('cep', elements.filterCep.value.trim());
    if (elements.filterCity.value) params.append('city', elements.filterCity.value.trim());

    
    const queryString = params.toString();
    return `${API_BASE_URL}${ENDPOINT_LIST}${queryString ? '?' + queryString : ''}`;
}

// 5. BUSCA DE DADOS (FETCH): Conversa com o Python
async function loadData() {
    // Verifica autenticação antes de cada requisição
    if (!checkAuthentication()) {
        return;
    }
    
    // Mostra o feedback visual de carregamento
    elements.loading.classList.remove('hidden');
    
    try {
        const response = await fetch(buildUrlWithParams(), {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${window.adminToken}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (response.status === 401) {
            // Token inválido ou expirado
            localStorage.removeItem('admin_token');
            sessionStorage.removeItem('admin_token');
            alert('Sessão inválida. Por favor, faça login novamente.');
            window.location.href = '/frontend/html/login.html';
            return;
        }
        
        if (!response.ok) throw new Error('Erro ao buscar dados do servidor');

        const data = await response.json();
        currentData = data; // Salva para o Excel não precisar buscar de novo
        
        renderTable(data);
    } catch (error) {
        console.error("Erro no Fetch:", error);
        alert("Erro ao conectar com o backend. Verifique se o FastAPI está rodando.");
    } finally {
        // Esconde o carregando
        elements.loading.classList.add('hidden');
    }
}

// 6. RENDERIZAÇÃO DA TABELA: Onde montamos as 12 colunas corrigidas
function renderTable(data) {
    elements.tableBody.innerHTML = ''; // Limpa a tabela atual
    elements.recordCount.textContent = `${data.length} registros encontrados`;
    
    data.forEach(person => {
        // Extração segura do objeto de endereço (evita erros se for null)
        const addr = person.address || {};
        
        // Transformação da lista de temas em pequenas tags (badges)
        const themesHTML = (person.themes && person.themes.length > 0)
            ? person.themes.map(t => `<span class="badge">${t.code}</span>`).join(' ')
            : '-';
        
        // MONTAGEM DA LINHA: Note que cada <td> corresponde a um <th> do seu HTML
        const row = `
            <tr>
                <td><strong>${person.full_name || '-'}</strong></td>
                <td>${person.email || '-'}</td>
                <td>${person.birth_date || '-'}</td>
                <td>${person.phone || '-'}</td>
                <td>${person.consent ? 'Sim' : 'Não'}</td>
                <td>${addr.cep || '-'}</td>
                <td>${addr.street || '-'}</td>
                <td>${addr.number || '-'}</td>
                <td>${addr.burgh || '-'}</td>
                <td>${addr.city || '-'}</td>
                <td>${addr.state_uf || '-'}</td>
                <td>${themesHTML}</td>
            </tr>
        `;
        
        // Insere a nova linha no corpo da tabela
        elements.tableBody.innerHTML += row;
    });
}

// 7. LIMPAR FILTROS: Reseta o formulário e recarrega tudo
function handleClear() {
    elements.filterName.value = '';
    elements.filterEmail.value = '';
    elements.filterTheme.value = '';
    elements.filterPhone.value = '';
    elements.filterCep.value = '';
    elements.filterCity.value = '';
    loadData();
}

// 8. EXPORTAÇÃO EXCEL: Usa a biblioteca SheetJS para gerar o arquivo
function handleExport() {
    if (currentData.length === 0) return alert("Não há dados para exportar.");

    // Mapeia o JSON complexo para uma estrutura plana (Excel não aceita objetos aninhados)
    const exportFormat = currentData.map(p => ({
        "Nome Completo": p.full_name,
        "E-mail": p.email,
        "Nascimento": p.birth_date,
        "Telefone": p.phone,
        "Consentimento": p.consent ? "Sim" : "Não",
        "CEP": p.address?.cep,
        "Rua": p.address?.street,
        "Número": p.address?.number,
        "Bairro": p.address?.burgh,
        "Cidade": p.address?.city,
        "UF": p.address?.state_uf,
        "Temas": p.themes.map(t => t.code).join(', ')
    }));

    // Cria a planilha e inicia o download
    const ws = XLSX.utils.json_to_sheet(exportFormat);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, "Lista de Pessoas");
    XLSX.writeFile(wb, `CRM_Export_${new Date().getTime()}.xlsx`);
}
