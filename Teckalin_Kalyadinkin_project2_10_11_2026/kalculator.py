import tkinter as tk

# Универсальная функция для добавления цифр и знаков в поле
def press_key(symbol):
    vvod.insert(tk.END, symbol)

# Функция для очистки поля (кнопка С)
def ochistit():
    vvod.delete(0, tk.END)

# Функция для подсчета (кнопка =)
def poschitat():
    try:
        primer = vvod.get() # Берем текст из поля
        otvet = eval(primer) # Считаем его
        vvod.delete(0, tk.END) # Стираем старое
        vvod.insert(0, str(otvet)) # Пишем ответ
    except Exception:
        vvod.delete(0, tk.END)
        vvod.insert(0, "Ошибка") # Если ввели что-то некорректное (например, 5++2)

# Создаем окно
okno = tk.Tk()
okno.title("Калькулятор")
okno.geometry("245x285")
okno.resizable(False, False) # Запрещаем менять размер окна, чтобы сетка не плыла

# Поле для ввода и вывода текста (растянуто на 4 столбца)
vvod = tk.Entry(okno, font=("Arial", 14), justify="right")
vvod.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Список кнопок в формате: (Текст кнопки, Номер строки, Номер столбца)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Создаем и размещаем кнопки с помощью цикла
for text, row, col in buttons:
    # Определяем, какую функцию должна вызывать кнопка
    if text == "C":
        cmd = ochistit
    elif text == "=":
        cmd = poschitat
    else:
        # lambda помогает передавать символ конкретной кнопки в общую функцию
        cmd = lambda x=text: press_key(x)
        
    # Создаем кнопку с фиксированной шириной и высотой для красивой квадратной формы
    btn = tk.Button(okno, text=text, width=5, height=2, font=("Arial", 12), command=cmd)
    # Размещаем в сетке grid
    btn.grid(row=row, column=col, padx=3, pady=3)

# Запуск приложения
okno.mainloop()