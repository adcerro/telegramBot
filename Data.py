import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("train.csv")
df.columns = ['ID','Sobrevivio','Clase','Nombre','Sexo','Edad','HerEsp','PadHij','Tiquete','Tarifa','Cabina','Puerto']
df['Cabina'] = df['Cabina'].str[0]
df['Sexo'] = df['Sexo'].replace({'male':'Hombre', 'female':'Mujer'})
df['Sobrevivio'] = df['Sobrevivio'].replace({0:'No', 1:'Si'})

def univariate():
    ax = sns.countplot(x='Sobrevivio', data=df)
    for p in ax.patches:
        ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x()+0.30, p.get_height()+4))
    
    plt.savefig('plots/sobrevivio.png')
    return 