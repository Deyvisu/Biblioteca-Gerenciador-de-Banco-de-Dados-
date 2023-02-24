#BIBLIOTECAS UTILIZADAS

import PySimpleGUI as sg 
import psycopg2
from Controle.classeConexao import Conexao
from Modelo.classeLivros import Livro
from Modelo.classeClientes import Cliente
from Modelo.classeAlugueis import Aluguel


# TELAS:

sg.theme("Reddit")

telaInicial = [
    [sg.Push(),sg.Text("Bem vindo a Biblioteca!"), sg.Push()],
    [sg.Push(),sg.Button("Gerenciamento de Livros",key="-GerenciamentoLivros-"),sg.Push()],
    [sg.Push(),sg.Button("Gerenciamento de Clientes",key="-GerenciamentoClientes-"),sg.Push()],
    [sg.Push(),sg.Button("Gerenciamento de Alugueis",key="-GerenciamentoAlugueis-"),sg.Push()],
    [sg.Push(),sg.Button("Sair", key="-TelaInicialSair-"), sg.Push()]
]

telaGerenciamentoClientes = [
    [sg.Push(),sg.Text("Gerenciamento de Clientes"),sg.Push()],
    [sg.Push(),sg.Button("Ver Clientes",key="-VerClientes-"),sg.Push()],
    [sg.Push(),sg.Button("Inserir Clientes",key="-InserirClientes-"),sg.Push()],
    [sg.Push(),sg.Button("Alterar Clientes", key="-AlterarClientes-"),sg.Push()],
    [sg.Push(),sg.Button("Deletar Clientes",key="-DeletarClientes-"),sg.Push()],
    [sg.Push(),sg.Button("Voltar", key="-TelaGerenciamentoClienteVoltar-"), sg.Push()]
]

telaInserirCliente = [
    [sg.Push(), sg.Text("Cadastro de Cliente"),sg.Push()],
    [sg.Text("Nome:"), sg.Input(key="-InserirNomeCliente-")],
    [sg.Text("CPF:"), sg.Input(key="-InserirCPFCliente-")],
    [sg.Text("Telefone:"), sg.Input(key="-InserirTelefoneCliente-")],
    [sg.Text("E-mail:"), sg.Input(key="-InserirEmailCliente-")],
    [sg.Button("Voltar", key="-InserirClienteVoltar-"), sg.Button("Enviar", key="-InserirClienteEnviar-")]
]

telaVerClientes = [
    [sg.Text("Digite o ID do Cliente que deseja visualizar: "), sg.Input(key="-InserirIdCliente-", size=(30,1))],
    [sg.Button("Verificar", key="-verificarVerIDCliente-"), sg.Button("Ver Todos os Clientes", key="-VerTodosClientes-")],
    [sg.Multiline(key="-todosClientes-",size=(65,10))], [sg.Button("Voltar", key="-voltarVerClientes-")]
]

telaDeletarCliente = [
    [sg.Text("Digite o ID do cliente que deseja excluir: "), sg.Input(key="-IDdeletarCliente-", size=(30,1))],
    [sg.Button("Deletar", key="-deletarCliente-"), sg.Button("Ver Todos os Clientes", key="-VerTodosDelCli-")],
    [sg.Multiline(key="-todosDelCli-",size=(65,10))], [sg.Button("Voltar", key="-voltarDeletarCliente-")]
]

telaAlterarCliente = [
    [sg.Text("Digite o ID do Cliente que deseja alterar: "), sg.Input(key="-AlterarIdCliente-", size=(30,1))],
    [sg.Button("Verificar", key="-verificarAlterarIDCli-"), sg.Button("Ver Todos os Clientes", key="-VerTodosAltCli-")],
    [sg.Multiline(key="-todosAltCli-",size=(65,10))], [sg.Button("Voltar", key="-voltarAltCli-")]
]

alterarCli = [
    [sg.Push(), sg.Text("Alterando Cliente"),sg.Push()],
    [sg.Text("Nome:"), sg.Input(key="-AlterarNomeCliente-")],
    [sg.Text("CPF:"), sg.Input(key="-AlterarCPFCliente-")],
    [sg.Text("Telefone:"), sg.Input(key="-AlterarTelefoneCliente-")],
    [sg.Text("E-mail:"), sg.Input(key="-AlterarEmailCliente-")],
    [sg.Button("Voltar", key="-AlterarClienteVoltar-"), sg.Button("Enviar", key="-AlterarClienteEnviar-")]
]

