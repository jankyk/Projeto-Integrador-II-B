import os
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

p2 = input('Digite uma pergunta sobre Segurança da Informação 2: ')
p2_r1 = input('Insira alteranativa de resposta 1: ')
p2_r2 = input('Insira alteranativa de resposta 2: ')
p2_r3 = input('Insira alteranativa de resposta 3: ')
rcerta2 = int(input('Qual será a resposta correta? '))

p3 = input('Digite uma pergunta sobre Segurança da Informação 3: ')
p3_r1 = input('Insira alteranativa de resposta 1: ')
p3_r2 = input('Insira alteranativa de resposta 2: ')
p3_r3 = input('Insira alteranativa de resposta 3: ')
rcerta3 = int(input('Qual será a resposta correta? '))


os.system('clear') or None

user = input('Insira o Nome do Jogador: ')

os.system('clear') or None

print('Apresentação das Perguntas: \n \n')

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
  

 

#input('Digite uma pergunta sobre Segurança da Informação: ')
#p5_r1 = input('Insira alteranativa de resposta 1: ')
#p5_r2 = input('Insira alteranativa de resposta 2: ')
#p5_r3 = input('Insira alteranativa de resposta 3: ')
'''