import re

estado = {'SP':'R$67.836,43', 'RJ':'R$36.678,66', 'MG':'R$29.229,88',
'ES':'R$27.165,48', 'Outros': 'R$19.849,53'}
soma=0
for est in estado.keys():
    estado[est]=float(re.sub('[^0-9,]', '', estado[est]).replace(",","."))
    soma+=estado[est]

for est in estado.keys():
    print(est, 'porcentagem: {:.2f}%'.format(estado[est]*100/soma))
