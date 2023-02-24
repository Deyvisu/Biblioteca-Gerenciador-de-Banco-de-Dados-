class Livro:

    def __init__(self,id,NomeLivro,IdiomaLivro,PaginasLivro):
        self._id = id
        self._NomeLivro = NomeLivro
        self._IdiomaLivro = IdiomaLivro
        self._PaginasLivro = PaginasLivro

    def inserirLivros(self, tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        Values({self._id},'{self._NomeLivro}','{self._IdiomaLivro}','{self._PaginasLivro}')
        '''

        return sql

    def listarLivros(self, tabela):
        
        sql = f'''
        SELECT * FROM "{tabela}" 
        WHERE "ID" = {self._id}
        
        '''
        return sql
    
    def DeletarLivros(self, tabela):

        sql = f'''
        DELETE FROM "{tabela}"
        WHERE "ID" = {self._id}
        
        '''
        return sql
    
    def alterarLivros(self, tabela):

        sql = f'''
        UPDATE "{tabela}"
        SET "NomeLivro" = '{self._NomeLivro}', "Idioma" = '{self._IdiomaLivro}', "NumeroPaginas" = '{self._PaginasLivro}'
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def imprimirLivroDeletado(self):
    
        return f'''
    O Livro selecionado foi excluído!
        '''

    def imprimirLivro(self):
    
        return f'''
    Livro:
    ID: {self._id}
    Nome: {self._NomeLivro}
    Idioma: {self._IdiomaLivro}
    Número de Páginas: {self._PaginasLivro}
        
        '''
    

