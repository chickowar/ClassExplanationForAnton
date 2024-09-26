if __name__ == '__main__':
    play = int(input("Введи на каком ты этапе:\t"))


"""Введение"""
...

# В питоне (как и почти любом языке программирования) есть КЛАССЫ, а есть ОБЪЕКТЫ

# Класс - это, считай, тип данных, который ты сам пишешь и делаешь удобным в использовании для своей работы.
# Объект - это экземпляр класса, то есть что-то что имеет поведение общего класса.

# То есть int (integer) - это класс, он говорит как ведут себя числа (целые).
# a = 5         a - это объект класса int

# Внутри класса есть атрибуты, которые делятся на Поля (значения) и Методы (функции)
# Ко всем атрибутам обращаемся через точку после объекта.

# Атрибуты могут быть общие, то есть принадлежать всему классу
# Либо атрибуты могут быть назначены конкретно для объекта, короче всё очень флексибл
# и класс - это как шаблон для всех объектов, но каждый объект можно ещё и переписывать как тебе удобно

...
# ----------------------------------------------------------------------------------------------------------------------
...

"""Создаём класс"""
# Задаём класс вот так вот
class Human:
    # всё, что после двоеточие это АТРБИТУТЫ класса

    species: str = "Homo sapiens"  # Это атрибут класса,
    # тут можно указать то, что будет общее для всех Human,
    # например их вид, всё-таки он вероятно у всех один будет

    chromosomes: int = 46

    # chromosomes: int
    # (через двоеточие после каждой создаваемой переменной
    # можно указать её тип, я для
    # удобства буду это делать)

    # Через def мы объявляем функции, внутри класса - это МЕТОДЫ (класса).
    def shout(self, what_to_shout: str = "ААААА"):
        #       Каждая функция может иметь на вход аргументы (self и
        # what_to_shout - это аргументы). У аргументов можно указывать
        # тип (: str) и дефолтное значение (= "AAAAA"), чему будет равен
        # аргумент если при вызове функции его не указать.

        #       Методы особенны тем, что имеют в себе всегда аргумент self
        # (его можно назвать иначе, это первый аргумент, по дефолту это self),
        # потому что по факту - методы, это просто функции, но которые
        # вызываются от "себя", то есть от какого-то объекта, который внутри
        # этой функции можно менять
        print(what_to_shout)
        return f"{self.species} shouted {what_to_shout}"    # Каждая функция что-то возвращает
                                                            # иногда это None, но здесь пусть
                                                            # будет строка.


...
# ----------------------------------------------------------------------------------------------------------------------
...

"""Тестим классы"""
...
if play == 1:
    anton = Human()
    danil = Human()
    print(f"anton: {anton.species},\t danil: {danil.species},\t Human: {Human.species}")
    print(f"anton: {anton.chromosomes},\t danil: {danil.chromosomes},\t Human: {Human.chromosomes}")

    anton.species = "Not Homo Sapiens"
    anton.chromosomes = 1000
    print('\nAfter anton.species = "Not Homo Sapiens"')
    print(f"anton: {anton.species},\t danil: {danil.species},\t Human: {Human.species}")
    print(f"anton: {anton.chromosomes},\t danil: {danil.chromosomes},\t Human: {Human.chromosomes}")

    Human.chromosomes -= 1
    print('\nAfter Human.chromosomes -= 1')
    print(f"anton: {anton.species},\t danil: {danil.species},\t Human: {Human.species}")
    print(f"anton: {anton.chromosomes},\t danil: {danil.chromosomes},\t Human: {Human.chromosomes}")

# Как видим, после изменений атрибутов у объекта anton, Human не унаследовал изменения,
# аналогично, Антону уже плевать какие атрибуты в Human, после того, как он поменял свои атрибуты,
# однако danil.species и Human.species - это буквально одна ячейка памяти, пока Данил не изменит свои
# атрибуты как Антон.

...
# ----------------------------------------------------------------------------------------------------------------------
...

