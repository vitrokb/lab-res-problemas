ladoDoVermelho = int(input(), base=16)
ladoDoVerde = int(input(), base=16)
ladoDoAzul = int(input(), base=16)

quantidadeDeVermelho = 1
quantidadeDeVerde = ladoDoVermelho // ladoDoVerde
print("quantidadeDeVerde", quantidadeDeVerde)
quantidadeDeVerde *= quantidadeDeVerde
print("quantidadeDeVerde 2", quantidadeDeVerde)
quantidadeDeAzul = ladoDoVerde // ladoDoAzul
quantidadeDeAzul *= quantidadeDeAzul
quantidadeDeAzul *= quantidadeDeVerde

print(hex(quantidadeDeVermelho + quantidadeDeVerde + quantidadeDeAzul))
