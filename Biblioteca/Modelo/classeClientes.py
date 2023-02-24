class Cliente:

    def __init__(self,id,NomeCliente,CPF,telefone,email):
        self._id = id
        self._NomeCliente = NomeCliente
        self._CPF = CPF
        self._telefone = telefone
        self._email = email

    def inserirCliente(self, tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        Values({self._id},'{self._NomeCliente}','{self._CPF}','{self._telefone}', '{self._email}')
        '''

        return sql

    def listarCliente(self, tabela):
        
        sql = f'''
        SELECT * FROM "{tabela}" 
        WHERE "ID" = {self._id}
        
        '''
        return sql
    
    def DeletarCliente(self, tabela):

        sql = f'''
        DELETE FROM "{tabela}"
        WHERE "ID" = {self._id}
        
        '''
        return sql
    
    def alterarCliente(self, tabela):

        sql = f'''
        UPDATE "{tabela}"
        SET "Nome" = '{self._NomeCliente}', "CPF" = '{self._CPF}', "Telefone" = '{self._telefone}', "E-mail" = '{self._email}'
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def imprimirClienteDeletado(self):
    
        return f'''
    O Cliente selecionado foi excluído!
        '''

    def imprimirCliente(self):
    
        return f'''
    Cliente:
    ID: {self._id}
    Nome do Cliente: {self._NomeCliente}
    CPF: {self._CPF}
    Telefone: {self._telefone}
    E-mail: {self._email}
        
        '''


