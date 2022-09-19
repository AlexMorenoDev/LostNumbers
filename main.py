# Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule
# y retorne todos los que faltan entre el mayor y el menor.
# - Lanza un error si el array de entrada no es correcto.

def check_array(array):
    last_n = None
    shown_numbers = set()
    for n in array:
        if last_n and (n < last_n or n in shown_numbers):
            return False
        last_n = n
        shown_numbers.add(n)

    return True

def find_lost_numbers(array):
    if check_array(array):
        lost_numbers = []
        array_set = set(array)
        lowest, greatest = array[0], array[-1]
        for n in range(lowest+1, greatest):
            if n not in array_set:
                lost_numbers.append(n)

        return lost_numbers
    else:
        print("ERROR: Array format is not correct!")
        return None

print(find_lost_numbers([1, 3, 5])) # [2, 4]
print(find_lost_numbers([5, 3, 1])) # Error
print(find_lost_numbers([5, 1])) # Error
print(find_lost_numbers([-5, 1])) # [-4, -3, -2, -1, 0]
print(find_lost_numbers([1, 3, 3, 5])) # Error
print(find_lost_numbers([5, 7, 1])) # Error
print(find_lost_numbers([10, 7, 1, 7])) # Error