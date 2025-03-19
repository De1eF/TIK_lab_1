import tkinter as ttk
import math

CONST_BYTES_PER_CHARACTER = 2

def validate_input(new_value):
    return new_value == "" or new_value.isdigit()


#Window
m = ttk.Tk()
m.geometry(f"200x300")
m.title("Кількість інформації при імовірності")
m.resizable(False, False)

vcmd = m.register(validate_input)

#Page number entry
lbl_pgNum = ttk.Label(m, text="Кількість сторінок")
lbl_pgNum.pack()

ntr_pgNum = ttk.Entry(m, validate="key", validatecommand=(vcmd, "%P"))
ntr_pgNum.pack()

#Page number entry
lbl_rowNum = ttk.Label(m, text="Кількість рядків на сторінці")
lbl_rowNum.pack()

ntr_rowNum = ttk.Entry(m, validate="key", validatecommand=(vcmd, "%P"))
ntr_rowNum.pack()

#Page number entry
lbl_charNum = ttk.Label(m, text="Кількість символів у рядку")
lbl_charNum.pack()

ntr_charNum = ttk.Entry(m, validate="key", validatecommand=(vcmd, "%P"))
ntr_charNum.pack()

#Start button
btn_calc = ttk.Button(m, text="Запуск", command = lambda : calc())
btn_calc.pack()

#Result
lbl_res = ttk.Label(m, text="Результат")
lbl_res.pack()

ntr_res = ttk.Entry(m)
ntr_res.config(state="disabled")
ntr_res.pack()

def calc():
    ntr_res.config(state="normal")
    calcResult = int(ntr_pgNum.get()) * int(ntr_rowNum.get()) * int(ntr_charNum.get()) * CONST_BYTES_PER_CHARACTER
    ntr_res.delete(0, ttk.END)
    ntr_res.insert(0, calcResult)
    ntr_res.config(state="disabled")

m.mainloop()
