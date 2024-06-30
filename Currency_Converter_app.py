from currency_converter import CurrencyConverter
import tkinter as tk

window = tk.Tk()
window.geometry("500x360")
t1 = tk.Label(window,text = "Currency Converter", font = "Times 20 bold").place(x = 120, y = 30)
t2 = tk.Label(window, text = "Enter amount: ",font = "Times 10 bold").place(x = 50,y=80)
window.mainloop()
# a = CurrencyConverter()
# print(a.convert(12,"USD","INR"))