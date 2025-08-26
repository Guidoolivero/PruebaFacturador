Extractor Inteligente de Datos de Facturas

Descripción

Esta aplicación permite procesar archivos PDF de facturas para extraer automáticamente los datos más importantes y generar un archivo Excel organizado. El sistema utiliza inteligencia artificial y técnicas de reconocimiento de patrones para identificar y extraer información de diversos formatos de facturas.

Características Principales

Extracción automatizada de datos clave:

Número de factura
Fecha
Montos desglosados (No Gravado, Exento, Gravado, IVA)
Monto total
Moneda (ARS, USD, EUR)
Reconocimiento inteligente:

Detección automática de moneda
Reconocimiento especializado para facturas de agencias de viajes
Soporte para facturas argentinas electrónicas (AFIP)
Detección de "Bienes y srvs. no computables"
Procesamiento híbrido:

OCR avanzado con Tesseract (gratuito)
Reconocimiento de patrones y aprendizaje automático
Expresiones regulares como respaldo
Generación de Excel organizado:

Una pestaña por factura con detalles completos
Pestañas de resumen por moneda
Resumen global de todas las facturas
Formatos monetarios aplicados correctamente
Campos personalizados para "Total a facturar"
Interfaz amigable:

Edición de datos extraídos antes de exportar
Visualización por categorías de moneda
Resumen de totales por moneda
Indicadores de progreso durante el procesamiento
Requisitos del Sistema

Python 3.7 o superior
Tesseract OCR instalado en el sistema (opcional, pero recomendado)
Bibliotecas Python:
streamlit
pypdf
pandas
openpyxl
pytesseract (si se usa OCR)
pdf2image (si se usa OCR)
opencv-python (si se usa OCR)
numpy
Instalación

Instalar Python 3.7 o superior

Instalar Tesseract OCR (opcional para OCR avanzado):

Windows: Descargar instalador
Mac: brew install tesseract
Linux: apt-get install tesseract-ocr
Instalar las bibliotecas de Python:

Code
pip install streamlit pypdf pandas openpyxl pytesseract pdf2image opencv-python numpy
Cómo usar

Ejecutar la aplicación:

Code
streamlit run extractor_facturas_web.py
Cargar archivos PDF:

Seleccionar uno o varios archivos PDF de facturas
Hacer clic en "Procesar Facturas"
Revisar y editar datos:

Verificar los datos extraídos de cada factura
Realizar correcciones si es necesario
Visualizar totales por moneda
Exportar a Excel:

Hacer clic en "Descargar Excel" para obtener el archivo generado
El Excel incluirá una pestaña por factura y resúmenes por moneda
Opciones de Configuración

Desde el panel lateral se pueden configurar:

Uso de OCR avanzado (Tesseract)
Reconocimiento de patrones
Ignorar patrones guardados
Modo depuración
Reiniciar base de conocimiento
Fase 1 Completada

La primera fase del desarrollo está completada. El sistema ya es funcional para extraer datos de facturas y generar el Excel organizado con todas las funcionalidades principales.

Futuras Mejoras

Integración con sistemas contables
Mejora del reconocimiento de facturas internacionales
Exportación en formatos adicionales
Implementación de IA más avanzada para interpretación contextual
© 2025 PruebaFacturador - Extractor Inteligente de Datos de Facturas
