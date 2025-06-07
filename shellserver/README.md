# shellserver

Servidor Python que expõe ferramentas para execução de comandos shell e simulação de execução de código malicioso, utilizando o framework FastMCP.

## Funcionalidades
- **run_command**: Executa um comando shell e retorna stdout, stderr e código de retorno.
- **malicious_code_example**: Baixa um arquivo da internet que simula execução de código malicioso e retorna o conteúdo.

## Aviso de Segurança ⚠️
- **NUNCA** utilize este servidor em ambientes de produção ou expostos à internet sem as devidas restrições! As funções expostas permitem execução arbitrária de comandos no sistema operacional.
- O exemplo de código malicioso é apenas para fins educacionais/demonstração.

## Requisitos
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (para gerenciamento de dependências)


## Instalação e Execução Local
1. Clone o repositório:
   ```sh
   git clone <url-do-repositorio>
   cd shellserver
   ```
2. Instale as dependências:
   ```sh
   uv sync --frozen
   ```
3. Execute o servidor:
   ```sh
   uv run server.py
   ```

## Uso
O servidor expõe ferramentas via protocolo MCP. Você pode interagir com ele usando clientes MCP compatíveis.

### Ferramentas Disponíveis
- `run_command(command: str)`: Executa um comando shell e retorna a saída.
- `malicious_code_example()`: Baixa um arquivo simulando execução de código malicioso.

## Estrutura do Projeto
- `server.py`: Código principal do servidor e definição das ferramentas.
- `pyproject.toml`, `uv.lock`: Gerenciamento de dependências.
