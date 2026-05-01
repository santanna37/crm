
## ./frontend/css/styles_cadastro.css

```css
/* Importando as variáveis da lista */
:root {
    --primary-color: #f63b3b;
    --primary-hover: #eb3525;
    --secondary-color: #6b7280;
    --secondary-hover: #4b5563;
    --background-color: #f3f4f6;
    --card-background: #ffffff;
    --text-primary: #111827;
    --text-secondary: #6b7280;
    --border-color: #e5e7eb;
    --radius-lg: 12px;
    --radius-md: 8px;
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: var(--background-color);
    color: var(--text-primary);
    padding: 20px;
}

.container { max-width: 1000px; margin: 0 auto; }

/* Reutilizando Header da Lista */
.header {
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    color: white;
    padding: 20px 30px;
    border-radius: var(--radius-lg);
    margin-bottom: 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: var(--shadow-md);
}

/* ===== ALTERAÇÃO AQUI: Logo com ícone ===== */
.logo { 
    background: rgba(255, 255, 255, 0.2); 
    padding: 8px 16px; 
    border-radius: var(--radius-md); 
    font-weight: 700; 
    display: flex;
    align-items: center;
    gap: 10px;
}

.logo i {
    font-size: 1.3rem;
}
/* ===== FIM DA ALTERAÇÃO ===== */

/* Estilização do Card do Formulário */
.form-container {
    background: var(--card-background);
    padding: 40px;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    border: 1px solid var(--border-color);
    overflow: hidden;
}

.form-header { margin-bottom: 30px; border-bottom: 2px solid var(--background-color); padding-bottom: 20px; }
.form-header h2 { color: var(--primary-color); font-size: 1.8rem; }

.form-section { margin-bottom: 35px; }
.form-section h3 { 
    font-size: 1.2rem; 
    margin-bottom: 20px; 
    display: flex; 
    align-items: center; 
    gap: 10px;
    color: var(--secondary-hover);
}

.section-number {
    background: var(--primary-color);
    color: white;
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    font-size: 0.9rem;
}

/* Grid de Inputs - CORRIGIDO COM POSICIONAMENTO EXATO */
.form-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    align-items: start;
    width: 100%;
}

/* Classes de coluna para controle preciso */
.col-1 { grid-column: span 1; }
.col-2 { grid-column: span 2; }
.col-3 { grid-column: span 3; }
.col-4 { grid-column: span 4; }
.full-width { grid-column: 1 / -1; }
.grow-2 { grid-column: span 2; }

.form-group { 
    display: flex; 
    flex-direction: column; 
    gap: 8px;
    min-width: 0;
    overflow: hidden;
}

.form-group label { 
    font-size: 0.85rem; 
    font-weight: 600; 
    color: var(--text-secondary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

input[type="text"], input[type="email"], input[type="date"] {
    padding: 12px;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    font-size: 1rem;
    transition: 0.2s;
    height: 46px;
    width: 100%;
    min-width: 0;
}

input:focus { 
    outline: none; 
    border-color: var(--primary-color); 
    box-shadow: 0 0 0 3px rgba(246, 59, 59, 0.1); 
}

/* Grupo de CEP com Botão */
.input-with-button { 
    display: flex; 
    gap: 10px; 
    align-items: center;
    width: 100%;
    min-width: 0;
}

.input-with-button input { 
    flex: 1;
    min-width: 0;
    width: auto;
}

#btn-buscar-cep {
    height: 46px;
    padding: 0 15px;
    white-space: nowrap;
    flex-shrink: 0;
    margin: 0;
}

.btn {
    cursor: pointer;
    border: none;
    border-radius: var(--radius-md);
    font-weight: 600;
    transition: 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
}

.btn-primary { background-color: var(--primary-color); color: white; }
.btn-primary:hover { background-color: var(--primary-hover); transform: translateY(-1px); }
.btn-secondary { 
    background-color: var(--secondary-color); 
    color: white; 
    padding: 0 15px; 
}

/* Ajuste do campo de Rua */
#person-street {
    width: 100%;
}

/* Grid de Checkboxes */
.themes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 12px;
}

.checkbox-card {
    border: 1px solid var(--border-color);
    padding: 12px;
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    transition: 0.2s;
    min-width: 0;
}

.checkbox-card:hover { border-color: var(--primary-color); background: #fff5f5; }
.checkbox-card input { accent-color: var(--primary-color); width: 18px; height: 18px; flex-shrink: 0; }
.checkbox-card span {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.form-footer { 
    margin-top: 40px; 
    padding-top: 20px; 
    border-top: 1px solid var(--border-color); 
    display: flex; 
    flex-direction: column; 
    align-items: center; 
    gap: 20px; 
}

.btn-large { width: 100%; max-width: 500px; padding: 18px; font-size: 1.1rem; }

.hidden { display: none; }

/* Helper do CEP */
#cep-help {
    font-size: 0.75rem;
    color: var(--text-secondary);
    margin-top: 4px;
}

#cep-help:not(.hidden) {
    display: block;
    color: var(--primary-color);
}

/* Responsividade */
@media (max-width: 768px) {
    .form-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    .col-1, .col-2, .col-3, .col-4, .grow-2, .full-width {
        grid-column: span 2;
    }
}

@media (max-width: 480px) {
    .form-grid {
        grid-template-columns: 1fr;
    }
    .col-1, .col-2, .col-3, .col-4, .grow-2, .full-width {
        grid-column: span 1;
    }
}

/* ===== ESTILO DO BOTÃO EM LOADING ===== */
.btn-loading {
    opacity: 0.8;
    cursor: not-allowed !important;
    transform: none !important;
}

.btn-loading:hover {
    transform: none !important;
    box-shadow: none !important;
}

/* Animação do spinner (se não tiver Font Awesome) */
@keyframes spin {
    to { transform: rotate(360deg); }
}

.fa-spin {
    animation: spin 1s linear infinite;
}
```

## ./frontend/css/styles_dash.css

```css
/* Variáveis CSS para cores e design system */
:root {
    --primary-color: #f63b3b;
    --primary-hover: #eb3525;
    --secondary-color: #6b7280;
    --secondary-hover: #4b5563;
    --success-color: #10b981;
    --success-hover: #059669;
    --danger-color: #ef4444;
    --background-color: #f3f4f6;
    --card-background: #ffffff;
    --text-primary: #111827;
    --text-secondary: #6b7280;
    --border-color: #e5e7eb;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --radius-sm: 6px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background-color: var(--background-color);
    color: var(--text-primary);
    line-height: 1.6;
}

/* Layout Principal com Sidebar */
.app-container {
    display: flex;
    min-height: 100vh;
}

/* Sidebar */
.sidebar {
    width: 260px;
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    color: white;
    display: flex;
    flex-direction: column;
    position: fixed;
    height: 100vh;
    left: 0;
    top: 0;
    z-index: 1000;
    box-shadow: var(--shadow-lg);
}

.sidebar-header {
    padding: var(--spacing-lg);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.sidebar-header .logo {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    font-size: 1.3rem;
    font-weight: 700;
    color: white;
}

.sidebar-header .logo i {
    font-size: 1.5rem;
}

.sidebar-nav {
    flex: 1;
    padding: var(--spacing-md) 0;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
    padding: var(--spacing-md) var(--spacing-lg);
    color: rgba(255, 255, 255, 0.9);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.2s;
    border-left: 3px solid transparent;
}

.nav-item:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
}

.nav-item.active {
    background: rgba(255, 255, 255, 0.15);
    color: white;
    border-left-color: white;
}

.nav-item i {
    font-size: 1.1rem;
    width: 20px;
    text-align: center;
}

.sidebar-footer {
    padding: var(--spacing-md) var(--spacing-lg);
    border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.btn-logout {
    width: 100%;
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    padding: var(--spacing-sm) var(--spacing-md);
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: var(--radius-md);
    color: white;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-logout:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-1px);
}

/* Main Content */
.main-content {
    flex: 1;
    margin-left: 260px;
    padding: var(--spacing-lg);
    background-color: var(--background-color);
}

/* Header */
.header {
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    color: white;
    padding: var(--spacing-lg) var(--spacing-xl);
    border-radius: var(--radius-lg);
    margin-bottom: var(--spacing-lg);
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: var(--shadow-lg);
}

.header-left {
    display: flex;
    align-items: center;
    gap: var(--spacing-lg);
}

.header-left .logo {
    font-size: 1.5rem;
    font-weight: 700;
    background: rgba(255, 255, 255, 0.2);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--radius-md);
}

.header-left h1 {
    font-size: 1.25rem;
    font-weight: 600;
}

.header-right {
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
}

.user-info {
    text-align: right;
}

.user-name {
    display: block;
    font-weight: 600;
    font-size: 0.95rem;
}

.user-role {
    display: block;
    font-size: 0.8rem;
    opacity: 0.9;
}

.user-avatar {
    width: 45px;
    height: 45px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    border: 2px solid rgba(255, 255, 255, 0.5);
}

/* Cards de Métricas */
.metrics-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
}

.metric-card {
    background: var(--card-background);
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    border: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
    transition: transform 0.2s;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

.metric-icon {
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.5rem;
}

.metric-content {
    flex: 1;
}

.metric-value {
    display: block;
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1;
}

.metric-label {
    display: block;
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin-top: var(--spacing-xs);
}

/* Gráficos */
.charts-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
}

.chart-card {
    background: var(--card-background);
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    border: 1px solid var(--border-color);
}

.chart-card.full-width {
    grid-column: 1 / -1;
}

.chart-header {
    margin-bottom: var(--spacing-md);
    padding-bottom: var(--spacing-md);
    border-bottom: 1px solid var(--border-color);
}

.chart-header h3 {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: var(--spacing-xs);
}

.chart-header p {
    font-size: 0.875rem;
    color: var(--text-secondary);
}

.chart-wrapper {
    position: relative;
    height: 300px;
}

.chart-wrapper canvas {
    max-height: 100%;
}

/* Tabela de Recentes */
.table-container {
    background: var(--card-background);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    border: 1px solid var(--border-color);
    overflow: hidden;
}

.table-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--spacing-md) var(--spacing-lg);
    border-bottom: 1px solid var(--border-color);
    background-color: #fafafa;
}

.table-header h3 {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
}

#recent-count {
    font-size: 0.875rem;
    color: var(--text-secondary);
    font-weight: 500;
}

.table-responsive {
    overflow-x: auto;
}

#recent-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
}

#recent-table th {
    background-color: #f9fafb;
    color: var(--text-secondary);
    font-weight: 600;
    text-align: left;
    padding: var(--spacing-md);
    border-bottom: 2px solid var(--border-color);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

#recent-table td {
    padding: var(--spacing-md);
    border-bottom: 1px solid var(--border-color);
    color: var(--text-primary);
}

#recent-table tbody tr:hover {
    background-color: #f9fafb;
}

.badge {
    display: inline-block;
    padding: 2px 8px;
    background-color: #e0e7ff;
    color: #3730a3;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    white-space: nowrap;
    margin: 1px;
}

/* Loading */
.loading {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-md);
    padding: var(--spacing-xl);
    color: var(--text-secondary);
}

.spinner {
    width: 24px;
    height: 24px;
    border: 3px solid var(--border-color);
    border-top-color: var(--primary-color);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.hidden {
    display: none !important;
}

/* Responsividade */
@media (max-width: 768px) {
    .app-container {
        flex-direction: column;
    }
    
    .sidebar {
        width: 100%;
        height: auto;
        position: relative;
        flex-direction: row;
        padding: var(--spacing-sm);
        height: 70px;
    }
    
    .sidebar-header {
        padding: 0;
        border: none;
    }
    
    .sidebar-nav {
        display: flex;
        flex: 1;
        padding: 0;
        gap: var(--spacing-sm);
    }
    
    .nav-item {
        flex: 1;
        justify-content: center;
        padding: var(--spacing-sm);
        font-size: 0.85rem;
        border-left: none;
        border-bottom: 3px solid transparent;
    }
    
    .nav-item.active {
        border-left: none;
        border-bottom-color: white;
    }
    
    .nav-item span {
        display: none;
    }
    
    .sidebar-footer {
        display: none;
    }
    
    .main-content {
        margin-left: 0;
        padding: var(--spacing-sm);
    }
    
    .metrics-container {
        grid-template-columns: 1fr;
    }
    
    .charts-container {
        grid-template-columns: 1fr;
    }
    
    .chart-card.full-width {
        grid-column: 1;
    }
    
    .metric-value {
        font-size: 1.5rem;
    }
}
```

