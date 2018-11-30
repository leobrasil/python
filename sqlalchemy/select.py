from sqlalchemy import select
from core import user_table


sel = select([user_table])

for registro in sel.execute():
    print(registro)

registros = [x for x in sel.execute()]
print(registros)

#c -> representa a coluna
sel = select([user_table]).where(user_table.c.nome=='leandro')
print (list(sel.execute()))