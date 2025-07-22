import pprint

filmesDict = {
    "filme1": {
        "nome": "Matrix",
        "ano": 1999,
        "nota": 8.7,
        "disponivel": True
    },
    "filme2": {
        "nome": "Matrix 2",
        "ano": 2003,
        "nota": 8.7,
        "disponivel": True
    },
    "filme3": {
        "nome": "Matrix 3",
        "ano": 2003,
        "nota": 8.7,
        "disponivel": True
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmesDict)

# 1 - Buscar informacoes do filme 2
print(filmesDict["filme2"]["nome"])
print(filmesDict["filme2"]["ano"])
print(filmesDict["filme2"]["nota"])
print(filmesDict["filme2"]["disponivel"])

# 3 add filme 4
filmesDict["filme4"] = {
    "nome": "Matrix 4",
    "ano": 2003,
    "nota": 8.7,
    "disponivel": True
}

pp.pprint(filmesDict)

# add novo item
filmesDict["filme4"]["diretor"] = "Lana Wachowski"

pp.pprint(filmesDict)

# excluir item
del filmesDict["filme4"]["diretor"]

pp.pprint(filmesDict)

# excluir item
del filmesDict["filme4"]

pp.pprint(filmesDict)
