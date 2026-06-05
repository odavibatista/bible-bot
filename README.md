# 📖 Vulgata Discord Bot

![São Jerônimo](image.png)

Bot para Discord desenvolvido em Python com o objetivo de consultar versículos da Bíblia Sagrada na tradução da **Vulgata Latina** diretamente através de comandos Slash Commands.

O sistema realiza buscas dinâmicas na plataforma **Vulgata Online**, processa o conteúdo HTML retornado e entrega ao usuário o texto completo dos versículos solicitados dentro do próprio Discord.

Você pode utilizar esse modelo de bot e adaptá-lo de acordo com suas necessidades, além de fazer o deploy dele em seu servidor ou até mesmo em algum provedor. Um dos que recomendo é o [Daki Bot Hosting](https://daki.cc/), que suporta tanto bots feitos em Python quanto em Node.js, com uma interface fácil de usar e preços acessíveis (além de clusters free para testes).

---

# 📑 Índice

- [Funcionalidades](#-funcionalidades)
- [Como Funciona](#️-como-funciona)
- [Comandos Disponíveis](#-comandos-disponíveis)
- [Formato de Consulta](#-formato-de-consulta)
- [Estrutura do Projeto](#️-estrutura-do-projeto)
- [Bibliotecas Utilizadas](#-bibliotecas-utilizadas)
- [Testes Unitários](#-testes-unitários)
- [Fonte dos Dados](#-fonte-dos-dados)
- [Instalação](#-instalação)
- [Exemplo de Uso](#-exemplo-de-uso)
- [Melhorias Futuras](#-melhorias-futuras)

---

# 📚 Funcionalidades

- Consulta de versículos da Vulgata Latina
- Suporte a capítulos e versículos específicos
- Suporte a intervalos de versículos
- Comandos Slash do Discord
- Menus de seleção para escolha dos livros
- Separação entre Antigo e Novo Testamento
- Busca automática em tempo real na Vulgata Online
- Extração e processamento de conteúdo HTML
- Resposta instantânea dentro do servidor Discord
- Organização modular do código
- Suporte a testes unitários
- Configuração segura através de variáveis de ambiente

---

# ⚙️ Como Funciona

O fluxo de funcionamento do bot é composto pelas seguintes etapas:

1. O usuário executa um comando Slash.
2. Seleciona um livro bíblico.
3. Informa capítulo e versículo.
4. O bot identifica a URL correspondente ao livro.
5. A página da Vulgata Online é consultada.
6. O HTML é processado utilizando BeautifulSoup.
7. Os versículos são localizados através de expressões regulares.
8. O texto é retornado ao usuário dentro do Discord.

---

# 📖 Comandos Disponíveis

## `/biblia1`

Consulta os primeiros 25 livros do Antigo Testamento.

### Exemplo

```text
/biblia1
Livro: Gênesis
Capítulo e Versículo: 1,1
```

---

## `/biblia2`

Consulta os últimos 21 livros do Antigo Testamento.

### Exemplo

```text
/biblia2
Livro: Profecia de Isaías
Capítulo e Versículo: 53,5
```

---

## `/biblia3`

Consulta os primeiros 25 livros do Novo Testamento.

### Exemplo

```text
/biblia3
Livro: Evangelho Segundo S. João
Capítulo e Versículo: 3,16
```

---

## `/biblia4`

Consulta os dois últimos livros do Novo Testamento.

### Exemplo

```text
/biblia4
Livro: Apocalipse de S. João
Capítulo e Versículo: 21,4
```

---

# 🔍 Formato de Consulta

## Versículo único

```text
capitulo,versiculo
```

Exemplo:

```text
3,16
```

---

## Intervalo de versículos

```text
capitulo,versiculoInicial-versiculoFinal
```

Exemplo:

```text
3,16-18
```

Resultado:

```text
João 3:16-18
```

---

# 🏗️ Estrutura do Projeto

```text
vulgata-discord-bot/
│
├── main.py
├── config.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
│
├── services/
│   └── verse_fetcher.py
│
├── book_lists/
│   ├── __init__.py
│   ├── books_lists.py
│   ├── antigo_testamento1.py
│   ├── antigo_testamento2.py
│   ├── novo_testamento1.py
│   └── novo_testamento2.py
│
└── tests/
    ├── test_regex.py
    ├── test_verse_fetcher.py
    └── fixtures/
```

---

# 📚 Bibliotecas Utilizadas

## PyCord

Biblioteca utilizada para integração com a API do Discord.

Responsável por:

- Slash Commands
- Interações
- Respostas aos usuários
- Estrutura do bot

Documentação:

https://docs.pycord.dev

---

## Requests

Responsável pelas requisições HTTP para a Vulgata Online.

```python
response = requests.get(url)
```

Documentação:

https://requests.readthedocs.io

---

## BeautifulSoup4

Responsável pelo parsing do HTML retornado.

```python
soup = BeautifulSoup(html, "html.parser")
```

Documentação:

https://www.crummy.com/software/BeautifulSoup

---

## LXML

Parser HTML de alta performance utilizado pelo BeautifulSoup.

```python
soup = BeautifulSoup(html, "lxml")
```

Documentação:

https://lxml.de

---

## Regex (re)

Utilizada para validação e interpretação das referências bíblicas.

```python
r'^(.+) (\d+),(\d+)(-(\d+))?$'
```

Documentação:

https://docs.python.org/3/library/re.html

---

## Python Dotenv

Utilizado para carregamento seguro das variáveis de ambiente.

```python
from dotenv import load_dotenv
```

Documentação:

https://pypi.org/project/python-dotenv

---

# 🧪 Testes Unitários

O projeto possui suporte para testes unitários utilizando **PyTest**.

Os testes contemplam:

- Validação da Regex de referências bíblicas
- Extração de versículos
- Tratamento dos intervalos de versículos
- Mock de requisições HTTP

---

## Bibliotecas de Desenvolvimento

### PyTest

Framework principal de testes.

```bash
pytest
```

Documentação:

https://docs.pytest.org

---

### PyTest Mock

Utilizado para mockar chamadas externas.

```python
@patch("requests.get")
```

Documentação:

https://pytest-mock.readthedocs.io

---

# 🌐 Fonte dos Dados

Todos os textos bíblicos são obtidos em tempo real através de:

https://vulgata.online

O projeto não armazena textos bíblicos localmente.

Todos os direitos dos textos pertencem aos respectivos mantenedores da plataforma.

---

# 🚀 Instalação

## Clonando o projeto

```bash
git clone https://github.com/seu-usuario/vulgata-discord-bot.git
```

```bash
cd vulgata-discord-bot
```

---

## Criando ambiente virtual

Linux/Mac:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

## Instalando dependências

```bash
pip install -r requirements.txt
```

---

## Configurando o Token

Crie um arquivo `.env`:

```env
DISCORD_TOKEN=SEU_TOKEN_AQUI
```

Ou copie:

```bash
cp .env.example .env
```

---

## Executando

```bash
python main.py
```

---

# 📄 Exemplo de Uso

Entrada:

```text
/biblia3
Livro: Evangelho Segundo S. João
Capítulo e Versículo: 3,16
```

Saída:

```text
[16] Sic enim Deus dilexit mundum, ut Filium suum unigenitum daret...
```

---

# 🚀 Melhorias Futuras

- Unificar os quatro comandos em um único `/biblia`
- Implementar cache de consultas
- Utilizar Embeds do Discord para respostas mais elegantes
- Adicionar suporte a outras traduções bíblicas
- Migrar os livros para arquivos JSON
- Adicionar GitHub Actions para CI/CD
- Implementar paginação para passagens longas
- Adicionar pesquisa por palavras-chave
- Disponibilizar Dockerfile para execução em containers

---

# 👨‍💻 Autor

Projeto desenvolvido para estudo e prática de:

- Python
- APIs Discord
- Web Scraping
- Processamento de Texto
- Expressões Regulares
- Arquitetura de Software
- Testes Automatizados
- Automação de Consultas Bíblicas