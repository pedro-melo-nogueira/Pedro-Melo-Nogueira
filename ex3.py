import json

def abrirArquivo():
    with open("dados.json", encoding='utf-8') as dadosJson:
        return  json.load(dadosJson)

def condition(value):
  return value['valor'] > 0.00

dados =abrirArquivo()
dados2 = [d for d in dados if condition(d)]
print("Melhor dia:",max(dados2, key=lambda x: x['valor']), "Pior dia:",min(dados2, key=lambda x: x['valor']))
media=sum(soma['valor'] for soma in dados2)/len(dados2)
diasAcimaMedia=0
for dias in dados2:
    if(dias['valor']>media):
        diasAcimaMedia+=1
        print(dias)
print("Dias acima da media",diasAcimaMedia)

