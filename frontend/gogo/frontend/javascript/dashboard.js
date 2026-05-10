/* ============================================================
   DASHBOARD.JS - Painel Administrativo
   ============================================================ */

document.addEventListener('DOMContentLoaded', async function() {
    if (!Auth.requireAuth()) return;
    Auth.setupLogoutButton();

    try {
        // Carrega dados
        const data = await API.get('/person/list');
        if (!data) return;

        // Métricas
        updateMetrics(data);

        // Gráficos
        renderCharts(data);

        // Tabela recente
        renderRecentTable(data);

    } catch (error) {
        console.error('Erro ao carregar dashboard:', error);
        Utils.showAlert('Erro ao carregar dados do dashboard', 'error');
    }
});

function updateMetrics(data) {
    document.getElementById('total-users').textContent = data.length;

    const consentCount = data.filter(p => p.consent).length;
    const consentRate = data.length > 0 ? Math.round((consentCount / data.length) * 100) : 0;
    document.getElementById('consent-rate').textContent = consentRate + '%';

    const states = new Set(data.map(p => p.address?.state_uf).filter(Boolean));
    document.getElementById('total-states').textContent = states.size;

    const ages = data.map(p => calculateAge(p.birth_date)).filter(a => a > 0);
    const avgAge = ages.length > 0 ? Math.round(ages.reduce((a, b) => a + b, 0) / ages.length) : 0;
    document.getElementById('avg-age').textContent = avgAge;
}

function calculateAge(birthDate) {
    if (!birthDate) return 0;
    const birth = new Date(birthDate);
    const today = new Date();
    let age = today.getFullYear() - birth.getFullYear();
    const monthDiff = today.getMonth() - birth.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birth.getDate())) {
        age--;
    }
    return age;
}

function renderCharts(data) {
    // Temas de interesse
    const themesCount = {};
    data.forEach(p => {
        (p.themes || []).forEach(t => {
            const code = t.code || t;
            themesCount[code] = (themesCount[code] || 0) + 1;
        });
    });

    new Chart(document.getElementById('themesChart'), {
        type: 'doughnut',
        data: {
            labels: Object.keys(themesCount),
            datasets: [{
                data: Object.values(themesCount),
                backgroundColor: ['#1d4ed8', '#3b82f6', '#60a5fa', '#93c5fd', '#bfdbfe', '#dbeafe']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom' } }
        }
    });

    // Estados
    const statesCount = {};
    data.forEach(p => {
        const uf = p.address?.state_uf;
        if (uf) statesCount[uf] = (statesCount[uf] || 0) + 1;
    });

    new Chart(document.getElementById('statesChart'), {
        type: 'bar',
        data: {
            labels: Object.keys(statesCount),
            datasets: [{
                label: 'Apoiadores',
                data: Object.values(statesCount),
                backgroundColor: '#1d4ed8',
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } }
        }
    });

    // Faixa etária
    const ageRanges = { '18-25': 0, '26-35': 0, '36-45': 0, '46-55': 0, '56-65': 0, '65+': 0 };
    data.forEach(p => {
        const age = calculateAge(p.birth_date);
        if (age >= 18 && age <= 25) ageRanges['18-25']++;
        else if (age <= 35) ageRanges['26-35']++;
        else if (age <= 45) ageRanges['36-45']++;
        else if (age <= 55) ageRanges['46-55']++;
        else if (age <= 65) ageRanges['56-65']++;
        else if (age > 65) ageRanges['65+']++;
    });

    new Chart(document.getElementById('ageChart'), {
        type: 'line',
        data: {
            labels: Object.keys(ageRanges),
            datasets: [{
                label: 'Apoiadores',
                data: Object.values(ageRanges),
                borderColor: '#1d4ed8',
                backgroundColor: 'rgba(29,78,216,0.1)',
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#1d4ed8',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } }
        }
    });
}

function renderRecentTable(data) {
    const tbody = document.getElementById('recent-body');
    const recent = data.slice(0, 5);

    tbody.innerHTML = recent.map(p => `
        <tr>
            <td><strong>${p.full_name || '-'}</strong></td>
            <td>${p.email || '-'}</td>
            <td>${p.address?.city || '-'}</td>
            <td>${(p.themes || []).map(t => `<span class="badge badge-primary">${t.code || t}</span>`).join(' ')}</td>
        </tr>
    `).join('');

    document.getElementById('recent-count').textContent = `mostrando ${recent.length} recentes`;
}
