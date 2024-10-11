# API : dexscreener

# Moodeng
# ethereum
# 0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad

# Shib inu
# ethereum
# 0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce

# # ======
# One Result
# import requests
# chainID = 'ethereum'
# pairId = '0x5552727005cc8194c1559289a532deb288964fd8'

# response = requests.get(
#     "https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}",
#     headers={},
# )

# data = response.json()
# # ======

# ======
# Multi Result
import requests

response = requests.get(
    "https://api.dexscreener.com/latest/dex/tokens/{tokenAddresses}",
    headers={},
)
data = response.json()
# ======
