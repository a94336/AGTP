import matplotlib.pyplot as plt
import os
import io
from os.path import join

def carregarBD(fnome):
    f = open(fnome, encoding="utf-8")
    bd=[]
    bd=json.load(f)
    i=1
    for filme in bd:
        filme['id']='f'+str(i)
        i=i+1
    return bd

def guardarBD(bd,fnome):
    f=open(fnome,'w',encoding='utf-8')
    json.dump(bd,f,ensure_ascii=False,indent=4)
    
def inserirFilme(bd,title,year,cast,genres):
    filme={}
    filme['title']=title
    filme['year']=year
    filme['cast']=cast
    filme['genres']=genres
    filme['id']='f'+str(len(bd)+1)
    return filme

def consultarID(bd,id):
    for filme in bd:
        if filme['id']==id:
            a=filme
    return a

def consultarNome(bd,nome):
    filmes=[]
    novoNome=nome.upper()
    for filme in bd:
        titulo=filme['title'].upper()
        if novoNome in titulo:
            filmes.append(filme)
    return filmes

def chaveOrd(a):
    return a['title']

def ordenar(bd):
    bd.sort(key=chaveOrd)
    return bd

def genero(bd,g):
    genero={}
    filmes=[]
    for filme in bd:
        if g in filme['genres']:
            filmes.append(filme)
    genero[g]=filmes
    return genero

def ator(bd,a):
    ator={}
    filmes=[]
    for filme in bd:
        if a in filme['cast']:
            filmes.append(filme)
    ator[a]=filmes
    return ator

def distribGenero(d):
    distribuicaoG={}
    for filme in d:
        for genero in filme['genres']:
            if genero in distribuicaoG.keys():
                distribuicaoG[genero]=distribuicaoG[genero]+1
            else:
                distribuicaoG[genero]=1
    return distribuicaoG

def distribAtor(d):
    distribuicaoA={}
    for filme in d:
        for ator in filme['cast']:
            if ator in distribuicaoA.keys():
                distribuicaoA[ator]=distribuicaoA[ator]+1
            else:
                distribuicaoA[ator]=1
    atores=sorted(distribuicaoA.items(),key=lambda x:x[1], reverse=True)
    atores.pop(0) #atores[0]=and
    atores.pop(1) #atores[1]=voice
    atores=atores[:10]
    return atores

def plotDistribGenero(bd):
    a=distribGenero(bd)
    tuplo=list(a.items())
    tuplo.sort(key=lambda x:x[1], reverse=True)
    height=[]
    left=[]
    label=[]
    for i in range(len(tuplo)):
        left.append(i)
    for elem in tuplo:
        height.append(elem[1])
        label.append(elem[0])
    fig= plt.subplots(figsize=(16, 6))
    plt.bar(left,height, label=label,
           width=0.8, color=["pink"])
    plt.xticks(range(len(label)),label, rotation = 'vertical')
    plt.title("Distribuição por Género", fontsize=18)
    for i, v in enumerate(height):
        plt.text(left[i] -0.45, v+20, str(v))
    plt.savefig(os.path.join('genero.jpg'), dpi=300, format='jpg')


def plotDistribAtor(bd):
    a=distribAtor(bd)
    a.sort(key=lambda x:x[1], reverse=True)
    height=[]
    left=[]
    label=[]
    for i in range(len(a)):
        left.append(i)
    for elem in a:
        height.append(elem[1])
        label.append(elem[0])
    fig= plt.subplots(figsize=(16, 6))
    plt.bar(left,height, label=label,
           width=0.8, color=["green"])
    plt.xticks(range(len(label)),label)
    plt.title("Atores - Top 10", fontsize=18)
    for i, v in enumerate(height):
        plt.text(left[i]-0.1, v+0.2,str(v),fontsize=12)
    plt.savefig(os.path.join('atores.jpg'), dpi=300, format='jpg')
    
def calcListaAtores(bd):
    ator=[]
    for filme in bd:
        for a in filme['cast']:
            if a not in ator:
                ator.append(a)
    ator.sort()
    return ator

def calcListaFilmes(bd,a):
    filmes=[]
    for filme in bd:
        if a in filme['cast']:
            filmes.append((filme['title'],filme['id']))
    return filmes

def indAtores(bd):
    indiceAtores=[]
    listaA = calcListaAtores(bd)
    for i in listaA:
        indiceAtores.append({
            'Ator':i,
            'Filmes':calcListaFilmes(bd,i)})
    return indiceAtores


def calcListaGeneros(bd):
    genero=[]
    for filme in bd:
        for a in filme['genres']:
            if a not in genero:
                genero.append(a)
    genero.sort()
    return genero

def calcListaFilmes(bd,a):
    filmes=[]
    for filme in bd:
        if a in filme['genres']:
            filmes.append((filme['title'],filme['id']))
    return filmes

def indGeneros(bd):
    indiceGeneros=[]
    listaG = calcListaGeneros(bd)
    for i in listaG:
        indiceGeneros.append({
            'Género':i,
            'Filmes':calcListaFilmes(bd,i)})
    return indiceGeneros