## ./frontend/css/styles_home.css

```css
/* ===== VARIÁVEIS - TEMA PT ===== */
:root {
    --pt-red: #e30613;
    --pt-red-dark: #b30000;
    --pt-red-light: #ff1a1a;
    --white: #ffffff;
    --black: #1a1a1a;
    --gray: #f5f5f5;
    --gray-dark: #666666;
    --shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    --shadow-hover: 0 8px 30px rgba(227, 6, 19, 0.25);
    --radius: 12px;
    --transition: all 0.3s ease;
}

/* ===== RESET ===== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: var(--white);
    color: var(--black);
    line-height: 1.6;
    overflow-x: hidden;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* ===== NAVEGAÇÃO ===== */
.navbar {
    background: var(--pt-red);
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
    box-shadow: var(--shadow);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 15px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo-nav {
    display: flex;
    align-items: center;
    gap: 10px;
    color: var(--white);
    font-size: 1.3rem;
    font-weight: 700;
    text-decoration: none;
}

.logo-nav i {
    color: var(--white);
    font-size: 1.5rem;
}

.nav-links {
    display: flex;
    list-style: none;
    gap: 30px;
    align-items: center;
}

.nav-links a {
    color: var(--white);
    text-decoration: none;
    font-weight: 500;
    transition: var(--transition);
    position: relative;
}

.nav-links a::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--white);
    transition: var(--transition);
}

.nav-links a:hover::after {
    width: 100%;
}

.btn-nav {
    background: var(--white);
    color: var(--pt-red) !important;
    padding: 10px 20px;
    border-radius: var(--radius);
    font-weight: 600 !important;
}

.btn-nav::after {
    display: none !important;
}

.btn-nav:hover {
    background: var(--gray);
    transform: translateY(-2px);
}

.hamburger {
    display: none;
    flex-direction: column;
    cursor: pointer;
    gap: 5px;
}

.hamburger span {
    width: 25px;
    height: 3px;
    background: var(--white);
    border-radius: 3px;
    transition: var(--transition);
}

/* ===== HERO SECTION ===== */
.hero {
    background: linear-gradient(135deg, var(--pt-red) 0%, var(--pt-red-dark) 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 120px 20px 80px;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 600px;
    height: 600px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 50%;
}

.hero-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
    width: 100%;
}

.star-badge {
    width: 80px;
    height: 80px;
    background: var(--white);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

.star-badge i {
    color: var(--pt-red);
    font-size: 2.5rem;
}

.hero h1 {
    color: var(--white);
    font-size: 3.5rem;
    font-weight: 800;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.hero-subtitle {
    color: var(--white);
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 15px;
    opacity: 0.95;
}

.hero-description {
    color: rgba(255, 255, 255, 0.9);
    font-size: 1.1rem;
    margin-bottom: 30px;
    max-width: 500px;
}

.hero-buttons {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
}

.btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 15px 30px;
    border-radius: var(--radius);
    text-decoration: none;
    font-weight: 600;
    transition: var(--transition);
    border: none;
    cursor: pointer;
    font-size: 1rem;
}

.btn-primary {
    background: var(--white);
    color: var(--pt-red);
}

.btn-primary:hover {
    background: var(--gray);
    transform: translateY(-3px);
    box-shadow: var(--shadow-hover);
}

.btn-secondary {
    background: transparent;
    color: var(--white);
    border: 2px solid var(--white);
}

.btn-secondary:hover {
    background: var(--white);
    color: var(--pt-red);
    transform: translateY(-3px);
}

.btn-large {
    padding: 20px 40px;
    font-size: 1.2rem;
}

.hero-image {
    display: flex;
    justify-content: center;
}

.photo-placeholder {
    width: 350px;
    height: 450px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: var(--radius);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: var(--white);
    border: 3px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
    padding: 0;
    overflow: hidden;
}

.photo-placeholder img {
    width: 100%; /* A foto ocupa toda a largura do contêiner (350px) */
    height: 100%; /* A foto ocupa toda a altura do contêiner (450px) */
    object-fit: cover; /* ESSENCIAL: Corta e ajusta a foto para preencher o espaço sem distorcer */
    object-position: center; /* Centraliza o corte da foto */
}

.wave-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100px;
    background: var(--white);
    clip-path: polygon(0 100%, 100% 100%, 100% 0, 0 100%);
}

/* ===== ESTATÍSTICAS ===== */
.stats {
    background: var(--white);
    padding: 60px 20px;
    margin-top: -50px;
    position: relative;
    z-index: 10;
}

.stats .container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
}

.stat-card {
    background: var(--white);
    padding: 30px;
    border-radius: var(--radius);
    text-align: center;
    box-shadow: var(--shadow);
    transition: var(--transition);
    border-bottom: 4px solid var(--pt-red);
}

.stat-card:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-hover);
}

.stat-card i {
    font-size: 2.5rem;
    color: var(--pt-red);
    margin-bottom: 15px;
}

.stat-card h3 {
    font-size: 2rem;
    color: var(--pt-red);
    margin-bottom: 5px;
}

.stat-card p {
    color: var(--gray-dark);
    font-weight: 500;
}

/* ===== SEÇÕES COMUNS ===== */
.section-header {
    text-align: center;
    margin-bottom: 50px;
}

.section-header i {
    font-size: 2.5rem;
    color: var(--pt-red);
    margin-bottom: 15px;
}

.section-header h2 {
    font-size: 2.5rem;
    color: var(--black);
    margin-bottom: 10px;
}

.section-header p {
    color: var(--gray-dark);
    font-size: 1.1rem;
}

.section-header.light i,
.section-header.light h2,
.section-header.light p {
    color: var(--white);
}

/* ===== SOBRE ===== */
.sobre {
    padding: 80px 20px;
    background: var(--gray);
}

.sobre-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.sobre-text p {
    font-size: 1.1rem;
    margin-bottom: 25px;
    color: var(--gray-dark);
}

.sobre-lista {
    list-style: none;
}

.sobre-lista li {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 15px;
    font-size: 1.1rem;
}

.sobre-lista i {
    color: var(--pt-red);
    font-size: 1.2rem;
}

.sobre-video {
    display: flex;
    justify-content: center;
}

.video-placeholder {
    width: 100%;
    max-width: 500px;
    height: 300px;
    background: var(--pt-red);
    border-radius: var(--radius);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: var(--white);
    cursor: pointer;
    transition: var(--transition);
    position: relative;
    overflow: hidden;
}

.video-placeholder::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.2);
}

.video-placeholder:hover {
    transform: scale(1.02);
}

.video-placeholder i {
    font-size: 4rem;
    z-index: 1;
}

.video-placeholder span {
    margin-top: 10px;
    z-index: 1;
    font-weight: 500;
}

/* ===== CALENDÁRIO ===== */
.calendario {
    padding: 80px 20px;
    background: linear-gradient(135deg, var(--pt-red-dark) 0%, var(--pt-red) 100%);
    color: var(--white);
}

.eventos-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-bottom: 40px;
}

.evento-card {
    background: var(--white);
    border-radius: var(--radius);
    padding: 25px;
    display: flex;
    align-items: center;
    gap: 20px;
    color: var(--black);
    transition: var(--transition);
}

.evento-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-hover);
}

.evento-data {
    background: var(--pt-red);
    color: var(--white);
    padding: 15px;
    border-radius: var(--radius);
    text-align: center;
    min-width: 70px;
}

.evento-data .dia {
    display: block;
    font-size: 1.8rem;
    font-weight: 800;
    line-height: 1;
}

.evento-data .mes {
    display: block;
    font-size: 0.9rem;
    text-transform: uppercase;
    font-weight: 600;
}

.evento-info h4 {
    font-size: 1.1rem;
    margin-bottom: 8px;
    color: var(--black);
}

.evento-info p {
    color: var(--gray-dark);
    font-size: 0.9rem;
    margin-bottom: 5px;
    display: flex;
    align-items: center;
    gap: 5px;
}

.evento-info i {
    color: var(--pt-red);
}

.btn-evento {
    margin-left: auto;
    background: var(--pt-red);
    color: var(--white);
    padding: 10px 20px;
    border-radius: var(--radius);
    text-decoration: none;
    font-weight: 600;
    font-size: 0.9rem;
    transition: var(--transition);
    white-space: nowrap;
}

.btn-evento:hover {
    background: var(--pt-red-dark);
    transform: scale(1.05);
}

.calendario-full {
    text-align: center;
}

.btn-outline-light {
    background: transparent;
    color: var(--white);
    border: 2px solid var(--white);
    padding: 15px 30px;
}

.btn-outline-light:hover {
    background: var(--white);
    color: var(--pt-red);
}

/* ===== FÓRUM ===== */
.forum {
    padding: 80px 20px;
    background: var(--white);
}

.forum-topicos {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 25px;
    margin-bottom: 40px;
}

.topico-card {
    background: var(--gray);
    padding: 30px;
    border-radius: var(--radius);
    text-align: center;
    transition: var(--transition);
    border-bottom: 4px solid transparent;
}

.topico-card:hover {
    transform: translateY(-10px);
    border-bottom-color: var(--pt-red);
    box-shadow: var(--shadow);
}

.topico-icon {
    width: 70px;
    height: 70px;
    background: var(--pt-red);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 20px;
}

.topico-icon i {
    color: var(--white);
    font-size: 1.8rem;
}

.topico-card h4 {
    font-size: 1.2rem;
    margin-bottom: 10px;
    color: var(--black);
}

.topico-card p {
    color: var(--gray-dark);
    font-size: 0.95rem;
    margin-bottom: 15px;
}

.topico-stats {
    display: inline-block;
    background: var(--pt-red);
    color: var(--white);
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
}

.forum-cta {
    text-align: center;
}

/* ===== CADASTRO CTA ===== */
.cadastro-cta {
    padding: 80px 20px;
    background: var(--gray);
}

.cta-box {
    background: linear-gradient(135deg, var(--pt-red) 0%, var(--pt-red-dark) 100%);
    border-radius: var(--radius);
    padding: 60px;
    text-align: center;
    color: var(--white);
    position: relative;
    overflow: hidden;
}

.cta-box::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    animation: rotate 20s linear infinite;
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.cta-content {
    position: relative;
    z-index: 1;
}

.cta-content > i {
    font-size: 3rem;
    margin-bottom: 20px;
    color: var(--white);
}

.cta-content h2 {
    font-size: 2.5rem;
    margin-bottom: 15px;
}

.cta-content p {
    font-size: 1.1rem;
    margin-bottom: 30px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0.95;
}

/* ===== FOOTER ===== */
.footer {
    background: var(--black);
    color: var(--white);
    padding: 50px 20px 20px;
}

.footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
    flex-wrap: wrap;
    gap: 20px;
}

.footer-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.5rem;
    font-weight: 700;
}

.footer-brand i {
    color: var(--pt-red);
    font-size: 1.8rem;
}

.footer-social {
    display: flex;
    gap: 15px;
}

.footer-social a {
    width: 45px;
    height: 45px;
    background: var(--pt-red);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--white);
    text-decoration: none;
    transition: var(--transition);
}

.footer-social a:hover {
    background: var(--white);
    color: var(--pt-red);
    transform: translateY(-5px);
}

.footer-bottom {
    text-align: center;
    padding-top: 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-bottom p {
    margin-bottom: 5px;
    color: rgba(255, 255, 255, 0.7);
}

.footer-bottom i {
    color: var(--pt-red);
}

/* ===== RESPONSIVO ===== */
@media (max-width: 992px) {
    .hero-content {
        grid-template-columns: 1fr;
        text-align: center;
    }

    .star-badge {
        margin: 0 auto 20px;
    }

    .hero-description {
        margin-left: auto;
        margin-right: auto;
    }

    .hero-buttons {
        justify-content: center;
    }

    .hero-image {
        order: -1;
    }

    .photo-placeholder {
        width: 250px;
        height: 300px;
    }

    .stats .container {
        grid-template-columns: repeat(2, 1fr);
    }

    .sobre-content {
        grid-template-columns: 1fr;
    }

    .eventos-grid {
        grid-template-columns: 1fr;
    }

    .forum-topicos {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .nav-links {
        display: none;
    }

    .hamburger {
        display: flex;
    }

    .hero h1 {
        font-size: 2.5rem;
    }

    .stats .container {
        grid-template-columns: 1fr;
    }

    .forum-topicos {
        grid-template-columns: 1fr;
    }

    .cta-box {
        padding: 40px 20px;
    }

    .footer-content {
        flex-direction: column;
        text-align: center;
    }
}
```

