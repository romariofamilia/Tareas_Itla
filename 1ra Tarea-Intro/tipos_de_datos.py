# 10 => int/enteros
# 10.5 => float/decimales/flotantes
# '10.5' => string/cadenas de texto
# true || false => bool
# [] => list/listas de datos
# {} => dict/diccionario

# devuelve el tipo de dato que le ingreses
def tipo_de_dato(dato):
    print(type(dato))


# Esta funcion hara una operacion la cual multiplicara los elementos de una lista y devolvera una lista con el resultado
def multi_list(li, num):
    for i in li:
        result = i * num
    return f'Este es el resultado => {[result]}'

print(multi_list([3,4.5,5.5], 5))