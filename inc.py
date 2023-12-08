class Human:
    def __init__(self, n, a, h):
        print('Создан объект класса Human')
        self.name=n
        self.age=a
        self.height=h
    
    def print(self):
        print(f'Имя:{self.name}')
        print(f'Возраст:{self.age}')
        print(f'Рост:{self.height}')
     
    @property
    def name(self):
        return self.__name.upper()
        
    @name.setter    
    def name(self, n):
        self.__name=n.capitalize()
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Недопустимый возраст")


class Student(Human):
    def study(self):
        print(f'{self.name} учится')
            

person1=Student('Maxim', 16, 189)
person1.print()
person1.study()
