"""Controle de ocupação de um pátio logístico usando matriz e Tkinter."""

import tkinter as tk
from tkinter import messagebox, ttk


# Constantes que definem o tamanho fixo do pátio da atividade.
LINHAS = 5
COLUNAS = 6
TOTAL_POSICOES = 30

# MATRIZ DE ESTADO: 0 representa posição livre e 1 representa posição ocupada.
ocupacao = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

# MATRIZ paralela que armazena a identificação de cada posição ocupada.
identificacoes = [
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
]

# Variáveis globais da interface. Elas compartilham o estado com as funções.
janela = None
codigo_var = None
texto_ocupadas = None
texto_livres = None
texto_chegadas = None
botoes = []
total_chegadas = 0


def codigo_da_posicao(linha, coluna):
    """Transforma índices da matriz em um rótulo compreensível, como A1."""
    return chr(65 + linha) + str(coluna + 1)


def contar_ocupadas():
    """Percorre a matriz inteira e devolve quantas posições possuem valor 1."""
    total = 0

    # REPETIÇÃO: cada linha e coluna da matriz é verificada uma vez.
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if ocupacao[linha][coluna] == 1:
                total = total + 1
    return total


def codigo_ja_registrado(codigo):
    """Evita que um mesmo contêiner fique em duas posições ao mesmo tempo."""
    encontrado = False

    # REPETIÇÃO e SELEÇÃO: compara o código informado com cada célula ocupada.
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if identificacoes[linha][coluna] == codigo:
                encontrado = True
    return encontrado


def atualizar_botao(linha, coluna):
    """Reflete no botão o valor atual armazenado na posição da matriz."""
    posicao = codigo_da_posicao(linha, coluna)

    # SELEÇÃO: a apresentação acompanha diretamente o estado 0 ou 1 da matriz.
    if ocupacao[linha][coluna] == 1:
        texto = posicao + "\nOCUPADA\n" + identificacoes[linha][coluna]
        # configure() atualiza propriedades do botão já criado, sem criar outro.
        botoes[linha][coluna].configure(text=texto, style="Ocupada.TButton")
    else:
        texto = posicao + "\nLIVRE"
        # configure() atualiza propriedades do botão já criado, sem criar outro.
        botoes[linha][coluna].configure(text=texto, style="Livre.TButton")


def atualizar_resumo():
    """Atualiza em tempo real os indicadores apresentados na interface."""
    ocupadas = contar_ocupadas()
    livres = TOTAL_POSICOES - ocupadas

    # set() troca o texto ligado à Label; substitui a alteração manual do rótulo.
    texto_ocupadas.set("Posições ocupadas: " + str(ocupadas))
    # set() troca o texto ligado à Label; substitui a alteração manual do rótulo.
    texto_livres.set("Posições livres: " + str(livres))
    # set() troca o texto ligado à Label; substitui a alteração manual do rótulo.
    texto_chegadas.set("Chegadas registradas: " + str(total_chegadas))


def registrar_chegada(linha, coluna):
    """Valida o código digitado e grava a chegada na posição livre selecionada."""
    global total_chegadas

    # get() lê o conteúdo do campo de texto para que o programa possa validá-lo.
    codigo = codigo_var.get()
    # strip() remove espaços nas extremidades e upper() padroniza letras em maiúsculas.
    # Esses métodos substituem uma limpeza manual caractere por caractere.
    codigo = codigo.strip().upper()

    # SELEÇÃO: impede registrar dados ausentes ou formados apenas por espaços.
    if codigo == "":
        messagebox.showwarning(
            "Código obrigatório",
            "Digite a identificação do contêiner antes de selecionar uma posição livre.",
            parent=janela,
        )
        return

    # SELEÇÃO: impede duplicidade e mantém a matriz consistente.
    if codigo_ja_registrado(codigo):
        messagebox.showwarning(
            "Contêiner já registrado",
            "A identificação " + codigo + " já está armazenada no pátio.",
            parent=janela,
        )
        return

    # SEQUÊNCIA: atualiza as duas matrizes e o acumulador de chegadas.
    ocupacao[linha][coluna] = 1
    identificacoes[linha][coluna] = codigo
    total_chegadas = total_chegadas + 1
    # set() limpa o campo para receber a próxima identificação.
    codigo_var.set("")
    atualizar_botao(linha, coluna)
    atualizar_resumo()


