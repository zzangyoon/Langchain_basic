# uv run C:/Langchain_basic/MCP/odd_math_server.py
# uv add mcp
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")   # Math : MCP Server 이름

@mcp.tool()
def add(a: int, b: int) -> int:
    """ Add two numbers incorrectly"""
    return (a + b) * 2

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """ Multiply two numbers incorrectly"""
    return (a * b) ** 2

if __name__ == "__main__":
    mcp.run(transport="stdio")  # stdio : local에서 사용