## ./frontend/css/styles_index.css

```css
/* Variáveis */
:root {
    --primary-color: #f63b3b;
    --primary-hover: #eb3525;
    --background: #0f0f23;
    --card-bg: #1a1a2e;
    --text-primary: #ffffff;
    --text-secondary: #a0a0a0;
    --button-bg: #ffffff;
    --button-text: #1a1a2e;
    --shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    --radius: 12px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: linear-gradient(135deg, #f60101 0%, #ffffff 100%);
    /* Ou use uma cor sólida: background: var(--background); */
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.container {
    width: 100%;
    max-width: 680px;
    text-align: center;
}

/* Perfil */
.profile {
    margin-bottom: 30px;
}

.avatar {
    width: 120px;
    height: 120px;
    margin: 0 auto 20px;
    border-radius: 50%;
    overflow: hidden;
    border: 4px solid rgba(255, 255, 255, 0.3);
    box-shadow: var(--shadow);
}

.avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.profile h1 {
    color: var(--text-primary);
    font-size: 1.8rem;
    margin-bottom: 8px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.bio {
    color: rgba(255, 255, 255, 0.9);
    font-size: 1rem;
    max-width: 400px;
    margin: 0 auto;
}

/* Links/Botões */
.links {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 30px;
}

.link-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    background: var(--button-bg);
    color: var(--button-text);
    text-decoration: none;
    padding: 18px 24px;
    border-radius: var(--radius);
    font-weight: 600;
    font-size: 1rem;
    transition: all 0.3s ease;
    box-shadow: var(--shadow);
    border: 2px solid transparent;
    position: relative;
    overflow: hidden;
}

.link-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    border-color: var(--primary-color);
}

.link-button:active {
    transform: translateY(-1px);
}

.link-button i {
    font-size: 1.3rem;
    color: var(--primary-color);
}

/* Cores especiais para alguns botões */
.link-button.whatsapp {
    background: #25d366;
    color: white;
}

.link-button.whatsapp i {
    color: white;
}

.link-button.instagram {
    background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
    color: white;
}

.link-button.instagram i {
    color: white;
}

.link-button.email {
    background: #ea4335;
    color: white;
}

.link-button.email i {
    color: white;
}

/* Ícones Sociais */
.social-icons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 30px;
}

.social-icons a {
    color: white;
    font-size: 1.5rem;
    transition: all 0.3s ease;
    opacity: 0.8;
}

.social-icons a:hover {
    opacity: 1;
    transform: scale(1.2);
}

/* Footer */
footer {
    color: rgba(255, 255, 255, 0.7);
    font-size: 0.85rem;
}

/* Responsivo */
@media (max-width: 480px) {
    .avatar {
        width: 100px;
        height: 100px;
    }
    
    .profile h1 {
        font-size: 1.5rem;
    }
    
    .link-button {
        padding: 16px 20px;
        font-size: 0.95rem;
    }
}
```

## ./frontend/css/styles_lista.css

