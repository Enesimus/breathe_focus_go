'''
Docstring para paginas.entrenamiento
'''

import datetime
import streamlit as st

fecha = st.date_input('Fecha',
              value= datetime.date.today,
              help= 'Ingrese la fecha del entrenamiento',
              format="DD/MM/YYYY")

hr_inicio = st.time_input('Hora inicio',
                          help= 'Ingrese la hora de inicio del entrenamiento')

