import pandas as pd
import os

def eliminar_not_applicable(archivo_entrada, archivo_salida=None):
    """
    Elimina todos los registros que tienen 'not_applicable' en la columna 'clasificacion_ISO_25010'
    
    Parámetros:
    archivo_entrada (str): Ruta del archivo CSV de entrada
    archivo_salida (str, opcional): Ruta del archivo CSV de salida. Si no se especifica,
                                   se guardará como '{nombre_original}_filtrado.csv'
    
    Retorna:
    dict: Diccionario con estadísticas del filtrado
    """
    try:
        # Leer el archivo CSV
        print(f"Leyendo archivo: {archivo_entrada}")
        df = pd.read_csv(archivo_entrada)
        
        # Mostrar información inicial
        total_registros = len(df)
        registros_not_applicable = len(df[df['clasificacion_ISO_25010'] == 'not_applicable'])
        
        print(f"Total de registros en el archivo original: {total_registros}")
        print(f"Registros con 'not_applicable': {registros_not_applicable}")
        
        # Filtrar registros que NO sean 'not_applicable'
        df_filtrado = df[df['clasificacion_ISO_25010'] != 'not_applicable']
        
        registros_restantes = len(df_filtrado)
        print(f"Registros después del filtrado: {registros_restantes}")
        
        # Generar nombre del archivo de salida si no se especifica
        if archivo_salida is None:
            nombre_base = os.path.splitext(archivo_entrada)[0]
            archivo_salida = f"{nombre_base}_filtrado.csv"
        
        # Guardar el archivo filtrado
        df_filtrado.to_csv(archivo_salida, index=False)
        print(f"Archivo filtrado guardado como: {archivo_salida}")
        
        # Mostrar distribución de clasificaciones restantes
        print("\nDistribución de clasificaciones después del filtrado:")
        print(df_filtrado['clasificacion_ISO_25010'].value_counts())
        
        # Retornar estadísticas
        return {
            'total_original': total_registros,
            'eliminados': registros_not_applicable,
            'restantes': registros_restantes,
            'porcentaje_eliminado': (registros_not_applicable / total_registros) * 100,
            'archivo_salida': archivo_salida
        }
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_entrada}")
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {str(e)}")
        return None

def main():
    """Función principal para ejecutar el filtrado"""
    archivo_entrada = "dataset_comentariosv2.csv"
    
    # Verificar si el archivo existe
    if not os.path.exists(archivo_entrada):
        print(f"Error: El archivo {archivo_entrada} no existe en el directorio actual.")
        return
    
    # Ejecutar el filtrado
    resultado = eliminar_not_applicable(archivo_entrada)
    
    if resultado:
        print(f"\n{'='*50}")
        print("RESUMEN DEL FILTRADO:")
        print(f"{'='*50}")
        print(f"Registros originales: {resultado['total_original']:,}")
        print(f"Registros eliminados: {resultado['eliminados']:,}")
        print(f"Registros restantes: {resultado['restantes']:,}")
        print(f"Porcentaje eliminado: {resultado['porcentaje_eliminado']:.2f}%")
        print(f"Archivo de salida: {resultado['archivo_salida']}")

if __name__ == "__main__":
    main()
