#  Gestor de Gastos em Python

Um projeto desenvolvido em Python para o registro e acompanhamento de despesas pessoais diretamente pelo terminal (console).

##  Funcionalidades

- **Registro de Despesas:** Permite cadastrar a descrição do item, o valor unitário e a quantidade comprada.
- **Extrato Detalhado com Subtotal:** Lista todos os itens registrados, calculando automaticamente o subtotal de cada compra (`quantidade × valor`) e formatando os valores em reais (ex.: `R$ 23.90`).
- **Proteção de Extrato Vazio:** Verifica se há itens cadastrados antes de gerar o extrato, exibindo um aviso amigável caso a lista esteja vazia.
- **Cálculo Automático do Total:** Soma os subtotais de todos os itens e apresenta o valor total gasto durante a sessão.
- **Menu Interativo e Saída Segura:** Laço contínuo que mantém o programa em execução no console e solicita confirmação (`S/N`) antes de encerrar, evitando a perda acidental dos dados.

##  Tecnologias e Conceitos Utilizados

- **Python 3:**
  - Estruturas de repetição (`while`, `for`)
  - Estruturas condicionais (`if`, `elif`, `else`)
  - Manipulação de listas aninhadas (`append`, `len`, indexação)
  - Conversão de tipos (`float`, `int`) e métodos de string (`.upper()`)
  - Formatação de strings (`f-strings` com casas decimais `:.2f`)

##  Como executar o projeto

1. Certifique-se de ter o **Python 3** instalado no seu computador ou celular.
2. Faça o clone deste repositório ou baixe o arquivo `gestor-de-gastos.py`.
3. Escolha como prefere executar:
   - **No PyCharm ou VS Code:** Abra a pasta do projeto no editor, selecione o arquivo `gestor-de-gastos.py` e clique no botão **Run (▶️)** (ou use o terminal integrado).
   - **No Celular (Pydroid 3 ou Termux):** Abra o arquivo no aplicativo e inicie a execução.
   - **Pelo Terminal:** Execute o comando abaixo na pasta do projeto:

```bash
python gestor-de-gastos.py