# Теперь покричим (используем методы)
if play == 2:
    anton = Human()
    anton.shout() # self передаётся в shout автоматически от антона
    Human.shout(Human) # а если вызывать от класса, а не объекта,
    # то придётся указывать self вручную, притом Human.shout(anton) эквивалентен anton.shout()
    print('\n')
    print(anton.shout()) # выводим в консоль то, что возвращает метод
    print(Human.shout(Human))

    anton.species = "Not Homo Sapiens"
    print('\nAfter anton.species = "Not Homo Sapiens"')
    anton.shout()
    Human.shout(Human)
    print('\n')
    print(anton.shout())
    print(Human.shout(Human))

...
# ----------------------------------------------------------------------------------------------------------------------
...

# И ещё тест на понимание того как работают функции
if play == 3:
    anton = Human()
    other_variable = anton.shout
    print(f"anton.shout \t= {anton.shout}\nother_variable \t= {other_variable}")
    print()
    print(anton.shout())
    print()
    print(other_variable())

# Как видим, пока не поставим скобки после shout, shout является объектом метод.
# А когда ставим, то метод (или функция) выполняется.
# То есть и поля и методы - это просто переменные, к которым можно обратится через точку, и в этом плане они одинаковы.
# Просто в отличие от полей, методы callable (а значит к ним можно поставить скобки) и они "выполнятся"

...
# ----------------------------------------------------------------------------------------------------------------------
...

"""Перегрузка"""

# Теперь поговорим про перегрузку. Практически всё в питоне можно перегрузить - то есть
# насильно поменять значение любой переменной где угодно (даже важной, тип можно написать print = 1, и ты не сможешь
# больше писать print(123), потому что print станет единичкой).

# В рамках классов можно перегрузить атрибуты класса. То что мы делали в 1-м и 2-м тесте это тоже была своего рода
# перегрузка... однако, обычно перегрузкой называют всё-таки изменение функций

if play == 4:
    from types import MethodType

    anton = Human
    anton.species = "Anton Sapiens" # перегрузили переменную

    def new_shout_func(self, what_to_shout: str = 'aaa'):
        # Теперь кричим капсом
        print(what_to_shout.upper())
        return f"{self.species} shouted {what_to_shout} VERY LOUD"

    new_shout = MethodType(new_shout_func, anton) # ты вряд ли так будешь делать,
    # но чтобы перегрузить метод у объекта, нужно создать именно метод привязанный к объекту,
    # а не просто функцию. Есчо тебе это вряд ли будет нужно.
    print(
f'''Разница между функцией и методом, в том, что метод воспринимает 
первый аргумент как объект от которого вызывается функция:
new_shout_func: {new_shout_func}\nnew_shout: {new_shout}\nshout: {anton.shout}'''
    )
    anton.old_shout = MethodType(anton.shout, anton) # добавили атрибут объекту anton
    anton.shout = new_shout
    print(f"""\nanton.old_shout: {anton.old_shout}\nanton.shout: {anton.shout}""")
    print(anton.old_shout("before"))
    print(anton.shout("after"))

# Так к чему же этот тест. Здесь видно, что в объекте можно перегружать как поля, так и методы.

...
# ----------------------------------------------------------------------------------------------------------------------
...

"""Предустановленные методы"""
# Почему это важно? Потому что все классы имеют в себе заранее предустановленные методы.

if play == 5: # Мелкий тест, где все они перечислены

    class EmptyClass:
        pass # pass - это команда которая буквально ничего не делает

    empty_object = EmptyClass()
    print(empty_object.__dir__())

    for atr_name in empty_object.__dir__():
        exec(f"print(atr_name, '\\n', empty_object.{atr_name})") # еxeс чо функция exec выполняет передаваемую ему строку
        print("====================================================================================")

...
# ----------------------------------------------------------------------------------------------------------------------
...

"""Познаём dunder методы (__init__)"""

# Мы поняли, что внутри любого класса есть скрытые методы. Как ты мог заметить, все заранее установленные методы
# отмечены двумя нижними подчёркиваниями. Поэтому все такие методы называют dunder методами (double under), но ещё их
# иногда называют магическими.
# При этом мы знаем, что мы можем перегружать методы.
# Самый важный метод для перегрузки - это __init__ (от слова initialize). Он вызывается, когда мы инициализируем
# (присваиваем переменной новый класс) объект. Когда мы пишем anton = Human() вызывается Human.__init__(anton).
# Поиграемся с этой концепцией

