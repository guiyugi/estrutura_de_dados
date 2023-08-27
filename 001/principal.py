import list_seq
lista1 = list_seq.Lista()

def mostrar_lista():
    global lista1
    print(f' Lista = {lista1.l}, Tamanho = {len(lista1.l)}')

def esvaziar_lista():
    global lista1
    lista1 = list_seq.Lista()
    print('Lista esvaziada com sucesso')
    return(lista1)

user_input = 3
while user_input!= 0:
    print()
    print('\tEDITOR DE LISTAS')
    print()
    print('\t1 - EXIBIR LISTA')
    print('\t2 - INSERIR')
    print('\t3 - REMOVER')
    print('\t4 - EXIBIR ELEMENTO')
    print('\t5 - EXIBIR POSIÇÃO')
    print('\t6 - ESVAZIAR')
    print('ESC - SAIR')
    print()
    user_input = int(input('DIGITE UMA OPCAO '))
    match user_input:
        case 1:
            print('='*40)
            mostrar_lista()
            print('='*40)
        case 2:
            value = int(input('Digite o valor do elemento a ser inserido: '))
            index = int(input('Digite a posição onde será efetuada a inserção: '))
            lista1.insert(value,index)
        case 3:
            index = int(input('Insira a a posição do elemento a  ser removido: '))
            lista1.remover(index)
        case 4:
            index = int(input('Insira a posição do elemento, em seguida será mostrado seu índice: '))
            print(lista1.show_value(index))
        case 5:
            value = int(input('Insira o valor do elemento, em seguida será mostrada sua posição: '))
            print(lista1.show_index(value))
        case 6: 
            print('='*40)
            lista1 = esvaziar_lista()
            print('='*40)
            print('SUCESSO!!!')