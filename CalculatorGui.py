from tkinter import *
global f_num

root = Tk()
root.title('Simple Calculator')
root.iconbitmap('F:/icons/data.ico')
e = Entry(root, width=35)
e.grid(row=0, column=0, columnspan=4, padx=0, pady=10)


def button_click(number):
    get = e.get()
    e.delete(0, END)
    e.insert(0, get + number)


def button_clear():
    e.delete(0, END)


def button_math(math):
    global f_num
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)
    if math == '+':
        button_math.opt = 'Add'
    elif math == '-':
        button_math.opt = 'Sub'
    elif math == '*':
        button_math.opt = 'Mul'
    elif math == '/':
        button_math.opt = 'Div'


def button_equal():
    second_number = e.get()
    s_num = int(second_number)
    e.delete(0, END)
    if button_math.opt == 'Add':
        e.insert(0, f_num + s_num)
    elif button_math.opt == 'Sub':
        e.insert(0, f_num - s_num)
    elif button_math.opt == 'Mul':
        e.insert(0, f_num * s_num)
    elif button_math.opt == 'Div':
        e.insert(0, f_num / s_num)


number0 = Button(root, fg='white', bg='black', text='0', padx=30, pady=15, command=lambda: button_click("0"))
number1 = Button(root, fg='white', bg='black', text='1', padx=30, pady=15, command=lambda: button_click('1'))
number2 = Button(root, fg='white', bg='black', text='2', padx=30, pady=15, command=lambda: button_click('2'))
number3 = Button(root, fg='white', bg='black', text='3', padx=30, pady=15, command=lambda: button_click('3'))
number4 = Button(root, fg='white', bg='black', text='4', padx=30, pady=15, command=lambda: button_click('4'))
number5 = Button(root, fg='white', bg='black', text='5', padx=30, pady=15, command=lambda: button_click('5'))
number6 = Button(root, fg='white', bg='black', text='6', padx=30, pady=15, command=lambda: button_click('6'))
number7 = Button(root, fg='white', bg='black', text='7', padx=30, pady=15, command=lambda: button_click('7'))
number8 = Button(root, fg='white', bg='black', text='8', padx=30, pady=15, command=lambda: button_click('8'))
number9 = Button(root, fg='white', bg='black', text='9', padx=30, pady=15, command=lambda: button_click('9'))
addition = Button(root, fg='white', bg='black', text='+', padx=29, pady=15, command=lambda: button_math('+'))
subtraction = Button(root, fg='white', bg='black', text='-', padx=30, pady=15, command=lambda: button_math('-'))
multiplication = Button(root, fg='white', bg='black', text='*', padx=30, pady=15, command=lambda: button_math('*'))
division = Button(root, fg='white', bg='black', text='/', padx=30, pady=15, command=lambda: button_math('/'))
equal = Button(root, fg='white', bg='black', text='=', padx=30, pady=15, command=button_equal)
clear = Button(root, fg='white', bg='black', text='C', padx=29, pady=15, command=button_clear)

number7.grid(row=1, column=0)
number8.grid(row=1, column=1)
number9.grid(row=1, column=2)
division.grid(row=1, column=3)

number4.grid(row=2, column=0)
number5.grid(row=2, column=1)
number6.grid(row=2, column=2)
multiplication.grid(row=2, column=3)

number1.grid(row=3, column=0)
number2.grid(row=3, column=1)
number3.grid(row=3, column=2)
subtraction.grid(row=3, column=3)

clear.grid(row=4, column=0)
number0.grid(row=4, column=1)
equal.grid(row=4, column=2)
addition.grid(row=4, column=3)

root.mainloop()
