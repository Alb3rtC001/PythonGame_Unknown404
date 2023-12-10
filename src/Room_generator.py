import random

def next_floor():
    # Parámetros preestablecidos
    min_longitud_array = 8
    max_longitud_array = 12
    room_needs = ["enfermería", "taller", "angar", "duchas", "navegación", "reactor", "tienda", "crafter", "void"]
    room_needs_prob = [0.4, 0.4, 0.4, 0.3, 0.8, 0.7, 0.3, 0.5 ,0.85]

    special_rooms = ["void", "super_secret_room", "secret_room"]
    special_rooms_prob = [0.93, 0.01, 0.06]

    # Crear un diccionario de arrays
    diccionario_arrays = []

    max_rooms = random.randint(min_longitud_array,max_longitud_array)
    random.shuffle(room_needs)
    array_rooms = []
    array_rooms.append("spawn")
    array_rooms.append("salida")
    pre_fault_rooms = 2
    # Seleccionar elementos con base en las probabilidades
    if max_rooms > 10:
        add_rooms(room_needs, room_needs_prob, array_rooms, pre_fault_rooms)
    add_rooms(room_needs, room_needs_prob, array_rooms, pre_fault_rooms)
    add_rooms(room_needs, room_needs_prob, array_rooms, pre_fault_rooms)
    add_rooms(special_rooms, special_rooms_prob, array_rooms, pre_fault_rooms)
    #print("----------------")
    for room in range(max_rooms - pre_fault_rooms):
        #probabilidad y certeza
        array_rooms.append("sala_comun")
    #Bien barajado
    random.shuffle(array_rooms)
    random.shuffle(array_rooms)
    random.shuffle(array_rooms)
    diccionario_arrays = array_rooms
    return diccionario_arrays

def add_rooms(special_rooms, special_rooms_prob, array_rooms, pre_fault_rooms):
    special_room_element = random.choices(special_rooms, weights=special_rooms_prob, k=1)[0]
    #print(special_room_element)
    if special_room_element != "void": 
        pre_fault_rooms =+1 
        array_rooms.append(special_room_element)


# Imprimir el diccionario resultante
def print_floor_rooms(diccionario_arrays):
    print("Diccionario de Arrays:")
    print(diccionario_arrays)
    #for valor in diccionario_arrays:
        #print(f"{valor}")

new_array = next_floor()
print_floor_rooms(new_array)