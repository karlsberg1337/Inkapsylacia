class Human:
    def __init__(self, n, a, h):
        print('Создан объект класса Human')
        self.name=n
        self.age=a
        self.height=h
# 1)-6) В этом коде мы сначала определяем Human класс.
#__init__ - это метод конструктора, который принимает три параметра: имя,возраст,рост,и выводит сообщение создан
    
    def print(self):
        print(f'Имя:{self.name}')
        print(f'Возраст:{self.age}')
        print(f'Рост:{self.height}')
     # 10)-13) Метод print используется для печати сведений о человеческом объекте, включая имя, возраст и рост.
    
    @property
    def name(self):
        return self.__name.upper()
    # 17)-19) Мы определяем name свойство с помощью @property декоратора. 
    # Это свойство возвращает имя объекта human в верхнем регистре. 
        
    @name.setter    
    def name(self, n):
        self.__name=n.capitalize()
    # 22)-24) Мы определяем name установочный метод с помощью @name.setter декоратора.
    # Этот метод использует заглавную букву предоставленного имени перед присвоением его __name атрибуту.

        
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Недопустимый возраст")
   # 29)-37) Свойство возвращает возраст объекта human , 
   #а метод setter проверяет, находится ли указанный возраст в диапазоне от 0 до 100,прежде чем присвоить human
   # Если возраст не входит в допустимый диапазон

class Student(Human):
    def study(self):
        print(f'{self.name} учится')
# 33)-35) Далее мы определяем Student класс, который наследуется от Human класса. 
# Он добавляет study метод, который печатает сообщение, указывающее, что ученик учится. 
            

person1=Student('Maxim', 16, 189)
person1.print()
person1.study()
#38)-40) Мы создаем объект person1 класса Student с именем "Maxim", возрастом 16 лет и ростом 189.
 #Затем мы вызываем print метод для печати сведений об person1 объекте. 
#После этого мы вызываем study метод для печати сообщения, указывающего на то, что учащийся занимается.
