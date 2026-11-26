
# Програма для роботи зі списком

numbers = [5, 10, 15, 20, 25]

# Функція виведення списку
def show_list():
    print("Наш список:", numbers)

# Функція додавання числа
def add_number(number):
    numbers.append(number)
    print("Число додано!")

# Функція пошуку числа
def find_number(number):
    if number in numbers:
        print("Число знайдено!")
    else:
        print("Число не знайдено!")

show_list()
add_number(30)
find_number(15)
show_list()

print("Програма для роботи зі списками")

# Виведення кількості елементів

print("Кількість елементів:", len(numbers))

# Сортування списку

numbers.sort()
print("Відсортований списокс:", numbers)

print("Перша копія проєкту:")

print("Друга копія проєкту")
