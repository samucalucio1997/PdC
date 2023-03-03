vaitem = int(input())
qtd = int(input())
tot = int(input())
totpag = vaitem*qtd
totpag = int(totpag)
troco = tot - totpag
troco = int(troco)
print(f'A pagar: {totpag}')
print(f'Troco  : {troco}')