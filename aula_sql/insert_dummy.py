from faker import Faker
import con

con = con.con_pgsql()

fake = Faker('pt-BR')
cur = con.cursor()
try:
    for x in range(1,1000):
        sql = "insert into usuario (nome, email, cpf, nascimento) values('{}','{}','{}','{}')".format(fake.name().strip().lower(),fake.email(),fake.cpf(),fake.date_of_birth().strftime('%d/%m/%y'))
        cur.execute(sql)
        con.commit()
        
except Exception as e:
    print(e)
finally:
    cur.close()
