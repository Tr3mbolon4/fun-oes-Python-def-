def cabecario_inicioapp():
  print('='*43)
  print('       Alexandre Santana Dos Santos:')
  print( ' *'*52)
  print('     cybersegurança em formação| linux | python | C++ | hardware | redes | Ethical Hacking')
  print('   *'*39)
  print('        C O D I G O - P Y T H O N')
  print('='*50)
  print('='*50)
  print('='*50)

cabecario_inicioapp()
def cadastro_loj():
  
  produto = input('Nome do Produto: ')
  cor = input('Qual a cor do Produto: ')
  estoque = int(input('Quantos em estoque: '))
  valor_venda = float(input('Qual valor do Produto: '))
  
  print('='*40)
  
  print(f'{produto} na Cor: {cor} Tem no Estoque: {estoque} Pelo Valor de R$[{valor_venda}]')
  print('='*40)
  venda = int(input('Quantos Deseja comprar?: '))
  print('='*40)
  
  restao = estoque - venda
  print('Restão Em estoque: ', restao)
  print('='*40)

cadastro_loj()
cadastro_loj()
cadastro_loj()
cadastro_loj()
cadastro_loj()