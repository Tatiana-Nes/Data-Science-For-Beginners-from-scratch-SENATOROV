"""Введение в Python и CPython."""

# 1.  Что такое CPython и чем он отличается от Python?
#     CPython - это одна из реализаций языка программирования Python, написана на языке С, является интерпритатором.
# 3.  Сколько существует реализаций Python, и какая из них самая популярная?
#     6, CPython
# 4.  На каком языке написан CPython?
#     на языке С
#
# 5.  Кто создал CPython?
#     Guido van Rossum
# 6.  Почему Python считается быстрым, несмотря на то, что это интерпретируемый язык?
#     Потому что в реализации CPython написана на языке программирования С и вызывает инструкции из С
# 7.  Напишите путь к Интерпретатору CPython на вашем компьютере
#     /opt/miniconda3/bin/python
#
# 8.  Что содержится в папке include в CPython?
#     файлы С (.h)
# 9.  Где можно найти исходный код CPython дайте ссылку на репозиторий гитхаб
#     https://github.com/python/cpython
# 10. Как работает интерпретатор CPython при выполнении кода?
#     CPython сначала читает текст программы и превращает его в абстрактное синтаксическое дерево.
#     Которое компилируется в байт-код — последовательность инструкций для виртуальной машины.
#     Виртуальная машина пошагово читает каждую инструкцию и выполняет её через написанные на C функции.
#     Когда весь байт-код выполнен, программа завершается.
#
# 11. Какая команда используется для запуска файла с помощью CPython?
#     Запуск файла через CPython — это обычный запуск Python-программы;
#     В Windows файл с расширением .exe - исполняемая программа интерпретатора
#     В терминале можно ввести путь до интерпритатора, пробел и путь до файла
# 12. Можно ли запускать текстовые файлы через интерпретатор Python? Почему?
#     Да, потому что интерпретатору неважно какое расширение файлов.
# 13. Как указать путь к интерпретатору и файлу для выполнения кода?
#     Чтобы указать путь к интерпритатору нажимаем на файл .exe правой кнопкой мыши, выбираем Properties в открывшемся окне рядом с Location будет указан путь, также делаем при выборе пути для нужного файла
#
# 14. Чем PyPy отличается от CPython?
#     PyPy работает в 10 раз быстрее чем CPython, но он еще не совместим со всемит проектами на питоне
# 15. Почему PyPy не может использоваться для всех проектов на Python?
#     Этот интерпритатор реализован в RPython который представляет собой ограниченное статически типизированное подмножество языка программирования пайтон
# 16. Где можно скачать PyPy?
#     На сайте https://pypy.org
#
# 17. Как установить PyPy после скачивания?
#     Распоковать архив, перейди в папку PyPy, запустить интерпритатор
# 18. Как запустить файл с помощью PyPy?
#     Скопировать путь до интерпритатора PyPy (можно выбрать любой файл .exe);
#     В терминале вставить путь до интерпритатора, пробел и путь до файла
# 19. Почему PyPy выполняет код быстрее, чем CPython?
#     PyPy использует JIT-компилятор,который компилирует часто выполняемый код в машинный, а CPython работает как чистый интерпретатор байткода.
#
#
# ПРАКТИЧЕСКИЕ ЗАДАНИЯ
#
# 1) Проверьте, установлен ли CPython на вашем компьютере:
#    Используйте поиск в меню "Пуск" (Windows) или терминале (Linux/Mac).
#    Введите команду python --version или python3 --version в терминале.
#    Если CPython не установлен, скачайте его с официального сайта Python https://www.python.org/downloads/ и установите.
#
# python3 --version
# Python 3.13.5
# (base) tatananesterovic@Mac Data-Science-For-Beginners-from-scratch-SENATOROV %
#
#
# 2) Найдите папку, где установлен Python (например, через команду which python в терминале или свойства ярлыка).
#    Откройте папку include и изучите её содержимое. Какое количество файлов на C там есть?
#    Перейдите на [GitHub-репозиторий CPython](https://github.com/python/cpython) и найдите файл README. Прочитайте информацию о проекте.
#
# /opt/miniconda3/include/python3.13 #путь к папке на компьютере
#
# pen /opt/miniconda3/include/python3.13
# (base) tatananesterovic@Mac Data-Science-For-Beginners-from-scratch-SENATOROV %
# find /opt/miniconda3/include/python3.13 -type f -name "*.h" | wc -l
#      264 # 264 файла на С в папке include
# (base) tatananesterovic@Mac Data-Science-For-Beginners-from-scratch-SENATOROV %
#
#
# 3) Создайте текстовый файл example.txt с содержимым:
#    print("Hello from CPython!")
#    Запустите файл через команду python <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему файлу).
#    Проверьте, что выводится на экран. Попробуйте изменить расширение файла на .py и повторите запуск.
#
# printf 'print("Hello from CPython!")\n' > example.txt
# (base) tatananesterovic@Mac Data-Science-For-Beginners-from-scratch-SENATOROV %
# /opt/miniconda3/bin/python example.txt
# Hello from CPython!
# (base) tatananesterovic@Mac Data-Science-For-Beginners-from-scratch-SENATOROV %
#
#
# 4) Перейдите на [официальный сайт PyPy](https://www.pypy.org/) и скачайте подходящую версию для вашей операционной системы.
#    Распакуйте скачанный архив в удобное место.
#    Создайте файл example_pypy.py с кодом:
#    print("Hello from pypy!")
#    Запустите файл через PyPy
#    pypy <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему файлу).
#    Проверьте, что выводится на экран. Попробуйте изменить расширение файла на .py и повторите запуск.
#
# (base) tatananesterovic@Mac bin % printf 'print("Hello from pypy!")\n' > example_pypy.py
# ./pypy3 example_pypy.py
# Hello from pypy!
# (base) tatananesterovic@Mac bin %
#
#
# 5) Создайте файл performance_test.py с кодом:
#     import time
#     start_time = time.time()
#     total = 0
#     for i in range(1, 10000000):
#         total += i
#     end_time = time.time()
#     print("Result:", total)
#     print("Execution time:", end_time - start_time, "seconds")
#    Запустите этот файл сначала через CPython, а затем через PyPy. Запишите результаты времени выполнения для обоих интерпретаторов.
#    Сделайте вывод о разнице в производительности.
#
# /opt/miniconda3/bin/python /Users/tatananesterovic/Projects/GitHub/Data-Science-For-Beginners-from-scratch-SENATOROV/performance_test.py
# (base) tatananesterovic@Mac Data-Science-For-Beginners-from-scratch-SENATOROV % /opt/miniconda3/bin/python /Users/tatananesterovi
# c/Projects/GitHub/Data-Science-For-Beginners-from-scratch-SENATOROV/performance_test.py
# Result: 49999995000000
# Execution time: 0.42944788932800293 seconds
# (base) tatananesterovic@Mac Data-Science-For-Beginners-from-scratch-SENATOROV %
#
# /Users/tatananesterovic/Documents/pypy3.11-v7.3.20-macos_arm64/bin/pypy3 /Users/tatananesterovic/Projects/GitHub/Data-Science-For-Beginners-from-scratch-SENATOROV/performance_test.py
# (base) tatananesterovic@Mac Data-Science-For-Beginners-from-scratch-SENATOROV % /Users/tatananesterovic/Documents/pypy3.11-v7.3.2
# 0-macos_arm64/bin/pypy3 /Users/tatananesterovic/Projects/GitHub/Data-Science-For-Beginners-from-scratch-SENATOROV/performance_tes
# t.py
# Result: 49999995000000
# Execution time: 0.02052927017211914 seconds
# (base) tatananesterovic@Mac Data-Science-For-Beginners-from-scratch-SENATOROV %
#
#
# Результаты: запуск кода через PyPy в 21 раз быстрее, чем через CPython
#
#
#
#

#
