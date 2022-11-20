from time import sleep

def line():
    return '-'*42

def header(txt):
    print(line())
    print(txt.center(42))
    print(line())

# listar estoque, add produto, remover produto
estoque=['feijão', 'arroz','carne']

def main(vetor):
    c= 1
    for element in vetor:
        print(f'{c}- {element}')
        c+=1
    print(line())


def showEstoque():
    header('**Estoque**')
    if len(estoque)==0:
        print('estoque vazio')
    else:
        main(estoque)

def addItem():
    item=input('digite o item que deseja adicionar:')
    if item in estoque:
        print('[erro] o item já existe')
    else:
        print('item adicionado com sucesso!')
        estoque.append(item)
    

def removeItem():
    item=input('digite o item que deseja remover:')
    if item in estoque:
        print('item removido com sucesso')
        estoque.remove(item)
    else:
        print('[erro], item não existe no estoque')


def resetEstoque():
    header('limpando estoque...')
    sleep(0.9)
    estoque.clear()
    print('estoque resetado')

dataOpc={
    '1':addItem,
    '2':showEstoque,
    '3':removeItem,
    '4':resetEstoque
}

# api de superMercado
# objetivo: modularizar, utilizar loops e manipular listas
