from currency_converter import CurrencyConverter
import tkinter as tk

window = tk.Tk()
window.geometry("500x360")
a = CurrencyConverter()

def clicked():
    am1 = int(e1.get())
    cur1 = e2.get().upper()
    cur2 = e3.get().upper()
    data = (a.convert(am1,cur1,cur2))
    l5 = tk.Label(window,text = data, font = "Times 17 bold").place(x = 120, y = 260)
    
t1 = tk.Label(window,text = "Currency Converter", font = "Times 22 bold").place(x = 120, y = 30)

t2 = tk.Label(window, text = "Enter amount: ",font = "Times 10 bold").place(x = 50,y=80)
e1 = tk.Entry(window)

t3 = tk.Label(window, text = "Enter current Currency: ",font = "Times 10 bold").place(x = 50,y=130)
e2 = tk.Entry(window)

t3 = tk.Label(window, text = "Enter New Currency: ",font = "Times 10 bold").place(x = 50,y=180)
e3 = tk.Entry(window)

b1 = tk.Button(window,text = "Convert",command = clicked).place(x = 200, y = 230)
e1.place(x = 190, y = 80)
e2.place(x = 190, y = 130)
e3.place(x = 190, y = 180)

window.mainloop()