class Human:
    species: str = "Homo sapiens"
    chromosomes: int = 46

    def __init__(self,
                 first_name: str,  # Не указав через '=' дефолтное состояние name,
                 # мы обязуем при создании объекта Human указывать хотя бы имя
                 last_name: str | None = None,  # указывая str | None мы говорим,
                 # что аргумент может быть типа str или типа None
                 age: int | None = None,  # Таким образом мы можем как указать, так и не указывать эти аргументы
                 number_of_chromosomes: int | None = None,
                 height: float | None = None,
                 interesting_facts: list = ["No interesting facts about this person"]
                 ):
        # Мы можем прямо в методе инициализации добавлять новые атрибуты создаваемому объекту

        self.name = first_name  # зачастую мы просто приравниваем атрибуты аргументам
        self.fullname = first_name
        self.age = age  # у аргумента могут быть с атрибутами одинаковые названия
        self.height = height
        self.about = interesting_facts

        if last_name is not None: # Если last_name указан, то добавим к фуллнейм фамилию
            self.fullname += f" {last_name}"
        if number_of_chromosomes is not None: # прямо в методе __init__ можно перегружать
            self.chromosomes = number_of_chromosomes # атрибуты класса для этого объекта

        self.surname = self.get_surname() # внутри __init__ можно сразу вызывать другие методы

    def get_surname(self): # часто методы нужны, чтобы достать инфу об объекте
        fullname_split_by_spaces = self.fullname.split()
        # Тут мы получаем фамилию разделив полное имя на две части (по
        # пробелу) и достав вторую часть (которая должна быть фамилией).
        if len(fullname_split_by_spaces) <= 1:
            return ''
        else:
            return fullname_split_by_spaces[1]


# Тестим
if play == 7:
    try:
        danil = Human()
    except Exception as tr:
        print(f"При danil = Human()\nвыводит ошибку {tr}\n")
    anton = Human("Антон")
    print("Данные Антона:")
    for i in anton.__dict__:
        print(f"\tanton.{i}  \t = {anton.__dict__[i]}")
    print()

    timur = Human("Тимур", "Губайдуллин", number_of_chromosomes=1618,
                  interesting_facts=["Крутой", "Любит Доктор Кто"])

    # данные можно задавать не по порядку, если ты хочешь чтобы необязательный аргумент был чему-то
    # равен, то можно просто написать {имя аргумента} = {значение}
    print("Данные Тимура:")
    for i in anton.__dict__:
        print(f"\ttimur.{i}  \t = {timur.__dict__[i]}")


...
# ----------------------------------------------------------------------------------------------------------------------
...

"""Операторы"""
# Подходим к следующей теме.
# a = 'abcde'. Объект a класса string имеет методы, например a.lower(). Однако помимо функций в Python есть операторы,
# это +, -, -=, +=, =, ==, |, |=, ^, **, ^= и тд.
# И вот сюрприз, ОПЕРАТОРЫ - ЭТО ТОЖЕ ФУНКЦИИ, а точнее методы. Например, a + b эквивалентно a.__add__(b).
# И раз мы умеем перегружать методы, то и операторы можем

