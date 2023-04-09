

class User:
    def __init__(self,
                  conn = "",
                  email = "",
                  senha = "",
                  nome = "",
                  idade = "",
                  loged = False
                  ):
        
        self.conn = conn
        self.loged = loged
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha
        

        #print(conn)
        

    @classmethod
    def login(self):
        
        roda = self.conn.execute("SELECT ID, email, senha from pessoas")
        
        for row in roda:
            if (row[1] == self.email) and (row[2] == self.senha):
                loged = True
                print("Conectado")
                
                ID = row[0]
                inp = input("clique 1 para editar user ou lique para 2 para deletar este user: ")
                if inp == 1:
                    self.editarUser(ID)
                elif inp == 2:
                    self.deletarUser(ID)

            elif (row[1] == self.email) and (row[2] != self.senha): 
                loged = False
                print("conecxão não efetuada, gostaria de mudar a senha")
                self.editarUser(ID)

            else:
                loged = False
                print("você não possui um cadastro")
                self.cadastro()
    
    @classmethod
    def cadastro(self):
        
        print("FUNFANDO")
        """ n = input("nome: ")
        i = int(input("Idade: "))
        e = input("Email: ")
        s = input("Senha: ") """

        sql = """ INSERT INTO pessoas (nome,idade,email,senha) VALUES (?, ?, ?, ?) """

        self.conn.execute(sql, (self.nome, self.idade, self.email, self.senha))
        self.conn.commit() 


    @classmethod
    def editarUser(self, id):
        sql = ""
        atribut = ["email", "senha"]

        if self.loged == True:

            inp = input("Aperte 1 para atualizar email, 2 para atualizar senha ou 3 para ambos: ")
            if inp == 1:
                e = input("Atualizar email: ")
                sql = """ UPDATE pessoas SET {:s} = {:s} WHERE ID = {:s} """.format(atribut[0], e, id)
            elif inp == 2:
                s = input("Atualizar senha: ")
                sql = """ UPDATE pessoas SET {:d} = {:d} WHERE ID = {:s} """.format(atribut[1], s, id) 
            elif inp == 3:
                e = input("Atualizar email: ")
                s = input("Atualizar email: ")
                sql = """ UPDATE pessoas SET {:s}, {:s}  = {:d}, {:s} WHERE ID = {:s} """.format(atribut[0], atribut[1], e, s, id)
        else:
            inp = input("digite nova senha: ")
        
            cursor = self.conn.execute("SELECT , senha from pessoas")

            for row in cursor:
                if (row[0] == inp):
                    print("senha já existente")
                elif (row[0] != inp):
                    self.conn.execute("UPDATE pessoas SET senha = {:s} WHERE ID = {:s}".format(inp, id))


        self.conn.execute(sql)
        self.conn.commit()

    @classmethod
    def deletarUser(self, id):
        self.conn.execute("DELETE from pessoas where ID = {:s};".format(id))
        self.conn.commit()

        