// ===== DADOS DOS EVENTOS =====
const meses = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
];

const semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'];

const eventos = {
    0: [ // Janeiro
        { dia: 15, tipo: 'Audiência', titulo: 'Audiência Pública - Orçamento 2026', hora: '14h00', desc: 'Discussão do orçamento municipal com participação da comunidade na Câmara.', seed: 'audience-jan' },
        { dia: 22, tipo: 'Reunião', titulo: 'Reunião com Lideranças Comunitárias', hora: '10h00', desc: 'Encontro para alinhar demandas dos bairros e planejar ações conjuntas.', seed: 'meeting-jan' },
        { dia: 28, tipo: 'Evento', titulo: 'Fórum da Cidadania', hora: '09h00', desc: 'Evento anual de debate sobre políticas públicas e direitos sociais.', seed: 'forum-jan' }
    ],
    1: [ // Fevereiro
        { dia: 05, tipo: 'Visita', titulo: 'Visita Técnica à Zona Leste', hora: '08h30', desc: 'Inspeção das obras de infraestrutura e escuta das demandas locais.', seed: 'visit-feb' },
        { dia: 12, tipo: 'Audiência', titulo: 'Audiência sobre Saúde Pública', hora: '14h00', desc: 'Debate sobre melhorias nos postos de saúde e acesso à medicamentos.', seed: 'health-feb' },
        { dia: 20, tipo: 'Reunião', titulo: 'Conselho Gestor do Bairro Novo', hora: '19h00', desc: 'Reunião ordinária do conselho para avaliação de projetos locais.', seed: 'council-feb' }
    ],
    2: [ // Março
        { dia: 08, tipo: 'Evento', titulo: 'Encontro Mulheres da Nossa Gente', hora: '09h00', desc: 'Celebração do Dia Internacional da Mulher com debates e homenagens.', seed: 'women-mar' },
        { dia: 15, tipo: 'Audiência', titulo: 'Audiência - Mobilidade Urbana', hora: '14h00', desc: 'Discussão sobre transporte público, ciclovias e acessibilidade.', seed: 'mobility-mar' },
        { dia: 22, tipo: 'Visita', titulo: 'Visita ao Centro Cultural', hora: '10h00', desc: 'Vistoria das instalações e planejamento de atividades culturais.', seed: 'culture-mar' },
        { dia: 29, tipo: 'Reunião', titulo: 'Reunião Geral de Gabinete', hora: '09h00', desc: 'Alinhamento estratégico da equipe para o segundo trimestre.', seed: 'office-mar' }
    ],
    3: [ // Abril
        { dia: 02, tipo: 'Evento', titulo: 'Palestra Direitos do Cidadão', hora: '19h00', desc: 'Palestra aberta sobre como exercer a cidadania e participar da política local.', seed: 'rights-apr' },
        { dia: 10, tipo: 'Audiência', titulo: 'Audiência - Educação Infantil', hora: '14h00', desc: 'Debate sobre vagas, merenda escolar e condições das creches municipais.', seed: 'edu-apr' },
        { dia: 18, tipo: 'Visita', titulo: 'Visita à Feira Livre do Centro', hora: '07h00', desc: 'Acompanhamento das demandas dos feirantes e regularização dos espaços.', seed: 'fair-apr' }
    ],
    4: [ // Maio
        { dia: 01, tipo: 'Evento', titulo: 'Café da Manhã com Trabalhadores', hora: '08h00', desc: 'Confraternização do Dia do Trabalho com lideranças sindicais.', seed: 'labor-may' },
        { dia: 09, tipo: 'Audiência', titulo: 'Audiência Pública - Meio Ambiente', hora: '14h00', desc: 'Discussão sobre áreas verdes, coleta seletiva e sustentabilidade.', seed: 'green-may' },
        { dia: 15, tipo: 'Reunião', titulo: 'Reunião com Secretários', hora: '10h00', desc: 'Reunião mensal de articulação entre o gabinete e as secretarias.', seed: 'sec-may' },
        { dia: 23, tipo: 'Evento', titulo: 'Dia do Ouvidor - Ação na Praça', hora: '09h00', desc: 'Atendimento itinerante para receber demandas diretamente da população.', seed: 'day-may' }
    ],
    5: [ // Junho
        { dia: 05, tipo: 'Visita', titulo: 'Visita à Escola Municipal Paulo Freire', hora: '09h00', desc: 'Acompanhamento do início do segundo semestre letivo.', seed: 'school-jun' },
        { dia: 12, tipo: 'Audiência', titulo: 'Audiência - Habitação e Moradia', hora: '14h00', desc: 'Debate sobre regularização fundiária e programas habitacionais.', seed: 'home-jun' },
        { dia: 20, tipo: 'Evento', titulo: 'Encontro de Lideranças Juvenis', hora: '14h00', desc: 'Workshop de formação política para jovens lideranças da cidade.', seed: 'youth-jun' },
        { dia: 26, tipo: 'Reunião', titulo: 'Reunião com Comissão de Obras', hora: '10h00', desc: 'Acompanhamento do cronograma de obras prioritárias.', seed: 'works-jun' }
    ],
    6: [ // Julho
        { dia: 03, tipo: 'Evento', titulo: 'Festa Julina Comunitária', hora: '18h00', desc: 'Arraiá beneficente com apresentações culturais e gastronomia local.', seed: 'fest-jul' },
        { dia: 08, tipo: 'Audiência', titulo: 'Audiência - Segurança Pública', hora: '14h00', desc: 'Debate sobre iluminação, patrulhamento e prevenção à violência.', seed: 'safe-jul' },
        { dia: 15, tipo: 'Visita', titulo: 'Visita ao Distrito Industrial', hora: '09h00', desc: 'Diálogo com empresários sobre incentivos e geração de empregos.', seed: 'ind-jul' },
        { dia: 22, tipo: 'Reunião', titulo: 'Reunião - Conselho do Idoso', hora: '14h00', desc: 'Reunião ordinária com foco em políticas para a terceira idade.', seed: 'elder-jul' }
    ],
    7: [ // Agosto
        { dia: 05, tipo: 'Evento', titulo: 'Seminário Participação Popular', hora: '08h30', desc: 'Seminário de dois dias sobre orçamento participativo e controle social.', seed: 'semi-aug' },
        { dia: 12, tipo: 'Audiência', titulo: 'Audiência - Esporte e Lazer', hora: '14h00', desc: 'Discussão sobre reforma de quadras e programas esportivos gratuitos.', seed: 'sport-aug' },
        { dia: 19, tipo: 'Visita', titulo: 'Visita ao Centro de Especialidades', hora: '09h00', desc: 'Vistoria das instalações e fluxo de atendimento médico especializado.', seed: 'med-aug' },
        { dia: 27, tipo: 'Reunião', titulo: 'Reunião com Cooperativas', hora: '10h00', desc: 'Articulação de apoio à economia solidária e cooperativas locais.', seed: 'coop-aug' }
    ],
    8: [ // Setembro
        { dia: 07, tipo: 'Evento', titulo: 'Desfile Cívico Independência', hora: '08h00', desc: 'Participação nas celebrações do 7 de Setembro com a comunidade.', seed: 'sep7-set' },
        { dia: 15, tipo: 'Audiência', titulo: 'Audiência - Cultura e Patrimônio', hora: '14h00', desc: 'Debate sobre preservação do patrimônio histórico e incentivo à cultura.', seed: 'cult-set' },
        { dia: 22, tipo: 'Visita', titulo: 'Visita ao Bairro Santa Clara', hora: '10h00', desc: 'Inspeção de demandas de pavimentação e drenagem na região.', seed: 'clara-set' },
        { dia: 28, tipo: 'Reunião', titulo: 'Reunião Geral de Balanço', hora: '14h00', desc: 'Avaliação trimestral das ações e planejamento para o último trimestre.', seed: 'balance-set' }
    ],
    9: [ // Outubro
        { dia: 05, tipo: 'Evento', titulo: 'Feira de Empreendedorismo Local', hora: '09h00', desc: 'Exposição de produtos de pequenos empreendedores com apoio do gabinete.', seed: 'ent-oct' },
        { dia: 12, tipo: 'Audiência', titulo: 'Audiência - Criança e Adolescente', hora: '14h00', desc: 'Debate sobre proteção infantil, lazer e educação integral.', seed: 'child-oct' },
        { dia: 20, tipo: 'Visita', titulo: 'Visita ao Horto Municipal', hora: '08h00', desc: 'Acompanhamento do projeto de hortas comunitárias e educação ambiental.', seed: 'hort-oct' },
        { dia: 25, tipo: 'Reunião', titulo: 'Reunião com Agentes de Saúde', hora: '10h00', desc: 'Diálogo com agentes comunitários sobre demandas dos territórios.', seed: 'agent-oct' }
    ],
    10: [ // Novembro
        { dia: 15, tipo: 'Evento', titulo: 'Celebração Proclamação da República', hora: '09h00', desc: 'Evento cívico com palestras e homenagens a cidadãos notáveis.', seed: 'rep-nov' },
        { dia: 20, tipo: 'Evento', titulo: 'Dia da Consciência Negra', hora: '14h00', desc: 'Programação especial com debates, arte e celebração da cultura afro.', seed: 'black-nov' },
        { dia: 25, tipo: 'Audiência', titulo: 'Audiência - Combate à Violência', hora: '14h00', desc: 'Debate sobre políticas de enfrentamento à violência doméstica.', seed: 'viol-nov' }
    ],
    11: [ // Dezembro
        { dia: 05, tipo: 'Evento', titulo: 'Natal Solidário Comunitário', hora: '17h00', desc: 'Entrega de cestas e brinquedos com apresentação da banda comunitária.', seed: 'xmas-dec' },
        { dia: 10, tipo: 'Audiência', titulo: 'Audiência - Avaliação Anual', hora: '14h00', desc: 'Balanço de 2026 e coleta de propostas para o próximo ano.', seed: 'year-dec' },
        { dia: 15, tipo: 'Reunião', titulo: 'Confraternização da Equipe', hora: '12h00', desc: 'Celebração de fim de ano com toda a equipe do gabinete.', seed: 'party-dec' },
        { dia: 20, tipo: 'Evento', titulo: 'Reunião de Agradecimento ao Povo', hora: '19h00', desc: 'Encontro de gratidão com a comunidade para fechar o ano.', seed: 'thanks-dec' }
    ]
};

