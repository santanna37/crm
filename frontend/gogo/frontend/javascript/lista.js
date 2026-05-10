/* ============================================================
   LISTA.JS - Gestão de Apoiadores
   ============================================================ */

let currentData = [];

document.addEventListener('DOMContentLoaded', function() {
    if (!Auth.requireAuth()) return;
    Auth.setupLogoutButton();

    // Event listeners
    document.getElementById('btn-search').addEventListener('click', loadData);
    document.getElementById('btn-clear').addEventListener('click', handleClear);
    document.getElementById('btn-export').addEventListener('click', handleExport);

    // Filtros em tempo real
    ['filter-name', 'filter-email', 'filter-theme', 'filter-phone', 'filter-cep', 'filter-city'].forEach(id => {
        document.getElementById(id).addEventListener('input', Utils.debounce(loadData, 500));
    });

    // Carrega dados iniciais
    loadData();
});

function buildUrlWithParams() {
    const params = new URLSearchParams();

    const fields = {
        'filter-name': 'full_name',
        'filter-email': 'email',
        'filter-theme': 'themes',
        'filter-phone': 'phone',
        'filter-cep': 'cep',
        'filter-city': 'city'
    };

    Object.entries(fields).forEach(([inputId, paramName]) => {
        const value = document.getElementById(inputId).value.trim();
        if (value) params.append(paramName, value);
    });

    const queryString = params.toString();
    return `/person/list${queryString ? '?' + queryString : ''}`;
}

async function loadData() {
    Utils.showLoading('loading');
    document.getElementById('empty-state').classList.add('hidden');

    try {
        const data = await API.get(buildUrlWithParams());
        if (!data) return;

        currentData = data;
        renderTable(data);
    } catch (error) {
        console.error('Erro ao carregar dados:', error);
        Utils.showAlert('Erro ao carregar dados da lista', 'error');
    } finally {
        Utils.hideLoading('loading');
    }
}

function renderTable(data) {
    const tbody = document.getElementById('table-body');
    tbody.innerHTML = '';

    document.getElementById('record-count').textContent = `${data.length} registros encontrados`;

    if (data.length === 0) {
        document.getElementById('empty-state').classList.remove('hidden');
        return;
    }

    data.forEach(person => {
        const addr = person.address || {};
        const themesHTML = (person.themes && person.themes.length > 0)
            ? person.themes.map(t => `<span class="badge badge-primary">${t.code || t}</span>`).join(' ')
            : '-';

        const row = document.createElement('tr');
        row.innerHTML = `
            <td><strong>${person.full_name || '-'}</strong></td>
            <td>${person.email || '-'}</td>
            <td>${Utils.formatDate(person.birth_date)}</td>
            <td>${Utils.formatPhone(person.phone)}</td>
            <td>${person.consent ? '<span class="badge badge-success">Sim</span>' : '<span class="badge badge-danger">Não</span>'}</td>
            <td>${Utils.formatCEP(addr.cep)}</td>
            <td>${addr.street || '-'}</td>
            <td>${addr.number || '-'}</td>
            <td>${addr.burgh || '-'}</td>
            <td>${addr.city || '-'}</td>
            <td>${addr.state_uf || '-'}</td>
            <td>${themesHTML}</td>
        `;
        tbody.appendChild(row);
    });
}

function handleClear() {
    ['filter-name', 'filter-email', 'filter-theme', 'filter-phone', 'filter-cep', 'filter-city'].forEach(id => {
        document.getElementById(id).value = '';
    });
    loadData();
}

function handleExport() {
    if (currentData.length === 0) {
        alert('Não há dados para exportar.');
        return;
    }

    const exportFormat = currentData.map(p => ({
        'Nome Completo': p.full_name,
        'E-mail': p.email,
        'Nascimento': p.birth_date,
        'Telefone': p.phone,
        'Consentimento': p.consent ? 'Sim' : 'Não',
        'CEP': p.address?.cep,
        'Rua': p.address?.street,
        'Número': p.address?.number,
        'Bairro': p.address?.burgh,
        'Cidade': p.address?.city,
        'UF': p.address?.state_uf,
        'Temas': (p.themes || []).map(t => t.code || t).join(', ')
    }));

    const ws = XLSX.utils.json_to_sheet(exportFormat);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Lista de Pessoas');
    XLSX.writeFile(wb, `CRM_Export_${new Date().getTime()}.xlsx`);
}
