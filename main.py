from tree import NoRaizData
import json

entrada = '01/01/2019'


def analise_lexica(entrada):
    lexico = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']
    for i in entrada:
        if i not in lexico:
            return False
    return True
    
def analise_sintatica (entrada):
    arvore = NoRaizData()
    for i in entrada:
        arvore.inserir(i)
    print(arvore)
    
lexico = analise_lexica(entrada)
if lexico:
    sintatica = analise_sintatica(entrada)
    print(json.dumps(sintatica))