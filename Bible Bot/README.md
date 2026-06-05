# 📖 Vulgata Discord Bot

![St.Jerome](image.png)

Bot para Discord desenvolvido em Python com o objetivo de consultar versículos da Bíblia Sagrada na tradução da **Vulgata Latina** diretamente por meio de comandos Slash Commands.

O sistema realiza buscas dinâmicas na plataforma Vulgata Online, processa o conteúdo HTML retornado e entrega ao usuário o texto completo dos versículos solicitados dentro do próprio Discord.

---

# 📚 Funcionalidades

- Consulta de versículos da Vulgata Latina
- Suporte a capítulos e versículos específicos
- Suporte a intervalos de versículos
- Comandos Slash do Discord
- Seleção guiada de livros através de menus de opções
- Separação entre Antigo e Novo Testamento
- Busca automática em tempo real na Vulgata Online
- Extração e tratamento do conteúdo HTML
- Resposta instantânea dentro do servidor Discord

---

# ⚙️ Como funciona

O fluxo de funcionamento do bot é composto pelas seguintes etapas:

1. O usuário executa um comando Slash.
2. Seleciona um livro bíblico.
3. Informa capítulo e versículo.
4. O bot monta a URL correspondente.
5. A página da Vulgata Online é consultada.
6. O HTML é processado com BeautifulSoup.
7. O versículo solicitado é localizado.
8. O texto é retornado ao Discord.

---

# 📖 Comandos Disponíveis

## `/biblia1`

Consulta os primeiros 25 livros do Antigo Testamento.

Exemplo:

```text
/biblia1
Livro: Gênesis
Capítulo e Versículo: 1,1
```

---

## `/biblia2`

Consulta os últimos 21 livros do Antigo Testamento.

Exemplo:

```text
/biblia2
Livro: Profecia de Isaías
Capítulo e Versículo: 53,5
```

---

## `/biblia3`

Consulta os primeiros 25 livros do Novo Testamento.

Exemplo:

```text
/biblia3
Livro: Evangelho Segundo S. João
Capítulo e Versículo: 3,16
```

---

## `/biblia4`

Consulta os dois últimos livros do Novo Testamento.

Exemplo:

```text
/biblia4
Livro: Apocalipse de S. João
Capítulo e Versículo: 21,4
```

---

# 🔍 Formato de Consulta

O parâmetro de capítulo e versículo deve seguir o formato:

```text
capitulo,versiculo
```

Exemplo:

```text
3,16
```

Também é possível informar intervalos:

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
project/
│
├── main.py
├── config.py
├── .env.example
├── .gitignore
│
├── book_lists/
│   ├── antigo_testamento1.py
│   ├── antigo_testamento2.py
│   ├── novo_testamento1.py
│   ├── novo_testamento2.py
│   └── books_lists.py
│
├── functions/
│   ├── pegar_versiculo.py
└── requirements.txt
```

---

# 📚 Bibliotecas Utilizadas

## Discord.py

Biblioteca principal utilizada para comunicação com a API do Discord.

Utilizada para:

- Criação do bot
- Slash Commands
- Opções de seleção
- Envio de respostas

Documentação:

https://discordpy.readthedocs.io

---

## Requests

Responsável pelas requisições HTTP para a Vulgata Online.

Exemplo:

```python
response = requests.get(url)
```

Documentação:

https://requests.readthedocs.io

---

## BeautifulSoup4

Responsável pelo parsing do HTML retornado pela Vulgata Online.

Exemplo:

```python
soup = BeautifulSoup(html, "html.parser")
```

Documentação:

https://www.crummy.com/software/BeautifulSoup

---

## Regex (re)

Utilizada para validar e interpretar o formato:

```text
capitulo,versiculo
```

ou

```text
capitulo,versiculo-inicio
```

Exemplo:

```python
r'^(.+) (\d+),(\d+)(-(\d+))?$'
```

Documentação:

https://docs.python.org/3/library/re.html

---

# 🌐 Fonte dos Dados

Todos os textos bíblicos são obtidos em tempo real através de:

https://vulgata.online

O projeto não armazena os textos bíblicos localmente.

---

# 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/vulgata-discord-bot.git
```

Entre na pasta:

```bash
cd vulgata-discord-bot
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure seu Token do Discord:

```python
TOKEN = "SEU_TOKEN"
```

Execute:

```bash
python main.py
```

---

# 📄 Exemplo de Resposta

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