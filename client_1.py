from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
import asyncio


async def main():
    # Create a client for the MCP server
    mcp_client = MultiServerMCPClient(
        {
            "Demo": {
                "url": "http://localhost:8000/mcp/",
                "transport": "streamable_http",
            }
        }
    )

    tools = await mcp_client.get_tools()

    # Create a react agent with the MCP client
    llm = ChatOllama(
        model="qwen3:8b",
        format="json",
        temperature=0.1,
        stream=False
    )

    agent = create_react_agent(
        model=llm,tools=tools
    )

    # Run the agent with a query
    query = "what is 5 + 2"
    response = await agent.ainvoke({"role": "user", "content": query})
    print(response.get("messages", []))


asyncio.run(main())