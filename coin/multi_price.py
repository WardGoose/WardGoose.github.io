# API : dexscreener

# Moodeng
# ethereum
# 0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad

# Shiba inu
# ethereum
# 0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce

import requests
import json

# tokenAddresses = "0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad,0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce"

API_URLS = {
    'moodengeth': f"0x28561b8a2360f463011c16b6cc0b0cbef8dbbcad",
    'moodengsol': f'22WrmyTj8x2TRVQen3fxxi2r4Rn6JDHWoMTpsSmn8RUd'
}

for filename, token in API_URLS.items():
    response = requests.get(
        f"https://api.dexscreener.com/latest/dex/tokens/{token}",
        headers={},
    )
    data = response.json()

    with open(f'coin/data/{filename}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    # price_load
        data1 = data['pairs']
        for i in data1:
            result = i['labels']
            if 'v3' in result:  # v2가 있는지 확인
                print(f"Symbol: {i['baseToken']['symbol']}, Price: {i.get('priceUsd', 'N/A')}")