import sys

def pertenceFibonacci(numero):
    sequencia=1
    anterior=0
    anterior2=1
    if(numero==0):
        return True
    while(sequencia<numero):
        sequencia=anterior+anterior2
        anterior2=anterior
        anterior=sequencia
        if(sequencia>float(sys.maxsize)):
            return False
    if(sequencia==numero):
        return True
    return False

numero=float(input())
if(numero<float(sys.maxsize)):
    print(pertenceFibonacci(numero))