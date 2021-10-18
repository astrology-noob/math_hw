import numpy as np

def system_matrix_input() -> np.array:
    # цикл для ввода, проверка на дурака (если вводится не два числа, цикл продолжается)
    while True:
        determ_size_input = input("Введите размер матрицы системы (количество равенств и количество переменных): ").split(" ")
        try:
            determ_row = int(determ_size_input[0])
            determ_col = int(determ_size_input[1])
            break
        except:
            print("Вы должны написать два числа, разделённые пробелом. Это не так сложно")
            continue

    # проверка, равно ли количество уравнений количеству переменных: в противном случае система не имеет решений
    if determ_row != determ_col:
        print(f"Количество уравнений не совпадает с количеством переменных ({determ_row} != {determ_col}): у системы нет решений или бесконечное количество решений.")
        # возвращаем пустой список, чтобы не входить в цикл while system_matrix.any(), потому что [].any()==False. В таком случае find_roots возвращает False
        return []

    # создаём матрицу нужного размера из нулей, куда будем записывать вводимыее значения, тип данных (float или int) не имеет значения
    system_matrix = np.zeros([determ_row, determ_col])

    # ввод главной матрицы системы
    print("Введите коэффициенты при переменных по строкам через пробел (если в одном из уравнений переменная отсутствует - напишите 0):")
    for i in range(determ_row):
        while True:
            # пробуем преобразовать input в список, если не получается, запускаем цикл заново
            try:
                row_input = [int(i) for i in input().split(" ")]
                # проверяем, равно ли количество значений заданному ранее размеру матрицы
                if len(row_input) == determ_col:
                    # присваиваем i-той строке значение row_input (соответствующие значения списка присваиваются значеням в ряду)
                    system_matrix[i] = row_input
                    break
                else:
                    print("Количество значений не совпадает с количеством столбцов определителя системы.")
            except:
                print("Введите строку заново. Один или несколько элементов не являются числами.")
                continue
    # возвращаем массив - главную матрицу системы
    return system_matrix

# считает определитель
def find_determinant(matrix):
    return np.linalg.det(matrix)

# проверяет систему на совместность
def is_consistent(system_matrix_det):
    return system_matrix_det != 0

# находит определители матриц с одним столбцом заменённым на столбец свободных членов
def find_root_determinant_value(root_index, system_matrix, const_terms):
    root_matrix = system_matrix.copy()
    for row_index in range(len(system_matrix)):
        root_matrix[row_index][root_index] = const_terms[row_index]
    root_determinant = find_determinant(root_matrix)
    return root_determinant

# главная функция, которая вычисляет корни; в случае, если какая-то вспомогательная функция возвращает False, гл. функция возвращает False (корней нет)
def find_roots() -> list:
    system_matrix = system_matrix_input()

    while system_matrix.any():
        system_det_value = find_determinant(system_matrix)
        if is_consistent(system_det_value):
            print("Введите свободные члены системы:")
        else:
            print("Определитель матрицы системы равен нулю: у системы нет решений или бесконечное количество решений.")
            return False

        while True:
            const_terms = [int(i) for i in input().split(" ")]
            if len(const_terms) == len(system_matrix):
                break
            else:
                print("Количество свободных членов системы не совпадает с количеством уравнений системы: введите их заново.")

        roots_list = []
        for root_index in range(len(system_matrix[0])):
            root = find_root_determinant_value(root_index, system_matrix, const_terms)/system_det_value
            # округляет в меньшую сторону если делить нацело (//)
            roots_list.append(round(root))
        return roots_list
    return False

roots1 = find_roots()

if roots1 == False:
    print("Нет корней")
else:
    print("Ответ: ", ', '.join([str(i) for i in roots1]))