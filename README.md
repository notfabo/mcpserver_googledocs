# mcpserver_googledocs

Este projeto implementa um servidor MCP (Model Context Protocol) que integra com a API do Google Docs, permitindo a criação de documentos Google Docs de forma programática.

## Funcionalidades

- **Autenticação com Google**: Scripts para autenticação OAuth2 e geração do token de acesso.
- **Criação de Documentos**: Função para criar documentos no Google Docs com título e texto personalizados.
- **Servidor MCP**: Expõe a funcionalidade de criação de documentos como uma ferramenta MCP, podendo ser utilizada por outros sistemas compatíveis.

## Como usar

1. **Instale as dependências**:
	```
	pip install -r requirements.txt
	```

2. **Configure as credenciais**:
	- Renomeie `credentials-example.json` para `credentials.json` e adicione suas credenciais do Google Cloud.
	- Execute o script de autenticação para gerar o `token.json`:
	  ```
	  python auth.py
	  ```

3. **Execute o servidor MCP para ver se esta rodando normal e depois adicione o mcp server a sua host com a estrutura do mcp-example.json**:
	```
	python mcp_server.py
	```

## Estrutura dos arquivos

- `auth.py`: Script para autenticação e geração do token de acesso.
- `docs_tools.py`: Funções utilitárias para criar documentos no Google Docs.
- `mcp_server.py`: Inicializa o servidor MCP e registra a ferramenta de criação de documentos.
- `requirements.txt`: Dependências do projeto.

## Observações

- É necessário ter um projeto no Google Cloud com a API do Google Docs habilitada.
- O arquivo `token.json` é gerado após a autenticação e deve ser mantido seguro.