# uv run C:\Langchain_basic\MCP\mcp_multi_client.py
# uv add langchain_mcp_adapters
import asyncio
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

# 실제 실행 파트
async def main():
    print("멀티 클라이언트 세팅중...")

    client = MultiServerMCPClient(
        {
            "Math" : {
                "command" : "python",
                "args" : ["C:/Langchain_basic/MCP/odd_math_server.py"],
                "transport" : "stdio"
            },
            "Weather" : {
                "url" : "http://localhost:8100/mcp",
                "transport" : "streamable_http"
            }

            # "mcp_weather_server" : {
            #     "command" : "cmd",
            #     "args" : [
            #         "/c",
            #         "npx",
            #         "-y",
            #         "@smithery/cli@latest",
            #         "run",
            #         "@isdaniel/mcp_weather_server",
            #         "--key",
            #         "",
            #         "--profile",
            #         ""
            #     ],
            #     "transport": "stdio"
            # }
        }
    )

    print(f"client ::: {client}")
    print("client.session ::: ", client.session("exa"))

    async with client.session("exa") as sess:
        # tools = await client.get_tools()
        print("client.session ::: ", client.session("exa"))

    # tools = await client.get_tools()
    # for item in tools:
    #     print(f"가져온 도구는 : {item.name}")

    # agent 만들기
    model = ChatOpenAI(
        model = "gpt-4.1-mini",
        temperature = 0
    )

    # 덧셈 도구 체크
    agent_executor = create_react_agent(model, tools)
    response = await agent_executor.ainvoke(
        {"messages" : [HumanMessage(content="1+2는?")]}
    )
    print(response["messages"][-1].content)

    # 곱셈 도구 체크
    response = await agent_executor.ainvoke(
        {"messages" : [HumanMessage(content="2 * 3 을 이상하게 계산하면?")]}
    )
    print(response["messages"][-1].content)

    # 날씨 도구 체크
    response = await agent_executor.ainvoke(
        {"messages" : [HumanMessage(content="석촌역의 날씨는?")]}
    )
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())