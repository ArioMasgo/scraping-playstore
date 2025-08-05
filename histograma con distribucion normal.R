install.packages(c("ggplot2","dplyr","tidyr","gridExtra"))
install.packages("tidyverse")
install.packages("fmsb")
library(fmsb)
library(ggplot2)
library(dplyr)
library(tidyr)
library(gridExtra)

# Preparar datos

# Asumo que 'datos' es tu dataframe con las columnas EE1, EE2, EE3, EE4
# Calcular promedio por encuestado
datos <- pruebas.estadisticas..piloto

datos$EE_promedio <- rowMeans(datos[, c("EE1", "EE2", "EE3", "EE4")])


----
ggplot(datos, aes(x = EE_promedio, y = EE1, color = EE2)) +
  geom_point(size = 3, alpha = 0.6) +
  geom_smooth(method = "lm", se = FALSE, color = "black") +
  labs(title = "Dispersión entre EE1 y Promedio",
       x = "Promedio EE", y = "EE1") +
  theme_minimal() +
  scale_color_gradient(low = "blue", high = "red", name = "EE2")


# 1. Boxplot de cada indicador de Expectativa de Esfuerzo
boxplot_ee <- datos %>%
  pivot_longer(cols = c(EE1, EE2, EE3, EE4), 
               names_to = "Indicador", 
               values_to = "Valor") %>%
  ggplot(aes(x = Indicador, y = Valor, fill = Indicador)) +
  geom_boxplot() +
  labs(title = "Distribución de Indicadores de Expectativa de Esfuerzo",
       x = "Indicadores", 
       y = "Puntuación") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set3")

# 2. Gráfico de barras para promedios de indicadores
barras_ee <- datos %>%
  pivot_longer(cols = c(EE1, EE2, EE3, EE4), 
               names_to = "Indicador", 
               values_to = "Valor") %>%
  group_by(Indicador) %>%
  summarise(Promedio = mean(Valor)) %>%
  ggplot(aes(x = Indicador, y = Promedio, fill = Indicador)) +
  geom_bar(stat = "identity") +
  labs(title = "Promedio por Indicador de Expectativa de Esfuerzo",
       x = "Indicadores", 
       y = "Promedio") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set3") +
  geom_text(aes(label = round(Promedio, 2)), 
            position = position_dodge(width = 0.9), 
            vjust = -0.5)

# 3. Tabla de análisis descriptivo
tabla_descriptiva <- datos %>%
  summarise(
    "Promedio General" = round(mean(EE_promedio), 2),
    "Desviación Estándar" = round(sd(EE_promedio), 2),
    "Mínimo" = round(min(EE_promedio), 2),
    "Máximo" = round(max(EE_promedio), 2),
    "Mediana" = round(median(EE_promedio), 2)
  )

# 4. Análisis de frecuencias por rango
datos$Rango_EE <- cut(datos$EE_promedio, 
                      breaks = c(0, 3, 6, 10), 
                      labels = c("Bajo (0-3)", "Medio (4-6)", "Alto (7-10)"))

frecuencias_ee <- table(datos$Rango_EE)
porcentajes_ee <- round(prop.table(frecuencias_ee) * 100, 2)

# 5. Gráfico de distribución de rangos
grafico_rangos <- ggplot(datos, aes(x = Rango_EE)) +
  geom_bar(aes(y = (..count..)/sum(..count..) * 100), fill = "skyblue") +
  labs(title = "Distribución de Rangos de Expectativa de Esfuerzo",
       x = "Rango", 
       y = "Porcentaje") +
  theme_minimal() +
  geom_text(aes(y = ((..count..)/sum(..count..) * 100), 
                label = paste0(round(((..count..)/sum(..count..) * 100), 1), "%")), 
            stat = "count", 
            vjust = -0.5)

# Mostrar resultados
print("Tabla Descriptiva:")
print(tabla_descriptiva)

print("\nFrecuencias por Rango:")
print(frecuencias_ee)

print("\nPorcentajes por Rango:")
print(porcentajes_ee)

# Guardar gráficos
ggsave("boxplot_ee.png", boxplot_ee, width = 10, height = 6)
ggsave("barras_ee.png", barras_ee, width = 10, height = 6)
ggsave("rangos_ee.png", grafico_rangos, width = 10, height = 6)

# Organizar gráficos en un panel
grid.arrange(boxplot_ee, barras_ee, grafico_rangos, ncol = 2)

getwd()

#------------------------------------------------ahora para ED

# Calcular promedio por encuestado
datos$ED_promedio <- rowMeans(datos[, c("ED1", "ED2", "ED3", "ED4")])

