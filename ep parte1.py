# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:13:44 2018

@author: luiza
"""

#Controle de estoque
Estoque={}
print("0-sair")
print("1-adicionar_item") 
print("2-remover_item")
print("3-alterar_item")
print("4-imprimir_estoque")

Escolha=int(input("Faca sua escolha: "))
while Escolha!=0:
#Escolha 1    
    if Escolha == 1:
      nome= input("Nome do produto: ")
      if nome not in Estoque :
          quantidade=int(input("quantidadde inicial: "))
          while quantidade < 0:
              print('Quantidade inicial não pode ser negativa')
              quantidade=int(input("quantidadde inicial: "))
          Estoque[nome]={'quantidade':quantidade}
      else:
          print ("Produto ja cadastrado")
      
#Escolha 2          
    if Escolha==2:
        nome=input("Nome do produto a ser removido:  ")
        if nome in Estoque:
            del Estoque[nome]         
            print ("Produto removido")
        else:
            print ("Elemento nao encontrado")      
#Escolha 3   
    if Escolha==3:
        nome= input("Nome do produto: ")
        if nome in Estoque:
          novaquantidade=int(input("Nova quantidade: "))
          Estoque[nome]['quantidade']+=novaquantidade
          print("Novo estoque de {0} é {1} unidades:".format(nome,Estoque[nome]['quantidade']))
        else:
            print("Elemento nao encontrado")      
#Escolha 4
    if Escolha==4:
        for nome in Estoque:
            print("{0}:{1}".format(nome,Estoque[nome]['quantidade']))
        
        
        
        
        
        
        
            
        
           
               

          
         
      
        
        
    
    
    print("0-sair")
    print("1-adicionar_item") 
    print("2-remover_item")
    print("3-alterar_item")
    print("4-imprimir_estoque")   
    Escolha=int(input("Faca sua escolha:"))
print("Ate mais")