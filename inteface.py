from engine import *

while True:
    header('superMercado v.1')

    main(['adicionar item', 'listar item', 'remover item','limpar estoque'])

    opc= input('escolha a opção que deseja:')

    dataOpc[opc]()