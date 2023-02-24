class Aluguel:

    def __init__(self, id, idCli, idLivro, dataAluguel, nomeCli, nomeLiv):
        self._id = id
        self._idCLi = idCli
        self._idLivro = idLivro
        self._dataAluguel = dataAluguel
        self._nomeCli = nomeCli
        self._nomeLiv = nomeLiv


    def cadastrarAluguel(self, tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        VALUES({self._id}, '{self._idCLi}', '{self._idLivro}', '{self._dataAluguel}')
        '''
        return sql

    def consultarAluguel(self, tabela):
        sql = f'''
        SELECT * FROM "{tabela}"
        WHERE "ID" = '{self._id}'
        '''
        return sql
    
    def consultarAluguelporIDCliente(self, tabela):
        sql = f'''
        SELECT * FROM "{tabela}"
        WHERE "ID_Clientes" = '{self._idCLi}'
        '''
        return sql
    
    def consultarAluguelporIDLivro(self, tabela):
        sql = f'''
        SELECT * FROM "{tabela}"
        WHERE "ID_Livros" = '{self._idLivro}'
        '''
        return sql

    def imprimirAluguel(self):
    
        return f'''
    Aluguel:
    ID do Aluguel: {self._id}
    ID do Cliente: {self._idCLi}
    Nome do Cliente: {self._nomeCli}
    ID do Livro: {self._idLivro}
    Nome do Livro: {self._nomeLiv}
    Data do Aluguel: {self._dataAluguel}
    '''

    