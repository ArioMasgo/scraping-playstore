# REPORTE DE ANÁLISIS: CLASIFICACIONES ISO 25010
## Dataset de Comentarios de Aplicaciones Bancarias

### 📊 RESUMEN EJECUTIVO

**Datos analizados:**
- Total de comentarios: **7,140**
- Bancos: **3** (INTERBANK, BN, BCP)
- Clasificaciones únicas: **9**

---

### 🎯 HALLAZGOS PRINCIPALES

#### 1. Distribución General de Clasificaciones

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| **not_applicable** | 4,781 | **67.0%** |
| **authenticity** | 1,693 | **23.7%** |
| accountability | 250 | 3.5% |
| integrity | 218 | 3.1% |
| resistance | 110 | 1.5% |
| confidentiality | 64 | 0.9% |
| non_repudiation | 22 | 0.3% |

#### 2. Comentarios con Problemas de Seguridad

- **Total con clasificación de seguridad: 2,359 comentarios (33.0%)**
- **Principales problemas de seguridad:**
  1. **Authenticity (Autenticidad)**: 1,693 comentarios (71.8% de problemas de seguridad)
  2. **Accountability (Responsabilidad)**: 250 comentarios (10.6%)
  3. **Integrity (Integridad)**: 218 comentarios (9.2%)

---

### 🏦 ANÁLISIS POR BANCO

#### INTERBANK
- **Comentarios analizados**: 2,441
- **Problemas de seguridad**: 989 comentarios (40.5%)
- **Principal problema**: Authenticity (26.9%)
- **Segundo problema**: Integrity (5.3%)

#### BN (Banco de la Nación)
- **Comentarios analizados**: 2,481
- **Problemas de seguridad**: 639 comentarios (25.8%)
- **Principal problema**: Authenticity (21.2%)
- **Segundo problema**: Integrity (1.8%)

#### BCP
- **Comentarios analizados**: 2,218
- **Problemas de seguridad**: 731 comentarios (33.0%)
- **Principal problema**: Authenticity (23.0%)
- **Segundo problema**: Accountability (4.7%)

### Banco BCP
| Banco | Clasificación ISO 25010 | Cantidad |
|-------|-------------------------|----------|
| BCP   | accountability          | 105      |
| BCP   | authenticity            | 510      |
| BCP   | confidentiality         | 36       |
| BCP   | integrity               | 44       |
| BCP   | non_repudiation         | 14       |
| BCP   | not_applicable          | 1487     |
| BCP   | resistance              | 22       |

### Banco BN
| Banco | Clasificación ISO 25010 | Cantidad |
|-------|-------------------------|----------|
| BN    | accountability          | 19       |
| BN    | authenticity            | 527      |
| BN    | confidentiality         | 20       |
| BN    | integrity               | 44       |
| BN    | non_repudiation         | 5        |
| BN    | not_applicable          | 1843     |
| BN    | resistance              | 23       |

### Banco INTERBANK
| Banco     | Clasificación ISO 25010 | Cantidad |
|-----------|-------------------------|----------|
| INTERBANK | accountability          | 126      |
| INTERBANK | authenticity            | 656      |
| INTERBANK | confidentiality         | 8        |
| INTERBANK | integrity               | 130      |
| INTERBANK | non_repudiation         | 3        |
| INTERBANK | not_applicable          | 1452     |
| INTERBANK | resistance              | 66       |
---

### 🔍 INTERPRETACIÓN DE RESULTADOS

#### Problemas Críticos Identificados:

1. **AUTHENTICITY (Autenticidad) - 23.7% del total**
   - Problemas con tokens digitales
   - Fallas en códigos de verificación
   - Dificultades con autenticación biométrica
   - Bloqueos de cuentas injustificados

2. **ACCOUNTABILITY (Responsabilidad) - 3.5% del total**
   - Falta de notificaciones de transacciones
   - Ausencia de comprobantes detallados
   - Problemas para capturar pantallas como evidencia

3. **INTEGRITY (Integridad) - 3.1% del total**
   - Discrepancias en saldos
   - Transacciones no procesadas correctamente
   - Cobros indebidos

#### Recomendaciones por Banco:

**INTERBANK**: Enfocar en mejorar sistemas de autenticación y integridad de datos
**BN**: Priorizar la confiabilidad del sistema de autenticación
**BCP**: Mejorar tanto autenticación como sistemas de seguimiento/responsabilidad

---

### 📈 MÉTRICAS CLAVE

- **67% de comentarios** no presentan problemas específicos de seguridad
- **33% de comentarios** identifican problemas de seguridad según ISO 25010
- **INTERBANK** tiene el mayor porcentaje de problemas de seguridad (40.5%)
- **Authenticity** es el problema más crítico en los 3 bancos

---

*Reporte generado el 10 de agosto de 2025*
*Basado en análisis de 7,140 comentarios de usuarios de aplicaciones bancarias*
