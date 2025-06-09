import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


llm = ChatOpenAI(model="gpt-4.1")

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:/Users/DDMX/Desktop/pessoal/MCP/langchain-adapter/servers/math_srv.py"],

)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            tools = await load_mcp_tools(session)
            
            agent = create_react_agent(llm, tools)
            
            agent_response = await agent.ainvoke({"messages": [HumanMessage("what's (3 + 5) x 12?")]})
            
            print(agent_response["messages"][-1].content)
        


if __name__ == "__main__":
    asyncio.run(main())
