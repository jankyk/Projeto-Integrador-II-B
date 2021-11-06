import os #importa parametros do windows
import time #importa função timer / pause


def leiaInt(msg):
  valida = False
  valor = 0
  while True:
   n =str(input(msg))
   if n.isnumeric():
    valor = int(n)
    valida = True    
   else:
    print("ERRO! Digite uma opção válida: ")
   if valida == True:
    break
  return valor


#Funcionalidades esperadas no programa:
#a) Cadastramento de perguntas e respostas;
#b) Apresentação das perguntas cadastradas;
#c) Apresentação das respostas disponíveis;
#d) Escolha de uma resposta;
#e) Apresentação de informações sobre o resultado da escolha (correta ou incorreta);
#f) Apresentação da quantidade de respostas corretas e pontuação total.
pontos = 0
qntrespostacerta = 0

#Pergunta 1 padrão
p1padrao = ('\nPaulo está efetuando uma auditoria na empresa BalasGoma com o intuito de diagnosticar vulnerabilidades e sugerir melhorias na segurança da informação. Paulo identificou que a empresa possui um datacenter onde estão localizados todos os servidores da instituição.'
'\nApós concluir o seu relatório, Paulo sugeriu três melhorias para a sala do datacenter, visando diminuir as vulnerabilidades físicas encontradas.\n'
'\nMarque a alternativa que corresponde a sugestão correta de Paulo para o Datacenter\n')
r1padrao_p1 = ('Implementar uma solução de Antivírus nos servidores, efetuar a substituição do rack aberto por um modelo fechado com chave e efetuar o backup dos arquivos para um ambiente na nuvem.\n')
r2padrao_p1 = ('Efetuar a manutenção nos Nobreak periodicamente para garantir a integridade das baterias, implementar um sistema de monitoramento para alertas do ambiente (energia, temperatura e umidade) e implementar um sistema biometria para restringir o acesso a sala do datacenter.\n')
r3padrao_p1 = ('Limitar o controle de acesso a sala do datacenter somente as pessoas autorizadas, efetuar um inventário de hardware e software das maquinas no DC e implementar uma solução de firewall para filtrar e barrar os pacotes de conexão indesejados.\n')
r1certapadrao_p1 = 2

#Pergunta 2 padrão
p2padrao = ('\nMaria trabalha na empresa InfoContabil, a qual sofreu um ataque cibernético recentemente. A InfoContabil contratou uma empresa de segurança para investigar o tipo de ataque e apresentar uma possível solução, visando prevenir ataques futuros.\nConversando com Maria, ela informou que o indivíduo mal intencionado conseguiu acesso ao e-mail do financeiro, onde emitiu uma guia de pagamento no valor de R$20.000,00 reais, se passando por um fornecedor da empresa.\nForam verificados todos os servidores e as estações de trabalho dos usuários, mas não foi encontrado nenhum rastro do ataque. Analisando os Logs da Central telefônica, foi possível encontrar um registro de entrada de uma  ligação vindo de um número desconhecido.\nNo resultado do Pentest (Penetration Test), o mesmo informou que a porta 443 (HTTPS) do servidor SRV01AD está aberta para a WAN sem restrição de origem. Essa publicação se trata do sistema da empresa, onde seus clientes efetuam o acesso. O relatório também informou que a senha do usuário administrador do servidor SRV01AD está com seu nível de segurança muito baixo.\nA conclusão apresentada pela empresa de segurança, identificou o tipo de ataque e sugeriu uma solução para que a InfoContabil consiga se prevenir, evitando ataques futuros deste mesmo tipo.\nAnalisando as informações acima,  selecione a resposta correta do tipo de ataque e solução identificada pelos analistas na auditoria.\n')

r1padrao_p2 = ('Ataque de força bruta, a sugestão é a instalação de antivírus nos servidores e também nas estações de trabalho;\n')
r2padrao_p2 = ('DDOS “Negação de Serviço”, a sugestão é efetuar a implantação de um Firewall\n')
r3padrao_p2 = ('Engenharia Social, a solução é realizar treinamento com os colaboradores da empresa')
r1certapadrao_p2 = 3

#Pergunta 3 padrão
p3padrao = ('\nA empresa DeixaComigo prestadora de serviços, oferece variados serviços como Desenvolvimento de Softwares, Pesquisa e Gerenciamento de Grandes Volumes de Dados e Gestão de Transferências Eletrônicas (TEF), a empresa já adotou um conjunto de requisitos, processos e controles que minimizam o risco da organização garantindo a proteção de pesquisas e dados de software, informações empresariais e além dos dados de clientes físicos e jurídicos que passam pela empresa e assim viabilizando um Sistema de Gestão de Segurança da Informação.\nA empresa resolveu se certificar segundo uma Norma da famila ISO 27000, A certificação que rege esse SGSI é:\n')

