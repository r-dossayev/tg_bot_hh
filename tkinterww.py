from io import BytesIO
from tkinter import *
from urllib.request import urlopen
import base64
brush_size = 5
color = "black"


def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def brush_size_change(new_size):
    global brush_size
    brush_size = new_size


def color_change(new_color):
    global color
    color = new_color


def select(value):
    global brush_size
    brush_size = int(value)


root = Tk()
root.title("paint by Sabina")
root.geometry("1000x600")
root.resizable(False, False)

w = Canvas(root, width=1000, height=600, bg="white")

w.bind("<B1-Motion>", paint)

yellow_btn = Button(text="sary", width=10, bg="yellow", command=lambda: color_change("yellow"))
red_btn = Button(text="qyzyl", width=10, bg="red", command=lambda: color_change("red"))
pink_btn = Button(text="qyzgylt", width=10, bg="pink", command=lambda: color_change("pink"))
purple_btn = Button(text="kulgyn", width=10, bg="purple", command=lambda: color_change("purple"))
blue_btn = Button(text="kok", width=10, bg="blue", command=lambda: color_change("blue"))
green_btn = Button(text="zhasyl", width=10, bg="green", command=lambda: color_change("green"))


URL = "https://cdn-icons-png.flaticon.com/512/3635/3635122.png"
u = urlopen(URL)
raw_data = u.read()


print(raw_data)
b64_data = base64.encodestring(raw_data)

# photo = PhotoImage(file=BytesIO(raw_data))
# photo2 = photo.subsample(25, 25)
white_btn = Button(text="oshirgish", width=10, command=lambda: color_change("white"))

clear_btn = Button(text="tazalau", width=10, command=lambda: w.delete("all"), image=BytesIO(raw_data))

v = IntVar(value=10)
Scale(root, variable=v, orient=HORIZONTAL, from_=1, to=20, command=select).grid(row=1, column=2)