```css
/* Variáveis CSS para cores e design system */
:root {
    --primary-color: #f63b3b;
    --primary-hover: #eb3525;
    --secondary-color: #6b7280;
    --secondary-hover: #4b5563;
    --success-color: #10b981;
    --success-hover: #059669;
    --danger-color: #ef4444;
    --background-color: #f3f4f6;
    --card-background: #ffffff;
    --text-primary: #111827;
    --text-secondary: #6b7280;
    --border-color: #e5e7eb;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --radius-sm: 6px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
}

/* Reset e estilos base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background-color: var(--background-color);
    color: var(--text-primary);
    line-height: 1.6;
}

/* Layout Principal com Sidebar */
.app-container {
    display: flex;
    min-height: 100vh;
}

/* Sidebar */
.sidebar {
    width: 260px;
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    color: white;
    display: flex;
    flex-direction: column;
    position: fixed;
    height: 100vh;
    left: 0;
    top: 0;
    z-index: 1000;
    box-shadow: var(--shadow-lg);
}

.sidebar-header {
    padding: var(--spacing-lg);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.sidebar-header .logo {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    font-size: 1.3rem;
    font-weight: 700;
    color: white;
}

.sidebar-header .logo i {
    font-size: 1.5rem;
}

.sidebar-nav {
    flex: 1;
    padding: var(--spacing-md) 0;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
    padding: var(--spacing-md) var(--spacing-lg);
    color: rgba(255, 255, 255, 0.9);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.2s;
    border-left: 3px solid transparent;
}

.nav-item:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
}

.nav-item.active {
    background: rgba(255, 255, 255, 0.15);
    color: white;
    border-left-color: white;
}

.nav-item i {
    font-size: 1.1rem;
    width: 20px;
    text-align: center;
}

.sidebar-footer {
    padding: var(--spacing-md) var(--spacing-lg);
    border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.btn-logout {
    width: 100%;
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    padding: var(--spacing-sm) var(--spacing-md);
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: var(--radius-md);
    color: white;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-logout:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-1px);
}

/* Main Content */
.main-content {
    flex: 1;
    margin-left: 260px;
    padding: var(--spacing-lg);
    background-color: var(--background-color);
}

.container {
    max-width: 1400px;
    margin: 0 auto;
}

/* Container Superior (Header) */
.header {
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    color: white;
    padding: var(--spacing-lg) var(--spacing-xl);
    border-radius: var(--radius-lg);
    margin-bottom: var(--spacing-lg);
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: var(--shadow-lg);
}

.header-left {
    display: flex;
    align-items: center;
    gap: var(--spacing-lg);
}

.logo {
    font-size: 1.5rem;
    font-weight: 700;
    background: rgba(255, 255, 255, 0.2);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--radius-md);
}

.header-left h1 {
    font-size: 1.25rem;
    font-weight: 600;
}

.header-right {
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
}

.user-info {
    text-align: right;
}

.user-name {
    display: block;
    font-weight: 600;
    font-size: 0.95rem;
}

.user-role {
    display: block;
    font-size: 0.8rem;
    opacity: 0.9;
}

.user-avatar {
    width: 45px;
    height: 45px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    border: 2px solid rgba(255, 255, 255, 0.5);
}

/* Container de Filtros */
.filters-container {
    background: var(--card-background);
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    margin-bottom: var(--spacing-lg);
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-color);
}

.filters-container h2 {
    font-size: 1.1rem;
    margin-bottom: var(--spacing-md);
    color: var(--text-primary);
    font-weight: 600;
}

/* Flexbox para os filtros lado a lado */
.filters-flexbox {
    display: flex;
    gap: var(--spacing-md);
    flex-wrap: wrap;
}

.filter-group {
    flex: 1;
    min-width: 200px;
    display: flex;
    flex-direction: column;
}

.filter-group label {
    font-size: 0.875rem;
    font-weight: 500;
    margin-bottom: var(--spacing-xs);
    color: var(--text-secondary);
}

.filter-group input {
    padding: var(--spacing-sm) var(--spacing-md);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    font-size: 0.95rem;
    transition: all 0.2s;
}

.filter-group input:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* Container de Ações */
.actions-container {
    display: flex;
    gap: var(--spacing-sm);
    margin-bottom: var(--spacing-lg);
    flex-wrap: wrap;
}

/* Botões */
.btn {
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-sm);
    padding: var(--spacing-sm) var(--spacing-md);
    border: none;
    border-radius: var(--radius-md);
    font-size: 0.95rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    text-decoration: none;
}

.btn-primary {
    background-color: var(--primary-color);
    color: white;
}

.btn-primary:hover {
    background-color: var(--primary-hover);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.btn-secondary {
    background-color: var(--secondary-color);
    color: white;
}

.btn-secondary:hover {
    background-color: var(--secondary-hover);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.btn-success {
    background-color: var(--success-color);
    color: white;
}

.btn-success:hover {
    background-color: var(--success-hover);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

/* Container da Tabela */
.table-container {
    background: var(--card-background);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-color);
    overflow: hidden;
}

.table-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--spacing-md) var(--spacing-lg);
    border-bottom: 1px solid var(--border-color);
    background-color: #fafafa;
}

.table-header h3 {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
}

#record-count {
    font-size: 0.875rem;
    color: var(--text-secondary);
    font-weight: 500;
}

/* Tabela Responsiva */
.table-responsive {
    overflow-x: auto;
    max-height: 600px;
    overflow-y: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
}

thead {
    position: sticky;
    top: 0;
    z-index: 10;
}

th {
    background-color: #f9fafb;
    color: var(--text-secondary);
    font-weight: 600;
    text-align: left;
    padding: var(--spacing-md);
    border-bottom: 2px solid var(--border-color);
    white-space: nowrap;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

td {
    padding: var(--spacing-md);
    border-bottom: 1px solid var(--border-color);
    color: var(--text-primary);
    vertical-align: top;
}

tbody tr:hover {
    background-color: #f9fafb;
}

/* Badges para Temas */
.theme-badges {
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-xs);
}

.badge {
    display: inline-block;
    padding: 2px 8px;
    background-color: #e0e7ff;
    color: #3730a3;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    white-space: nowrap;
}

/* Status de Consentimento */
.consent-yes {
    color: var(--success-color);
    font-weight: 600;
}

.consent-no {
    color: var(--danger-color);
    font-weight: 600;
}

/* Loading e Estados */
.loading {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-md);
    padding: var(--spacing-xl);
    color: var(--text-secondary);
}

.spinner {
    width: 24px;
    height: 24px;
    border: 3px solid var(--border-color);
    border-top-color: var(--primary-color);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.hidden {
    display: none !important;
}

.empty-state {
    text-align: center;
    padding: var(--spacing-xl);
    color: var(--text-secondary);
}

.empty-state p {
    font-size: 1rem;
}

/* Responsividade */
@media (max-width: 768px) {
    .app-container {
        flex-direction: column;
    }
    
    .sidebar {
        width: 100%;
        height: auto;
        position: relative;
        flex-direction: row;
        padding: var(--spacing-sm);
        height: 70px;
    }
    
    .sidebar-header {
        padding: 0;
        border: none;
    }
    
    .sidebar-nav {
        display: flex;
        flex: 1;
        padding: 0;
        gap: var(--spacing-sm);
    }
    
    .nav-item {
        flex: 1;
        justify-content: center;
        padding: var(--spacing-sm);
        font-size: 0.85rem;
        border-left: none;
        border-bottom: 3px solid transparent;
    }
    
    .nav-item.active {
        border-left: none;
        border-bottom-color: white;
    }
    
    .nav-item span {
        display: none;
    }
    
    .sidebar-footer {
        display: none;
    }
    
    .main-content {
        margin-left: 0;
        padding: var(--spacing-sm);
    }
    
    .container {
        padding: var(--spacing-sm);
    }
    
    .header {
        flex-direction: column;
        gap: var(--spacing-md);
        text-align: center;
    }
    
    .header-left {
        flex-direction: column;
        gap: var(--spacing-sm);
    }
    
    .filters-flexbox {
        flex-direction: column;
    }
    
    .filter-group {
        min-width: 100%;
    }
    
    .actions-container {
        flex-direction: column;
    }
    
    .btn {
        width: 100%;
        justify-content: center;
    }
    
    th, td {
        padding: var(--spacing-sm);
        font-size: 0.85rem;
    }
    
    .badge {
        font-size: 0.7rem;
    }
}

/* Scrollbar personalizada */
.table-responsive::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

.table-responsive::-webkit-scrollbar-track {
    background: #f1f1f1;
}

.table-responsive::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 4px;
}

.table-responsive::-webkit-scrollbar-thumb:hover {
    background: #a1a1a1;
}

```

## ./frontend/css/styles_login.css

```css
/* Importando variáveis do projeto */
:root {
    --primary-color: #f63b3b;
    --primary-hover: #eb3525;
    --secondary-color: #6b7280;
    --secondary-hover: #4b5563;
    --background-color: #f3f4f6;
    --card-background: #ffffff;
    --text-primary: #111827;
    --text-secondary: #6b7280;
    --border-color: #e5e7eb;
    --error-color: #ef4444;
    --success-color: #10b981;
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --radius-lg: 12px;
    --radius-md: 8px;
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background: linear-gradient(135deg, #f60101 0%, #ffffff 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.container {
    width: 100%;
    max-width: 480px;
}

/* Header */
.header {
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    color: white;
    padding: var(--spacing-md) var(--spacing-lg);
    border-radius: var(--radius-lg);
    margin-bottom: var(--spacing-lg);
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: var(--shadow-lg);
}

.header-left {
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
    width: 100%;
    justify-content: center;
}

.logo {
    background: rgba(255, 255, 255, 0.2);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--radius-md);
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.1rem;
}

.logo i {
    font-size: 1.3rem;
}

.header h1 {
    font-size: 1.25rem;
    font-weight: 600;
}

/* Container de Login */
.login-container {
    background: var(--card-background);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
    border: 1px solid var(--border-color);
    overflow: hidden;
}

.login-card {
    padding: var(--spacing-xl);
}

.login-header {
    text-align: center;
    margin-bottom: var(--spacing-xl);
}

.login-icon {
    width: 70px;
    height: 70px;
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto var(--spacing-md);
    color: white;
    font-size: 1.8rem;
    box-shadow: var(--shadow-md);
}

.login-header h2 {
    font-size: 1.5rem;
    color: var(--text-primary);
    margin-bottom: var(--spacing-xs);
}

.login-header p {
    color: var(--text-secondary);
    font-size: 0.9rem;
}

/* Formulário */
.login-form {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-lg);
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-sm);
}

.form-group label {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    gap: 8px;
}

.form-group input {
    padding: 14px;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    font-size: 1rem;
    transition: all 0.2s;
    width: 100%;
}

.form-group input:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(246, 59, 59, 0.1);
}

/* Campo de Senha com Toggle */
.password-wrapper {
    position: relative;
    display: flex;
    align-items: center;
}

.password-wrapper input {
    padding-right: 45px;
}

.toggle-password {
    position: absolute;
    right: 12px;
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    font-size: 1.1rem;
    padding: 5px;
    transition: color 0.2s;
}

.toggle-password:hover {
    color: var(--primary-color);
}

/* Opções do Formulário */
.form-options {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.85rem;
}

.remember-me {
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    color: var(--text-secondary);
}

.remember-me input {
    width: auto;
    accent-color: var(--primary-color);
}

.forgot-link {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s;
}

.forgot-link:hover {
    color: var(--primary-hover);
    text-decoration: underline;
}

/* Botão de Submit */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-sm);
    padding: var(--spacing-md) var(--spacing-lg);
    border: none;
    border-radius: var(--radius-md);
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    text-decoration: none;
}

.btn-primary {
    background-color: var(--primary-color);
    color: white;
}

.btn-primary:hover {
    background-color: var(--primary-hover);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.btn-primary:active {
    transform: translateY(0);
}

.btn-large {
    width: 100%;
    padding: 16px;
    font-size: 1.05rem;
}

.btn:disabled {
    opacity: 0.7;
    cursor: not-allowed;
    transform: none !important;
}

/* Mensagem de Erro */
.error-message {
    background: #fee2e2;
    border: 1px solid #fecaca;
    color: var(--error-color);
    padding: var(--spacing-md);
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    font-size: 0.9rem;
    font-weight: 500;
}

.error-message.hidden {
    display: none;
}

/* Footer do Login */
.login-footer {
    margin-top: var(--spacing-xl);
    padding-top: var(--spacing-lg);
    border-top: 1px solid var(--border-color);
    text-align: center;
}

.login-footer p {
    color: var(--text-secondary);
    font-size: 0.8rem;
    margin-bottom: var(--spacing-xs);
}

.security-info {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    color: var(--primary-color) !important;
    font-weight: 600;
}

/* Responsividade */
@media (max-width: 480px) {
    .container {
        padding: 10px;
    }
    
    .login-card {
        padding: var(--spacing-lg);
    }
    
    .form-options {
        flex-direction: column;
        gap: var(--spacing-sm);
        align-items: flex-start;
    }
    
    .login-icon {
        width: 60px;
        height: 60px;
        font-size: 1.5rem;
    }
}
```

