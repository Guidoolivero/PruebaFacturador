# 📊 Extractor Inteligente de Datos de Facturas

Sistema de extracción híbrido para procesar facturas y generar Excel con separación por monedas. Esta aplicación permite extraer automáticamente información clave de facturas en formato PDF, utilizando múltiples técnicas de reconocimiento para lograr una alta precisión en diversos formatos de facturación.

## 🌟 Características principales

- **Extracción automática de datos clave**:
  - Número de factura
  - Fecha de emisión
  - Montos desglosados (No Gravado, Exento, Gravado, IVA)
  - Importe total
  - Detección automática de moneda (ARS, USD, EUR)

- **Sistema de extracción híbrido**:
  - OCR avanzado con Tesseract (gratuito)
  - Reconocimiento de patrones y aprendizaje automático
  - Expresiones regulares como respaldo
  - Procesamiento especializado para facturas de agencias de viajes

- **Detección inteligente**:
  - Reconocimiento automático del tipo de factura (A, B, Electrónica, etc.)
  - Identificación de "Bienes y srvs. no computables"
  - Soporte para facturas electrónicas AFIP
  - Detección de patrones específicos por proveedor

- **Generación avanzada de Excel**:
  - Una pestaña por factura con detalles completos
  - Pestañas de resumen agrupadas por moneda
  - Resumen global de todas las facturas
  - Formato profesional con estilos y campos monetarios
  - Campo adicional para "Total a facturar"

- **Interfaz de usuario intuitiva**:
  - Vista previa y edición de datos extraídos
  - Visualización por categorías de moneda
  - Resúmenes de totales
  - Barra de progreso durante el procesamiento

## 🔧 Requisitos técnicos

- Python 3.7 o superior
- Bibliotecas principales:
  - streamlit
  - pypdf
  - pandas
  - openpyxl
  - pytesseract (opcional, para OCR)
  - pdf2image (opcional, para OCR)
  - opencv-python (opcional, para OCR)

- Para OCR avanzado:
  - Tesseract OCR instalado en el sistema

## 📦 Instalación

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/Guidoolivero/PruebaFacturador.git
   cd PruebaFacturador