w.grid(row=6, column=0, columnspan=10, padx=2, pady=2, sticky=E + S + W + N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

Label(root, text="tuster:").grid(row=0, column=0)
Label(root, text="kalyndygy:").grid(row=1, column=0)

yellow_btn.grid(row=0, column=1)
red_btn.grid(row=0, column=2)
pink_btn.grid(row=0, column=3)
purple_btn.grid(row=0, column=4)
blue_btn.grid(row=0, column=5)
yellow_btn.grid(row=0, column=6)
green_btn.grid(row=0, column=7)
white_btn.grid(row=0, column=8)
clear_btn.grid(row=0, column=9)

root.mainloop()

# from tkinter import *
# from tkinter import ttk as enter
#
#
# def add():
#     new_language = language_entry.get()
#     language_entry.delete(0, END)
#     languages_listbox.insert(0, new_language)
#
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("300x250")
# root.columnconfigure(index=0, weight=4)
# root.columnconfigure(index=1, weight=1)
# root.rowconfigure(index=0, weight=1)
# root.rowconfigure(index=1, weight=3)
# root.rowconfigure(index=2, weight=1)
# menu = Menu(root)
# root.config(menu=menu)
#
# file_menu = Menu(menu)
# menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Quit", command=root.destroy)
#
# edit_menu = Menu(menu)
# menu.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Undo", command=add)
# edit_menu.add_command(label="Cut", command=add)
# edit_menu.add_command(label="Copy", command=add)
# edit_menu.add_command(label="Paste", command=add)
# language_entry = enter.Entry()
# language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
# enter.Button(text="Button", command=add).grid(column=1, row=0, padx=6, pady=6)
#
# languages_listbox = Listbox()
# languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
#
# Checkbutton1 = IntVar()
#
# Button1 = Checkbutton(root, text="Checkbox",
#                       variable=Checkbutton1,
#                       onvalue=1,
#                       offvalue=0,
#                       height=2,
#                       width=10)
#
# Button1.grid(row=2, column=0)
#
# python = "алғашқы әскери дайындық"
# java = "Еңбекке баулу"
# javascript = "Бейнелеу өнері"
#
# lang = StringVar(value=java)
#
# header = enter.Label(textvariable=lang)
# header.grid(row=3, column=0)
#
# python_btn = enter.Radiobutton(text=python, value=python, variable=lang)
# python_btn.grid(row=6, column=0)
#
# javascript_btn = enter.Radiobutton(text=javascript, value=javascript, variable=lang)
# javascript_btn.grid(row=4, column=0)
#
# java_btn = enter.Radiobutton(text=java, value=java, variable=lang)
# java_btn.grid(row=5, column=0)
#
# root.mainloop()
#
# # from tkinter import *
# #
# #
# # def undo():
# #     pass
# #
# #
# # def cut():
# #     pass
# #
# #
# # def copy():
# #     pass
# #
# #
# # def paste():
# #     pass
# #
# #
# # root = Tk()
# # root.title("Мысалдар")
# # root.geometry("500x500")
# #
# # # canvas = Canvas(root, width=800, height=600, bg="white")
# # # canvas.grid()
# # menu = Menu(root)
# # root.config(menu=menu)
# #
# # file_menu = Menu(menu)
# # menu.add_cascade(label="File", menu=file_menu)
# # file_menu.add_command(label="New")
# # file_menu.add_command(label="Open")
# # file_menu.add_separator()
# # file_menu.add_command(label="Quit", command=root.destroy)
# #
# # edit_menu = Menu(menu)
# # menu.add_cascade(label="Edit", menu=edit_menu)
# # edit_menu.add_command(label="Undo", command=undo)
# # edit_menu.add_command(label="Cut", command=cut)
# # edit_menu.add_command(label="Copy", command=copy)
# # edit_menu.add_command(label="Paste", command=paste)
# #
# #
# # # удаление выделенного элемента
# # def delete():
# #     selection = languages_listbox.curselection()
# #     # мы можем получить удаляемый элемент по индексу
# #     # selected_language = languages_listbox.get(selection[0])
# #     languages_listbox.delete(selection[0])
# #
# #
# # # добавление нового элемента
# # def add():
# #     new_language = language_entry.get()
# #     languages_listbox.insert(0, new_language)
# #
# #
# # root = Tk()
# # root.title("METANIT.COM")
# # root.geometry("300x250")
# # root.columnconfigure(index=0, weight=4)
# # root.columnconfigure(index=1, weight=1)
# # root.rowconfigure(index=0, weight=1)
# # root.rowconfigure(index=1, weight=3)
# # root.rowconfigure(index=2, weight=1)
# #
# # # текстовое поле и кнопка для добавления в список
# # language_entry = ttk.Entry()
# # language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
# # ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
# #
# # # создаем список
# # languages_listbox = Listbox()
# # languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
# #
# # # добавляем в список начальные элементы
# # languages_listbox.insert(END, "Python")
# # languages_listbox.insert(END, "C#")
# #
# # ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)
# #
# # root.mainloop()
# # root.mainloop()
#
# # # from tkinter import *
# # # from PIL import Image, ImageDraw
# # # from random import randint
# #
# # from tkinter import *
# #
# # root = Tk()
# # root.title("painttt")
# #
# # canvas = Canvas(root, width=800, height=600, bg="white")
# # canvas.grid()
# # canvas.pack()
# #
# #
# # def select_brush():
# #     canvas.config(cursor="cross")
# #
# #
# # def select_pencil():
# #     canvas.config(cursor="pencil")
# #
# #
# # def select_eraser():
# #     canvas.config(cursor="crosshair")
# #
# #
# # def start_drawing(event):
# #     canvas.create_oval(event.x, event.y, event.x, event.y, fill="black", outline="black")
# #
# #
# # def draw(event):
# #     canvas.create_oval(event.x, event.y, event.x, event.y, fill="black", outline="black")
# #
# #
# # def stop_drawing(event):
# #     pass
# #
# #
# # canvas.bind("<Motion>", start_drawing)
# # canvas.bind("<Motion>", draw)
# #
# #
# # # canvas.bind("<B1-Motion>", stop_drawing)
# # def clear_canvas():
# #     canvas.delete("all")
# #
# #
# # menu = Menu(tearoff=3)
# # root.config(menu=menu)
# # file_menu = Menu(menu)
# # menu.add_cascade(label="Файл", menu=file_menu)
# # menu.add_command(label="Очистить холст", command=clear_canvas)
# # root.mainloop()
# #
# # # from tkinter import colorchooser, messagebox
# # #
# # # def draw(event):
# # #     x1, y1 = (event.x - brush_size), (event.y - brush_size)
# # #     x2, y2 = (event.x + brush_size), (event.y + brush_size)
# # #     canvas.create_oval(x1, y1, x2, y2, fill=color, widht=0)
# # #     draw_img.ellipse(x1, y1, x2, y2, fill=color, widht=0)
# # #
# # # def chooseColor():
# # #     global color
# # #     (rgb, hx)= colorchooser.askcolor()
# # #     color=hx
# # #     color_lab["bg"]=hx
# # #
# # # def select(value):
# # #     global brush_size
# # #     brush_size= int(value)
# # #
# # # def pour():
# # #     canvas.delete("alt")
# # #     canvas["bg"]= color
# # #     draw_img.rectangle((0,0,1280, 720), width=0, fill=color)
# # #     draw_img.rectangle((0, 0, 1280, 720), width=0, fill=color)
# # #
# # # def clear_canvas():
# # #     canvas.delete("all")
# # #     canvas["bg"]="white"
# # #     draw_img.rectangle((0, 0, 1280, 720), width=0, fill=color)
# # #
# # # def save_img():
# # #     filename = f'image_{randint(0,10000)}.png'
# # #     image1.save(filename)
# # #     messagebox.showinfo("сохранение", "сохранено под название %s" % filename)
# # #
# # # def popup(event):
# # #     global x, y
# # #     x=event.x
# # #     y=event.y
# # #     menu.post(event.x_root, event.y_root)
# # #
# # # def square():
# # #     canvas.create_rectangle(x, y, x + brush_size, y + brush_size, fill=color, width=0)
# # #     draw_img.polygon((x, y, x + brush_size, y, x + brush_size, y + brush_size, x, y + brush_size), fill=color)
# # #
# # # def circle():
# # #     canvas.create_oval(x, y, x + brush_size, y + brush_size, fill=color, width=0)
# # #     draw_img.ellipse((x, y, x + brush_size, y + brush_size), fill=color)
# # #
# # #
# # #
# # # x=0
# # # y=0
# # #
# # # root = Tk()
# # # root.title("Paint")
# # # root.geometry("1280x720")
# # # root.resizable(0,0)
# # #
# # # brush_size = 10
# # # color = "black"
# # #
# # # root.columnconfigure(6, weight=1)
# # # root.rowconfigure(2,weight=1)
# # #
# # # canvas = Canvas(root, bg="white")
# # # canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)
# # #
# # # canvas.bind("<B1-Motion>",draw)
# # # canvas.bind("<Button-3>", popup)
# # #
# # # menu = Menu(tearoff=3)
# # # menu.add_command(label="квадрат", command=square)
# # # menu.add_command(label="круг", command=circle)
# # # image1=Image.new("RGB", (1280, 640), "white")
# # # draw_img = ImageDraw.Draw(image1)
# # #
# # # Label(root, text="параметры:").grid(row=0, column=0, padx=6)
# # #
# # # Button(root, text="выбрать цвет", width=11, command=chooseColor).grid(row=0, column=1, padx=6)
# # #
# # # color_lab = Label(root, bg=color, width=10)
# # # color_lab.grid(row=0, column=2, padx=6)
# # #
# # # v = IntVar(value=10)
# # # Scale(root, variable=v, from_=1, to=100, orient=HORIZONTAL, command=select).grid(row=0, column=3, padx=6)
# # #
# # # Label(root, text="действие:").grid(row=1, column=0, padx=6)
# # #
# # # Button(root, text="заливка", width=10, command=pour).grid(row=1, column=1)
# # #
# # # Button(root, text="очистить", width=10, command=clear_canvas).grid(row=1, column=2)
# # #
# # # Button(root, text="сохранить", width=10, command=save_img).grid(row=1, column=6)
# # #
# # # root.mainloop()