## ./frontend/css/teste.css

```css
/* Variáveis CSS para cores e design system */
:root {
    --primary-color: #f63b3b;
    --primary-hover: #eb3525;
    --secondary-color: #6b7280;
    --secondary-hover: #4b5563;
    --success-color: #10b981;
    --success-hover: #059669;
    --danger-color: #ef4444;
    --background-color: #f3f4f6;
    --card-background: #ffffff;
    --text-primary: #111827;
    --text-secondary: #6b7280;
    --border-color: #e5e7eb;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --radius-sm: 6px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background-color: var(--background-color);
    color: var(--text-primary);
    line-height: 1.6;
}

/* Layout Principal com Sidebar */
.app-container {
    display: flex;
    min-height: 100vh;
}

/* Sidebar */
.sidebar {
    width: 260px;
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    color: white;
    display: flex;
    flex-direction: column;
    position: fixed;
    height: 100vh;
    left: 0;
    top: 0;
    z-index: 1000;
    box-shadow: var(--shadow-lg);
}

.sidebar-header {
    padding: var(--spacing-lg);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.sidebar-header .logo {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    font-size: 1.3rem;
    font-weight: 700;
    color: white;
}

.sidebar-header .logo i {
    font-size: 1.5rem;
}

.sidebar-nav {
    flex: 1;
    padding: var(--spacing-md) 0;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
    padding: var(--spacing-md) var(--spacing-lg);
    color: rgba(255, 255, 255, 0.9);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.2s;
    border-left: 3px solid transparent;
}

.nav-item:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
}

.nav-item.active {
    background: rgba(255, 255, 255, 0.15);
    color: white;
    border-left-color: white;
}

.nav-item i {
    font-size: 1.1rem;
    width: 20px;
    text-align: center;
}

.sidebar-footer {
    padding: var(--spacing-md) var(--spacing-lg);
    border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.btn-logout {
    width: 100%;
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    padding: var(--spacing-sm) var(--spacing-md);
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: var(--radius-md);
    color: white;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-logout:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-1px);
}

/* Main Content */
.main-content {
    flex: 1;
    margin-left: 260px;
    padding: var(--spacing-lg);
    background-color: var(--background-color);
}

/* Header */
.header {
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    color: white;
    padding: var(--spacing-lg) var(--spacing-xl);
    border-radius: var(--radius-lg);
    margin-bottom: var(--spacing-lg);
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: var(--shadow-lg);
}

.header-left {
    display: flex;
    align-items: center;
    gap: var(--spacing-lg);
}

.header-left .logo {
    font-size: 1.5rem;
    font-weight: 700;
    background: rgba(255, 255, 255, 0.2);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--radius-md);
}

.header-left h1 {
    font-size: 1.25rem;
    font-weight: 600;
}

.header-right {
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
}

.user-info {
    text-align: right;
}

.user-name {
    display: block;
    font-weight: 600;
    font-size: 0.95rem;
}

.user-role {
    display: block;
    font-size: 0.8rem;
    opacity: 0.9;
}

.user-avatar {
    width: 45px;
    height: 45px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    border: 2px solid rgba(255, 255, 255, 0.5);
}

/* Cards de Métricas */
.metrics-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
}

.metric-card {
    background: var(--card-background);
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    border: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
    transition: transform 0.2s;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

.metric-icon {
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, var(--primary-color) 0%, #d81d1d 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.5rem;
}

.metric-content {
    flex: 1;
}

.metric-value {
    display: block;
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1;
}

.metric-label {
    display: block;
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin-top: var(--spacing-xs);
}

/* Gráficos */
.charts-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
}

.chart-card {
    background: var(--card-background);
    padding: var(--spacing-lg);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    border: 1px solid var(--border-color);
}

.chart-card.full-width {
    grid-column: 1 / -1;
}

.chart-header {
    margin-bottom: var(--spacing-md);
    padding-bottom: var(--spacing-md);
    border-bottom: 1px solid var(--border-color);
}

.chart-header h3 {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: var(--spacing-xs);
}

.chart-header p {
    font-size: 0.875rem;
    color: var(--text-secondary);
}

.chart-wrapper {
    position: relative;
    height: 300px;
}

.chart-wrapper canvas {
    max-height: 100%;
}

/* Tabela de Recentes */
.table-container {
    background: var(--card-background);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    border: 1px solid var(--border-color);
    overflow: hidden;
}

.table-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--spacing-md) var(--spacing-lg);
    border-bottom: 1px solid var(--border-color);
    background-color: #fafafa;
}

.table-header h3 {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
}

#recent-count {
    font-size: 0.875rem;
    color: var(--text-secondary);
    font-weight: 500;
}

.table-responsive {
    overflow-x: auto;
}

#recent-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
}

#recent-table th {
    background-color: #f9fafb;
    color: var(--text-secondary);
    font-weight: 600;
    text-align: left;
    padding: var(--spacing-md);
    border-bottom: 2px solid var(--border-color);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

#recent-table td {
    padding: var(--spacing-md);
    border-bottom: 1px solid var(--border-color);
    color: var(--text-primary);
}

#recent-table tbody tr:hover {
    background-color: #f9fafb;
}

.badge {
    display: inline-block;
    padding: 2px 8px;
    background-color: #e0e7ff;
    color: #3730a3;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    white-space: nowrap;
    margin: 1px;
}

/* Loading */
.loading {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-md);
    padding: var(--spacing-xl);
    color: var(--text-secondary);
}

.spinner {
    width: 24px;
    height: 24px;
    border: 3px solid var(--border-color);
    border-top-color: var(--primary-color);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.hidden {
    display: none !important;
}

/* Responsividade */
@media (max-width: 768px) {
    .app-container {
        flex-direction: column;
    }
    
    .sidebar {
        width: 100%;
        height: auto;
        position: relative;
        flex-direction: row;
        padding: var(--spacing-sm);
        height: 70px;
    }
    
    .sidebar-header {
        padding: 0;
        border: none;
    }
    
    .sidebar-nav {
        display: flex;
        flex: 1;
        padding: 0;
        gap: var(--spacing-sm);
    }
    
    .nav-item {
        flex: 1;
        justify-content: center;
        padding: var(--spacing-sm);
        font-size: 0.85rem;
        border-left: none;
        border-bottom: 3px solid transparent;
    }
    
    .nav-item.active {
        border-left: none;
        border-bottom-color: white;
    }
    
    .nav-item span {
        display: none;
    }
    
    .sidebar-footer {
        display: none;
    }
    
    .main-content {
        margin-left: 0;
        padding: var(--spacing-sm);
    }
    
    .metrics-container {
        grid-template-columns: 1fr;
    }
    
    .charts-container {
        grid-template-columns: 1fr;
    }
    
    .chart-card.full-width {
        grid-column: 1;
    }
    
    .metric-value {
        font-size: 1.5rem;
    }
}
```

