import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate




# Título de  la página
st.set_page_config(layout="centered",
    page_title="Plan Comisiones Epoch Acadamy",
    page_icon="🕰️"
)
t1, t2 = st.columns([0.3,0.7]) 
t1.image('CrezcamosYa (1000 x 500 px).png')
t2.title(":blue[Etapas del proyecto]")
t2.markdown("Equipo Epoch Academy")


X=np.array([3225,8600,25800,103200,825600])
Y=np.array([20, 40, 60, 80, 95])
tck = interpolate.splrep(X, Y) 
xnew = np.linspace(3000, 113200, 1000)
ynew = interpolate.splev(xnew, tck)
p1= interpolate.splev(5, tck)
fig, axs = plt.subplots(figsize=(16, 8))
plt.plot(X, Y, 'o', xnew, ynew, color='#093773')
plt.xlabel('Número de suscriptores')
plt.ylabel('Porcentaje de Epoch Times')

plt.xticks([3225,25800,103200,825600], rotation=45)
plt.annotate('(3225, 20)', xy=(7225, 20))
plt.annotate('(8600, 40)', xy=(12000, 40))
plt.annotate('(25800, 60)', xy=(34800, 60))
plt.annotate('(103200, 80)', xy=(113200, 80))
plt.annotate('(825600, 95)', xy=(750000, 95))

st.pyplot(fig)

df=pd.DataFrame({'suscrip':xnew, 'PET': ynew})
st.line_chart(data=df, x='suscrip', y='PET', x_label='Número de suscripciones', 
              y_label='Porcentaje de Epoch Times',
              color=['#36CCD3'])

usuarios=st.number_input('Número de suscriptores', min_value=0)

PET=interpolate.splev(usuarios, tck)
st.write(f'Con un total de {usuarios} suscripciones')
if usuarios <X[1]:
    st.write('El proyecto está en la etapa I')
    st.write('El porcetaje de partiticiación de Epoch Times es: 20%')
    st.write(f'El total de ingresos para Epoch Times es {usuarios*5*0.2}')
elif usuarios < X[2] and X[1]<= usuarios:
    st.write(f'El proyecto está en la etapa II')
    st.write(f'El porcetaje de partiticiación de Epoch Times es: {int(PET)}%')
    st.write(f'El total de ingresos para Epoch Times es {int(usuarios/100*5*PET)}') 
elif usuarios < X[3] and X[2]<= usuarios:
    st.write('El proyecto está en la etapa III')
    st.write(f'El porcetaje de partiticiación de Epoch Times es: {int(PET)}%')
    st.write(f'El total de ingresos para Epoch Times es {int(usuarios/100*5*PET)}') 
elif usuarios < X[4] and X[3]<= usuarios:
    st.write(f"El proyecto está en la etapa IV")
    st.write(f'El porcetaje de partiticiación de Epoch Times es: {int(PET)}%')
    st.write(f'El total de ingresos para Epoch Times es {int(usuarios*5/100*PET)}') 
elif usuarios >= X[4]:
    st.write('El proyecto está en la etapa V')
    st.write('El porcetaje de partiticiación de Epoch Times es: 95%')
    st.write(f'El total de ingresos para Epoch Times es {int(usuarios/100*5*0.95)}') 
        
