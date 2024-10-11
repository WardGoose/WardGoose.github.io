# API : dexscreener

import requests

chainID = 'ethereum'
pairId = '0x5552727005cc8194c1559289a532deb288964fd8'

response = requests.get(
    "https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}",
    headers={},
)

data = response.json()
