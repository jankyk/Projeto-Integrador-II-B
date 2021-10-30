import os #importa parametros do windows

#Funcionalidades esperadas no programa:
#a) Cadastramento de perguntas e respostas;
#b) Apresentação das perguntas cadastradas;
#c) Apresentação das respostas disponíveis;
#d) Escolha de uma resposta;
#e) Apresentação de informações sobre o resultado da escolha (correta ou incorreta);
#f) Apresentação da quantidade de respostas corretas e pontuação total.
pontos = 0

p1 = input('Digite uma pergunta sobre Segurança da Informação 1: ')
p1_r1 = input('Insira alteranativa de resposta 1: ')
p1_r2 = input('Insira alteranativa de resposta 2: ')
p1_r3 = input('Insira alteranativa de resposta 3: ')
rcerta1 = int(input('Qual será a resposta correta? '))

# Valida se a respota correta foi informada entre 1 a 3
if (rcerta1 <1 or rcerta1 >3):
  while (rcerta1 <1) or (rcerta1>3):
   print ("Inforação inválida!")
   rcerta1 = int(input('Qual será a resposta correta? '))

#esse comando limpa a tela do console
os.system('clear') or None

user = input('Insira seu nome: ')
os.system('clear') or None

print('Pergunta de numer 1: \n')

#apresentação pergunta 1
print (p1 + '\n')

print ('Opção 1: ' + p1_r1)
print ('Opção 2: ' + p1_r2)
print ('Opção 3: ' + p1_r3)
print ('\n' + 'Para opção 1 digite o numeral 1, para opção digite o numeral 2 e para opção 3 digite o numeral 3 ')

rusuario = int(input('\n' + 'Qual será a resposta correta? '))
# Valide se o usuario digitou um numero de 1 a 3
if (rusuario >= 1 and rusuario <= 3):
  if (rusuario == rcerta1):
    print ('\n' + 'Parabéns ' +user + ', você acertou!')
    pontos += 20
  else:
    print ('\n' + 'Resporta incorreta')
  
# usuário digitou opção inválida - Vai inforamr o erro, e solicitar a pergunta novamente

else:
  while (rusuario <1) or (rusuario >3):
    os.system('clear') or None
    print ("Informação inválida, Você digitou: " + str(rusuario) + " favor informar uma opção válida") 
    print (p1)
    print ('\n')
    print ('Opção 1: '+ p1_r1)
    print ('Opção 2: '+ p1_r2)
    print ('Opção 3: '+ p1_r3)
    print ('\n')
    print ('Para opção 1 digite o numeral 1, para opção 2 digite o numeral 2 e para opção 3 digite o numeral 3 ')

    rusuario = int(input('Informe a alternativa correta? '))

#mostra a quantidade de pontos até o momento
print ('\n' + 'Você tem', + pontos, 'pontos')





'''
ptest = ("\n"
"\n"
  "Paulo está efetuando uma auditoria na empresa BalasGoma com o intuito de diagnosticar vulnerabilidades e sugerir melhorias na segurança da informação. Paulo identificou que a empresa possui um datacenter onde estão localizados todos os servidores da instituição."
"\nApós concluir o seu relatório, Paulo sugeriu três melhorias para a sala do datacenter, visando diminuir as vulnerabilidades físicas encontradas."
"\n"
"\nMarque a alternativa que corresponde a sugestão correta de Paulo para o Datacenter"
"\n"
"\n"
"1- Implementar uma solução de Antivírus nos servidores, efetuar as substituição do rack aberto por um modelo fechado com chave e efetuar o backup dos arquivos para um ambiente na nuvem."
"\n"
"\n"
"2- Efetuar a manutenção nos Nobreak periodicamente para garantir a integridade das baterias, implementar um sistema de monitoramento para alertas do ambiente (energia, temperatura e umidade) e implementar de um sistema biometria para restringir o acesso a salda do datacenter."
"\n"
"\n"
"3- Limitar o controle de acesso a sala do datacenter somente as pessoas autorizadas, efetuar um inventário de hardware e software das maquinas no DC e implementar uma solução de firewall para filtrar e barrar os pacotes de conexão indesejados."
"\n"
"\n")


print (ptest)

rtest = int(input("Informe a resposta correta: " ))
if (rtest == 1):
  print ("\nVoce escolheu a respota:", rtest,)
#else (print (ptest)
#rtest = int(input("Informe a resposta correata: " )))
  

'''