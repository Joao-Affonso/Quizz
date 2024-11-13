print('Bem vindo ao Quizz do João')

answer_user = input('Deseja começar o quizz? (S/N) ')
score = 0

if answer_user != 'S':
    quit()
    
print('Ok! Vamos começar:  \n')
print('Qual dos nomes abaixo é um jogo de poker?\n')
print('(A)Omaha\n(B)Truco\n(C)New York Holdem\n(D)Sueca\n')

answer_1 = input('Resposta: ')

if answer_1 == 'A':
    print('Correto!')
    score = score + 1
else:
    print('Incorreto!')
    
    
print('Com quantas cartas se joga o Texas Holdem?\n')
print('(A)3\n(B)5\n(C)2\n(D)4\n')

answer_2 = input('Resposta: ')

if answer_2 == 'C':
    print('Correto!')
    score = score + 1
else:
    print('Incorreto!')
    
    
print('Qual mão no poker é mais forte que sequência?\n')
print('(A)2 pares\n(B)Trinca\n(C)Par Holdem\n(D)Flush\n')

answer_3 = input('Resposta: ')

if answer_3 == 'D':
    print('Correto!')
    score = score + 1
else:
    print('Incorreto!')
    
print(f'Quizz finalizado, sua pontuação é {score}/3')