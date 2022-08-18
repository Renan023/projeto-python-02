
n = str(input('Seu nome é '))
s = str(input('Qual seu sexo?[M/F] '))
if s == 'M' or s == 'm' :
    print("""\nBonito seu nome!!!
{}, muito prazer. Me chamo Isadora""".format(n))
else:
    print("""\nBonito nome!!
Me chamo Pedro. Muito prazer, {}""".format(n))
print("""Vamos verificar suas notas do curso de comunicação empresarial\n
Informe suas notas das 4 avaliações""")
n4 = float(input('\nQual sua nota '))
n1 = float(input('Qual sua nota '))
n2 = float(input('Qual sua nota '))
n3 = float(input('Qual sua nota '))
m = (n4+n1+n2+n3)/4
if m < 6.9:
    print('\n{} sua nota foi {:.1f}. Foi reprovado. Estude um pouco mais e tente novamente. Não desista'.format( n , m ))
else:
    print('\nParabéns {}. Você foi aprovado!!!Sua nota foi {:.1f}'.format( n , m ))
