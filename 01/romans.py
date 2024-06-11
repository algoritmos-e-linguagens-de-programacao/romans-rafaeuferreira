import tkinter as tk



def int_to_roman(num):

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    roman_num = ''

    for i in range(len(val)):

        while num >= val[i]:

            roman_num += syb[i]

            num -= val[i]

    return roman_num



def convert():

    num = int(entry.get())

    result.set(int_to_roman(num))



root = tk.Tk()

root.title("Calculadora de Números Romanos")



entry = tk.Entry(root)

entry.pack()



button = tk.Button(root, text="Converter", command=convert)

button.pack()



result = tk.StringVar()

label = tk.Label(root, textvariable=result)

label.pack()



root.mainloop()
