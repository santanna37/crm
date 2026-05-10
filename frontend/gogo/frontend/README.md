# Projeto CRM Campanha Política 2026

## Estrutura do Projeto

```
/frontend/
  ├── css/
  │   └── theme.css          # CSS ÚNICO para todas as páginas
  ├── js/
  │   ├── app.js             # Módulos compartilhados (Auth, API, Utils, CEP)
  │   ├── index.js           # Página de Links/Bio
  │   ├── home.js            # Landing Page
  │   ├── cadastro.js        # Formulário de Apoiadores
  │   ├── calendario.js      # Calendário de Eventos
  │   ├── login.js           # Autenticação Admin
  │   ├── dashboard.js       # Painel Administrativo
  │   └── lista.js           # Lista de Apoiadores
  ├── index.html             # Página de Links/Bio
  ├── home.html              # Site Principal (Landing Page)
  ├── cadastro.html          # Formulário de Apoiadores
  ├── calendario.html        # Calendário de Eventos 2026
  ├── login.html             # Login Administrativo
  ├── dashboard.html         # Dashboard Admin
  ├── lista.html             # Gestão de Apoiadores
  ├── disparo.html           # Disparo de Emails (em desenvolvimento)
  └── fundacao.html          # Página em Construção
```

## Páginas Públicas (Sem Login)

| Página | Descrição |
|--------|-----------|
| `index.html` | Página de links/bio do candidato |
| `home.html` | Landing page completa com stats, sobre, eventos, fórum |
| `cadastro.html` | Formulário para cadastro de apoiadores |
| `calendario.html` | Calendário interativo de eventos 2026 |
| `fundacao.html` | Página "em construção" para funcionalidades futuras |

## Páginas Administrativas (Requer Login)

| Página | Descrição |
|--------|-----------|
| `login.html` | Tela de autenticação via Supabase |
| `dashboard.html` | Dashboard com métricas e gráficos (Chart.js) |
| `lista.html` | Lista filtrável e exportável de apoiadores (SheetJS) |
| `disparo.html` | Disparador de emails (placeholder) |

## CSS Único - theme.css

Todas as páginas usam o mesmo arquivo `theme.css` com:

- **Sistema de containers**: `.container`, `.container-sm`, `.container-md`, `.container-lg`
- **Layout com sidebar**: `.page-layout` + `.sidebar` + `.main-content`
- **Componentes padronizados**: cards, buttons, forms, tables, badges, metrics
- **Variáveis CSS**: cores azul (#1d4ed8), sombras, espaçamentos, bordas arredondadas
- **Responsividade**: breakpoints em 1024px, 768px e 480px

## JS Compartilhado - app.js

Módulos globais disponíveis em todas as páginas admin:

- `Auth` - Gerenciamento de autenticação (login/logout/token)
- `API` - Requisições HTTP para o backend
- `Utils` - Formatação de data, telefone, CEP, loading states
- `CEP` - Busca de endereço via ViaCEP

## Configuração

Edite `app.js` para alterar:
- `API_BASE_URL` - URL do backend FastAPI
- `SUPABASE_URL` e `SUPABASE_ANON_KEY` - Credenciais do Supabase

## Uso

1. Abra `index.html` para acessar a página pública de links
2. Navegue pelas páginas públicas sem necessidade de login
3. Acesse `login.html` para entrar na área administrativa
4. Use `dashboard.html` para visualizar métricas
5. Use `lista.html` para gerenciar e exportar apoiadores

## Dependências Externas (CDN)

- Font Awesome 6.4.0 (ícones)
- Google Fonts - Montserrat (tipografia)
- Chart.js (gráficos no dashboard)
- SheetJS (exportação Excel na lista)