# Полезные ссылки:
# все операторы: https://www.w3schools.com/python/python_operators.asp
# операторы с примерами: https://www.programiz.com/python-programming/operators
# операторы с дандер методами (ту мач инфо): https://www.pythonmorsels.com/every-dunder-method/
if play == 8: # Мелкий тест, где перечислены большинство

    def boldprint(text): # returns red and bold text
        print('\033[1m' + '\033[91m' + text + '\033[0m' + '\033[0m')

    'For ints'
    a, b = 10, -3
    print(f"\na = {a}, b = {b}")
    print(f"----------------------------Comparison----------------------------")
    boldprint(f"< and > \tis\t __lt__(self, other) and __gt__(self, other):") # less than, greater than
    print(f"a < b equivalent to a.__lt__(b) -> {a<b}")
    print(f"a > b equivalent to a.__gt__(b) -> {a>b}")
    print()

    boldprint(f"<= and >= \tis\t __le__(self, other) and __ge__(self, other):") # less or equals, greater or equals
    print(f"a <= b equivalent to a.__le__(b) -> {a<=b}")
    print(f"a >= b equivalent to a.__ge__(b) -> {a>=b}")
    print()

    boldprint(f"== and != \tis\t __eq__(self, other) and __ne__(self, other):") # equals, not equals
    print(f"a == b equivalent to a.__eq__(b) -> {a==b}")
    print(f"a != b equivalent to a.__ne__(b) -> {a!=b}")
    print()

    print(f"\n----------------------------Arithmetic----------------------------")
    boldprint(f"- and + \tis\t __neg__(self) and __pos__(self):")
    print(f"+a equivalent to a.__pos__() -> {+a}")
    print(f"-a equivalent to a.__neg__() -> {-a}")
    print()

    boldprint(f"- and + \tis\t __sub__(self, other) and __add__(self, other)")
    print(f"a+b equivalent to a.__add__(b) -> {a+b}")
    print(f"a-b equivalent to a.__sub__(b) -> {a-b}")
    print()

    boldprint(f"/ and * \tis\t __truediv__(self, other) and __mul__(self, other)")
    print(f"a*b equivalent to a.__mul__(b) -> {a*b}")
    print(f"a/b equivalent to a.__truediv__(b) -> {a/b}")
    print()

    boldprint(f"// and % \tis\t __floordiv__(self, other) and __mod__(self, other)")
    print(f"a//b equivalent to a.__floordiv__(b) -> {a//b}")
    print(f"a%b equivalent to a.__mod__(b) -> {a%b}")
    print()

    boldprint(f"** and @ \tis\t __pow__(self, other) and __matmul__(self, other)")
    print(f"a**b equivalent to a.__pow__(b) -> {a**b}")
    print(f"a@b equivalent to a.__matmul__(b) -> doesn't work for numbers (works in numpy matrices tho)")
    print()

    print(f"\n----------------------------Bitwise/Logical----------------------------")
    a = 10
    b = 13
    print(f"a and b in binary:\n\ta = {a} -> {bin(a)},\tb = {b} -> {bin(b)}")
    boldprint(f"~ \tis\t __invert__(self):")
    print(f"~a equivalent to a.__invert__(self) -> {~a}")
    print()

    boldprint(f"&, | and ^ \tis\t __and__(self, other), __or__(self, other) and __xor__(self, other)")
    print(f"a&b equivalent to a.__and__(b) -> {a&b} == {bin(a&b)}")
    print(f"a|b equivalent to a.__or__(b) -> {a|b} == {bin(a|b)}")
    print(f"a^b equivalent to a.__xor__(b) -> {a.__xor__(b)} == 0b0111")
    print()

    boldprint(f">> and << \tis\t __rshift__(self, other) and __lshift__(self, other)")
    print(f"a>>1 equivalent to a.__rshift__(1) -> {a>>1} == {bin(a>>1)}")
    print(f"a<<2 equivalent to a.__lshift__(2) -> {a<<2} == {bin(a<<2)}")
    print()

    print(f"\n----------------------------In-place----------------------------")
    print(f"""For arithmetic and logical (non unary) operations there are also in-place 
operations, like instead of a + b you can do a += b which adds b to the value a""")
    boldprint("+= \tis\t __iadd__(self, other) \nAND SO IS EVERY IN-PLACE OPERATOR (you just add i at the start)")
    print(f"a += b equivalent to a.__iadd__(b) -> a += b, a is now {a+b}")
    print('\n')

    '''For sets and arrays'''
    m = [0, 1, 2, 3]
    print(f"\nm is {m} (list)")
    print(f"----------------------------Containers----------------------------")

    boldprint(f"len(m), reversed(m) \tis\t m.__len__(self), m.__reversed__(self)")
    print(f"len(m) == {m.__len__()}, \nreversed(m) == {m.__reversed__()}")
    print()

    boldprint(f"m[key] is m.__getitem__(self, key); \tm[key] = value is m.__setitem__(self, key, value)")
    print(f"m[1] == {m.__getitem__(1)}")
    m.__setitem__(1, 13)
    print(f"m[1] = 13 \t->\t{m}")
    print()

    boldprint(f"a in m \tis\t m.__contains__(self, a)")
    print(f"4 in m -> True")
    print(f"600 in m -> False")
    print()
    # Также есть итераторы и тд, но про них отдельно если что

    pass