telaGerenciamento = [
    [sg.Push(),sg.Text("Gerenciamento de Livros"),sg.Push()],
    [sg.Push(),sg.Button("Ver Livros",key="-VerLivros-"),sg.Push()],
    [sg.Push(),sg.Button("Inserir Livros",key="-InserirLivros-"),sg.Push()],
    [sg.Push(),sg.Button("Alterar Livros", key="-AlterarLivros-"),sg.Push()],
    [sg.Push(),sg.Button("Deletar Livros",key="-DeletarLivros-"),sg.Push()],
    [sg.Push(),sg.Button("Voltar", key="-TelaGerenciamentoVoltar-"), sg.Push()]
]

telaInserir = [
    [sg.Push(), sg.Text("Insira um Livro"),sg.Push()],
    [sg.Text("Nome do Livro:"), sg.Input(key="-InserirNomeLivros-")],
    [sg.Text("Idioma do Livro:"), sg.Input(key="-InserirIdiomaLivros-")],
    [sg.Text("Número de Páginas:"), sg.Input(key="-InserirNPaginasLivros-")],
    [sg.Button("Voltar", key="-LivrosInserirVoltar-"), sg.Button("Enviar", key="-LivrosInserirEnviar-")]
]

telaVer = [
    [sg.Text("Digite o ID do livro que deseja visualizar: "), sg.Input(key="-InserirIdLivro-", size=(30,1))],
    [sg.Button("Verificar", key="-verificarVerID-"), sg.Button("Ver Todos os Livros", key="-VerTodos-")],
    [sg.Multiline(key="-todos-",size=(65,10))], [sg.Button("Voltar", key="-voltarVer-")]
]

telaDeletar = [
    [sg.Text("Digite o ID do livro que deseja apagar: "), sg.Input(key="-IDdeletar-", size=(30,1))],
    [sg.Button("Deletar", key="-deletar-"), sg.Button("Ver Todos os Livros", key="-VerTodosDel-")],
    [sg.Multiline(key="-todosDel-",size=(65,10))], [sg.Button("Voltar", key="-voltarDeletar-")]
]

telaAlterar = [
    [sg.Text("Digite o ID do livro que deseja alterar: "), sg.Input(key="-AlterarIdLivro-", size=(30,1))],
    [sg.Button("Verificar", key="-verificarAlterarID-"), sg.Button("Ver Todos os Livros", key="-VerTodosAlt-")],
    [sg.Multiline(key="-todosAlt-",size=(65,10))], [sg.Button("Voltar", key="-voltarAlt-")]
]

alterar = [
    [sg.Push(), sg.Text("Alterando Livro"),sg.Push()],
    [sg.Text("Nome do Livro:"), sg.Input(key="-AlterarNomeLivro-")],
    [sg.Text("Idioma do Livro:"), sg.Input(key="-AlterarIdiomaLivro-")],
    [sg.Text("Número de Páginas:"), sg.Input(key="-AlterarNPaginasLivro-")],
    [sg.Button("Voltar", key="-AlterarLivroVoltar-"), sg.Button("Alterar", key="-AlterarLivroEnviar-")]
]

telaGerenciamentoAlugueis = [
    [sg.Push(),sg.Text("Alugueis"), sg.Push()],
    [sg.Push(),sg.Button("Cadastrar Novo Aluguel",key="-CadastrarNovoAluguel-"),sg.Push()],
    [sg.Push(),sg.Button("Ver Alugueis",key="-VerAlugueis-"),sg.Push()],
    [sg.Push(),sg.Button("Voltar", key="-VoltarAlugueis-"), sg.Push()]
]

cadastrarNovoAluguel = [
    [sg.Push(), sg.Text("Cadastro de Novo Aluguel"),sg.Push()],
    [sg.Text("Digite o ID do Cliente:"), sg.Input(key="-IDClienteAluguel-", size=(50,1))],
    [sg.Text("Digite o ID do Livro:"), sg.Input(key="-IDLivroAluguel-", size=(52,1))],
    [sg.Text("Digite a Data do Aluguel: "), sg.Input(key="-DataAluguel-", size=(47,1))],
    [sg.Push(),sg.Button("Ver Livros", key="-verLivrosAlugar-"),sg.Push(), sg.Push(),sg.Button("Ver Clientes", key="-verClientesAlugar-"), sg.Push()], 
    [sg.Multiline(key="-verLivrosTelinha-", size=(40,10)), sg.Multiline(key="-verClientesTelinha-", size=(40,10))],
    [sg.Button("Voltar", key="-AlugarVoltar-"), sg.Button("Alugar", key="-AlugarLivro-")]
]

