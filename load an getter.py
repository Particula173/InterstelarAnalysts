import xarray as xr
import os
import pandas as pd
import earthaccess
import netCDF4 as nc

def download_data (dir):
  auth = earthaccess.login()

  results = earthaccess.search_data(
      doi="10.5067/TXBMLX370XX8",
      temporal=('2024-05-25', '2024-05-31'), 
      bounding_box=( -126, 30.375, -67.465, 46.898) 
  )

  downloaded_files = earthaccess.download(
      results,
      local_path=dir
  )
  
def get_data (carpeta):
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.nc4'):
            # Construye la ruta completa al archivo
            ruta_archivo = os.path.join(carpeta, archivo)
            
            try:
                # Abre el archivo .nc4
                dataset = nc.Dataset(ruta_archivo, 'r')
                
                # Imprime el nombre del archivo
                print(f"Procesando: {archivo}")

                # Muestra las dimensiones
                print("Dimensiones:")
                for dim in dataset.dimensions.values():
                    print(f"  {dim.name}: {dim.size}")

                # Muestra las variables y sus atributos
                print("Variables y atributos:")
                for var_name, variable in dataset.variables.items():
                    print(f"  Variable: {var_name}")
                    print(f"    Atributos: {variable.__dict__}")  # Muestra atributos de la variable
                
                # Cierra el archivo
                dataset.close()
            except Exception as e:
                print(f"Error al procesar {archivo}: {e}")
  
