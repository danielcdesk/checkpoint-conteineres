# 📦 Controle de Organização de Contêineres

> 🎓 **Projeto acadêmico desenvolvido para a disciplina de Programação 2.**

Aplicação desktop em **Python** para simular a organização de contêineres recém-chegados em um **pátio logístico**. O projeto foi desenvolvido com foco na aplicação prática de **lógica de programação estruturada, matrizes e interface gráfica**.

## 🎯 Objetivo

Demonstrar, de forma visual e funcional, como uma **matriz bidimensional** pode ser utilizada para representar e controlar posições de armazenamento em um pátio.

A matriz principal possui **5 linhas × 6 colunas**, totalizando **30 posições**:

- `0` → posição livre;
- `1` → posição ocupada por um contêiner.

Cada posição exibida na interface corresponde diretamente a uma posição da matriz utilizada pela aplicação.

## ✨ Funcionalidades

- 📥 Registrar a chegada de um contêiner;
- 🆔 Associar uma identificação ao contêiner armazenado;
- 🗺️ Visualizar as 30 posições do pátio;
- ✅ Identificar posições livres e ocupadas;
- 📤 Registrar a saída de um contêiner e liberar sua posição;
- 🔎 Impedir o cadastro duplicado do mesmo código de contêiner;
- 📊 Exibir a quantidade de posições ocupadas e disponíveis;
- 🧾 Gerar um resumo dos contêineres presentes no pátio;
- 📈 Manter o total de chegadas registradas durante a execução;
- 🏁 Exibir um resumo final ao encerrar o sistema.

## 🧠 Conceitos aplicados

- Matrizes bidimensionais;
- Estruturas condicionais;
- Estruturas de repetição;
- Funções e métodos;
- Manipulação de estado;
- Validação de dados;
- Eventos de interface gráfica;
- Organização básica de código em Python.

## 🛠️ Tecnologias

- **Python 3**
- **Tkinter** — biblioteca gráfica incluída na instalação padrão do Python
- **Git** e **GitHub** — versionamento e portfólio acadêmico

Não é necessário instalar bibliotecas externas.

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/danielcdesk/checkpoint-conteineres.git
```

### 2. Acesse a pasta

```bash
cd checkpoint-conteineres
```

### 3. Execute a aplicação

No Windows:

```bash
py main.py
```

ou:

```bash
python main.py
```

## 🗂️ Estrutura do projeto

```text
checkpoint-conteineres/
├── main.py
├── README.md
├── REGRA_DE_NEGOCIO.md
└── .gitignore
```

## 📐 Representação do pátio

```text
       1    2    3    4    5    6
A     A1   A2   A3   A4   A5   A6
B     B1   B2   B3   B4   B5   B6
C     C1   C2   C3   C4   C5   C6
D     D1   D2   D3   D4   D5   D6
E     E1   E2   E3   E4   E5   E6
```

O estado de cada posição é armazenado na matriz `ocupacao`.

## 🏫 Contexto acadêmico

Este repositório foi publicado para fins **acadêmicos, educacionais e de portfólio**. O sistema representa uma simulação simplificada de um pátio logístico e **não pretende substituir soluções profissionais utilizadas em terminais portuários ou operadores logísticos reais**.

Por segurança e privacidade, esta versão pública **não inclui nomes de integrantes, matrículas, documentos institucionais, capturas de tela, credenciais ou outros dados pessoais**.

## 🔐 Segurança e privacidade

O projeto não utiliza chaves de API, tokens, senhas ou serviços externos. Arquivos locais de configuração, ambientes virtuais, caches e possíveis arquivos de credenciais são ignorados pelo Git por meio do `.gitignore`.

> ⚠️ Nunca publique senhas, tokens, arquivos `.env`, credenciais ou dados pessoais em repositórios públicos.

---

### 💻 Portfólio acadêmico

Projeto criado para registrar a evolução prática no uso de **Python, Git, GitHub, interfaces gráficas e lógica de programação**.
