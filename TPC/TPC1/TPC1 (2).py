#!/usr/bin/env python
# coding: utf-8

# In[86]:



def segundo ():
    a=21
    c=0
    while a>1:
        b=int(input('\nQuantos fósforos desejas retirar? '))
        if b >= 5 or b==0:
            print('Somente podes retirar de 1 a 4 fósforos')
        elif a-b<1:
            print('Escolhas outra quantidade de fósforos para retirar')
        else:
            a = a - b
            print('Restam',a,'fósforos')
            c = 5 - b
            a = a - c
            if a == 1:
                print('\nAgora é minha vez! Retirei',c,'! E sobrou',a,'fósforo!'
                  '\nYOU LOSE!!!')
                again=input('\nDesejas recomeçar o jogo? Responda com "sim" ou "nao" ')
                x=again.upper()
                if x == 'SIM':
                    return inicio (segundo,primeiro)
                else:
                    print('Até a próxima!!!')
            else:
                print('\nAgora é minha vez! Retirei',c,'! Sobram',a,'fósforos!')
                   

def primeiro ():
    a=21
    a=a-4
    c=0
    print('\nRetirei 4 fósforos! Restam',a)
    while a>10:
        b=int(input('\nQuantos fósforos desejas retirar? '))
        if b >= 5 or b==0:
            print('Somente podes retirar de 1 a 4 fósforos')
        elif a-b<1:
            print('Escolhas outra quantidade de fósforos para retirar')
        else:
            a=a-b
            print('Restam',a,'fósforos')
            if a<=10:
                c=a-6
                a=a-c
                print('\nRetirei',c,'! Sobram',a,'fósforos!')
                break
            else:
                c=b
                a=a-c
                print('\nRetirei',c,'! Sobram',a,'fósforos!')
    if a<=10:
        return primeiro_2(primeiro,a)

def primeiro_2(primeiro,a):   
    while a<=10:
        b=int(input('\nQuantos fósforos desejas retirar? '))
        if b >=5 or b==0:
            print('Somente podes retirar de 1 a 4 fósforos')
        elif a-b<1:
            print('Escolhas outra quantidade de fósforos para retirar')
        else:
            a=a-b
            if a==1:
                print('Sobrou 1 fósforo! YOU WON!')
                again=input('\nDesejas recomeçar o jogo? Responda com "sim" ou "nao" ')
                x=again.upper()
                if x == 'SIM':
                    return inicio (segundo,primeiro)
                else:
                    print('Até a próxima!!!')
                    break
            elif a==6:
                print('Restam',a,'fósforos')
                c=1
                a=a-c
                print('\nRetirei',c,'! Sobram',a,'fósforos!') 
            elif a<6:
                print('Restam',a,'fósforos')
                c=a-1
                a=a-c
                print('\nAgora é minha vez! Retirei',c,'! E sobrou',a,'fósforo!'
                      '\nYOU LOSE!!!')
                again=input('\nDesejas recomeçar o jogo? Responda com "sim" ou "nao" ')
                x=again.upper()
                if x == 'SIM':
                    return inicio (segundo,primeiro)
                else:
                    print('Até a próxima!!!')
                    break
            else:
                print('Restam',a,'fósforos')
                c=a-6
                a=a-c
                print('\nRetirei',c,'! Sobram',a,'fósforos!')
           
   
            
def inicio (segundo,primeiro):
    print('\nOlá, seja bem vindo ao jogo dos 21 FÓSFOROS'
      '\n'
      '\nAs regras são simples:'
      '\n* Há 21 fosfóros no início e 2 jogadores a jogar'
      '\n* Cada jogador pode tirar 1,2,3 ou 4 fósforos alternadamente'
      '\n* Perde o jogador em que sua vez restar apenas 1 fósforo para retirar')
    ut=int(input('\nDesejas ser o 1 ou o 2 jogador? '))
    if ut == 1:
        print('Ok, então vamos começar! Sou o segundo a jogar!')
        jogar=segundo()
    else:
        print('\nOk, então vamos começar! Sou o primeiro a jogar!')
        jogar=primeiro()
start=inicio(segundo,primeiro)
        


# In[ ]:





# In[ ]:




