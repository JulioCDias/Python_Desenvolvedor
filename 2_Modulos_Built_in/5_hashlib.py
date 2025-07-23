import hashlib

# 1 Verificar os algoritmos disponiveis
print(hashlib.algorithms_available)

print("**"*50)
# 2 Verificar algoritomos de acordo com o SO
print(hashlib.algorithms_guaranteed)

print("**"*50)
# 3 Gerar um hash com o algoritmo SHA256
message = "Ola, tudo bem? Estou aprendendo Python"
hash_object = hashlib.sha256(message.encode('utf-8'))
print(hash_object.hexdigest())
print("**"*50)

# 4 Gerar um hash com o algoritmo MD5
message = "Ola, tudo bem? Estou aprendendo Python"
hash_object = hashlib.md5(message.encode('utf-8'))
print(hash_object.hexdigest())