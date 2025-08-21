#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Función para unir los archivos CSV de comentarios negativos de los bancos
BCP, BN e Interbank en un solo dataset consolidado.
"""

import pandas as pd
import os

def unir_datasets_comentarios():
    """
    Une los archivos CSV de comentarios negativos de BCP, BN e Interbank
    en un solo archivo dataset_comentariosv1.csv con IDs incrementales.
    
    Los archivos se procesan en el orden: INTERBANK -> BN -> BCP
    """
    
    # Definir los archivos en el orden especificado
    archivos = [
        'comentarios_negativos_INTERBANK_2440.csv',
        'comentarios_negativos_BN_2481.csv', 
        'comentarios_negativos_BCP_2218.csv',
        'comentarios_negativos_BBVA_2241.csv',
        'comentarios_negativos_SCOTIABANK_2847.csv',
        'comentarios_negativos_YAPE_1464.csv'
    ]
    
    # Lista para almacenar los DataFrames
    dataframes = []
    
    # Contador para IDs incrementales
    id_contador = 1
    
    print("Procesando archivos...")
    
    for archivo in archivos:
        if not os.path.exists(archivo):
            print(f"ERROR: No se encontró el archivo {archivo}")
            continue
            
        print(f"Leyendo {archivo}...")
        
        # Leer el archivo CSV
        df = pd.read_csv(archivo)
        
        # Verificar que tenga las columnas necesarias
        if 'comentario' not in df.columns:
            print(f"ERROR: El archivo {archivo} no tiene la columna 'comentario'")
            continue
            
        # Crear una copia del DataFrame para no modificar el original
        df_copia = df.copy()
        
        # Normalizar los nombres de las columnas de clasificación
        if 'Clasificacion_ISO_25010' in df_copia.columns:
            df_copia = df_copia.rename(columns={'Clasificacion_ISO_25010': 'clasificacion_ISO_25010'})
        elif 'clasificación_ISO_25010' in df_copia.columns:
            df_copia = df_copia.rename(columns={'clasificación_ISO_25010': 'clasificacion_ISO_25010'})
        
        # Si no existe la columna de clasificación, crearla con 'not_applicable'
        if 'clasificacion_ISO_25010' not in df_copia.columns:
            df_copia['clasificacion_ISO_25010'] = 'not_applicable'
        
        # Asignar nuevos IDs incrementales
        df_copia['id'] = range(id_contador, id_contador + len(df_copia))
        id_contador += len(df_copia)
        
        # Agregar columna para identificar el banco de origen
        if 'INTERBANK' in archivo:
            df_copia['banco'] = 'INTERBANK'
        elif 'BN' in archivo:
            df_copia['banco'] = 'BN'
        elif 'BCP' in archivo:
            df_copia['banco'] = 'BCP'
        elif 'BBVA' in archivo:
            df_copia['banco'] = 'BBVA'
        elif 'SCOTIABANK' in archivo:
            df_copia['banco'] = 'SCOTIABANK'
        elif 'YAPE' in archivo:
            df_copia['banco'] = 'YAPE'
        
        # Seleccionar solo las columnas necesarias en el orden correcto
        df_final = df_copia[['id', 'comentario', 'clasificacion_ISO_25010', 'banco']]
        
        dataframes.append(df_final)
        print(f"  - Procesadas {len(df_final)} filas")
    
    if not dataframes:
        print("ERROR: No se pudieron procesar los archivos")
        return False
    
    # Concatenar todos los DataFrames
    print("\nConcatenando datasets...")
    dataset_final = pd.concat(dataframes, ignore_index=True)
    
    # Guardar el archivo final
    archivo_salida = 'dataset_comentariosv2.csv'
    dataset_final.to_csv(archivo_salida, index=False, encoding='utf-8')
    
    print(f"\n✅ Archivo creado exitosamente: {archivo_salida}")
    print(f"   Total de registros: {len(dataset_final)}")
    print(f"   Columnas: {list(dataset_final.columns)}")
    
    # Mostrar resumen por banco
    print("\nResumen por banco:")
    resumen = dataset_final.groupby('banco').size()
    for banco, cantidad in resumen.items():
        print(f"   {banco}: {cantidad} comentarios")
    
    # Mostrar resumen por clasificación
    print("\nResumen por clasificación:")
    resumen_clase = dataset_final['clasificacion_ISO_25010'].value_counts()
    for clase, cantidad in resumen_clase.head(10).items():
        print(f"   {clase}: {cantidad} comentarios")
    
    return True

if __name__ == "__main__":
    # Cambiar al directorio del script si es necesario
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("=== UNIÓN DE DATASETS DE COMENTARIOS ===\n")
    
    # Ejecutar la función
    exito = unir_datasets_comentarios()
    
    if exito:
        print("\n🎉 Proceso completado exitosamente!")
    else:
        print("\n❌ El proceso falló. Revisa los errores arriba.")
