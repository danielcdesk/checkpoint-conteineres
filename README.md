# 🚢 Controle de Contêineres

Aplicação acadêmica desenvolvida em **Python** para a disciplina **Programação 2**. O projeto simula o controle de um pátio logístico usando uma matriz, regras de negócio explícitas e uma interface gráfica desktop com Tkinter.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Interface](https://img.shields.io/badge/Interface-Tkinter-2F6FA3)](https://docs.python.org/3/library/tkinter.html)
[![Paradigma](https://img.shields.io/badge/Paradigma-Procedural-5B8C5A)](#-requisitos-atendidos)
[![Status](https://img.shields.io/badge/Status-Checkpoint%203-6C63FF)](#-execução)

## 🎯 Objetivo

Representar visualmente um pátio com **5 linhas × 6 colunas**, totalizando **30 posições**. A matriz é a fonte de verdade do sistema:

- `0` → posição livre;
- `1` → posição ocupada.

A interação é direta: o usuário informa a identificação do contêiner e clica na posição desejada. O programa valida a operação, atualiza a matriz e mantém os indicadores da tela sincronizados.

## ✨ Funcionalidades

- 🟢 Registro de chegada em uma posição livre;
- 🔴 Registro de saída com confirmação do usuário;
- 🧾 Identificação armazenada em cada posição ocupada;
- 🛡️ Bloqueio de identificações duplicadas;
- 📊 Atualização imediata de posições ocupadas, livres e chegadas;
- 🧭 Visualização das posições no formato `A1` até `E6`;
- 📋 Resumo final com a situação do pátio ao encerrar;
- 🎨 Interface organizada com widgets `ttk`, estilo nativo, cores e legenda visual.

## 🖥️ Como usar

1. Digite a identificação do contêiner.
2. Clique em uma posição marcada como **LIVRE**.
3. Para liberar uma posição **OCUPADA**, clique nela e confirme a saída.
4. Consulte os cartões de ocupação, disponibilidade e movimentação.
5. Clique em **Encerrar e ver resumo** para visualizar o estado final.

## ⚙️ Execução

O projeto não utiliza bibliotecas externas. É necessário ter **Python 3** com suporte ao Tkinter.

```powershell
git clone https://github.com/danielcdesk/checkpoint-conteineres.git
cd checkpoint-conteineres
py main.py
```

Se o comando `py` não estiver disponível, use:

```powershell
python main.py
```

## 🧩 Requisitos atendidos

- Python com `tkinter` e `tkinter.ttk`;
- estilo nativo configurado com `ttk.Style`;
- paradigma estritamente procedural, sem classes próprias;
- matriz 5 × 6 como fonte de verdade do pátio;
- validações e confirmações com `messagebox`;
- organização visual com os gerenciadores `grid` e `pack`;
- comentários pedagógicos sobre estruturas de controle e funções nativas de alto nível.

## 📁 Estrutura do projeto

```text
checkpoint-conteineres/
├── main.py                 # Interface e lógica principal
├── README.md               # Documentação do projeto
├── REGRA_DE_NEGOCIO.md     # Fluxos e regras no formato Dado Quando Então
├── ROADMAP.md              # Planejamento de evoluções
├── MEMORY.md               # Memória de trabalho e contexto arquitetural
└── ia/
    └── Prompt Python.md    # Especificação pedagógica utilizada no projeto
```

## 🧪 Verificação local

Para verificar a sintaxe do código, execute:

```powershell
python -m py_compile main.py
```

Depois, abra a aplicação em um ambiente gráfico para conferir os cliques, as validações, as caixas de diálogo e o resumo final.

## 🔒 Privacidade

O repositório público foi mantido sem nomes completos de integrantes, matrículas, documentos institucionais, capturas de tela, senhas, tokens ou chaves de API. As informações de equipe pertencem somente ao arquivo privado de entrega, quando necessário.

## 📌 Repositório

🔗 [github.com/danielcdesk/checkpoint-conteineres](https://github.com/danielcdesk/checkpoint-conteineres)

Projeto acadêmico desenvolvido para o Checkpoint 3 de Programação 2.
