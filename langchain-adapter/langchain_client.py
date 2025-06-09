import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1")

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["C:/Users/DDMX/Desktop/pessoal/MCP/langchain-adapter/servers/math_srv.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://127.0.0.1:8000/sse",
                "transport": "sse",
            },
        }
    )
    
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    agent_response = await agent.ainvoke({"messages": [{"role": "user", "content": "what is the wather like in Rio de Janeiro?"}]})
    print(agent_response["messages"][-1].content)
    
    
    
if __name__ == "__main__":
    asyncio.run(main())