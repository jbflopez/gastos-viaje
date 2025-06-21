Perfecto ✅. Aquí tienes **ambas cosas**:

---

## 📄 1. README listo para tu repositorio `gastos-viaje`

Copia y pega esto en un archivo llamado `README.md` en la raíz de tu proyecto:

```markdown
# 🧾 Gastos de Viaje – App Web con Flask

Aplicación web para la **liquidación de gastos de viaje**, diseñada para ser usada desde móvil o PC por un comercial. Permite introducir tickets con foto, guardar datos en Excel, y reiniciar el ciclo tras cada liquidación.

---

## 🎯 Funcionalidades

- Formulario con selección de item, fecha, importe, cliente, comensales y ticket.
- Subida de imagen del justificante (foto del ticket).
- Guardado automático en un archivo Excel (`gastos.xlsx`).
- Reset de formulario y datos.
- Acceso desde cualquier navegador vía despliegue en Render.

---

## 📁 Estructura de Archivos

```

gastos-viaje/
├── app.py                     # Backend Flask
├── requirements.txt           # Dependencias
├── render.yaml                # (Opcional) Configuración para Render
├── templates/
│   └── index.html             # Formulario web
├── static/
│   └── uploads/               # Carpeta donde se guardan las imágenes
└── gastos.xlsx                # Excel con los registros de gastos

````

---

## ⚙️ Instalación local

```bash
pip install flask pandas openpyxl
python app.py
````

Accede en `http://127.0.0.1:5000`

---

## 🌐 Despliegue en Render

1. Crea un repositorio en GitHub con estos archivos.
2. Ve a [https://render.com](https://render.com), crea un "Web Service".
3. Configura:

   * Runtime: Python 3
   * Build Command: `pip install -r requirements.txt`
   * Start Command: `python app.py`
4. (Opcional) Usa `render.yaml` para control automático.
5. ¡Listo! Tu app estará disponible en una URL pública.

---

## 📤 Descarga de datos

Puedes añadir esta ruta para descargar el Excel directamente:

```python
@app.route('/descargar_excel')
def descargar_excel():
    return send_file('gastos.xlsx', as_attachment=True)
```

---

## 🔐 Notas

* Render no permite acceder al sistema de archivos directamente.
* Todos los datos e imágenes subidas se guardan en el servidor compartido (Render).
* Las imágenes son accesibles desde URLs públicas bajo `/static/uploads/`.

---

## 🛠 Pendientes / Mejoras

* Protección con contraseña
* Panel de resumen de gastos
* Descarga de todos los tickets en ZIP
* Envío automático por email

---

## 🧑‍💻 Autor

App desarrollada como ejercicio práctico de despliegue Flask + HTML + Render.

````

---

## 📦 2. Paquete mínimo del proyecto (estructura clonable)

Asegúrate de tener estos **mínimos archivos** para que todo funcione desde cero:

### ✅ `app.py`
(ya lo tienes perfecto)

### ✅ `requirements.txt`

```txt
Flask
pandas
openpyxl
````

### ✅ `templates/index.html`

(ya te lo di antes, puedes copiarlo igual)

### ✅ `render.yaml` (opcional)

```yaml
services:
  - type: web
    name: gastos-viaje
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python app.py"
```

### ✅ Carpeta vacía `static/uploads/`

(No subas imágenes; basta con que la ruta esté bien en el código)

---

¿Quieres que te genere todo esto como un ZIP descargable ahora mismo? ¿O vas a actualizar tu repositorio manualmente?
