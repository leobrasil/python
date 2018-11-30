from core import user_table, engine

con = engine.connect()
ins = user_table.insert()

new = ins.values(nome='leandro', idade=24,senha='4linux')

con.execute(new)