#Вариант 1, функции
#Даны четыре действительных числа: x1, y1, x2, y2.
#Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
#Считайте четыре действительных числа и выведите результат работы этой функции.
x1, y1, x2, y2 = map(float, input("Введите x1, y1, x2, y2 через пробелы\n").split())
print("Переданные аргументы: \n", "x10 = ", x1, " ; ", "y1 = ", y1, "\n", "x2 = ", x2, " ; ", "y2 = ", y2, "\n")
def distance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    return ((a **2 + b ** 2) ** 0.5)
print("Расстояние между точками (x1,y1) и (x2,y2): ", distance(x1,y1,x2,y2))
