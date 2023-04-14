class Teste:
    coluna = 'teste'

    def filter_by(self, **kwargs):
        print('keys', kwargs.keys())
        print('values', kwargs.values())
        print('-----')

    def exec(self):
        #manualmente
        self.filter_by(teste=1)

        #dinamicamente
        self.filter_by(**{self.coluna: 1})

foo = Teste()
foo.exec()