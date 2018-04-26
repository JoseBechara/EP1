# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 18:49:02 2018

@author: luiza e jose 
"""

    
from firebase import firebase 

firebase=firebase.FirebaseApplication('https://ep-1-luizajose.firebaseio.com',None)

if firebase.get('dados', None) is None:
    ListaLojas={}
else:
    ListaLojas= firebase.get("dados", None)    
 

print("""
0 - Sair
1 - Adicionar loja
2 - Escolher loja
3 - Deletar loja
""")
choice=int(input("Faça sua escolha:  "))   
while choice!=0:
    if choice==1:
       Loja=input("Digite o nome da nova loja:  ")
       if Loja in ListaLojas:
            print("Loja ja cadastrada!")
       else:
            ListaLojas[Loja]={}
       break    
    
    if choice==2:
        
        Loja=input("Digite o nome da loja:  ")
        break
    if choice==3:
        Loja=input("Loja a ser deletada:  ")
        ctz=int(input("Tem certeza? (Sim-1 / Não-2):   ")) 
        if ctz==1:
          del ListaLojas[Loja]
          firebase.delete('https://ep-1-luizajose.firebaseio.com/dados',Loja)
          print("Loja deletada com sucesso!")
        if ctz==2:
            print("Não vou apagar!")
    print("""
0 - Sair
1 - Adicionar loja
2 - Escolher loja
3 - Deletar loja
""")
    
    
    choice=int(input("Faça sua escolha:  "))               
            
        
print("0 - Sair")
print("1 - Adicionar item") 
print("2 - Remover item")
print("3 - Alterar item")
print("4 - Imprimir estoque")
    
    
if choice != 0:    
    Escolha=int(input("Faca sua escolha: "))
    print(" ")
    while Escolha!=0:
    #Escolha 1    
        if Escolha == 1:
          nome= input("Nome do produto: ")
          if nome not in ListaLojas[Loja]:
              quantidade=int(input("quantidadde inicial: "))
              valor=float(input("Valor do produto:  "))
              if valor<0:
                  print("Valor nao pode ser negativo")
                  valor=float(input("Valor do produto:  "))
              while quantidade < 0:
                  print('Quantidade inicial não pode ser negativa')
                  quantidade=int(input("quantidadde inicial: "))
              ListaLojas[Loja][nome]={'quantidade':quantidade,'valor':valor}
          else:
              print ("Produto ja cadastrado")
          print(" ")    
          for nome in ListaLojas[Loja]:
                print("Produto adicionado")
                
    #Escolha 2          
        if Escolha==2:
            nome=input("Nome do produto a ser removido:  ")
            if nome in ListaLojas[Loja]:
                del ListaLojas[Loja][nome]
                print ("Produto removido ")
                print("  ")
            else:
                print ("Produto nao encontrado")
            
    #Escolha 3   
        if Escolha==3:
            nome= input("Nome do produto: ")
            if nome in ListaLojas[Loja]:
              Nquantidade=int(input("Deseja alterar a quantidade? (Sim: digite 1 / Nao: digite 2)  "))
              if Nquantidade==1:
                  novaquantidade=int(input("Nova quantidade: "))
                  ListaLojas[Loja][nome]['quantidade']+=novaquantidade
                  nvalor=int(input("Deseja alterar o valor? (Sim: digite 1 / Nao: digite 2)  "))
                  if nvalor==1:
                   novovalor=int(input("Novo Valor:  "))
                   ListaLojas[Loja][nome]['valor']=novovalor
              elif Nquantidade==2:
                   novovalor=int(input("Novo Valor:  "))
                   ListaLojas[Loja][nome]['valor']=novovalor
                  
                
              print("Novo estoque de {0} é {1} unidades e o valor é {2} Reais ".format(nome,ListaLojas[Loja][nome]['quantidade'],ListaLojas[Loja][nome]['valor']))
            else:
                print("Elemento nao encontrado")
            
    #Escolha 4
        if Escolha==4:
            vmonetario=0
            negativo=int(input("Estoque inteiro - 1/ Estoque negativo - 2:   "))
            print("  ")
            if negativo==1:
              for nome in ListaLojas[Loja]:
                print("{0}:  {1} unidades - valor: {2}".format(nome,ListaLojas[Loja][nome]['quantidade'],ListaLojas[Loja][nome]['valor']))
                valormonetario= ListaLojas[Loja][nome]['quantidade']*ListaLojas[Loja][nome]['valor']
                vmonetario+=valormonetario
              print("O valor total do estoque é {0} Reais ".format(vmonetario))
            elif negativo==2:
                print("Os estoques negativos sao: ")
                print("  ")
                for nome in ListaLojas[Loja]:
                     if ListaLojas[Loja][nome]['quantidade']<0:
                         print(" {0}:{1} unidades".format(nome,ListaLojas[Loja][nome]['quantidade']))
    
        print("   ")
        print("0 - Sair")
        print("1 - Adicionar item") 
        print("2 - Remover item")
        print("3 - Alterar item")
        print("4 - Imprimir estoque")   
        Escolha=int(input("Faca sua escolha:"))
        print("  ")
print("Ate mais")  
    

firebase.patch('https://ep-1-luizajose.firebaseio.com/dados',ListaLojas)


