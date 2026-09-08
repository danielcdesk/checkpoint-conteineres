import tkinter as tk
from tkinter import messagebox, simpledialog

LINHAS = 5
COLUNAS = 6
TOTAL_POSICOES = LINHAS * COLUNAS


class PatioConteineresApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Controle de Contêineres — Checkpoint")
        self.root.geometry("900x650")
        self.root.minsize(780, 560)

        self.ocupacao = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
        self.conteineres = [[None for _ in range(COLUNAS)] for _ in range(LINHAS)]

        self.botoes = []
        self.total_chegadas = 0

        self._montar_interface()
        self._atualizar_resumo()

    def _montar_interface(self) -> None:
        cabecalho = tk.Frame(self.root, padx=20, pady=15)
        cabecalho.pack(fill="x")

        tk.Label(
            cabecalho,
            text="📦 Organização de Contêineres em Pátio Logístico",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w")

        tk.Label(
            cabecalho,
            text="Projeto acadêmico — Programação 2 | Matriz 5 × 6",
            font=("Segoe UI", 10),
        ).pack(anchor="w", pady=(4, 0))

        resumo = tk.Frame(self.root, padx=20, pady=8)
        resumo.pack(fill="x")

        self.lbl_ocupadas = tk.Label(resumo, font=("Segoe UI", 11, "bold"))
        self.lbl_ocupadas.pack(side="left", padx=(0, 25))

        self.lbl_livres = tk.Label(resumo, font=("Segoe UI", 11, "bold"))
        self.lbl_livres.pack(side="left", padx=(0, 25))

        self.lbl_chegadas = tk.Label(resumo, font=("Segoe UI", 11, "bold"))
        self.lbl_chegadas.pack(side="left")

        patio = tk.LabelFrame(
            self.root,
            text="Pátio de armazenamento",
            padx=16,
            pady=16,
            font=("Segoe UI", 11, "bold"),
        )
        patio.pack(fill="both", expand=True, padx=20, pady=10)

        for linha in range(LINHAS):
            linha_botoes = []
            for coluna in range(COLUNAS):
                codigo_posicao = f"{chr(65 + linha)}{coluna + 1}"
                botao = tk.Button(
                    patio,
                    text=f"{codigo_posicao}\nLIVRE",
                    width=13,
                    height=4,
                    font=("Segoe UI", 9, "bold"),
                    command=lambda l=linha, c=coluna: self._clicar_posicao(l, c),
                )
                botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
                linha_botoes.append(botao)

            self.botoes.append(linha_botoes)

        for coluna in range(COLUNAS):
            patio.grid_columnconfigure(coluna, weight=1)
        for linha in range(LINHAS):
            patio.grid_rowconfigure(linha, weight=1)

        rodape = tk.Frame(self.root, padx=20, pady=15)
        rodape.pack(fill="x")

        tk.Button(
            rodape,
            text="📊 Resumo",
            width=15,
            command=self._mostrar_resumo,
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            rodape,
            text="🧹 Limpar pátio",
            width=15,
            command=self._limpar_patio,
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            rodape,
            text="Encerrar",
            width=15,
            command=self._encerrar,
        ).pack(side="right")

    def _clicar_posicao(self, linha: int, coluna: int) -> None:
        if self.ocupacao[linha][coluna] == 0:
            self._registrar_chegada(linha, coluna)
        else:
            self._liberar_posicao(linha, coluna)

    def _registrar_chegada(self, linha: int, coluna: int) -> None:
        codigo = simpledialog.askstring(
            "Registrar chegada",
            "Informe o código/identificação do contêiner:",
            parent=self.root,
        )

        if codigo is None:
            return

        codigo = codigo.strip().upper()
        if not codigo:
            messagebox.showwarning("Atenção", "Informe um código válido para o contêiner.")
            return

        if self._codigo_ja_esta_no_patio(codigo):
            messagebox.showwarning(
                "Contêiner já registrado",
                f"O contêiner {codigo} já está armazenado no pátio.",
            )
            return

        self.ocupacao[linha][coluna] = 1
        self.conteineres[linha][coluna] = codigo
        self.total_chegadas += 1
        self._atualizar_botao(linha, coluna)
        self._atualizar_resumo()

    def _liberar_posicao(self, linha: int, coluna: int) -> None:
        codigo = self.conteineres[linha][coluna]
        posicao = f"{chr(65 + linha)}{coluna + 1}"

        confirmar = messagebox.askyesno(
            "Liberar posição",
            f"Confirmar a saída do contêiner {codigo} da posição {posicao}?",
        )
        if not confirmar:
            return

        self.ocupacao[linha][coluna] = 0
        self.conteineres[linha][coluna] = None
        self._atualizar_botao(linha, coluna)
        self._atualizar_resumo()

    def _codigo_ja_esta_no_patio(self, codigo: str) -> bool:
        for linha in self.conteineres:
            if codigo in linha:
                return True
        return False

    def _atualizar_botao(self, linha: int, coluna: int) -> None:
        botao = self.botoes[linha][coluna]
        posicao = f"{chr(65 + linha)}{coluna + 1}"

        if self.ocupacao[linha][coluna] == 1:
            codigo = self.conteineres[linha][coluna]
            botao.config(text=f"{posicao}\nOCUPADA\n{codigo}", relief="sunken")
        else:
            botao.config(text=f"{posicao}\nLIVRE", relief="raised")

    def _contar_ocupadas(self) -> int:
        return sum(sum(linha) for linha in self.ocupacao)

    def _atualizar_resumo(self) -> None:
        ocupadas = self._contar_ocupadas()
        livres = TOTAL_POSICOES - ocupadas

        self.lbl_ocupadas.config(text=f"Ocupadas: {ocupadas}")
        self.lbl_livres.config(text=f"Livres: {livres}")
        self.lbl_chegadas.config(text=f"Chegadas registradas: {self.total_chegadas}")

    def _mostrar_resumo(self) -> None:
        ocupadas = self._contar_ocupadas()
        livres = TOTAL_POSICOES - ocupadas

        armazenados = []
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                if self.ocupacao[linha][coluna] == 1:
                    posicao = f"{chr(65 + linha)}{coluna + 1}"
                    armazenados.append(f"• {posicao}: {self.conteineres[linha][coluna]}")

        lista = "\n".join(armazenados) if armazenados else "Nenhum contêiner armazenado."
        mensagem = (
            f"Posições ocupadas: {ocupadas}\n"
            f"Posições livres: {livres}\n"
            f"Total de chegadas registradas: {self.total_chegadas}\n\n"
            f"Contêineres no pátio:\n{lista}"
        )
        messagebox.showinfo("Resumo do pátio", mensagem)

    def _limpar_patio(self) -> None:
        if not messagebox.askyesno(
            "Limpar pátio",
            "Deseja liberar todas as posições? O total histórico de chegadas será mantido.",
        ):
            return

        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                self.ocupacao[linha][coluna] = 0
                self.conteineres[linha][coluna] = None
                self._atualizar_botao(linha, coluna)

        self._atualizar_resumo()

    def _encerrar(self) -> None:
        ocupadas = self._contar_ocupadas()
        livres = TOTAL_POSICOES - ocupadas

        messagebox.showinfo(
            "Encerramento",
            "Resumo final do período:\n\n"
            f"Contêineres atualmente armazenados: {ocupadas}\n"
            f"Posições disponíveis: {livres}\n"
            f"Chegadas registradas no período: {self.total_chegadas}",
        )
        self.root.destroy()


def main() -> None:
    root = tk.Tk()
    PatioConteineresApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
