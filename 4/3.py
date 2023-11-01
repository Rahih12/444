def calculate_GDP(C, I, G, Ex, Im):
    return C + I + G + Ex - Im

values_list = []
values_dict = {}

C = int(input("Введите значение C: "))
I = int(input("Введите значение I: "))
G = int(input("Введите значение G: "))
Ex = int(input("Введите значение Ex: "))
Im = int(input("Введите значение Im: "))

values_list = [C, I, G, Ex, Im]
values_dict = {'C': C, 'I': I, 'G': G, 'Ex': Ex, 'Im': Im}

def print_GDP(*args, **kwargs):
    GDP = calculate_GDP(*args, **kwargs)
    print("GDP:", GDP)

print_GDP(*values_list)
print_GDP(**values_dict)
