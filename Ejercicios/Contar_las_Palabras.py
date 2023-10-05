"""
# PRUEBA TECNICA #

En la variable 'text' dispones de una cadena de texto.
Debes contar las palabras y devolver cuantas veces se repiten cada una.
Ejemplo => 'nadie' aparece 2 veces

"""

text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar."

# Dejar todo en minuscula.
def to_lower_case(text):
    lower_case = text.lower() 
    return lower_case
      
lower_Case = to_lower_case(text)



#Eliminar los puntos y las comas.
def clean_text(text_lower_case):
    cleaned_text = text_lower_case.replace('.','').replace(',','') 
    separated_text = cleaned_text.split(' ')# separar por cada espacio. El metodo split devuelve un array.
    
    return separated_text

cleaned_Text = clean_text(lower_Case)

#print(cleaned_Text)

# Iterar el array para contar las palabras.
def count_words(cleaned_Text):
    # Es una buena practica hacer un diccionario.
    dic = {}
    for word in cleaned_Text:
        if word in dic:
            dic[word]+= 1
        else:
            dic[word] = 1
            
    return dic

total = count_words(cleaned_Text)

print(total)

    
    