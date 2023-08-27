import list_seq
import random

L1 = list_seq.Lista()
L2 = list_seq.Lista()
L3 = list_seq.Lista()
L4 = list_seq.Lista()

def inserir_numeros_aleatorios(lista):
    for i in range(10):
        numero = random.randint(0, 99)
        lista.insert_at_index(numero, i)

inserir_numeros_aleatorios(L1)
inserir_numeros_aleatorios(L2)
L3.l = L1.l + L2.l
L4.l = L3.l[::-1]

print('Lista L1:', L1.l)
print('Lista L2:', L2.l)
print('Lista L3:', L3.l)
print('Lista L4:', L4.l)