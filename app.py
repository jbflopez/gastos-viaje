from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
import os
import pandas as pd
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
EXCEL_FILE = 'gastos.xlsx'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crear carpeta si no existe
if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Inicializar Excel si no existe
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=['Item', 'Date', 'Amount', 'Customer', 'Diners', 'Ticket'])
    df.to_excel(EXCEL_FILE, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar_gasto', methods=['POST'])
def guardar_gasto():
    item = request.form.get('item')
    date = request.form.get('date')
    amount = float(request.form.get('amount'))
    customer = request.form.get('customer')
    diners = request.form.get('diners') if item == 'ext_entert' else ''

    # Guardar imagen
    ticket = request.files['ticket']
    filename = secure_filename(f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{ticket.filename}")
    ticket_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    ticket.save(ticket_path)

    # Cargar Excel y añadir fila
    df = pd.read_excel(EXCEL_FILE)
    df.loc[len(df)] = [item, date, amount, customer, diners, ticket_path]
    df.to_excel(EXCEL_FILE, index=False)

    return ('', 204)  # 204 No Content → evita recarga

@app.route('/reset', methods=['POST'])
def reset():
    df = pd.DataFrame(columns=['Item', 'Date', 'Amount', 'Customer', 'Diners', 'Ticket'])
    df.to_excel(EXCEL_FILE, index=False)
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
