import Model.DataBase_class as db

import Model.SQLITE_User_class as usr

c = input("digite 1 para login, 2 para cadastro ")



#user = usr.User()
#user.conn = db.Database()

if  c == 1:
    user.login()
    pass
elif c == 2:
    print("AAAAAA") 
    user.cadastro()
    pass
elif c == 3:
    pass