verAlugueis = [
    [sg.Text("ID do Aluguel que deseja visualizar:"), sg.Input(key="-VerAluguelPorID-", size=(20,1)),sg.Button("Verificar", key="-verificarVerIDAluguel-")],
    [sg.Text("ID do Cliente que deseja visualizar aluguel:"), sg.Input(key="-VerAluguelPorIDCliente-", size=(14,1)),sg.Button("Verificar", key="-verificarVerIDClienteAluguel-")],
    [sg.Text("ID do Livro que deseja visualizar aluguel:"), sg.Input(key="-VerAluguelPorIDLivro-", size=(16,1)),sg.Button("Verificar", key="-verificarVerIDLivroAluguel-")],
    [sg.Push(),sg.Button("Ver todos os Alugueis", key="-VerTodosAlugueis-"), sg.Push()],
    [sg.Push(),sg.Multiline(key="-todosAlugueis-",size=(40,10)),sg.Push()],
    [sg.Button("Voltar", key="-voltarVerAlugueis-")]
]

layout = [[sg.Column(telaInicial, key="-TelaInicial-", visible=True),sg.Column(telaGerenciamento, key="-TelaGerenciamento-", visible=False), sg.Column(telaInserir, key="-TelaInserir-",visible=False), sg.Column(telaVer, key="-TelaVer-", visible=False), sg.Column(telaDeletar, key="-TelaDeletar-", visible=False), sg.Column(telaAlterar, key="-TelaAlterar-", visible=False), sg.Column(alterar, key="-AlterarDefinitivamente-", visible=False), sg.Column(telaGerenciamentoClientes, key="-TelaGerenciamentoCliente-", visible=False), sg.Column(telaInserirCliente, key="-TelaInserirCliente-", visible=False), sg.Column(telaVerClientes, key="-TelaVerCliente-", visible=False), sg.Column(telaDeletarCliente, key="-TelaDeletarCliente-", visible=False), sg.Column(telaAlterarCliente, key="-TelaAlterarCliente-", visible=False), sg.Column(alterarCli, key="-AlterarCli-", visible=False), sg.Column(telaGerenciamentoAlugueis, key="-TelaGerenciamentoAlugueis-", visible=False), sg.Column(cadastrarNovoAluguel, key="-TelaCadastrarNovoAluguel-", visible=False), sg.Column(verAlugueis, key="-TelaVerAlugueis-", visible=False)]]

window = sg.Window("Biblioteca", layout)

# CONEXÃO COM O PGADMIN

try:
    con = Conexao("Biblioteca", "localhost","5432","postgres","postgres")

    print("Conectado")

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro - ", error)

