# def outer():
#     x = 10
#     def inner():
#         y = 20
#     inner()
#     return x + y

# my_func = outer

# print my_func()
##################################################################

import tkinter as tk

app = tk.Tk()
app.title("GUI App")
app.geometry("320x240")

label = tk.Label(
    app,
    font=("Helvetica", 16, "bold"),
)
label.pack()

def callback(text):
    def closure():
        label.config(text=text)

    return closure

button = tk.Button(
    app,
    text="Greet",
    command=callback("Hello, World!"),
)
button.pack()

app.mainloop()


##################################################################
# h1_tag = html_tag('h1')
# print h1_tag

# def html_tag(tag):
#     def print_tag(text):
#         return '<{0}>{1}</{0}>'.format(tag,text)
#     return print_tag

# h1_tag = html_tag('h1')
# print h1_tag('This is a headline!')


##################################################################

# from stack_v1 import Stack

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# stack.pop()
# # 3

# stack._items
# # [1, 2]

##################################################################

# class Stack:
#     def __init__(self):
#         self._items = []

#     def push(self, item):
#         self._items.append(item)

#     def pop(self):
#         return self._items.pop()

# def Stack():
#     _items = []

#     def push(item):
#         _items.append(item)

#     def pop():
#         return _items.pop()

#     def closure():
#         pass

#     closure.push = push
#     closure.pop = pop
#     return closure

##################################################################