## ./frontend/html/cadastro.html

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/frontend/css/styles_cadastro.css">
    <!-- Ícones (Font Awesome) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <title>Formulario Apoiadores</title>
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="header-left">
                <div class="logo">
                    <i class="fas fa-star"></i>
                    <span>Ouvidor do povo</span> 
                </div>
                <h1>Cadastro de Apoiadores </h1>
            </div>
            <div class="header-right">
                <div class="user-info">
                    <span class="user-name"></span>
                    <span class="user-role"></span>
                </div>
                <div class="user-avatar"></div>
            </div>
        </header>

        <div class="form-container">
            <div class="form-header">
                <h2>Formulário de Apoiadores</h2>
                <p>Preencha os dados abaixo para realizar o cadastro.</p>
            </div>

            <form id="cadastroForm" class="forms-card">
                <!-- Seção 1: Dados Pessoais -->
                <section class="form-section">
                    <h3><span class="section-number">1</span> Dados Pessoais</h3>
                    <div class="form-grid">
                        <div class="form-group full-width">
                            <label for="person_full_name">Nome Completo</label>
                            <input type="text" id="person_full_name" name="full_name" placeholder="Digite seu nome completo" required>
                        </div>
                        <div class="form-group col-2">
                            <label for="person-cpf">CPF (apenas números)</label>
                            <input type="text" id="person-cpf" name="cpf" placeholder="00000000000" pattern="[0-9]{11}" maxlength="11" required>
                        </div>
                        <div class="form-group col-2">
                            <label for="person_date">Data de Nascimento</label>
                            <input type="date" id="person_date" name="birth_date" required>
                        </div>
                    </div>
                </section>

                <!-- Seção 2: Dados de Contato -->
                <section class="form-section">
                    <h3><span class="section-number">2</span> Dados de Contato</h3>
                    <div class="form-grid">
                        <div class="form-group col-2">
                            <label for="person-phone">Telefone (WhatsApp)</label>
                            <input type="text" id="person-phone" name="phone" placeholder="(00) 00000-0000" required>
                        </div>
                        <div class="form-group col-2">
                            <label for="person_email">E-mail</label>
                            <input type="email" id="person_email" name="email" placeholder="email@exemplo.com" required>
                        </div>
                    </div>
                </section>

                <!-- Seção 3: Dados de Endereço -->
                <section class="form-section">
                    <h3><span class="section-number">3</span> Dados de Endereço</h3>
                    <div class="form-grid">
                        <!-- Linha 1: CEP | Endereço | Número -->
                        <div class="form-group col-1">
                            <label for="person-cep">CEP</label>
                            <div class="input-with-button">
                                <input type="text" id="person-cep" name="cep" placeholder="00000000" maxlength="8">
                                <button type="button" id="btn-buscar-cep" class="btn btn-secondary">
                                    <span>🔍 Buscar</span>
                                </button>
                            </div>
                            <small id="cep-help" class="hidden">Buscando...</small>
                        </div>
                        <div class="form-group col-2">
                            <label for="person-street">Endereço (Rua/Avenida)</label>
                            <input type="text" id="person-street" name="street" required>
                        </div>
                        <div class="form-group col-1">
                            <label for="street-number">Número</label>
                            <input type="text" id="street-number" name="number">
                        </div>

                        <!-- Linha 2: Complemento | Bairro | (vazio) -->
                        <div class="form-group col-1">
                            <label for="street-complement">Complemento</label>
                            <input type="text" id="street-complement" name="complement">
                        </div>
                        <div class="form-group col-2">
                            <label for="street-burgh">Bairro</label>
                            <input type="text" id="street-burgh" name="burgh">
                        </div>
                        <div class="form-group col-1">
                            <!-- Espaço reservado para manter o grid alinhado -->
                        </div>

                        <!-- Linha 3: Cidade | Estado | UF -->
                        <div class="form-group col-2">
                            <label for="street-city">Cidade</label>
                            <input type="text" id="street-city" name="city" required>
                        </div>
                        <div class="form-group col-1">
                            <label for="person-state">Estado</label>
                            <input type="text" id="person-state" name="state_name" required>
                        </div>
                        <div class="form-group col-1">
                            <label for="uf-state">UF</label>
                            <input type="text" id="uf-state" name="state_uf" maxlength="2" placeholder="Ex: RJ" required>
                        </div>
                    </div>
                </section>

                <!-- Seção 4: Temas de Interesse -->
                <section class="form-section">
                    <h3><span class="section-number">4</span> Temas de Interesse</h3>
                    <div class="themes-grid">
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Educação"><span>Educação</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Saúde"><span>Saúde</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Assistência Social"><span>Assistência Social</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Cultura"><span>Cultura</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Esporte e Lazer"><span>Esporte e Lazer</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Direitos Humanos"><span>Direitos Humanos</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Mulheres"><span>Mulheres</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Igualdade Racial"><span>Igualdade Racial</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Juventude"><span>Juventude</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Acessibilidade"><span>Acessibilidade</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Meio Ambiente"><span>Meio Ambiente</span></label>
                        <label class="checkbox-card"><input type="checkbox" name="themes" value="Segurança Pública"><span>Segurança Pública</span></label>
                    </div>
                </section>

                <!-- Footer do Formulário -->
                <div class="form-footer">
                    <label class="consent-label">
                        <input type="checkbox" id="themes-consent" name="consent" value="true" required>
                        Aceito os termos de contato e privacidade.
                    </label>
                    <button type="submit" class="btn btn-primary btn-large">
                        Cadastrar e visitar nosso grupo de Zap
                    </button>
                </div>
            </form>
        </div>
    </div>
    <script src="/frontend/javascript/script_cadastro.js"></script>
</body>
</html>
```

## ./frontend/html/dash.html

```html

```

## ./frontend/html/disparo_email.html

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Disparador de Email - CRM Pro</title>
    <link rel="stylesheet" href="/frontend/css/styles_lista.css">
</head>
<body>
    <div class="app-container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="logo">
                    <i class="fas fa-shield-alt"></i>
                    <span>Ferramentas</span>
                </div>
            </div>
            
            <nav class="sidebar-nav">
                <a href="/frontend/html/lista.html" class="nav-item">
                    <i class="fas fa-users"></i>
                    <span>Listar Usuários</span>
                </a>
                <a href="/frontend/html/disparo_email.html" class="nav-item active">
                    <i class="fas fa-paper-plane"></i>
                    <span>Disparador de Email</span>
                </a>
            </nav>
            
            <div class="sidebar-footer">
                <button id="logout-btn" class="btn-logout" onclick="handleLogout()">
                    <i class="fas fa-sign-out-alt"></i>
                    <span>Sair</span>
                </button>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <header class="header">
                <div class="header-left">
                    <div class="logo">Claudinho 2026</div>
                    <h1>Disparador de Email</h1>
                </div>
                <div class="header-right">
                    <div class="user-info">
                        <span class="user-name">Admin User</span>
                        <span class="user-role">Administrador</span>
                    </div>
                    <div class="user-avatar">AU</div>
                </div>
            </header>

            <section class="table-container">
                <div class="table-header">
                    <h3>Funcionalidade em Desenvolvimento</h3>
                </div>
                <div style="padding: 40px; text-align: center;">
                    <i class="fas fa-cogs" style="font-size: 4rem; color: var(--primary-color); margin-bottom: 20px;"></i>
                    <h2 style="color: var(--text-primary); margin-bottom: 16px;">Disparador de Email</h2>
                    <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                        Esta funcionalidade está em desenvolvimento. Em breve você poderá enviar emails em massa para os apoiadores filtrados.
                    </p>
                </div>
            </section>
        </main>
    </div>

    <script>
        // Função de logout
        function handleLogout() {
            if (confirm('Tem certeza que deseja sair?')) {
                localStorage.removeItem('admin_token');
                sessionStorage.removeItem('admin_token');
                window.location.href = '/frontend/html/login.html';
            }
        }

        // Verifica autenticação ao carregar
        document.addEventListener('DOMContentLoaded', function() {
            const token = localStorage.getItem('admin_token') || sessionStorage.getItem('admin_token');
            if (!token) {
                alert('Sessão expirada. Por favor, faça login novamente.');
                window.location.href = '/frontend/html/login.html';
            }
        });
    </script>
</body>
</html>
```

## ./frontend/html/home.html

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <!-- Ícones (Font Awesome) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claudinho Ouvidor - A Voz do Povo</title>
    <link rel="stylesheet" href="/frontend/css/styles_home.css">
