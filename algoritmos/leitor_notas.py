
executar=True
#aprovado - media >=7
qteAlunosAprovados = 0
qteAlunosReprovados = 0
qteAlunosNota10 = 0
qteAlunosNota0 = 0
mediaGeral = 0
qteAlunos = 0

while executar:
    print('Digite 1 para receber notas \n')
    print('Digite 2 para ver estatisticas \n')
    print('Digite 3 para sair \n')

    opc = int(input('Digite sua opcao: '))

    if opc == 1:
        print('\n\nCadastrando notas dos alunos, digite -1 para parar')
        while True:
            nota1 = float(input('Digite a nota 1: '))
            if(nota1 < 0):
                break
            nota2 = float(input('Digite a nota 2: '))
            if(nota2 < 0):
                break
            nota3 = float(input('Digite a nota 3: '))
            if(nota3 < 0):
                break
            
            mediaAluno = (nota1+nota2+nota3)/3
            qteAlunos = qteAlunos+1
            mediaGeral = mediaGeral+mediaAluno
            if mediaAluno >=7:
                qteAlunosAprovados = qteAlunosAprovados+1
                if mediaAluno == 10:
                    qteAlunosNota10 +=1
            elif mediaAluno <7:
                qteAlunosReprovados = qteAlunosReprovados+1
                if mediaAluno == 0:
                    qteAlunosNota0 +=1
    elif opc == 2:
        print('Estatisticas dos alunos')
        print('quantidade de alunos: ', qteAlunos)
        print('Media geral: ', (mediaGeral/qteAlunos) )
        print('Quantidade alunos aprovados: ',qteAlunosAprovados)
    elif opc ==3:
        break
    else:
        print('Opcao invalida... tente de novamente \n')
            
