from openpyxl import Workbook
from io import BytesIO
import streamlit as st
import pypdf
import pandas as pd
import re
from datetime import datetime
import os
from openpyxl import Workbook


def generar_excel(datos_list):
    """
    Genera un solo archivo Excel en memoria con una pestaña por factura.
    """
    output = BytesIO()
    wb = Workbook()
    
    # Eliminar la hoja por defecto solo después de crear al menos una hoja
    default_sheet = wb.active
    
    for i, datos in enumerate(datos_list):
        sheet_name = datos['Numero_Factura'] or os.path.basename(datos['Nombre_Archivo']).replace('.pdf', '')[:31]
        
        # Para la primera factura, reutilizar la hoja activa
        if i == 0:
            ws = default_sheet
            ws.title = sheet_name
        else:
            ws = wb.create_sheet(title=sheet_name)
        
        # Agregar encabezados
        headers = ['FECHA', 'NO GRAVADO', 'EXENTO', 'GRAVADO', 'IVA', 'TOTAL']
        for col_idx, header in enumerate(headers, 1):
            ws.cell(row=1, column=col_idx, value=header)
        
        # Agregar datos
        ws.cell(row=2, column=1, value=datos['Fecha'])
        ws.cell(row=2, column=2, value=datos['No_Gravado'])
        ws.cell(row=2, column=3, value=datos['Exento'])
        ws.cell(row=2, column=4, value=datos['Gravado'])
        ws.cell(row=2, column=5, value=datos['IVA'])
        ws.cell(row=2, column=6, value=datos['Total'])
    
    wb.save(output)
    output.seek(0)
    return output