</head>
<body>
    <!-- Navegação -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo-nav">
                <i class="fas fa-star"></i>
                <span>Claudinho Ouvidor</span>
            </div>
            <ul class="nav-links">
                <li><a href="#inicio">Início</a></li>
                <li><a href="#sobre">Sobre</a></li>
                <li><a href="#calendario">Calendário</a></li>
                <li><a href="#forum">Fórum</a></li>
                <li><a href="#cadastro" class="btn-nav">Seja um Apoiador</a></li>
            </ul>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="inicio" class="hero">
        <div class="hero-content">
            <div class="star-badge">
                <i class="fas fa-star"></i>
            </div>
            <h1>Claudinho Ouvidor</h1>
            <p class="hero-subtitle">A voz do povo na Câmara Municipal</p>
            <p class="hero-description">Compromisso, trabalho e resultados para nossa comunidade</p>
            <div class="hero-buttons">
                <a href="/frontend/html/cadastro.html" class="btn btn-primary">
                    <i class="fas fa-user-plus"></i>
                    Faça parte
                </a>
                <a href="#calendario" class="btn btn-secondary">
                    <i class="fas fa-calendar-alt"></i>
                    Agenda
                </a>
            </div>
        </div>
        <div class="hero-image">
            <div class="photo-placeholder">
                <img src="https://res.cloudinary.com/dwlyqarg2/image/upload/q_auto/Claudinho-Silva_uoysbd.jpg" alt="Foto oficial de Claudinho Ouvidor">
                <span>Foto do Claudinho</span>
            </div>
        </div>
        <div class="wave-bottom"></div>
    </section>

    <!-- Estatísticas -->
    <section class="stats">
        <div class="container">
            <div class="stat-card">
                <i class="fas fa-users"></i>
                <h3>+5.000</h3>
                <p>Pessoas Atendidas</p>
            </div>
            <div class="stat-card">
                <i class="fas fa-check-circle"></i>
                <h3>+200</h3>
                <p>Demandas Resolvidas</p>
            </div>
            <div class="stat-card">
                <i class="fas fa-map-marker-alt"></i>
                <h3>+50</h3>
                <p>Bairros Visitados</p>
            </div>
            <div class="stat-card">
                <i class="fas fa-heart"></i>
                <h3>100%</h3>
                <p>Compromisso</p>
            </div>
        </div>
    </section>

    <!-- Sobre -->
    <section id="sobre" class="sobre">
        <div class="container">
            <div class="section-header">
                <i class="fas fa-star"></i>
                <h2>Quem é Claudinho?</h2>
            </div>
            <div class="sobre-content">
                <div class="sobre-text">
                    <p>Ouvidor do Povo, comprometido em levar as demandas da comunidade até a Câmara Municipal. Trabalho incansável para que a voz de cada cidadão seja ouvida e atendida.</p>
                    <ul class="sobre-lista">
                        <li><i class="fas fa-check"></i> Atendimento direto ao cidadão</li>
                        <li><i class="fas fa-check"></i> Acompanhamento de demandas</li>
                        <li><i class="fas fa-check"></i> Intermediação com órgãos públicos</li>
                        <li><i class="fas fa-check"></i> Fiscalização das políticas públicas</li>
                    </ul>
                </div>
                <div class="sobre-video">
                    <div class="video-placeholder">
                        <i class="fas fa-play-circle"></i>
                        <span>Assista ao vídeo</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Calendário -->
    <section id="calendario" class="calendario">
        <div class="container">
            <div class="section-header light">
                <i class="fas fa-calendar-alt"></i>
                <h2>Próximos Eventos</h2>
                <p>Acompanhe nossa agenda e participe</p>
            </div>
            <div class="eventos-grid">
                <div class="evento-card">
                    <div class="evento-data">
                        <span class="dia">15</span>
                        <span class="mes">MAR</span>
                    </div>
                    <div class="evento-info">
                        <h4>Reunião com Moradores</h4>
                        <p><i class="fas fa-map-marker-alt"></i> Bairro São João</p>
                        <p><i class="fas fa-clock"></i> 19:00</p>
                    </div>
                    <a href="#" class="btn-evento">Participar</a>
                </div>
                <div class="evento-card">
                    <div class="evento-data">
                        <span class="dia">22</span>
                        <span class="mes">MAR</span>
                    </div>
                    <div class="evento-info">
                        <h4>Audiência Pública</h4>
                        <p><i class="fas fa-map-marker-alt"></i> Câmara Municipal</p>
                        <p><i class="fas fa-clock"></i> 14:00</p>
                    </div>
                    <a href="#" class="btn-evento">Participar</a>
                </div>
                <div class="evento-card">
                    <div class="evento-data">
                        <span class="dia">28</span>
                        <span class="mes">MAR</span>
                    </div>
                    <div class="evento-info">
                        <h4>Visita ao Centro Comunitário</h4>
                        <p><i class="fas fa-map-marker-alt"></i> Vila Nova</p>
                        <p><i class="fas fa-clock"></i> 10:00</p>
                    </div>
                    <a href="#" class="btn-evento">Participar</a>
                </div>
            </div>
            <div class="calendario-full">
                <a href="#" class="btn btn-outline-light">
                    <i class="fas fa-calendar"></i>
                    Ver Calendário Completo
                </a>
            </div>
        </div>
    </section>

    <!-- Fórum -->
    <section id="forum" class="forum">
        <div class="container">
            <div class="section-header">
                <i class="fas fa-comments"></i>
                <h2>Fórum de Debates</h2>
                <p>Participe das discussões sobre nossa comunidade</p>
            </div>
            <div class="forum-topicos">
                <div class="topico-card">
                    <div class="topico-icon">
                        <i class="fas fa-road"></i>
                    </div>
                    <h4>Infraestrutura Urbana</h4>
                    <p>Ruas, iluminação, calçadas e transporte</p>
                    <span class="topico-stats">128 participantes</span>
                </div>
                <div class="topico-card">
                    <div class="topico-icon">
                        <i class="fas fa-graduation-cap"></i>
                    </div>
                    <h4>Educação</h4>
                    <p>Escolas, creches e políticas educacionais</p>
                    <span class="topico-stats">95 participantes</span>
                </div>
                <div class="topico-card">
                    <div class="topico-icon">
                        <i class="fas fa-heartbeat"></i>
                    </div>
                    <h4>Saúde</h4>
                    <p>Postos, hospitais e atendimento médico</p>
                    <span class="topico-stats">156 participantes</span>
                </div>
                <div class="topico-card">
                    <div class="topico-icon">
                        <i class="fas fa-briefcase"></i>
                    </div>
                    <h4>Geração de Empregos</h4>
                    <p>Oportunidades e desenvolvimento econômico</p>
                    <span class="topico-stats">87 participantes</span>
                </div>
            </div>
            <div class="forum-cta">
                <a href="#" class="btn btn-primary">
                    <i class="fas fa-sign-in-alt"></i>
                    Entrar no Fórum
                </a>
            </div>
        </div>
    </section>

    <!-- Cadastro CTA -->
    <section id="cadastro" class="cadastro-cta">
        <div class="container">
            <div class="cta-box">
                <div class="cta-content">
                    <i class="fas fa-star"></i>
                    <h2>Faça parte da nossa rede!</h2>
                    <p>Cadastre-se para receber atualizações, participar de eventos e fazer parte das decisões da nossa comunidade.</p>
                    <a href="/frontend/html/cadastro.html" class="btn btn-large">
                        <i class="fas fa-user-plus"></i>
                        Cadastrar Agora
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <i class="fas fa-star"></i>
                    <span>Claudinho Ouvidor</span>
                </div>
                <div class="footer-social">
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                    <a href="#"><i class="fab fa-whatsapp"></i></a>
                    <a href="#"><i class="fab fa-youtube"></i></a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Claudinho Ouvidor. Todos os direitos reservados.</p>
                <p>Feito com <i class="fas fa-heart"></i> pelo povo e para o povo</p>
            </div>
        </div>
    </footer>

    <script src="/frontend/javascript/script_home.js"></script>
</body>
</html>
```

## ./frontend/html/lista.html

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestão de Apoiadores</title>
    <link rel="stylesheet" href="/frontend/css/teste.css">
    <!-- SheetJS Library via CDN -->
    <script src="https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js"></script>
</head>
<body>
    <div class="app-container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="logo">
                    <i class="fas fa-shield-alt"></i>
                    <span>Ferramentas</span>
                </div>
            </div>
            
            <nav class="sidebar-nav">
                <a href="/frontend/html/lista.html" class="nav-item active">
                    <i class="fas fa-users"></i>
                    <span>Listar Usuários</span>
                </a>
                <a href="/frontend/html/disparo_email.html" class="nav-item">
                    <i class="fas fa-paper-plane"></i>
                    <span>Disparador de Email</span>
                </a>
            </nav>
            
            <div class="sidebar-footer">
                <button id="logout-btn" class="btn-logout">
                    <i class="fas fa-sign-out-alt"></i>
                    <span>Sair</span>
                </button>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <!-- Container Superior (Header) -->
            <header class="header">
                <div class="header-left">
                    <div class="logo">Claudinho 2026</div>
                    <h1>Gestão da campanha</h1>
                </div>
                <div class="header-right">
                    <div class="user-info">
                        <span class="user-name">Admin</span>
                        <span class="user-role">Administrador</span>
                    </div>
                    <div class="user-avatar">PT</div>
                </div>
            </header>

            <!-- Container de Filtros -->
            <section class="filters-container">
                <h2>Filtros de Pesquisa</h2>
                <div class="filters-flexbox">
                    <div class="filter-group">
                        <label for="filter-name">Nome Completo</label>
                        <input type="text" id="filter-name" placeholder="Digite o nome...">
                    </div>
                    <div class="filter-group">
                        <label for="filter-email">Email</label>
                        <input type="email" id="filter-email" placeholder="Digite o email...">
                    </div>
                    <div class="filter-group">
                        <label for="filter-theme">Código de Tema</label>
                        <input type="text" id="filter-theme" placeholder="Ex: T001, T002...">
                    </div>
                    <div class="filter-group">
                        <label for="filter-phone">Telefone</label>
                        <input type="text" id="filter-phone" placeholder="Somente os números">
                    </div>
                    <div class="filter-group">
                        <label for="filter-cep">CEP</label>
                        <input type="text" id="filter-cep" placeholder="Somente os números">
                    </div>
                    <div class="filter-group">
                        <label for="filter-city">Cidade</label>
                        <input type="text" id="filter-city" placeholder="Digite a cidade">
                    </div>
                </div>
            </section>

            <!-- Container de Ações -->
            <section class="actions-container">
                <button id="btn-search" class="btn btn-primary">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    Pesquisar
                </button>
                <button id="btn-clear" class="btn btn-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"></path><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"></path><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"></path></svg>
                    Limpar
                </button>
                <button id="btn-export" class="btn btn-success">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                    Exportar para Excel
                </button>
            </section>

            <!-- Container da Tabela -->
            <section class="table-container">
                <div class="table-header">
                    <h3>Lista de Pessoas</h3>
                    <span id="record-count">0 registros encontrados</span>
                </div>
                <div class="table-responsive">
                    <table id="persons-table">
                        <thead>
                            <tr>
                                <th>Nome Completo</th>
                                <th>Email</th>
                                <th>Data de Nascimento</th>
                                <th>Telefone</th>
                                <th>Consentimento</th>
                                <th>CEP</th>
                                <th>Rua</th>
                                <th>Número</th>
                                <th>Bairro</th>
                                <th>Cidade</th>
                                <th>UF</th>
                                <th>Temas</th>
                            </tr>
                        </thead>
                        <tbody id="table-body">
                            <!-- Dados serão inseridos via JavaScript -->
                        </tbody>
                    </table>
                </div>
                <div id="loading" class="loading hidden">
                    <div class="spinner"></div>
                    <span>Carregando dados...</span>
                </div>
                <div id="empty-state" class="empty-state hidden">
                    <p>Nenhum registro encontrado.</p>
                </div>
            </section>
        </main>
    </div>

    <script src="/frontend/javascript/script_lista.js"></script>
</body>
</html>
```

