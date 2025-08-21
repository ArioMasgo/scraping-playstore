import csv

# Nombre de los archivos
input_file = "comentarios_negativos_YAPE_1464.csv"   # archivo original
output_file = "salida.csv"   # archivo sin la 4ta columna

with open(input_file, "r", newline="", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) >= 4:   # si la fila tiene al menos 4 columnas
            del row[3]      # elimina la cuarta columna (índice 3)
        writer.writerow(row)

print("✅ Se eliminó la cuarta columna y se guardó en", output_file)