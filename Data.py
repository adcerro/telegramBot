import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("train.csv")
df.columns = ['ID','Sobrevivio','Clase','Nombre','Sexo','Edad','HerEsp','PadHij','Tiquete','Tarifa','Cabina','Puerto']
df['Cabina'] = df['Cabina'].str[0]
df['Sexo'] = df['Sexo'].replace({'male':'Hombre', 'female':'Mujer'})
df['Sobrevivio'] = df['Sobrevivio'].replace({0:'No', 1:'Si'})
df['Puerto'] = df['Puerto'].replace({'S':'Southampton', 'C':'Cherbourg', 'Q' : 'Queenstown'})

def desc(a):
    if(a=='Hermanos-Pareja'):
        var = df['HerEsp']
    elif(a=='Padres-Hijos'):
        var = df['PadHij']
    else:
        var = df[a]
    analisis =var.describe().round(4)
    result = analisis.to_string()
    result = result.replace('count','entradas')
    result = result.replace('mean','media')
    result = result.replace('std','desv. est.')
    result = result.__add__(f'\nmediana: {var.median()}')
    return result   #f'Media: {var.mean()} \nModa: {var.mode().} \nMediana: {var.median()} \nMáximo: {var.max()} \nMínimo: {var.min()}'

def descCat(a):
    analisis =df[a].astype('category').describe()
    result = analisis.to_string()
    result = result.replace('count','Entradas')
    result = result.replace('top','Moda')
    result = result.replace('unique','Categorias')
    result = result.replace('freq','Frecuen.')
    result = result.__add__(f'\nConteo por valor: \n{df[a].value_counts().to_string()}')
    return result