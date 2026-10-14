# 💰 Gestor de Gastos em Python

Bem-vindo ao meu Gestor de Gastos! Este projeto nasceu do meu objetivo de criar algo útil para o dia a dia enquanto estudo e aplico as melhores práticas de programação em Python. 

É um sistema prático e direto ao ponto, focado em registrar, acompanhar e gerenciar despesas pessoais diretamente pelo terminal (console), construído com foco em lógica limpa e prevenção de erros.

## ✨ Funcionalidades

- **Registro de Despesas:** Permite cadastrar a descrição do item, o valor unitário e a quantidade comprada de forma intuitiva.
- **Validação de Dados:** O sistema é robusto e à prova de falhas. Impede descrições vazias e protege o programa contra erros de digitação (como tentar colocar letras no lugar do preço ou quantidade).
- **Busca e Remoção de Itens:** Digitou errado ou desistiu da compra? É possível buscar e remover gastos específicos apenas digitando o nome do produto.
- **Extrato Detalhado com Subtotal:** Lista todos os itens registrados, calculando automaticamente o subtotal de cada compra (`quantidade × valor`) e formatando os valores em reais (ex.: `R$ 23.90`).
- **Proteção de Extrato Vazio:** Verifica se há itens cadastrados antes de gerar o extrato, exibindo um aviso amigável caso a lista esteja limpa.
- **Cálculo Automático do Total:** Soma os subtotais de todos os itens e apresenta o valor total gasto durante a sessão de forma clara.
- **Menu Interativo e Saída Segura:** Um laço contínuo que mantém o programa em execução e solicita confirmação (`S/N`) antes de encerrar, evitando a perda acidental dos dados.

## 🛠 Tecnologias e Conceitos Utilizados

- **Python 3:**
  - Estruturas de repetição (`while`, `for`) e estruturas condicionais (`if`, `elif`, `else`).
  - Tratamento de Exceções (`try`, `except`) para validação rigorosa de entradas de dados.
  - Manipulação de listas aninhadas (`append`, `len`, `.remove()`, indexação).
  - Tratamento de strings e formatação (`.upper()`, `.strip()`, `f-strings` com casas decimais `:.2f`).
  - Conversão de tipos de dados (`float`, `int`).

## 🚀 Como executar o projeto

1. Certifique-se de ter o **Python 3** instalado no seu computador ou celular.
2. Faça o clone deste repositório ou baixe o arquivo `gestor-de-gastos.py`.
3. Escolha como prefere executar:
   - **No VS Code ou PyCharm:** Abra a pasta do projeto, selecione o arquivo `gestor-de-gastos.py` e execute no terminal integrado.
   - **No Celular (Pydroid 3 ou Termux):** Abra o arquivo no aplicativo e inicie a execução.
   - **Pelo Terminal:** Execute o comando abaixo na pasta do projeto:

```bash
python gestor-de-gastos.py