while True:

    event, values = window.read()
    
    #BOTÃO X E SAIR:
    if event in ("-TelaInicialSair-", sg.WIN_CLOSED):
        break
    
    #BOTÕES DE TRANSIÇÃO DAS TELAS DOS GERENCIADORES:

    if event == "-GerenciamentoAlugueis-":
        window["-TelaInicial-"].update(visible=False)
        window["-TelaGerenciamentoAlugueis-"].update(visible=True)

    if event == "-GerenciamentoLivros-":
        window["-TelaInicial-"].update(visible=False)
        window["-TelaGerenciamento-"].update(visible=True)

    if event == "-GerenciamentoClientes-":
        window["-TelaInicial-"].update(visible=False)
        window["-TelaGerenciamentoCliente-"].update(visible=True)

    #BOTÃO CADASTRAR NOVO ALUGUEL:
    
    if event == "-CadastrarNovoAluguel-":
        window["-TelaGerenciamentoAlugueis-"].update(visible=False)
        window["-TelaCadastrarNovoAluguel-"].update(visible=True)

    #BOTÃO VER ALUGUEIS:

    if event == "-VerAlugueis-":
        window["-TelaGerenciamentoAlugueis-"].update(visible=False)
        window["-TelaVerAlugueis-"].update(visible=True)

    #BOTÃO VER CLIENTES:

    if event == "-VerClientes-":
        window["-TelaGerenciamentoCliente-"].update(visible=False)
        window["-TelaVerCliente-"].update(visible=True)

    #BOTÃO VER LIVROS:

    if event == "-VerLivros-":
        window['-TelaGerenciamento-'].update(visible=False)
        window['-TelaVer-'].update(visible=True)

    #BOTÃO INSERIR LIVROS:

    if event == "-InserirLivros-":
        window['-TelaGerenciamento-'].update(visible=False)
        window['-TelaInserir-'].update(visible=True)

    #BOTÃO ALTERAR LIVROS:

    if event == "-AlterarLivros-":
        window['-TelaGerenciamento-'].update(visible=False)
        window['-TelaAlterar-'].update(visible=True)

    #BOTÃO DELETAR LIVROS:

    if event == "-DeletarLivros-":
        window["-TelaGerenciamento-"].update(visible=False)
        window["-TelaDeletar-"].update(visible=True)
    
    #BOTÃO INSERIR CLIENTES:

    if event == "-InserirClientes-":
        window["-TelaInserirCliente-"].update(visible=True)
        window["-TelaGerenciamentoCliente-"].update(visible=False)
    
    #BOTÃO DELETAR CLIENTES:

    if event == "-DeletarClientes-":
        window["-TelaGerenciamentoCliente-"].update(visible=False)
        window["-TelaDeletarCliente-"].update(visible=True)

    #BOTÃO ALTERAR CLIENTES:

    if event == "-AlterarClientes-":
        window["-TelaGerenciamentoCliente-"].update(visible=False)
        window["-TelaAlterarCliente-"].update(visible=True)
    

    #BOTÕES VOLTAR:

    if event == "-voltarVerAlugueis-":
        window["-TelaVerAlugueis-"].update(visible=False)
        window["-TelaGerenciamentoAlugueis-"].update(visible=True)

    if event == "-AlugarVoltar-":
        window["-TelaCadastrarNovoAluguel-"].update(visible=False)
        window["-TelaGerenciamentoAlugueis-"].update(visible=True)

    if event == "-VoltarAlugueis-":
        window["-TelaGerenciamentoAlugueis-"].update(visible=False)
        window["-TelaInicial-"].update(visible=True)

    if event == "-AlterarClienteVoltar-":
        window["-AlterarCli-"].update(visible=False)
        window["-TelaAlterarCliente-"].update(visible=True)

    if event == "-voltarAltCli-":
        window["-TelaAlterarCliente-"].update(visible=False)
        window["-TelaGerenciamentoCliente-"].update(visible=True)

    if event == "-voltarDeletarCliente-":
        window["-TelaDeletarCliente-"].update(visible=False)
        window["-TelaGerenciamentoCliente-"].update(visible=True)

    if event == "-InserirClienteVoltar-":
        window["-TelaInserirCliente-"].update(visible=False)
        window["-TelaGerenciamentoCliente-"].update(visible=True)

    if event == "-TelaGerenciamentoClienteVoltar-":
        window["-TelaGerenciamentoCliente-"].update(visible=False)
        window["-TelaInicial-"].update(visible=True)

    if event == "-voltarVerClientes-":
        window["-TelaVerCliente-"].update(visible=False)
        window["-TelaGerenciamentoCliente-"].update(visible=True)

    if event == "-TelaGerenciamentoVoltar-":
        window["-TelaInicial-"].update(visible=True)
        window["-TelaGerenciamento-"].update(visible=False)

    if event == "-voltarDeletar-":
        window["-TelaDeletar-"].update(visible=False)
        window["-TelaGerenciamento-"].update(visible=True)

    if event =="-LivrosInserirVoltar-":
        window['-TelaGerenciamento-'].update(visible=True)
        window['-TelaInserir-'].update(visible=False)

    if event =="-voltarVer-":
        window['-TelaVer-'].update(visible=False)
        window['-TelaGerenciamento-'].update(visible=True)

    if event =="-voltarAlt-":
        window["-TelaAlterar-"].update(visible=False)
        window["-TelaGerenciamento-"].update(visible=True)

    if event =="-AlterarLivroVoltar-":
        window["-AlterarDefinitivamente-"].update(visible=False)
        window["-TelaAlterar-"].update(visible=True)
    

    # INSERIR LIVRO

    if event =="-LivrosInserirEnviar-":
        if values["-InserirNomeLivros-"] == "" and values["-InserirIdiomaLivros-"] == "" and values["-InserirNPaginasLivros-"] == "":
            sg.popup("Todos os campos estão vazios! Digite-os!")
        elif values["-InserirNomeLivros-"] == "":
            sg.popup("Campo 'Nome do Livro' está vazio! Digite-o!")
        elif values["-InserirIdiomaLivros-"] == "":
            sg.popup("Campo 'Idioma do Livro' está vazio! Digite-o!")
        elif values["-InserirNPaginasLivros-"] == "":
            sg.popup("Campo 'Número de Páginas' está vazio! Digite-o!")
        else:
            livros = Livro("default", values["-InserirNomeLivros-"], values["-InserirIdiomaLivros-"], values["-InserirNPaginasLivros-"] )
            con.manipularBanco(livros.inserirLivros("Livros"))
            sg.popup(f"Livro '{livros._NomeLivro}' adicionado à Biblioteca!")
    

    # INSERIR CLIENTE

    if event =="-InserirClienteEnviar-":
        if values["-InserirNomeCliente-"] == "" and values["-InserirCPFCliente-"] == "" and values["-InserirTelefoneCliente-"] == "" and values["-InserirEmailCliente-"] == "":
            sg.popup("Todos os campos estão vazios! Digite-os!")
        elif values["-InserirNomeCliente-"] == "":
            sg.popup("Campo 'Nome' está vazio! Digite-o!")
        elif values["-InserirCPFCliente-"] == "":
            sg.popup("Campo 'CPF' está vazio! Digite-o!")
        elif values["-InserirTelefoneCliente-"] == "":
            sg.popup("Campo 'Telefone' está vazio! Digite-o!")
        elif values["-InserirEmailCliente-"] == "":
            sg.popup("Campo 'E-mail' está vazio! Digite-o!")
        else:
            cliente = Cliente("default", values["-InserirNomeCliente-"], values["-InserirCPFCliente-"], values["-InserirTelefoneCliente-"], values["-InserirEmailCliente-"] )
            con.manipularBanco(cliente.inserirCliente("Clientes"))
            sg.popup(f"Cliente '{cliente._NomeCliente}' adicionado!")

    # OPÇÃO VER TODOS DA TELA VER LIVROS:

    if event =="-VerTodos-":
        livro = Livro(None, None, None, None)
        resultado = con.consultarBanco('''SELECT * FROM "Livros" ORDER BY "ID" ASC''')
        msg = ""
        for r in resultado:

            livro._id = r [0]
            livro._NomeLivro = r [1]
            livro._IdiomaLivro = r [2]
            livro._PaginasLivro = r [3]
            msg = msg + "\n" + livro.imprimirLivro()
        window["-todos-"].update(msg)
    
    # OPÇÃO VER TODOS DA TELA VER CLIENTES:

    if event =="-VerTodosClientes-":
        cliente = Cliente(None, None, None, None, None)
        resultado = con.consultarBanco('''SELECT * FROM "Clientes" ORDER BY "ID" ASC''')
        msg = ""
        for r in resultado:

            cliente._id = r [0]
            cliente._NomeCliente = r [1]
            cliente._CPF = r [2]
            cliente._telefone = r [3]
            cliente._email = r [4]
            msg = msg + "\n" + cliente.imprimirCliente()
        window["-todosClientes-"].update(msg)

    # OPÇÃO VER TODOS DA TELA DELETAR LIVROS:

    if event =="-VerTodosDel-":
        livro = Livro(None, None, None, None)
        resultado = con.consultarBanco('''SELECT * FROM "Livros" ORDER BY "ID" ASC''')
        msg = ""
        for r in resultado:

            livro._id = r [0]
            livro._NomeLivro = r [1]
            livro._IdiomaLivro = r [2]
            livro._PaginasLivro = r [3]
            msg = msg + "\n" + livro.imprimirLivro()
        window["-todosDel-"].update(msg)

    # OPÇÃO VER TODOS DA TELA DELETAR CLIENTES:

    if event =="-VerTodosDelCli-":
        cliente = Cliente(None, None, None, None, None)
        resultado = con.consultarBanco('''SELECT * FROM "Clientes" ORDER BY "ID" ASC''')
        msg = ""
        for r in resultado:

            cliente._id = r [0]
            cliente._NomeCliente = r [1]
            cliente._CPF = r [2]
            cliente._telefone = r [3]
            cliente._email = r [4]
            msg = msg + "\n" + cliente.imprimirCliente()
        window["-todosDelCli-"].update(msg)
    
    # VER TODOS DA TELA ALTERAR CLIENTES

    if event =="-VerTodosAltCli-":
        cliente = Cliente(None, None, None, None, None)
        resultado = con.consultarBanco('''SELECT * FROM "Clientes" ORDER BY "ID" ASC''')
        msg = ""
        for r in resultado:

            cliente._id = r [0]
            cliente._NomeCliente = r [1]
            cliente._CPF = r [2]
            cliente._telefone = r [3]
            cliente._email = r [4]
            msg = msg + "\n" + cliente.imprimirCliente()
        window["-todosAltCli-"].update(msg)


    # VERIFICAR ID NA TELA INSERIR LIVRO

    if event =="-verificarVerID-":
        if values["-InserirIdLivro-"] == "" :
            msg = "ID vazio! Por favor, insira um ID!"
        else:
            livro = Livro(values["-InserirIdLivro-"], None, None, None)
            resultado = con.consultarBanco(livro.listarLivros("Livros"))
            if resultado == []:
                msg = "ID não existe! Por favor, insira um ID valido!"
            else:
                livro._NomeLivro = resultado [0][1]
                livro._IdiomaLivro = resultado [0][2]
                livro._PaginasLivro = resultado [0][3]
                msg = livro.imprimirLivro()
        sg.popup(msg)
    
    # VERIFICAR SE O ID DO CLIENTE EXISTE NA TELA VER

    if event =="-verificarVerIDCliente-":
        if values["-InserirIdCliente-"] == "" :
            msg = "ID vazio! Por favor, insira um ID!"
        else:
            cliente = Cliente(values["-InserirIdCliente-"], None, None, None, None)
            resultado = con.consultarBanco(cliente.listarCliente("Clientes"))
            if resultado == []:
                msg = "ID não existe! Por favor, insira um ID valido!"
            else:
                cliente._NomeCliente = resultado [0][1]
                cliente._CPF = resultado [0][2]
                cliente._telefone = resultado [0][3]
                cliente._email = resultado [0][4]
                msg = cliente.imprimirCliente()
        sg.popup(msg)
    
    # VERIFICAR ID NA TELA DELETAR LIVRO:

    if event == "-deletar-":
        if values["-IDdeletar-"] == "":
            msg = "ID vazio! Por favor, insira um ID!"
        else:
            livro = Livro(values["-IDdeletar-"], None, None, None)
            resultado = con.consultarBanco(livro.listarLivros("Livros"))
            if resultado == []:
                msg = "ID não existe! Por favor, insira um ID valido!"
            else:
                livro = con.manipularBanco(livro.DeletarLivros("Livros"))
                msg = "O livro foi deletado!"
        sg.popup(msg)
    
    # VERIFICAR ID NA TELA DELETAR CLIENTE:

    if event == "-deletarCliente-":
        if values["-IDdeletarCliente-"] == "":
            msg = "ID vazio! Por favor, insira um ID!"
        else:
            cliente = Cliente(values["-IDdeletarCliente-"], None, None, None, None)
            resultado = con.consultarBanco(cliente.listarCliente("Clientes"))
            if resultado == []:
                msg = "ID não existe! Por favor, insira um ID valido!"
            else:
                cliente = con.manipularBanco(cliente.DeletarCliente("Clientes"))
                msg = "O Cliente foi deletado!"
        sg.popup(msg)


    # OPÇÃO VER TODOS DA TELA DELETAR LIVROS:

    if event =="-VerTodosAlt-":
        livro = Livro(None, None, None, None)
        resultado = con.consultarBanco('''SELECT * FROM "Livros" ORDER BY "ID" ASC''')
        msg = ""
        for r in resultado:

            livro._id = r [0]
            livro._NomeLivro = r [1]
            livro._IdiomaLivro = r [2]
            livro._PaginasLivro = r [3]
            msg = msg + "\n" + livro.imprimirLivro()
        window["-todosAlt-"].update(msg)


    # VERIFICAR ID NA ALTERAR LIVRO:

    if event =="-verificarAlterarID-":
        if values["-AlterarIdLivro-"] == "" :
            msg = "ID vazio! Por favor, insira um ID!"
        else:
            livro = Livro(values["-AlterarIdLivro-"], None, None, None)
            resultado = con.consultarBanco(livro.listarLivros("Livros"))
            if resultado == []:
                msg = "ID não existe! Por favor, insira um ID valido!"
            else:
                livro._NomeLivro = resultado [0][1]
                livro._IdiomaLivro = resultado [0][2]
                livro._PaginasLivro = resultado [0][3]
                msg = livro.imprimirLivro()
                window["-TelaAlterar-"].update(visible=False)
                window["-AlterarDefinitivamente-"].update(visible=True)
        sg.popup(msg)

    # VERIFICAR ID NA TELA ALTERAR CLIENTE:

    if event =="-verificarAlterarIDCli-":
        if values["-AlterarIdCliente-"] == "" :
            msg = "ID vazio! Por favor, insira um ID!"
        else:
            cliente = Cliente(values["-AlterarIdCliente-"], None, None, None, None)
            resultado = con.consultarBanco(cliente.listarCliente("Clientes"))
            if resultado == []:
                msg = "ID não existe! Por favor, insira um ID valido!"
            else:
                cliente._NomeCliente = resultado [0][1]
                cliente._CPF = resultado [0][2]
                cliente._telefone = resultado [0][3]
                cliente._email = resultado [0][4]
                msg = cliente.imprimirCliente()
                window["-TelaAlterarCliente-"].update(visible=False)
                window["-AlterarCli-"].update(visible=True)
        sg.popup(msg)
        
    # ALTERAR LIVRO:

    if event =="-AlterarLivroEnviar-":
        if values["-AlterarNomeLivro-"] == "" and values["-AlterarIdiomaLivro-"] == "" and values["-AlterarNPaginasLivro-"] == "":
            sg.popup("Todos os campos estão vazios! Digite-os!")
        elif values["-AlterarNomeLivro-"] == "":
            sg.popup("Campo 'Nome do Livro' está vazio! Digite-o!")
        elif values["-AlterarIdiomaLivro-"] == "":
            sg.popup("Campo 'Idioma do Livro' está vazio! Digite-o!")
        elif values["-AlterarNPaginasLivro-"] == "":
            sg.popup("Campo 'Número de Páginas' está vazio! Digite-o!")
        else:
            livros = Livro(values["-AlterarIdLivro-"], values["-AlterarNomeLivro-"], values["-AlterarIdiomaLivro-"], values["-AlterarNPaginasLivro-"])
            con.manipularBanco(livros.alterarLivros("Livros"))
            sg.popup(f"Livro alterado para '{livros._NomeLivro}' salvo na Biblioteca!")
    
    # ALTERAR CLIENTE:

    if event =="-AlterarClienteEnviar-":
        if values["-AlterarNomeCliente-"] == "" and values["-AlterarCPFCliente-"] == "" and values["-AlterarTelefoneCliente-"] == "" and values["-AlterarEmailCliente-"] == "":
            sg.popup("Todos os campos estão vazios! Digite-os!")
        elif values["-AlterarNomeCliente-"] == "":
            sg.popup("Campo 'Nome' está vazio! Digite-o!")
        elif values["-AlterarCPFCliente-"] == "":
            sg.popup("Campo 'CPF' está vazio! Digite-o!")
        elif values["-AlterarTelefoneCliente-"] == "":
            sg.popup("Campo 'Telefone' está vazio! Digite-o!")
        elif values["-AlterarEmailCliente-"] == "":
            sg.popup("Campo 'E-mail' está vazio! Digite-o!")
        else:
            cliente = Cliente(values["-AlterarIdCliente-"], values["-AlterarNomeCliente-"], values["-AlterarCPFCliente-"], values["-AlterarTelefoneCliente-"], values["-AlterarEmailCliente-"] )
            con.manipularBanco(cliente.alterarCliente("Clientes"))
            sg.popup(f"Cliente '{cliente._NomeCliente}' alterado!")

    # ALUGAR LIVRO

    if event =="-AlugarLivro-":
        if values["-DataAluguel-"] == "" and values["-IDLivroAluguel-"] == "" and values["-IDClienteAluguel-"] == "":
            sg.popup("Todos os campos estão vazios! Digite-os!")
        elif values["-DataAluguel-"] == "":
            sg.popup("Campo 'Data do Aluguel' está vazio! Digite-o!")
        elif values["-IDLivroAluguel-"] == "":
            sg.popup("Campo 'ID do Livro' está vazio! Digite-o!")
        elif values["-IDClienteAluguel-"] == "":
            sg.popup("Campo 'ID do Cliente' está vazio! Digite-o!")
        else:
            cliente = Cliente(values["-IDClienteAluguel-"], None, None, None, None)
            resultado1 = con.consultarBanco(cliente.listarCliente("Clientes"))
            livro = Livro(values["-IDLivroAluguel-"], None, None, None)
            resultado2 = con.consultarBanco(livro.listarLivros("Livros"))
            if resultado1 == []:
                sg.popup("ID não existe! Por favor, insira um ID de cliente válido!")
            elif resultado2 == []:
                sg.popup("ID não existe! Por favor, insira um ID de livro válido!")
            else:
                aluguel = Aluguel("default", values["-IDClienteAluguel-"], values["-IDLivroAluguel-"], values["-DataAluguel-"])
                con.manipularBanco(aluguel.cadastrarAluguel("Alugueis"))
                sg.popup("Aluguel Efetuado com Sucesso!")

            
    #VER CLIENTES DENTRO DA TELA ALUGUEL:

    if event =="-verClientesAlugar-":
        cliente = Cliente(None, None, None, None, None)
        resultado = con.consultarBanco('''SELECT * FROM "Clientes" ORDER BY "ID" ASC''')
        msg = ""
        for r in resultado:

            cliente._id = r [0]
            cliente._NomeCliente = r [1]
            cliente._CPF = r [2]
            cliente._telefone = r [3]
            cliente._email = r [4]
            msg = msg + "\n" + cliente.imprimirCliente()
        window["-verClientesTelinha-"].update(msg)

    #VER LIVROS DENTRO DA TELA ALUGUEL:

    if event =="-verLivrosAlugar-":
        livro = Livro(None, None, None, None)
        resultado = con.consultarBanco('''SELECT * FROM "Livros" ORDER BY "ID" ASC''')
        msg = ""
        for r in resultado:

            livro._id = r [0]
            livro._NomeLivro = r [1]
            livro._IdiomaLivro = r [2]
            livro._PaginasLivro = r [3]
            msg = msg + "\n" + livro.imprimirLivro()
        window["-verLivrosTelinha-"].update(msg)


    #VERIFICAR ALUGUEL POR ID DE ALUGUEL:

    if event =="-verificarVerIDAluguel-":
        if values["-VerAluguelPorID-"] == "" :
            msg = "ID vazio! Por favor, insira um ID!"
        else:
            aluguel = Aluguel(values["-VerAluguelPorID-"], None, None, None, None, None)
            resultado = con.consultarBanco(aluguel.consultarAluguel("Alugueis"))
            if resultado == []:
                msg = "ID não existe! Por favor, insira um ID valido!"
            else:
                aluguel._id = resultado[0][0]
                aluguel._idCLi = resultado [0][1]

                aluguel._nomeCli= con.consultarBanco(f'''SELECT "Nome" FROM "Clientes"
                WHERE "ID" = '{aluguel._idCLi}' ''')[0][0]

                aluguel._idLivro = resultado [0][2]

                aluguel._nomeLiv = con.consultarBanco(f'''SELECT "NomeLivro" FROM "Livros"
                WHERE "ID" = '{aluguel._idLivro}' ''')[0][0]

                aluguel._dataAluguel = resultado [0][3]
                msg = aluguel.imprimirAluguel()
                
        sg.popup(msg)

    #VERIFICAR ALUGUEL POR ID DE CLIENTE:

    if event =="-verificarVerIDClienteAluguel-":
        if values["-VerAluguelPorIDCliente-"] == "" :
            msg = "ID vazio! Por favor, insira um ID!"
        else:
            aluguel = Aluguel(None, values["-VerAluguelPorIDCliente-"], None, None, None, None)
            resultado = con.consultarBanco(aluguel.consultarAluguelporIDCliente("Alugueis"))
            if resultado == []:
                msg = "ID não existe! Por favor, insira um ID valido!"
            else:
                aluguel._id = resultado[0][0]
                aluguel._idCLi = resultado [0][1]
                aluguel._nomeCli= con.consultarBanco(f'''SELECT "Nome" FROM "Clientes"
                WHERE "ID" = '{aluguel._idCLi}' ''')[0][0]

                aluguel._idLivro = resultado [0][2]

                aluguel._nomeLiv = con.consultarBanco(f'''SELECT "NomeLivro" FROM "Livros"
                WHERE "ID" = '{aluguel._idLivro}' ''')[0][0]
                aluguel._dataAluguel = resultado [0][3]
                msg = aluguel.imprimirAluguel()
        sg.popup(msg)

    #VERIFICAR ALUGUEL POR ID DE LIVRO:

    if event =="-verificarVerIDLivroAluguel-":
        if values["-VerAluguelPorIDLivro-"] == "" :
            msg = "ID vazio! Por favor, insira um ID!"
        else:
            aluguel = Aluguel(None, None, values["-VerAluguelPorIDLivro-"], None, None, None)
            resultado = con.consultarBanco(aluguel.consultarAluguelporIDLivro("Alugueis"))
            if resultado == []:
                msg = "ID não existe! Por favor, insira um ID valido!"
            else:
                aluguel._id = resultado[0][0]
                aluguel._idCLi = resultado [0][1]
                aluguel._nomeCli= con.consultarBanco(f'''SELECT "Nome" FROM "Clientes"
                WHERE "ID" = '{aluguel._idCLi}' ''')[0][0]

                aluguel._idLivro = resultado [0][2]

                aluguel._nomeLiv = con.consultarBanco(f'''SELECT "NomeLivro" FROM "Livros"
                WHERE "ID" = '{aluguel._idLivro}' ''')[0][0]
                aluguel._dataAluguel = resultado [0][3]
                msg = aluguel.imprimirAluguel()
        sg.popup(msg)

    #BOTÃO VER TODOS OS ALUGUEIS:

    if event =="-VerTodosAlugueis-":
        aluguel = Aluguel(None, None, None, None, None, None)
        resultado = con.consultarBanco('''SELECT * FROM "Alugueis" ORDER BY "ID" ASC''')
        msg = ""
        for r in resultado:

            aluguel._id = r [0]
            aluguel._idCLi = r [1]
            aluguel._nomeCli= con.consultarBanco(f'''SELECT "Nome" FROM "Clientes"
                WHERE "ID" = '{aluguel._idCLi}' ''')[0][0]

            aluguel._idLivro = r [2]

            aluguel._nomeLiv = con.consultarBanco(f'''SELECT "NomeLivro" FROM "Livros"
                WHERE "ID" = '{aluguel._idLivro}' ''')[0][0]
            aluguel._dataAluguel = r [3]
            msg = msg + "\n" + aluguel.imprimirAluguel()
        window["-todosAlugueis-"].update(msg)

window.close()