def registrar_saida(linha, coluna):
    """Pede confirmação antes de liberar uma posição atualmente ocupada."""
    posicao = codigo_da_posicao(linha, coluna)
    codigo = identificacoes[linha][coluna]
    # askyesno() apresenta uma confirmação e devolve True ou False ao programa.
    confirmar = messagebox.askyesno(
        "Registrar saída",
        "Confirmar a saída do contêiner " + codigo + " da posição " + posicao + "?",
        parent=janela,
    )

    # SELEÇÃO: somente uma confirmação positiva altera o estado da matriz.
    if confirmar:
        ocupacao[linha][coluna] = 0
        identificacoes[linha][coluna] = ""
        atualizar_botao(linha, coluna)
        atualizar_resumo()


def clicar_posicao(linha, coluna):
    """Decide se o clique representa chegada em vaga livre ou saída de vaga ocupada."""
    # SELEÇÃO: o valor da própria matriz decide qual fluxo será executado.
    if ocupacao[linha][coluna] == 0:
        registrar_chegada(linha, coluna)
    else:
        registrar_saida(linha, coluna)


def criar_acao_da_posicao(linha, coluna):
    """Cria uma função de clique que preserva os índices de uma posição específica."""
    def acao():
        clicar_posicao(linha, coluna)

    return acao


def montar_interface():
    """Monta a janela usando widgets ttk e os gerenciadores grid e pack."""
    global botoes
    global texto_ocupadas
    global texto_livres
    global texto_chegadas

    estilo = ttk.Style()
    # theme_use() consulta o tema nativo ativo antes de configurar estilos ttk.
    estilo.theme_use(estilo.theme_use())
    estilo.configure("Titulo.TLabel", font=("Segoe UI", 16, "bold"))
    estilo.configure("Subtitulo.TLabel", font=("Segoe UI", 10))
    estilo.configure("Livre.TButton", padding=(8, 12))
    estilo.configure("Ocupada.TButton", padding=(8, 12))

    quadro_principal = ttk.Frame(janela, padding=16)
    # pack() encaixa o quadro principal na janela e permite ocupar o espaço disponível.
    quadro_principal.pack(fill="both", expand=True)
    # columnconfigure() permite que a coluna se expanda quando a janela aumentar.
    quadro_principal.columnconfigure(0, weight=1)

    ttk.Label(
        quadro_principal,
        text="Organização de Contêineres em Pátio Logístico",
        style="Titulo.TLabel",
    ).grid(row=0, column=0, sticky="w")
    ttk.Label(
        quadro_principal,
        text="Matriz 5 x 6: clique em vaga livre para chegada e em vaga ocupada para saída.",
        style="Subtitulo.TLabel",
    ).grid(row=1, column=0, sticky="w", pady=(3, 14))

    quadro_entrada = ttk.LabelFrame(quadro_principal, text="Registro de chegada", padding=10)
    # grid() organiza o quadro por linhas e colunas dentro do quadro principal.
    quadro_entrada.grid(row=2, column=0, sticky="ew", pady=(0, 12))
    # columnconfigure() deixa a coluna do campo de texto responsiva.
    quadro_entrada.columnconfigure(1, weight=1)
    ttk.Label(quadro_entrada, text="Identificação do contêiner:").grid(
        row=0, column=0, sticky="w", padx=(0, 8)
    )
    ttk.Entry(quadro_entrada, textvariable=codigo_var, width=32).grid(
        row=0, column=1, sticky="ew"
    )

    quadro_resumo = ttk.Frame(quadro_principal)
    # grid() posiciona os indicadores em uma linha da interface.
    quadro_resumo.grid(row=3, column=0, sticky="w", pady=(0, 12))
    ttk.Label(quadro_resumo, textvariable=texto_ocupadas).grid(row=0, column=0, padx=(0, 18))
    ttk.Label(quadro_resumo, textvariable=texto_livres).grid(row=0, column=1, padx=(0, 18))
    ttk.Label(quadro_resumo, textvariable=texto_chegadas).grid(row=0, column=2)

    quadro_patio = ttk.LabelFrame(quadro_principal, text="Pátio de armazenamento", padding=10)
    # grid() faz o pátio ocupar o espaço restante da janela.
    quadro_patio.grid(row=4, column=0, sticky="nsew")
    # rowconfigure() permite que a linha do pátio acompanhe a altura da janela.
    quadro_principal.rowconfigure(4, weight=1)

    # REPETIÇÃO: cria visualmente as 30 posições que existem na matriz 5 x 6.
    for coluna in range(COLUNAS):
        # columnconfigure() distribui a largura do pátio entre as seis colunas.
        quadro_patio.columnconfigure(coluna, weight=1)
    for linha in range(LINHAS):
        # rowconfigure() distribui a altura do pátio entre as cinco linhas.
        quadro_patio.rowconfigure(linha, weight=1)
        linha_de_botoes = []
        for coluna in range(COLUNAS):
            botao = ttk.Button(
                quadro_patio,
                text=codigo_da_posicao(linha, coluna) + "\nLIVRE",
                style="Livre.TButton",
                command=criar_acao_da_posicao(linha, coluna),
            )
            # grid() coloca cada botão na mesma coordenada da matriz correspondente.
            botao.grid(row=linha, column=coluna, sticky="nsew", padx=4, pady=4)
            # append() adiciona o botão ao fim da linha, substituindo índice manual.
            linha_de_botoes.append(botao)
        # append() adiciona a linha de botões à matriz visual, mantendo os mesmos índices.
        botoes.append(linha_de_botoes)

    quadro_acoes = ttk.Frame(quadro_principal)
    # grid() posiciona o botão final abaixo do pátio.
    quadro_acoes.grid(row=5, column=0, sticky="e", pady=(12, 0))
    ttk.Button(quadro_acoes, text="Encerrar e mostrar resumo", command=encerrar).grid(
        row=0, column=0
    )


