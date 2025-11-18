FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia las dependencias y las instala
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto 5000 para la API
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