// ===== ELEMENTOS DO DOM =====
const monthTitle = document.getElementById('monthTitle');
const eventsList = document.getElementById('eventsList');
const emptyState = document.getElementById('emptyState');
const prevBtn = document.getElementById('prevMonth');
const nextBtn = document.getElementById('nextMonth');

let currentMonth = new Date().getMonth(); // Começa no mês atual
const currentYear = 2026;

// ===== FUNÇÕES =====

function getWeekday(dia, mes) {
    const d = new Date(currentYear, mes, dia);
    return semana[d.getDay()];
}

function getImageUrl(seed) {
    return `https://picsum.photos/seed/${seed}/900/400`;
}

function renderEventos(mesIndex) {
    const lista = eventos[mesIndex] || [];

    // Atualiza título
    monthTitle.textContent = `${meses[mesIndex]} ${currentYear}`;

    // Limpa lista
    eventsList.innerHTML = '';

    if (lista.length === 0) {
        eventsList.classList.add('hidden');
        emptyState.classList.remove('hidden');
        return;
    }

    eventsList.classList.remove('hidden');
    emptyState.classList.add('hidden');

    lista.forEach((ev, index) => {
        const card = document.createElement('article');
        card.className = 'event-card';
        card.style.animationDelay = `${index * 0.08}s`;

        const diaSemana = getWeekday(ev.dia, mesIndex);
        const imgUrl = getImageUrl(ev.seed);

        card.innerHTML = `
            <div class="event-date-panel">
                <span class="event-day">${ev.dia}</span>
                <span class="event-weekday">${diaSemana}</span>
            </div>
            <div class="event-visual">
                <img src="${imgUrl}" alt="${ev.titulo}" loading="lazy">
                <span class="event-type">${ev.tipo}</span>
                <div class="event-info">
                    <h3 class="event-title">${ev.titulo}</h3>
                    <span class="event-time">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        ${ev.hora}
                    </span>
                    <p class="event-desc">${ev.desc}</p>
                </div>
            </div>
        `;

        eventsList.appendChild(card);
    });
}

function changeMonth(delta) {
    const newMonth = currentMonth + delta;
    if (newMonth < 0 || newMonth > 11) return;
    currentMonth = newMonth;
    renderEventos(currentMonth);
}

// ===== EVENT LISTENERS =====
prevBtn.addEventListener('click', () => changeMonth(-1));
nextBtn.addEventListener('click', () => changeMonth(1));

// Inicializa
renderEventos(currentMonth);
