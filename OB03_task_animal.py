# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы
# (`make_sound()`, `eat()`) для всех животных.

# Создание базового класса Animal
class Animal():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

# Создание подклассов животных
class Mammal(Animal):
    def eat(self):
        print(f"Млекопитающее {self.name} кушает")

    def procreative_care(self):
        print(f"Млекопитающее {self.name} заботится о потомстве")

    def make_sound(self):
        print(f"Млекопитающее {self.name} издает звуки")

class Bird(Animal):
    def eat(self):
        print(f"Птица {self.name} кушает")

    def procreative_care(self):
        print(f"Птица {self.name} заботится о потомстве")

    def make_sound(self):
        print(f"Птица {self.name} поет")

class Reptile(Animal):
    def eat(self):
        print(f"Рептилия {self.name} кушает")

    def procreative_care(self):
        print(f"Рептилия {self.name} заботится о потомстве")

    def make_sound(self):
        print(f"Рептилия {self.name} издает звуки")

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.

# Создание списка животных
animals = [Mammal("белый медведь", 10, "девочка"),
           Bird("канарейка", 4, "мальчик"),
           Reptile("варан", 7, "девочка")]

# Создание функции animal_sound(animals) для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.animal_sound()

for animal in animals:
    animal.make_sound()

# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

# Создание класса Zoo
class Zoo():
    def __init__(self, animals = None, zooworkers = None):
        self.animals = animals if animals is not None else []
        self.zooworkers = zooworkers if zooworkers is not None else []

    # Вывод информации о животных и сотрудниках
    def get_animal_info(self):
        if self.animals:
            for animal in self.animals:
                print(f"Животное - {animal.name}, возраст - {animal.age}, пол - {animal.sex}")
        else:
            print("В зоопарке пока нет животных. ")

    def get_zooworkers_info(self):
        if self.zooworkers:
            for zooworker in self.zooworkers:
                print(f"Сотрудник - {zooworker}")
        else:
            print("В зоопарке пока нет сотрудников. ")

    # Добавление новых животных и сотрудников
    def add_new_animal(self, new_animal):
        self.animals.append(new_animal)
        print(f"Животное {new_animal.name} успешно добавлено. ")

    def add_new_zooworker(self, new_zooworker):
        self.zooworkers.append(new_zooworker)
        print(f"Сотрудник {new_zooworker} успешно добавлен. ")

# Создание объекта zoo и добавление новых животных
zoo = Zoo()
zoo.add_new_animal(Mammal("Тигр", 6, "мальчик"))
zoo.add_new_animal(Bird("Попугай", 2, "девочка"))

# Вывод информации о животных
zoo.get_animal_info()

# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

# Создание базового класса сотрудников
class ZooWorker:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # Представление данных в виде строки
    def __str__(self):
        return f"ID: {self.id}; {self.name}"

# Создание подклассов сотрудников
class Zoologist(ZooWorker):
    def investigate_animal(self):
        print(f"Зоолог исследует поведение животных. ")

class Veterinarian(ZooWorker):
    def heal_animal(self):
        print(f"Ветеринар лечит животных. ")

class Zookeeper(ZooWorker):
    def feed_animal(self):
        print(f"Зоокипер кормит животных")

# Добавление новых сотрудников
zoo.add_new_zooworker(Veterinarian(1, "Дмитрий"))
zoo.add_new_zooworker(Zoologist(2, "Анна"))
zoo.add_new_zooworker(Zookeeper(3, "Кирилл"))