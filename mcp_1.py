# server.py
from mcp.server.fastmcp import FastMCP
from langchain_community.tools import DuckDuckGoSearchRun

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """description Add two numbers
        :arg a: first number
        :arg b: second number
        :return: sum of a and b
    """
    return a + b


#
@mcp.tool()
def search(query: str) -> str:
    """search on web for the latest news/information/"""
    search_tool = DuckDuckGoSearchRun()
    result = search_tool.run(query)
    return result

if __name__ == '__main__':
    # Run the MCP server
    mcp.run(transport="streamable-http")
