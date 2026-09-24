import qrcode
import os

#  Aquí pones tu link
link = "https://magistraturaverificai.netlify.app/"

#Carpeta donde se guardará el QR
carpeta = "qr_generados"

# Crear carpeta si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

# Nombre del archivo
nombre_archivo = os.path.join(carpeta, "mi_qr.png")

# Crear QR
qr = qrcode.make(link)

# Guardar imagen
qr.save(nombre_archivo)

print("✅ QR generado correctamente en:", nombre_archivo)