# Boxplot de cada indicador de Desempeño Percibido
boxplot_ed <- datos %>%
  pivot_longer(cols = c("ED1", "ED2", "ED3", "ED4"), 
               names_to = "Indicador", 
               values_to = "Valor") %>%
  ggplot(aes(x = Indicador, y = Valor, fill = Indicador)) +
  geom_boxplot() +
  labs(title = "Distribución de Indicadores de Desempeño Percibido",
       x = "Indicadores", 
       y = "Puntuación") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set3")

# Gráfico de barras para promedios de indicadores
barras_ed <- datos %>%
  pivot_longer(cols = c("ED1", "ED2", "ED3", "ED4"), 
               names_to = "Indicador", 
               values_to = "Valor") %>%
  group_by(Indicador) %>%
  summarise(Promedio = mean(Valor)) %>%
  ggplot(aes(x = Indicador, y = Promedio, fill = Indicador)) +
  geom_bar(stat = "identity") +
  labs(title = "Promedio por Indicador de Desempeño Percibido",
       x = "Indicadores", 
       y = "Promedio") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set3") +
  geom_text(aes(label = round(Promedio, 2)), 
            position = position_dodge(width = 0.9), 
            vjust = -0.5)

# Tabla descriptiva
tabla_descriptiva_ed <- datos %>%
  summarise(
    "Promedio General" = round(mean(ED_promedio), 2),
    "Desviación Estándar" = round(sd(ED_promedio), 2),
    "Mínimo" = round(min(ED_promedio), 2),
    "Máximo" = round(max(ED_promedio), 2),
    "Mediana" = round(median(ED_promedio), 2)
  )
# 4. Análisis de frecuencias por rango
datos$Rango_ED <- cut(datos$ED_promedio, 
                      breaks = c(0, 3, 6, 10), 
                      labels = c("Bajo (0-3)", "Medio (4-6)", "Alto (7-10)"))

frecuencias_ed <- table(datos$Rango_ED)
porcentajes_ed <- round(prop.table(frecuencias_ed) * 100, 2)

# 5. Gráfico de distribución de rangos
grafico_rangos_ed <- ggplot(datos, aes(x = Rango_ED)) +
  geom_bar(aes(y = (..count..)/sum(..count..) * 100), fill = "skyblue") +
  labs(title = "Distribución de Rangos de Desempeño Percibido",
       x = "Rango", 
       y = "Porcentaje") +
  theme_minimal() +
  geom_text(aes(y = ((..count..)/sum(..count..) * 100), 
                label = paste0(round(((..count..)/sum(..count..) * 100), 1), "%")), 
            stat = "count", 
            vjust = -0.5)

# Guardar gráfico
ggsave("rangos_ed.png", grafico_rangos_ed, width = 10, height = 6)

ggsave("boxplot_ed.png", boxplot_ed, width = 10, height = 6)
ggsave("barras_ed.png", barras_ed, width = 10, height = 6)
# Organizar gráficos en un panel
grid.arrange(boxplot_ed, barras_ed, grafico_rangos_ed, ncol = 2)

#--------------------------------para CF--------------------------

# Calcular promedio por encuestado
datos$CF_promedio <- rowMeans(datos[, c("CF1", "CF2", "CF3", "CF4")])

# Boxplot de cada indicador de Facilitadores Tecnológicos
boxplot_cf <- datos %>%
  pivot_longer(cols = c("CF1", "CF2", "CF3", "CF4"), 
               names_to = "Indicador", 
               values_to = "Valor") %>%
  ggplot(aes(x = Indicador, y = Valor, fill = Indicador)) +
  geom_boxplot() +
  labs(title = "Distribución de Indicadores de Facilitadores Tecnológicos",
       x = "Indicadores", 
       y = "Puntuación") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set3")

# Gráfico de barras para promedios de indicadores
barras_cf <- datos %>%
  pivot_longer(cols = c("CF1", "CF2", "CF3", "CF4"), 
               names_to = "Indicador", 
               values_to = "Valor") %>%
  group_by(Indicador) %>%
  summarise(Promedio = mean(Valor)) %>%
  ggplot(aes(x = Indicador, y = Promedio, fill = Indicador)) +
  geom_bar(stat = "identity") +
  labs(title = "Promedio por Indicador de Facilitadores Tecnológicos",
       x = "Indicadores", 
       y = "Promedio") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set3") +
  geom_text(aes(label = round(Promedio, 2)), 
            position = position_dodge(width = 0.9), 
            vjust = -0.5)

# Tabla descriptiva
tabla_descriptiva_cf <- datos %>%
  summarise(
    "Promedio General" = round(mean(CF_promedio), 2),
    "Desviación Estándar" = round(sd(CF_promedio), 2),
    "Mínimo" = round(min(CF_promedio), 2),
    "Máximo" = round(max(CF_promedio), 2),
    "Mediana" = round(median(CF_promedio), 2)
  )

