from mcp.server.fastmcp import FastMCP
from docs_tools import create_document

mcp = FastMCP("google_docs")

@mcp.tool()
async def create_google_doc(title: str, text: str) -> str:
    """
    Cria um Google Docs com o título e texto fornecidos.
    """
    return create_document(title, text)
print("MCP Tool registered!")


if __name__ == "__main__":
    mcp.run(transport="stdio")
