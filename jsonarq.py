import json
# lista1 = json.dumps([1, 'simple', 'list'])

# print(lista1)

# with open("arquivo.json", "a") as f:
#     f.write(lista1)

with open("arquivo.json", "r") as f:
    y = f.read()
    print(y[0])
    lista1 = json.loads(y)
    print(lista1[0])