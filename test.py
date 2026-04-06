import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient

async def test():
    path = os.path.abspath("clanki/build/index.js")
    print("Path:", path)

    client = MultiServerMCPClient(
        {
            "clanki": {
                "command": "node",
                "args": [path],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()
    print("Loaded tools:", tools)

asyncio.run(test())
