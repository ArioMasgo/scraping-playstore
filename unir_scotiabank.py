import pandas as pd
import glob
import os

def unir_archivos_scotiabank():
    patron = "comentarios_BBVA_*_clasificados.csv"
    archivos = glob.glob(patron)
    
    if not archivos:
        print(f"No se encontraron archivos con el patrón: {patron}")
        return
    
    archivos.sort(key=lambda x: int(x.split('_')[2]))
    
    dataframes = []
    
    for archivo in archivos:
        print(f"Procesando: {archivo}")
        
        try:
            df = pd.read_csv(archivo)
            
            if len(df.columns) == 3:
                df.columns = ['numero_comentario', 'comentario', 'clasificacion_iso_25010']
            
            dataframes.append(df)
            
        except Exception as e:
            print(f"Error procesando {archivo}: {e}")
            continue
    
    if dataframes:
        df_unido = pd.concat(dataframes, ignore_index=True)
        
        df_unido.reset_index(drop=True, inplace=True)
        df_unido['numero_comentario'] = range(1, len(df_unido) + 1)
        
        archivo_salida = "comentarios_BBVA_unificados.csv"
        df_unido.to_csv(archivo_salida, index=False)
        
        print(f"\nArchivos unidos exitosamente!")
        print(f"Total de comentarios: {len(df_unido)}")
        print(f"Archivo guardado como: {archivo_salida}")
        
        return df_unido
    else:
        print("No se pudieron procesar archivos")
        return None

if __name__ == "__main__":
    unir_archivos_scotiabank()