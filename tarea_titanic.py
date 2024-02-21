import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Titanic')
st.markdown('*priscila cervantes*')
st.header('Data set')

df=pd.read_csv('Titanic-Dataset.csv')
st.dataframe(df)
print('\n')

grouped_data = df.groupby("Survived")
fig, ax = plt.subplots(figsize=(8, 6))# tamaño figura
colors = ['lightgreen', 'darkgreen']
for i, (group_name, group_data) in enumerate(grouped_data):
    ax.hist(group_data["Survived"], bins=2, alpha=0.5, label=str(group_name), color=colors[i])
ax.set_title('Sobrevivientes', fontname='Arial', fontsize=16,fontweight='bold')# Cambiar título y etiquetas de los ejes
ax.set_xlabel("0 no sobrevivientes, 1 sobrevivientes")
ax.legend()
st.pyplot(fig)#histograma utilizando Streamlit
print('\n')

grouped_data = df.groupby("Pclass")
fig, ax = plt.subplots(figsize=(8, 6))# tamaño figura
for group_name, group_data in grouped_data:# Iterar sobre los grupos y trazar un histograma para cada uno
    ax.hist(group_data["Pclass"], bins=2, alpha=0.5, label=str(group_name))
ax.set_title('Clase a la que pertenecía el pasajero', fontname='Arial', fontsize=16,fontweight='bold')# Cambiar título y etiquetas de los ejes
ax.set_xlabel("1.primera, 2.segunda, 3.tercera")
ax.legend()
st.pyplot(fig)#histograma utilizando Streamlit
print('\n')
print('\n')

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
grouped_data = df.groupby('Age_Group').size()
fig, ax = plt.subplots(figsize=(8, 6))
grouped_data.plot(kind='bar', color='red', alpha=0.7)
ax.set_title('Edad de los Pasajeros', fontname='Arial', fontsize=16,fontweight='bold')
ax.set_xlabel("Rango de Edad")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
print('\n')

grouped_data = df.groupby("Sex")
fig, ax = plt.subplots(figsize=(8, 6))# tamaño figura
colors = ['orange', 'darkorange'] 
for i, (group_name, group_data) in enumerate(grouped_data):
    ax.hist(group_data["Sex"], bins=2, alpha=0.5, label=str(group_name), color=colors[i])
ax.set_title('Géneros', fontname='Arial', fontsize=16,fontweight='bold')# Cambiar título y etiquetas de los ejes
ax.set_xlabel("Separación de los pasajeros por su sexo Femenino o Masculino")
ax.legend()
st.pyplot(fig)#histograma utilizando Streamlit
print('\n')

grouped_data = df.groupby("SibSp")
fig, ax = plt.subplots(figsize=(8, 6))# tamaño figura
for group_name, group_data in grouped_data:# Iterar sobre los grupos y trazar un histograma para cada uno
    ax.hist(group_data["SibSp"], bins=2, alpha=0.5, label=str(group_name))
ax.set_title('Número de herman@s abordo', fontname='Arial', fontsize=16,fontweight='bold')# Cambiar título y etiquetas de los ejes
ax.set_xlabel("0 a 8, siendo 0 solo, 8 varios parientes")
ax.legend()
st.pyplot(fig)#histograma utilizando Streamlit
print('\n')

grouped_data = df.groupby("Parch")
fig, ax = plt.subplots(figsize=(8, 6))# tamaño figura
for group_name, group_data in grouped_data:# Iterar sobre los grupos y trazar un histograma para cada uno
    ax.hist(group_data["Parch"], bins=2, alpha=0.5, label=str(group_name))
ax.set_title('Número de padres e hijos en el barco.', fontname='Arial', fontsize=16,fontweight='bold')# Cambiar título y etiquetas de los ejes
ax.set_xlabel("0 a 6, siendo 0 solo, 6 familia grande")
ax.legend()
st.pyplot(fig)#histograma utilizando Streamlit
print('\n')

bins = [0, 100, 200, 300, 400, 500, 600]
labels = ['0-99', '100-199', '200-299', '300-399', '400-499', '500-599']
df['Fare_Group'] = pd.cut(df['Fare'], bins=bins, labels=labels)
grouped_data = df.groupby('Fare_Group').size()
fig, ax = plt.subplots(figsize=(8, 6))
grouped_data.plot(kind='bar', color='orange', alpha=0.7)
ax.set_title('Precio Pagado por el Billete', fontname='Arial', fontsize=16,fontweight='bold')
ax.set_xlabel("Rango de Precio")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
print('\n')
print('\n')

grouped_data = df.groupby("Embarked")
fig, ax = plt.subplots(figsize=(8, 6))# tamaño figura
colores = ['darkblue', 'cornflowerblue', 'lightblue']
for i, (group_name, group_data) in enumerate(grouped_data):
    ax.hist(group_data["Embarked"].tolist(), bins=2, alpha=0.5, label=str(group_name), color=colores[i])
ax.set_title('Embarcaciones', fontname='Arial', fontsize=16,fontweight='bold')# Cambiar título y etiquetas de los ejes
ax.set_xlabel("Tipos de embarcaciones")
ax.legend()
st.pyplot(fig)#histograma utilizando Streamlit
print('\n')