...
# ----------------------------------------------------------------------------------------------------------------------
...

"""Перегрузка операторов"""

# Теперь сделаем финальную версию Human с перегруженными операторами
# Полезные материалы:
# https://mathspp.com/blog/pydonts/overloading-arithmetic-operators-with-dunder-methods


class Human:
    species: str = "Homo sapiens"
    chromosomes: int = 46

    def __init__(
            self, first_name: str, last_name: str | None = None, age: int | None = None,
            number_of_chromosomes: int | None = None, height: float | None = None,
            interesting_facts: list = ['No interesting facts about this person'],
            ):
        self.name, self.fullname, self.age, self.height = first_name, first_name, age, height
        if last_name is not None: self.fullname += f" {last_name}"
        if number_of_chromosomes is not None: self.chromosomes = number_of_chromosomes
        self.surname, self.about = self.get_surname(), interesting_facts

    def get_surname(self):
        fullname_split_by_spaces = self.fullname.split()
        if len(fullname_split_by_spaces) <= 1: return ''
        else: return fullname_split_by_spaces[1]
    ...


    "self == other"
    # Будем считать, что люди эквивалентны, если между ними нет несоответствий, то есть разной фамилии, разного
    # имени или возраста (притом Антон 20 лет и Антон Муртазин 20 лет эквивалентны, также эквивалентны )
    def __eq__(self, other):
        d1 = self.__dict__
        d2 = other.__dict__
        for atr in d1:
            if atr == 'about':
                continue
            if atr == 'fullname' and d1[atr] != d2[atr]:
                return False
            if d1[atr] is None or d2[atr] is None:
                continue
            if d1[atr] != d2[atr]:
                return False
        return True


    "self != other"
    def __ne__(self, other):
        return not (self == other)


    "self[key]"
    def __getitem__(self, key: int | str | Human):
        if isinstance(key, Human):
            print("Здесь можно прописать какие взаимоотношения у {self} и {key}.")
            return ":)"
        if isinstance(key, str): # age Human[age] == Human.age
            return self.__dict__[key]
        if 0 <= key < len(self.about):
            return self.about[key]
        else:
            raise f"{self} does not have a fact with index {key}."


    "self[key] = val"
    def __setitem__(self, key, val):
        if isinstance(key, Human):
            print(
                "Здесь можно записать какие взаимоотношения у {self} и {key} при помощи val, а потом выводить их при self[key].")
            return "Отношения между {self} и {key} изменены"
        if isinstance(key, str):
            self[key] = val
            return self[key]
        if 0 <= key < len(self.about):
            tmp = self.about[key]
            self.about[key] = val
            return tmp
        else:
            raise f"{self} does not have a fact with index {key}."


    "self < other"
    def __lt__(self, other):
        if self.age is None or self.other is None:
            raise "{self} and {other} are incomlarable"
        return self.age < other.age

    "self > other"
    def __gt__(self, other):
        if self.age is None or self.other is None:
            raise "{self} and {other} are incomlarable"
        return self.age > other.age

    "self <= other"
    def __le__(self, other):
        if self.age is None or self.other is None:
            raise "{self} and {other} are incomlarable"
        return self.age <= other.age

    "self >= other"
    def __ge__(self, other):
        if self.age is None or self.other is None:
            raise "{self} and {other} are incomlarable"
        return self.age >= other.age


    "str(self)"
    def __str__(self):
        if self.age is None:
            return self.fullname
        else:
            return f"{self.fullname} ({self.age})"

    "len(self)"
    def __len__(self):
        return self.height


    "self + other"
    def __add__(self, other):
        return [self, other]



    "self.key = value"
    def __setattr__(self, key, value):
        if key in {'name', 'fullname', 'age', 'height', 'about', 'chromosomes', 'surname'}:
            self.__dict__[key] = value
            return
        raise BaseException("Read-only")

...
# Балуйся
if play == 9:
    anton = Human("Антон")
    anton.newatr = 2



