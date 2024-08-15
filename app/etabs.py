import pandas as pd
import json 

def calc():

  df = pd.read_csv('trabes.csv')

  # Dividir el DataFrame en dos: uno para momentos negativos y otro para positivos
  df_negative = df[df['Moment negative'] < 0]
  df_positive = df[df['Moment positive'] > 0]

  # Diccionarios para almacenar los valores más bajos y más altos para cada grupo
  min_negative_values = {}
  max_positive_values = {}

  # Agrupar los momentos negativos por 'Location' y obtener el menor valor de 'Moment'
  grouped_negative = df_negative.groupby('Location')
  for location, group in grouped_negative:
     min_row_neg = group.nsmallest(3, 'Moment negative').to_dict(orient='records')
     min_negative_values[location] = min_row_neg

  # Agrupar los momentos positivos por 'Location' y obtener el mayor valor de 'Moment'
  grouped_positive = df_positive.groupby('Location')
  for location, group in grouped_positive:
     max_row_pos =  group.nlargest(3, 'Moment positive').to_dict(orient='records')
     max_positive_values[location] = max_row_pos

  # Crear un diccionario final con los resultados
  result = {
    "min_negativos": min_negative_values,
    "max_positivos": max_positive_values
  }

  # Guardar los resultados en un archivo JSON
  with open('resultados_trabes.json', 'w') as json_file:
      json.dump(result, json_file, indent=4)

  print("Resultados guardados en 'resultados_trabes.json'.")

if __name__ == "__main__":
    calc()