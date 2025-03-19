import tkinter as ttk
import math

def validate_input(new_value):
    if new_value == "" or new_value.isdigit():
        return True
    if new_value.count('.') == 1 and new_value.replace('.', '').isdigit():
        return True
    return False


#Window
m = ttk.Tk()
m.geometry(f"200x300")
m.title("Кількість інформації при імовірності")
m.resizable(False, False)

#probability entry
vcmd = m.register(validate_input)
lbl_pgNum = ttk.Label(m, text="Імовірність")
lbl_pgNum.pack()

ntr_pgNum = ttk.Entry(m, validate="key", validatecommand=(vcmd, "%P"))
ntr_pgNum.pack()

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
    calcResult = math.log2(1/ float(ntr_pgNum.get()))
    ntr_res.delete(0, ttk.END)
    ntr_res.insert(0, calcResult)
    ntr_res.config(state="disabled")

m.mainloop()
