# uv run C:/Langchain_basic/MCP/weather_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Weather",
    host = "0.0.0.0",
    port = 8100
    )

@mcp.tool()
async def get_weather(location: str) -> str:
    """ Get weather for location """
    return "석촌역의 날씨는 비옵니다"

if __name__ == "__main__":
    mcp.run(
        transport = "streamable-http"
    )
