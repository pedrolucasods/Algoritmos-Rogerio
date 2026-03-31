comando = "sair"

match comando:
    case 'novo':
        print('Novo comando')
    case 'salvar':
        print('Documento salvo')
    case 'editar':
        print('Editar Documento')
    case _:
        print('opção inválida')