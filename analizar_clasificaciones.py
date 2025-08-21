#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análisis de clasificaciones ISO 25010 en el dataset de comentarios
"""

import pandas as pd

def analizar_clasificaciones():
    """
    Realiza un análisis completo de las clasificaciones ISO 25010
    """
    # Cargar datos
    df = pd.read_csv('dataset_comentariosv2.csv')
    
    print("=" * 60)
    print("ANÁLISIS DE CLASIFICACIONES ISO 25010")
    print("=" * 60)
    print()
    
    # 1. Resumen general
    print("📊 RESUMEN GENERAL")
    print("-" * 30)
    print(f"Total de comentarios: {len(df):,}")
    print(f"Bancos analizados: {df['banco'].nunique()}")
    print(f"Clasificaciones únicas: {df['clasificacion_ISO_25010'].nunique()}")
    print()
    
    # 2. Conteo total por clasificación
    print("📈 DISTRIBUCIÓN GENERAL POR CLASIFICACIÓN")
    print("-" * 50)
    conteo_total = df['clasificacion_ISO_25010'].value_counts()
    
    for i, (clasificacion, cantidad) in enumerate(conteo_total.items(), 1):
        porcentaje = (cantidad / len(df)) * 100
        print(f"{i:2d}. {clasificacion:<20}: {cantidad:>5,} ({porcentaje:>5.1f}%)")
    print()
    
    # 3. Análisis por banco
    print("🏦 ANÁLISIS POR BANCO")
    print("-" * 30)
    
    # Crear tabla cruzada
    tabla_cruzada = pd.crosstab(df['banco'], df['clasificacion_ISO_25010'], margins=True)
    print("Tabla de frecuencias absolutas:")
    print(tabla_cruzada)
    print()
    
    # Tabla de porcentajes por banco
    print("Porcentajes por banco:")
    tabla_porcentajes = pd.crosstab(df['banco'], df['clasificacion_ISO_25010'], normalize='index') * 100
    print(tabla_porcentajes.round(1))
    print()
    
    # 4. Top clasificaciones por banco
    print("🎯 TOP 3 CLASIFICACIONES POR BANCO")
    print("-" * 40)
    
    for banco in ['INTERBANK', 'BN', 'BCP']:
        print(f"\n{banco}:")
        banco_data = df[df['banco'] == banco]
        top_3 = banco_data['clasificacion_ISO_25010'].value_counts().head(3)
        
        for i, (clasificacion, cantidad) in enumerate(top_3.items(), 1):
            porcentaje = (cantidad / len(banco_data)) * 100
            print(f"  {i}. {clasificacion:<20}: {cantidad:>4} ({porcentaje:>5.1f}%)")
    
    # 5. Clasificaciones de seguridad (excluyendo not_applicable)
    print("\n🔒 CLASIFICACIONES DE SEGURIDAD")
    print("-" * 35)
    clasificaciones_seguridad = df[df['clasificacion_ISO_25010'] != 'not_applicable']
    print(f"Total comentarios con clasificación de seguridad: {len(clasificaciones_seguridad):,}")
    print(f"Porcentaje del total: {(len(clasificaciones_seguridad)/len(df)*100):.1f}%")
    print()
    
    conteo_seguridad = clasificaciones_seguridad['clasificacion_ISO_25010'].value_counts()
    for i, (clasificacion, cantidad) in enumerate(conteo_seguridad.items(), 1):
        porcentaje = (cantidad / len(clasificaciones_seguridad)) * 100
        print(f"{i:2d}. {clasificacion:<20}: {cantidad:>4} ({porcentaje:>5.1f}%)")
    
    return df, conteo_total, tabla_cruzada

def crear_reporte_resumen():
    """
    Crea un reporte resumen en formato CSV
    """
    df = pd.read_csv('dataset_comentariosv1.csv')
    
    # Resumen por clasificación
    resumen_clasificacion = df['clasificacion_ISO_25010'].value_counts().reset_index()
    resumen_clasificacion.columns = ['clasificacion', 'cantidad']
    resumen_clasificacion['porcentaje'] = (resumen_clasificacion['cantidad'] / len(df) * 100).round(2)
    
    # Resumen por banco y clasificación
    resumen_banco_clasificacion = df.groupby(['banco', 'clasificacion_ISO_25010']).size().reset_index(name='cantidad')
    
    # Guardar reportes
    resumen_clasificacion.to_csv('reporte_clasificaciones.csv', index=False)
    resumen_banco_clasificacion.to_csv('reporte_banco_clasificaciones.csv', index=False)
    
    print("📄 Reportes creados:")
    print("   - reporte_clasificaciones.csv")
    print("   - reporte_banco_clasificaciones.csv")
    
    return resumen_clasificacion, resumen_banco_clasificacion

if __name__ == "__main__":
    # Ejecutar análisis
    df, conteo_total, tabla_cruzada = analizar_clasificaciones()
    
    print("\n" + "="*60)
    
    # Crear reportes
    resumen_cls, resumen_banco_cls = crear_reporte_resumen()
    
    print("\n✅ Análisis completado exitosamente!")
