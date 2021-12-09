#Módulo para realização do TPC8

def getEMD(texto):
    novoTexto=texto.replace("\n","")
    EMD=[]
    dados=novoTexto.split(",")
    for i in range(len(dados)):
        EMD.append(dados[i])
    EMD.pop(1)
    return EMD

def lerDataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = []
    f.readline()
    for linha in f:
        bd.append(getEMD(linha))
    for i in range(len(bd)):
        bd[i][0]='emd'+str(i+1)
    return bd

def chaveOrd(a):
    return a[1]

def listarDataset(bd):
    bd.sort(key=chaveOrd, reverse=True)
    print('  id         data        nome          apto')
    print('___________________________________________')
    for elem in bd:
        print(elem[0] + ' | ' + elem[1] + ' | ' + (elem[2]+ ' '+elem[3]) + ' | '+ elem[11])

def consultarDataset(d, id):
    i=0
    for i in range(len(d)):
        if d[i][0]==id:
            print (d[i])

def modalidades(d):
    mod=[]
    for elem in d:
        if elem[7] not in mod:
            mod.append(elem[7])
    mod.sort()
    return mod

def distribPorModalidade(d):
    distribuicaoM={}
    for elem in d:
        if elem[7] in distribuicaoM.keys():
            distribuicaoM[elem[7]]=distribuicaoM[elem[7]]+1
        else:
            distribuicaoM[elem[7]]=1
    return distribuicaoM

def distribPorClube(d):
    distribuicaoC={}
    for elem in d:
        if elem[8] in distribuicaoC.keys():
            distribuicaoC[elem[8]]=distribuicaoC[elem[8]]+1
        else:
            distribuicaoC[elem[8]]=1
    return distribuicaoC

def distribPorAno(d):
    distribuicaoA={}
    for elem in d:
        if elem[1][:4] in distribuicaoA.keys():
            distribuicaoA[elem[1][:4]]=distribuicaoA[elem[1][:4]]+1
        else:
            distribuicaoA[elem[1][:4]]=1
    return distribuicaoA

def distrib(d,a):
    if a == 'ano':
        distribuicaoA={}
        for elem in d:
            if elem[1][:4] in distribuicaoA.keys():
                distribuicaoA[elem[1][:4]]=distribuicaoA[elem[1][:4]]+1
            else:
                distribuicaoA[elem[1][:4]]=1
        return distribuicaoA
    elif a == 'genero':
        distribuicaoG={}
        for elem in d:
            if elem[5] in distribuicaoG.keys():
                distribuicaoG[elem[5]]=distribuicaoG[elem[5]]+1
            else:
                distribuicaoG[elem[5]]=1
        return distribuicaoG
    elif a == 'modalidade':
        distribuicaoM={}
        for elem in d:
            if elem[7] in distribuicaoM.keys():
                distribuicaoM[elem[7]]=distribuicaoM[elem[7]]+1
            else:
                distribuicaoM[elem[7]]=1
        return distribuicaoM
    elif a == 'clube':
        distribuicaoC={}
        for elem in d:
            if elem[8] in distribuicaoC.keys():
                distribuicaoC[elem[8]]=distribuicaoC[elem[8]]+1
            else:
                distribuicaoC[elem[8]]=1
        return distribuicaoC
    elif a == 'federado':
        distribuicaoF={}
        for elem in d:
            if elem[10] in distribuicaoF.keys():
                distribuicaoF[elem[10]]=distribuicaoF[elem[10]]+1
            else:
                distribuicaoF[elem[10]]=1
        return distribuicaoF
    else:
        distribuicaoAP={}
        for elem in d:
            if elem[11] in distribuicaoAP.keys():
                distribuicaoAP[elem[11]]=distribuicaoAP[elem[11]]+1
            else:
                distribuicaoAP[elem[11]]=1
        return distribuicaoAP

import matplotlib.pyplot as plt
def plotDistribPorModalidade(d):
    a=distribPorModalidade(d)
    tuplo=a.items()
    x=[]
    y=[]
    for elem in tuplo:
        x.append(elem[0])
    for elem in tuplo:
        y.append(elem[1])
    fig= plt.subplots(figsize=(16, 6))
    plt.bar(x,y,color=['red','blue'])
    plt.xlabel('Modalidades', fontsize=12)
    plt.ylabel('EMD', fontsize=12)
    plt.title('Distribuição de EMD por modalidade', fontsize=12)
    plt.show()

def plotDistrib(d,b):
    fig = plt.figure()
    b.lower()
    a=distrib(d,b)
    tuplo=a.items()
    x=[]
    y=[]
    for elem in tuplo:
        x.append(elem[0])
    for elem in tuplo:
        y.append(elem[1])
    if b == 'modalidade':
        fig= plt.subplots(figsize=(16, 6))
    if b == 'clube':
        fig= plt.subplots(figsize=(12, 6))
    plt.bar(x,y,color=['red','blue'])
    plt.xlabel(str(b))
    plt.ylabel('EMD')
    plt.title('Distribuição de EMD por '+str(b))
    plt.show()

def bdOrd(bd):
    bd.sort(key=chaveOrd, reverse=True)
    return bd