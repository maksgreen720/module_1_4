my_string=input("какое сейчас время года ") # Ответ: середина осени
m_1= " две тысячи двадцать четвертого года".upper()
print(my_string + m_1) # сложили время года и добавили год, год вывел оидельно в верхний регистр
m_s=my_string+m_1
print(len(m_s)) # вывел длинну всех символов
input("нажмите клавишу enter")
print(my_string.upper()) # вывел в верхний регистр
input("нажмите клавишу enter")
print(my_string.lower()) # вывел в нижний регистр
print(m_s.replace(' ', '')) #убрал пробелы
# метод .Litle не получается вывести выдает ошибку, возможно его нет в бесплатной версии
# выдает такой баг AttributeError: 'str' object has no attribute 'litle'. Did you mean: 'title'?
print(m_s .lower().split()) # поэтому вывел списком
print(m_s [0])  # вывел первый символ str
print(m_s [-1]) # вывел последний символ str
print(m_s [0:2] .upper()) # вывел первые два символа в верхнем регистре
print(m_s [-1] .upper()) # вывел последний символ в верхнем регистре
m_s1= m_s .replace('ДВЕ', "четыре") # заменил слово две на четыре
print(m_s1) # вывел с новым значением









