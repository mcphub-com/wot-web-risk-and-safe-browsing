import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/mywot-mywot-default/api/wot-web-risk-and-safe-browsing'

mcp = FastMCP('wot-web-risk-and-safe-browsing')

@mcp.tool()
def get_reputation_data(t: Annotated[str, Field(description='')]) -> dict: 
    '''Get reputation data for specific domains, up to 10 domains per request'''
    url = 'https://wot-web-risk-and-safe-browsing.p.rapidapi.com/targets'
    headers = {'x-rapidapi-host': 'wot-web-risk-and-safe-browsing.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        't': t,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
