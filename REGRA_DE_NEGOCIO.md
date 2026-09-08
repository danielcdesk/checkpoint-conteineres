# 📋 Regra de Negócio — Organização de Contêineres

A aplicação controla a ocupação de um pátio de armazenamento de contêineres recém-chegados. O pátio é representado por uma **matriz 5 × 6**, totalizando 30 posições.

## Estado da matriz

- `0` — posição disponível;
- `1` — posição ocupada.

## Regras comportamentais

### Inicialização

**DADO** que o sistema seja iniciado  
**QUANDO** o usuário abrir a interface  
**ENTÃO** todas as posições da matriz deverão iniciar livres, com valor `0`.

### Chegada de contêiner

**DADO** que exista uma posição disponível no pátio  
**QUANDO** o usuário selecionar uma posição livre e informar o código do contêiner  
**ENTÃO** a posição correspondente na matriz deverá mudar de `0` para `1` e o contêiner será registrado naquela posição.

### Identificação visual

**DADO** que uma posição esteja ocupada  
**QUANDO** o sistema identificar o valor `1` naquela posição da matriz  
**ENTÃO** a interface deverá apresentar a posição como ocupada e exibir o código do contêiner.

### Saída de contêiner

**DADO** que um contêiner esteja armazenado em uma posição  
**QUANDO** o usuário confirmar sua saída  
**ENTÃO** a posição correspondente na matriz deverá voltar de `1` para `0`.

### Atualização do pátio

**DADO** que ocorram entradas ou saídas de contêineres  
**QUANDO** o estado de uma posição for alterado  
**ENTÃO** o sistema deverá recalcular e apresentar o total de posições ocupadas e disponíveis.

### Encerramento

**DADO** que o usuário tenha terminado o controle do período  
**QUANDO** clicar no botão de encerrar  
**ENTÃO** o sistema deverá apresentar um resumo com o número de contêineres armazenados, posições disponíveis e total de chegadas registradas.

---

> Documento resumido da lógica do projeto. Esta versão pública não inclui nomes de integrantes, matrículas, documentos institucionais ou outros dados pessoais.