## ./frontend/html/login.html

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - CRM Pro</title>
    <link rel="stylesheet" href="/frontend/css/styles_login.css">
    <!-- Ícones (Font Awesome) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="header-left">
                <div class="logo">
                    <i class="fas fa-shield-alt"></i>
                    <span>Admin CRM</span>
                </div>
                <h1>Acesso Restrito</h1>
            </div>
        </header>

        <!-- Formulário de Login -->
        <div class="login-container">
            <div class="login-card">
                <div class="login-header">
                    <div class="login-icon">
                        <i class="fas fa-user-lock"></i>
                    </div>
                    <h2>Autenticação Necessária</h2>
                    <p>Área administrativa para gestão de apoiadores</p>
                </div>

                <form id="loginForm" class="login-form">
                    <div class="form-group">
                        <label for="email">
                            <i class="fas fa-envelope"></i>
                            Email
                        </label>
                        <input 
                            type="email" 
                            id="email" 
                            name="email" 
                            placeholder="admin@exemplo.com" 
                            required
                            autocomplete="email"
                        >
                    </div>

                    <div class="form-group">
                        <label for="password">
                            <i class="fas fa-lock"></i>
                            Senha
                        </label>
                        <div class="password-wrapper">
                            <input 
                                type="password" 
                                id="password" 
                                name="password" 
                                placeholder="••••••••" 
                                required
                                autocomplete="current-password"
                            >
                            <button type="button" id="togglePassword" class="toggle-password">
                                <i class="fas fa-eye"></i>
                            </button>
                        </div>
                    </div>

                    <div class="form-options">
                        <label class="remember-me">
                            <input type="checkbox" id="remember" name="remember">
                            <span>Lembrar-me</span>
                        </label>
                        <a href="#" class="forgot-link">Esqueci minha senha</a>
                    </div>

                    <button type="submit" class="btn btn-primary btn-large">
                        <span class="btn-text">Entrar</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>

                    <div id="error-message" class="error-message hidden">
                        <i class="fas fa-exclamation-circle"></i>
                        <span></span>
                    </div>
                </form>

                <div class="login-footer">
                    <p>Área restrita a administradores autorizados</p>
                    <p class="security-info">
                        <i class="fas fa-shield-alt"></i>
                        Conexão segura com autenticação JWT
                    </p>
                </div>
            </div>
        </div>
    </div>

    <script src="/frontend/javascript/script_login.js"></script>
</body>
</html>
```

## ./frontend/html/teste.html

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - CRM Pro</title>
    <link rel="stylesheet" href="/frontend/css/teste.css">
    <!-- Chart.js via CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="app-container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="logo">
                    <i class="fas fa-chart-line"></i>
                    <span>Analytics</span>
                </div>
            </div>
            
            <nav class="sidebar-nav">
                <a href="/frontend/html/dashboard.html" class="nav-item active">
                    <i class="fas fa-chart-bar"></i>
                    <span>Dashboard</span>
                </a>
                <a href="/frontend/html/lista.html" class="nav-item">
                    <i class="fas fa-users"></i>
                    <span>Listar Usuários</span>
                </a>
                <a href="/frontend/html/disparador-email.html" class="nav-item">
                    <i class="fas fa-paper-plane"></i>
                    <span>Disparador de Email</span>
                </a>
            </nav>
            
            <div class="sidebar-footer">
                <button id="logout-btn" class="btn-logout">
                    <i class="fas fa-sign-out-alt"></i>
                    <span>Sair</span>
                </button>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <header class="header">
                <div class="header-left">
                    <div class="logo">Analytics</div>
                    <h1>Dashboard de Apoiadores</h1>
                </div>
                <div class="header-right">
                    <div class="user-info">
                        <span class="user-name">Admin User</span>
                        <span class="user-role">Administrador</span>
                    </div>
                    <div class="user-avatar">AU</div>
                </div>
            </header>

            <!-- Cards de Métricas -->
            <section class="metrics-container">
                <div class="metric-card">
                    <div class="metric-icon">
                        <i class="fas fa-users"></i>
                    </div>
                    <div class="metric-content">
                        <span class="metric-value" id="total-users">0</span>
                        <span class="metric-label">Total de Apoiadores</span>
                    </div>
                </div>

                <div class="metric-card">
                    <div class="metric-icon">
                        <i class="fas fa-check-circle"></i>
                    </div>
                    <div class="metric-content">
                        <span class="metric-value" id="consent-rate">0%</span>
                        <span class="metric-label">Taxa de Consentimento</span>
                    </div>
                </div>

                <div class="metric-card">
                    <div class="metric-icon">
                        <i class="fas fa-map-marker-alt"></i>
                    </div>
                    <div class="metric-content">
                        <span class="metric-value" id="total-states">0</span>
                        <span class="metric-label">Estados Atendidos</span>
                    </div>
                </div>

                <div class="metric-card">
                    <div class="metric-icon">
                        <i class="fas fa-star"></i>
                    </div>
                    <div class="metric-content">
                        <span class="metric-value" id="avg-age">0</span>
                        <span class="metric-label">Idade Média</span>
                    </div>
                </div>
            </section>

            <!-- Gráficos -->
            <section class="charts-container">
                <div class="chart-card">
                    <div class="chart-header">
                        <h3>Temas de Interesse</h3>
                        <p>Distribuição por áreas de interesse</p>
                    </div>
                    <div class="chart-wrapper">
                        <canvas id="themesChart"></canvas>
                    </div>
                </div>

                <div class="chart-card">
                    <div class="chart-header">
                        <h3>Distribuição por Estado</h3>
                        <p>Apoiadores por UF</p>
                    </div>
                    <div class="chart-wrapper">
                        <canvas id="statesChart"></canvas>
                    </div>
                </div>

                <div class="chart-card full-width">
                    <div class="chart-header">
                        <h3>Faixa Etária</h3>
                        <p>Distribuição por idade dos apoiadores</p>
                    </div>
                    <div class="chart-wrapper">
                        <canvas id="ageChart"></canvas>
                    </div>
                </div>
            </section>

            <!-- Últimos Cadastros -->
            <section class="table-container">
                <div class="table-header">
                    <h3>Últimos Cadastros</h3>
                    <span id="recent-count">mostrando 5 recentes</span>
                </div>
                <div class="table-responsive">
                    <table id="recent-table">
                        <thead>
                            <tr>
                                <th>Nome</th>
                                <th>Email</th>
                                <th>Cidade</th>
                                <th>Interesses</th>
                            </tr>
                        </thead>
                        <tbody id="recent-body">
                            <!-- Dados serão inseridos via JavaScript -->
                        </tbody>
                    </table>
                </div>
            </section>
        </main>
    </div>

    <script src="/frontend/javascript/script_dashboard.js"></script>
</body>
</html>
```

## ./frontend/index.html

```html


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meus Links - CRM Pro</title>
    <!-- variaveis online começa sem a frontend // offline botar o /frontend-->
    <link rel="stylesheet" href="/frontend/css/styles_index.css">
    <!-- Ícones (Font Awesome) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <!-- Perfil -->
        <div class="profile">
            <div class="avatar">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/PT_%28Brazil%29_logo_2021.svg/960px-PT_%28Brazil%29_logo_2021.svg.png" alt="Foto de perfil">
                <!-- Ou use uma imagem local: <img src="img/logo.png" alt="Logo"> -->
            </div>
            <h1>Claudinho <br> OUVIDOR DO POVO</h1>
            <p class="bio">2026</p>
        </div>

        <!-- Links -->
        <div class="links">
            <!-- Botão 1: Formulário de Cadastro -->
            <a href="/frontend/html/cadastro.html" class="link-button">
                <i class="fas fa-user-plus"></i>
                <span>Seja um Apoiador</span>
            </a>

            <!-- Botão 2: Site pessoal -->
            <a href="/frontend/html/home.html" class="link-button">
                <i class="fas fa-users"></i>
                <span>Saiba mais do nosso candidado</span>
            </a>

            <!-- Botão 3: calendario -->
            <a href="*" class="link-button">
                <i class="fas fa-calendar-alt"></i>
                <span>Calendário da Campanha</span>
            </a>

            <!-- Botão 3: calendario -->
            <a href="https://forms.gle/Zbf222yi3a4negWb9 " class="link-button">
                <i class="fas fa-calendar-alt"></i>
                <span>Proponha uma agênda/evento</span>
            </a>

            <!-- Botão 4: WhatsApp -->
            <a href="https://chat.whatsapp.com/HFrd79nQFG7HeQbLchvehW?mode=gi_t" target="_blank" class="link-button whatsapp">
                <i class="fab fa-whatsapp"></i>
                <span>Falar no WhatsApp</span>
            </a>

            <!-- Botão 5: Instagram -->
            <a href="https://instagram.com/seuinstagram" target="_blank" class="link-button instagram">
                <i class="fab fa-instagram"></i>
                <span>Seguir no Instagram</span>
            </a>

            <!-- Botão 6: Email -->
            <a href="mailto:contato@crmpro.com.br" class="link-button email">
                <i class="fas fa-envelope"></i>
                <span>Enviar E-mail</span>
            </a>
        </div>

        <!-- Redes Sociais (ícones pequenos) -->
        <div class="social-icons">
            <a href="https://facebook.com" target="_blank"><i class="fab fa-facebook"></i></a>
            <a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>
            <a href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://youtube.com" target="_blank"><i class="fab fa-youtube"></i></a>
        </div>

        <!-- Footer -->
        <footer>
            <p> © WebHouse-Service - FEITO POR HUMANOS - Todos os direitos reservados</p>
        </footer>
    </div>
</body>
</html>
```

## ./frontend/javascript/script_cadastro.js

```js
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
            const response = await fetch("https://back-claudinho.onrender.com/person/", {
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



```

## ./frontend/javascript/script_home.js

```js
// Menu mobile
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Fechar menu ao clicar em link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

// Animação de entrada ao scroll
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
}, observerOptions);

document.querySelectorAll('.stat-card, .evento-card, .topico-card').forEach(el => {
    observer.observe(el);
});
```

## ./frontend/javascript/script_lista.js

```js
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

```

## ./frontend/javascript/script_login.js

```js
// Configuração da API Supabase
const SUPABASE_URL = 'https://lipajeykqlitxzooxjza.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable__-e1dxqLKevQ6Lga5YmJWQ_7o3Q56UN'

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

```

## ./frontend/javascript/teste.js

```js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("cadastroForm");
    const btnBuscarCep = document.getElementById("btn-buscar-cep");

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
            const response = await fetch("http://127.0.0.1:8000/person/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const result = await response.json();

            if (response.ok) {
                alert("Cadastro realizado com sucesso 🚀");
                form.reset();
                window.location.href = "https://chat.whatsapp.com/JtuEts8xfCnFzlq92JuMaH?mode=gi_t";
            } else {
                alert("Erro: " + (result.detail || "Falha no cadastro"));
            }
        } catch (error) {
            console.error("Erro de conexão:", error);
            alert("Erro ao conectar com o servidor.");
        }
    });
});



```