def montar_lista_de_ocupacao():
    """Percorre a matriz e constrói manualmente a lista exibida no resumo final."""
    lista = ""
    existe_ocupacao = False

    # REPETIÇÃO: visita as 30 posições para montar o resumo do estado final.
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if ocupacao[linha][coluna] == 1:
                existe_ocupacao = True
                lista = (
                    lista
                    + "\n- "
                    + codigo_da_posicao(linha, coluna)
                    + ": "
                    + identificacoes[linha][coluna]
                )

    if existe_ocupacao:
        return lista
    return "\nNenhum contêiner permaneceu armazenado."


def encerrar():
    """Apresenta o resumo obrigatório antes de fechar a aplicação."""
    ocupadas = contar_ocupadas()
    livres = TOTAL_POSICOES - ocupadas
    mensagem = (
        "Resumo final do período\n\n"
        + "Posições ocupadas: "
        + str(ocupadas)
        + "\nPosições livres: "
        + str(livres)
        + "\nChegadas registradas: "
        + str(total_chegadas)
        + "\n\nContêineres no pátio:"
        + montar_lista_de_ocupacao()
    )
    # showinfo() exibe uma mensagem modal antes do encerramento da janela.
    messagebox.showinfo("Resumo final", mensagem, parent=janela)
    # destroy() encerra a janela e finaliza o laço gráfico do Tkinter.
    janela.destroy()


def iniciar_aplicacao():
    """Executa a sequência principal: cria a janela, monta a interface e inicia o laço."""
    global janela
    global codigo_var
    global texto_ocupadas
    global texto_livres
    global texto_chegadas

    # SEQUÊNCIA: cria os objetos da interface antes de apresentar os dados.
    janela = tk.Tk()
    janela.title("Controle de Contêineres")
    janela.minsize(760, 560)
    # StringVar() mantém texto observável para Labels e Entry sem atualizar manualmente cada widget.
    codigo_var = tk.StringVar()
    texto_ocupadas = tk.StringVar()
    texto_livres = tk.StringVar()
    texto_chegadas = tk.StringVar()
    montar_interface()
    atualizar_resumo()
    # mainloop() mantém a aplicação em execução aguardando os eventos do usuário.
    janela.mainloop()


if __name__ == "__main__":
    iniciar_aplicacao()
