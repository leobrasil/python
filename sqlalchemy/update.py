from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

upd = update(user_table).where(user_table.c.nome == 'leandro')

upd = upd.values(nome='LeoBrasil')

resultado = con.execute(upd)

print('linhas alteradas: ', resultado.rowcount)