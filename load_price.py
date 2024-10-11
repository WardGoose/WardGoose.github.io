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
# pairId = '0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad'

# response = requests.get(
#     "https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}",
#     headers={},
# )

# data = response.json()
# # ======

# ======
# Multi Result
import requests
import json

# tokenAddresses = "0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad,0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce"
tokenAddresses = "0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad"

response = requests.get(
    f"https://api.dexscreener.com/latest/dex/tokens/{tokenAddresses}",
    headers={},
)
data = response.json()

with open('history.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    data1 = data['pairs']
    for i in data1:
        result = i['labels']
        if 'v3' in result:
            print(i['priceUsd'])
# ======