r1padrao_p3 = ('Certificação ISO 27005''\n')
r2padrao_p3 = ('Certificação ISO 27001''\n')
r3padrao_p3 = ('Certificação ISO 27002')
r1certapadrao_p3 = 2

# Solicita a pergunta 1
p1 = input('Segurança da Informação: Cadastrar pergunta 1: ')
#Valida se é pra exibir a pergtunta pré cadastrada na Pergutna 1
if (p1 == "p1padrao"):
  p1 = p1padrao
  p1_r1 = r1padrao_p1
  p1_r2 = r2padrao_p1
  p1_r3 = r3padrao_p1
  rcerta1 = r1certapadrao_p1

else:
  p1_r1 = input('Insira alteranativa de resposta 1: ')
  p1_r2 = input('Insira alteranativa de resposta 2: ')
  p1_r3 = input('Insira alteranativa de resposta 3: ')
  rcerta1 = leiaInt('Qual será a resposta correta? ')

# Valida se a respota correta foi informada entre 1 a 3
if ((rcerta1 < 1 or rcerta1 > 3)):
  while (rcerta1 < 1) or (rcerta1 > 3):
    print ("Inforação inválida!")
    rcerta1 = int(input('Qual será a resposta correta? '))


#esse comando limpa a tela do console
os.system('clear') or None

#Solicita a pergunta 2
p2 = input('Segurança da Informação: Cadastrar pergunta 2: ')
#Valida se é pra exibir a pergtunta pré cadastrada na Pergunta 2
if (p2 == "p2padrao"):
  p2 = p2padrao
  p2_r1 = r1padrao_p2
  p2_r2 = r2padrao_p2
  p2_r3 = r3padrao_p2
  rcerta2 = r1certapadrao_p2

else:
  p2_r1 = input('Insira alteranativa de resposta 1: ')
  p2_r2 = input('Insira alteranativa de resposta 2: ')
  p2_r3 = input('Insira alteranativa de resposta 3: ')
  rcerta2 = leiaInt('Qual será a resposta correta? ')

# Valida se a respota correta foi informada entre 1 a 3
if (rcerta2 < 1 or rcerta2 > 3):
  while (rcerta2 < 1) or (rcerta2 > 3):
   print ("Inforação inválida!")
   rcerta2 = leiaInt('Qual será a resposta correta? ')


#esse comando limpa a tela do console
os.system('clear') or None

# Solicita a pergunta 3
p3 = input('Segurança da Informação: Cadastrar pergunta 3: ')
#Valida se é pra exibir a pergtunta pré cadastrada na Pergutna 3
if (p3 == "p3padrao"):
  p3 = p3padrao
  p3_r1 = r1padrao_p3
  p3_r2 = r2padrao_p3
  p3_r3 = r3padrao_p3
  rcerta3 = r1certapadrao_p3

else:
  p3_r1 = input('Insira alteranativa de resposta 1: ')
  p3_r2 = input('Insira alteranativa de resposta 2: ')
  p3_r3 = input('Insira alteranativa de resposta 3: ')
  rcerta3 = leiaInt('Qual será a resposta correta? ')

# Valida se a respota correta foi informada entre 1 a 3
if ((rcerta3 < 1 or rcerta3 > 3)):
  while (rcerta3 < 1) or (rcerta3 > 3):
    print ("Inforação inválida!")
    rcerta3 = int(input('Qual será a resposta correta? '))


#esse comando limpa a tela do console
os.system('clear') or None

user = input('Insira seu nome: ')
os.system('clear') or None

#apresentação pergunta 1
print('Pergunta de número 1: \n')

print (p1 + '\n')

print ('Opção 1: ' + p1_r1)
print ('Opção 2: ' + p1_r2)
print ('Opção 3: ' + p1_r3)
print ('\n' + 'Para opção 1 digite o numeral 1, para opção digite o numeral 2 e para opção 3 digite o numeral 3 ')

rusuario = leiaInt('\n' + 'Qual será a resposta correta? ')

# Valide se o usuario digitou um numero de 1 a 3 na pergunta 1
if (rusuario >= 1 and rusuario <= 3):
  if (rusuario == rcerta1):
    pontos += 20
    qntrespostacerta += 1
    os.system('clear') or None
    print ('\n' + 'Parabéns ' +user + ', você acertou e está com ' + str(pontos) + ' pontos')
  else:
    os.system('clear') or None
    print ('\n' + 'Resporta incorreta, '+user+'\nA resposta correta é: ', rcerta1)
  
