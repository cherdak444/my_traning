class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            raise TypeError("Нельзя сравнивать объект класса House с объектом другого типа")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            raise TypeError("Нельзя сравнивать объект класса House с объектом другого типа")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            raise TypeError("Нельзя сравнивать объект класса House с объектом другого типа")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            raise TypeError("Нельзя сравнивать объект класса House с объектом другого типа")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            raise TypeError("Нельзя сравнивать объект класса House с объектом другого типа")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            raise TypeError("Нельзя сравнивать объект класса House с объектом другого типа")

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

        else:
            raise TypeError("Можно складывать только целые числа и объекты класса House")

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)  # Создаем новый объект с измененным количеством этажей

        else:
            raise TypeError("Можно складывать только целые числа и объекты класса House")

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value  # Изменяем текущий объект в месте
            return self

        else:
            raise TypeError("Можно складывать только целые числа и объекты класса House")

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)



print(h1)

print(h2)



print(h1 == h2) # __eq__



h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)



h1 += 10 # __iadd__

print(h1)



h2 = 10 + h2 # __radd__

print(h2)



print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__
