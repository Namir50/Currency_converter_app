from currency_converter import CurrencyConverter
import tkinter as tk

window = tk.Tk()
window.geometry("500x360")
a = CurrencyConverter()

def clicked():
    am1 = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data = (a.convert(am1,cur1,cur2))
    l5 = tk.Label(window,text = data, font = "Times 17 bold").place(x = 120, y = 260)
    

t1 = tk.Label(window,text = "Currency Converter", font = "Times 20 bold").place(x = 120, y = 30)
t2 = tk.Label(window, text = "Enter amount: ",font = "Times 10 bold").place(x = 50,y=80)
e1 = tk.Entry(window).place(x = 175, y = 80)
t3 = tk.Label(window, text = "Enter Currency: ",font = "Times 10 bold").place(x = 50,y=130)
e2 = tk.Entry(window).place(x = 175, y = 130)
t3 = tk.Label(window, text = "Enter New Currency: ",font = "Times 10 bold").place(x = 50,y=180)
e3 = tk.Entry(window).place(x = 175, y = 180)
b1 = tk.Button(window).place(x = 120, y = 230).si

window.mainloop()
# 
# print