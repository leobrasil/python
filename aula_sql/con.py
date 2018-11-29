from psycopg2 import connect

def con_pgsql():
    try:
        con = connect("host=localhost user=python password=4linux dbname=fundamentals")
        #cur = con.cursor()

        #cur.execute("insert into usuario (nome, email, cpf, nascimento) values('{}','{}','{}','{}')".format('teste','teste@teste.com','xxx.xxx.xxx-xx','02/01/1980'))

    #    con.commit()
    #    print(cur.execute("select * from usuario"))
        
    except Exception as e:
        print(e)
        exit()
    #finally:
    #    try:
    #        cur.close()
    #        con.close()
    #    except Exception as e:
    #        print(e)
    return con