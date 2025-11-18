# Proyecto Final: IBM AI Enterprise Workflow Specialization

## Autor
Este proyecto fue creado por Esteban M. Cruz Seoane.

## ¿Qué es este proyecto?
Es una API sencilla que hace predicciones usando un modelo. También guarda logs y tiene pruebas para verificar que todo funciona.

## Archivos importantes
- **app.py**: Aquí está la API.
- **model.py**: El modelo que hace las predicciones.
- **logger.py**: Guarda los logs.
- **data_ingestion.py**: Maneja los datos.
- **run_tests.py**: Pruebas para verificar que todo funciona.
- **requirements.txt**: Lista de cosas que necesitas instalar.
- **Dockerfile**: Para usar Docker (opcional).

## Carpetas
- **sample_data/**: Datos de ejemplo.
- **models/**: Modelos guardados.
- **logs/**: Archivos de logs.
- **tests/**: Pruebas.

## ¿Qué necesitas para empezar?
1. **Python**: Asegúrate de tener Python 3.8 o más nuevo.
2. **pip**: Para instalar las cosas necesarias.
3. **Docker** (opcional): Si quieres usar contenedores.

## Pasos para usarlo
1. **Descarga el proyecto**:
   ```bash
   git clone https://github.com/pinkbunnies/curso-ibm.git
   ```
2. **Ve a la carpeta**:
   ```bash
   cd curso-ibm/capstone-solution
   ```
3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecuta la API**:
   ```bash
   python app.py
   ```
5. **Prueba la API**:
   Abre tu navegador o usa Postman para ir a:
   ```
   http://127.0.0.1:5000
   ```

## ¿Cómo probar que funciona?
Ejecuta las pruebas:
```bash
python run_tests.py
```

## ¿Y si quiero usar Docker?
1. **Crea la imagen**:
   ```bash
   docker build -t capstone-solution .
   ```
2. **Ejecuta el contenedor**:
   ```bash
   docker run -p 5000:5000 capstone-solution
   ```