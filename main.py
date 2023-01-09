import subprocess 
import pandas as pd

Data = subprocess.check_output(['wmic', 'product', 'get', 'name']) 
a = str(Data) 
lista = []
try: 

    for i in range(len(a)): 
        print(a.split("\\r\\r\\n")[6:][i]) 
        lista.append(a.split("\\r\\r\\n")[6:][i])
  
except IndexError as e: 
    print("All Done")
    
saida = pd.DataFrame(lista)

file = 'softwares.xlsx'

saida.to_excel(file)