# 4. Análisis de frecuencias por rango
datos$Rango_CF <- cut(datos$CF_promedio, 
                      breaks = c(0, 3, 6, 10), 
                      labels = c("Bajo (0-3)", "Medio (4-6)", "Alto (7-10)"))

frecuencias_cf <- table(datos$Rango_CF)
porcentajes_cf <- round(prop.table(frecuencias_cf) * 100, 2)

# 5. Gráfico de distribución de rangos
grafico_rangos_cf <- ggplot(datos, aes(x = Rango_CF)) +
  geom_bar(aes(y = (..count..)/sum(..count..) * 100), fill = "skyblue") +
  labs(title = "Distribución de Rangos de Facilitadores Tecnológicos",
       x = "Rango", 
       y = "Porcentaje") +
  theme_minimal() +
  geom_text(aes(y = ((..count..)/sum(..count..) * 100), 
                label = paste0(round(((..count..)/sum(..count..) * 100), 1), "%")), 
            stat = "count", 
            vjust = -0.5)

# Guardar gráfico
ggsave("rangos_cf.png", grafico_rangos_cf, width = 10, height = 6)
ggsave("boxplot_cf.png", boxplot_cf, width = 10, height = 6)
ggsave("barras_cf.png", barras_cf, width = 10, height = 6)

# Organizar gráficos en un panel
grid.arrange(boxplot_cf, barras_cf, grafico_rangos_cf, ncol = 2)


#----------------------------------------------para IS-----------
  
# Calcular promedio por encuestado
datos$IS_promedio <- rowMeans(datos[, c("IS1", "IS2", "IS3")])

# Boxplot de cada indicador de Influencia Social
boxplot_is <- datos %>%
  pivot_longer(cols = c("IS1", "IS2", "IS3"), 
               names_to = "Indicador", 
               values_to = "Valor") %>%
  ggplot(aes(x = Indicador, y = Valor, fill = Indicador)) +
  geom_boxplot() +
  labs(title = "Distribución de Indicadores de Influencia Social",
       x = "Indicadores", 
       y = "Puntuación") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set3")

# Gráfico de barras para promedios de indicadores
barras_is <- datos %>%
  pivot_longer(cols = c("IS1", "IS2", "IS3"), 
               names_to = "Indicador", 
               values_to = "Valor") %>%
  group_by(Indicador) %>%
  summarise(Promedio = mean(Valor)) %>%
  ggplot(aes(x = Indicador, y = Promedio, fill = Indicador)) +
  geom_bar(stat = "identity") +
  labs(title = "Promedio por Indicador de Influencia Social",
       x = "Indicadores", 
       y = "Promedio") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set3") +
  geom_text(aes(label = round(Promedio, 2)), 
            position = position_dodge(width = 0.9), 
            vjust = -0.5)

# Tabla descriptiva
tabla_descriptiva_is <- datos %>%
  summarise(
    "Promedio General" = round(mean(IS_promedio), 2),
    "Desviación Estándar" = round(sd(IS_promedio), 2),
    "Mínimo" = round(min(IS_promedio), 2),
    "Máximo" = round(max(IS_promedio), 2),
    "Mediana" = round(median(IS_promedio), 2)
  )

# 4. Análisis de frecuencias por rango
datos$Rango_IS <- cut(datos$IS_promedio, 
                      breaks = c(0, 3, 6, 10), 
                      labels = c("Bajo (0-3)", "Medio (4-6)", "Alto (7-10)"))

frecuencias_is <- table(datos$Rango_IS)
porcentajes_is <- round(prop.table(frecuencias_is) * 100, 2)

# 5. Gráfico de distribución de rangos
grafico_rangos_is <- ggplot(datos, aes(x = Rango_IS)) +
  geom_bar(aes(y = (..count..)/sum(..count..) * 100), fill = "skyblue") +
  labs(title = "Distribución de Rangos de Influencia Social",
       x = "Rango", 
       y = "Porcentaje") +
  theme_minimal() +
  geom_text(aes(y = ((..count..)/sum(..count..) * 100), 
                label = paste0(round(((..count..)/sum(..count..) * 100), 1), "%")), 
            stat = "count", 
            vjust = -0.5)

# Guardar gráfico

ggsave("rangos_is.png", grafico_rangos_is, width = 10, height = 6)
ggsave("boxplot_is.png", boxplot_is, width = 10, height = 6)
ggsave("barras_is.png", barras_is, width = 10, height = 6)

# Organizar gráficos en un panel
grid.arrange(boxplot_is, barras_is, grafico_rangos_is, ncol = 2)

