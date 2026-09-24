def contar_palabras(texto):
    return len(texto.split())

# Ejemplo de uso
frase = "El enfoque humanista me parece el más útil porque coloca al estudiante y sus emociones en el centro. Sin un ambiente seguro y motivador, el aprendizaje se bloquea por estrés o depresión. Como futura docente auxiliar, quiero que mis estudiantes retengan la información y puedan desarrollar autonomía significativa."
print("Número de palabras:", contar_palabras(frase))
