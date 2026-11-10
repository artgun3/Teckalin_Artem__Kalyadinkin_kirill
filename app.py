import random
import tkinter as tk

# Загадываем число сразу при старте
a = random.randint(1, 100)


def proverka():
    # Берем число из текстового поля и превращаем в int
    b = int(vvod.get())

    if a > b:
        otvet.config(text="БОЛЬШЕ")
    elif a < b:
        otvet.config(text="МЕНЬШЕ")
    else:
        otvet.config(text="ПОБЕДА")


def perezapusk():
    global a
    a = random.randint(1, 100)  # Загадываем новое число
    otvet.config(text="Новая игра началась!")  # Меняем текст
    vvod.delete(0, tk.END)  # Очищаем поле ввода


# Создаем обычное окно
okno = tk.Tk()
okno.title("Игра")
okno.geometry("200x300")

# Текст внутри окна
text = tk.Label(okno, text="Угадай число от 1 до 100:")
text.pack()

# Поле для ввода числа
vvod = tk.Entry(okno)
vvod.pack()

# Кнопка для проверки числа
knopka_proverit = tk.Button(okno, text="Проверить", command=proverka)
knopka_proverit.pack()

# Текст, который будет показывать БОЛЬШЕ/МЕНЬШЕ/ПОБЕДА
otvet = tk.Label(okno, text="")
otvet.pack()

# Кнопка для перезапуска
knopka_perezapusk = tk.Button(okno, text="Начать заново", command=perezapusk)
knopka_perezapusk.pack()

# Запуск окна
okno.mainloop()