# usuário digitou opção inválida - Vai inforamr o erro, e solicitar a pergunta novamente

else:
  while (rusuario <1) or (rusuario >3):
    os.system('clear') or None
    print ('Informação inválida, Você digitou: ' + str(rusuario) + ' favor informar uma opção válida') 
    print (p1)
    print ('\n')
    print ('Opção 1: '+ p1_r1)
    print ('Opção 2: '+ p1_r2)
    print ('Opção 3: '+ p1_r3)
    print ('\n')
    print ('Para opção 1 digite o numeral 1, para opção 2 digite o numeral 2 e para opção 3 digite o numeral 3 ')
    rusuario = leiaInt('Informe a alternativa correta? ')

time.sleep(3) #função de espera
os.system('clear') or None

#apresentação pergunta 2:
print('-------------------------------')
print('\n' + 'Pergunta de número 2: \n')

print (p2 + '\n')

print ('Opção 1: ' + p2_r1)
print ('Opção 2: ' + p2_r2)
print ('Opção 3: ' + p2_r3)
print ('\n' + 'Para opção 1 digite o numeral 1, para opção digite o numeral 2 e para opção 3 digite o numeral 3 ')

rusuario = leiaInt('\n' + 'Qual será a resposta correta? ')

# Valide se o usuario digitou um numero de 1 a 3 na pergunta 2
if (rusuario >= 1 and rusuario <= 3):
  if (rusuario == rcerta2):
    os.system('clear') or None
    pontos += 20
    qntrespostacerta += 1
    print ('\n' + 'Parabéns ' +user + ', você acertou e está com ' + str(pontos) + ' pontos')
    
  else:
    os.system('clear') or None
    print ('\n' + 'Resporta incorreta, '+user+'\nA resposta correta é: ',rcerta2)
  
# usuário digitou opção inválida - Vai inforamr o erro, e solicitar a pergunta novamente

else:
  while (rusuario <1) or (rusuario >3):
    os.system('clear') or None
    print ('Informação inválida, Você digitou: ' + str(rusuario) + ' favor informar uma opção válida') 
    print (p2)
    print ('\n')
    print ('Opção 1: '+ p2_r1)
    print ('Opção 2: '+ p2_r2)
    print ('Opção 3: '+ p2_r3)
    print ('\n')
    print ('Para opção 1 digite o numeral 1, para opção 2 digite o numeral 2 e para opção 3 digite o numeral 3 ')
    rusuario = leiaInt('Informe a alternativa correta? ')

time.sleep(3) #função de espera
os.system('clear') or None

#apresentação pergunta 3:
print('-------------------------------')
print('\n' + 'Pergunta de número 3: \n')

print (p3 + '\n')

print ('Opção 1: ' + p3_r1)
print ('Opção 2: ' + p3_r2)
print ('Opção 3: ' + p3_r3)
print ('\n' + 'Para opção 1 digite o numeral 1, para opção digite o numeral 2 e para opção 3 digite o numeral 3 ')

rusuario = leiaInt('\n' + 'Qual será a resposta correta? ')

# Valide se o usuario digitou um numero de 1 a 3 na resporta 3
if (rusuario >= 1 and rusuario <= 3):
  if (rusuario == rcerta3):
    os.system('clear') or None
    pontos += 20
    qntrespostacerta += 1
    print ('\n' + 'Parabéns ' +user + ', você acertou e está com ' + str(pontos) + ' pontos')
  else:
    os.system('clear') or None
    print ('\n' + 'Resporta incorreta, '+user+'\nA resposta correta é: ',rcerta3)
  
# usuário digitou opção inválida - Vai inforamr o erro, e solicitar a pergunta novamente
else:
  while (rusuario <1) or (rusuario >3):
    os.system('clear') or None
    print ('Informação inválida, Você digitou: ' + str(rusuario) + ' favor informar uma opção válida') 
    print (p3)
    print ('\n')
    print ('Opção 1: '+ p3_r1)
    print ('Opção 2: '+ p3_r2)
    print ('Opção 3: '+ p3_r3)
    print ('\n')
    print ('Para opção 1 digite o numeral 1, para opção 2 digite o numeral 2 e para opção 3 digite o numeral 3 ')
    rusuario = leiaInt('Informe a alternativa correta? ')

time.sleep(3) #função de espera
os.system('clear') or None

#mostra a quantidade de pontos até o momento e tmbém a quantidade de respotas certas
print ('Resultado final:')
print ( user + ', Você fez', + pontos, 'pontos! O total de acertos é =',qntrespostacerta)