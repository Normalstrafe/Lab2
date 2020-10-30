#Виведіть вбудовані константи, (2-3 на вибір)
print(False);
print(__debug__);
print(None);
# Виведіть результат роботи вбудованих функцій (2-3 на вибір)
print('         next:           ')
print(bool(1));
print(abs(-10));
print(divmod(7,5));
# Познайомтесь з циклами та розгалуженнями. Напишіть будь-який код який демонструє роботу циклу або розгалужень, (2-3 на вибір)
# 1
A=5;
print("A>5" if A>5 else  "A<=5");
# 2
B = "Python"
print("it`s snake" if B =="Python" else "It`s not snake");
# 3
C = 5 ; D = 10;
print("C + D =" , C+D);
print("          next:    ");
# Конструкція try->except->finally. У мові Python код не компілюється, а виконується відразу.
# Можливі помилки нам треба виловлювати самим. Напишіть свій варіант коду з помилкою.
A = "r";
try:
    print("Що буде якщо", 10/A, "?")
except Exception as e:
    print(e);
finally:
    print("А вот воно що!");
# Контекст-менеджер with. Можете почитати тут. Напишіть свій код з контекст-менеджером
with open('add tools.txt', 'w') as opened_file:
    opened_file.write('it`s work!!');
# Познайомтесь з Python lambdas. Напишіть свій приклад коду та як Ви розумієте Лямбди
import math
def SQRT(x):
    return math.sqrt(x)
SQR = lambda x: math.sqrt(x)
print(SQRT(25));