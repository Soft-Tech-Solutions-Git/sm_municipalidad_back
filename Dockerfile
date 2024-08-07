# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos en el contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto en el contenedor
COPY . .

# Define la variable de entorno para Flask
ENV FLASK_APP=run.py

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
