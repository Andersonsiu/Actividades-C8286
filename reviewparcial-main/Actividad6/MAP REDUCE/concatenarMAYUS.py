def main():
    words = ['hola', 'mundo', 'programación', 'funcional', 'Python']
    # Convertir todas las palabras a mayúsculas
    upper_words = map(str.upper, words)
    
    # Concatenar todas las palabras en una cadena separada por comas usando un bucle for
    result = ""
    for word in upper_words:
        if result:  # Si result ya tiene contenido, añadimos una coma antes del siguiente elemento
            result += ","
        result += word

    print(result)

if __name__ == '__main__':
    main()
