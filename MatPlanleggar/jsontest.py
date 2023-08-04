import json

olist = {
    "fast" : [1,2,3],
    "medium": ["a","b","c"],
    "slow": []
}

x = json.dumps(olist)

print(x)

y = json.loads(x)

print(y["fast"][1])