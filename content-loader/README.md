# Word Loader MCP Server

Um servidor MCP (Model Context Protocol) para integração com Claude Desktop que permite salvar respostas do Claude diretamente em documentos Word no seu computador.

## Instalação

### Pré-requisitos
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (gerenciador de pacotes Python)

### Setup

1. Clone o repositório:
```bash
git clone https://github.com/gabrielnichio/MCP
cd content-loader
```

2. Instale as dependências com uv:
```bash
uv pip install -e .
```

## Configuração no Claude Desktop

Adicione o servidor ao arquivo de configuração do Claude Desktop:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`  
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "word-loader": {
      "command": "python",
      "args": ["caminho/para/loader_server.py"]
    }
  }
}
```

## Uso

O servidor disponibiliza duas ferramentas:

### `set_document`
Define o documento Word de trabalho.
- `document_name`: Nome do documento (com ou sem .docx)
- `document_path`: Caminho completo (opcional, padrão: Desktop)

### `load_content`
Salva conteúdo no documento atual com suporte a formatação Markdown.
- `content`: Texto com formatação Markdown

## Formatação Suportada

- Headers: `#`, `##`, `###`, `####`
- **Negrito**: `**texto**`
- *Itálico*: `*texto*`
- `Código inline`: `` `código` ``
- Listas com bullets: `- item` ou `* item`
- Listas numeradas: `1. item`
- Blocos de código: ` ```código``` `

## Dependências

- fastmcp>=2.7.1
- python-docx>=1.1.2
- mcp[cli]>=1.9.3