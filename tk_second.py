import tkinter as tk


my_questions = [
    "Your name:",
]
counter = 0


def create_questionnaire(questions):
    root = tk.Toplevel(mainRoot)
    root.title("Анкета")

    def save_answers():
        global counter
        counter = counter + 1
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(str(counter) + "). Ответы на вопросы:\n")
            for idx, questionLoop in enumerate(questions):
                answer = answers[idx].get()
                file.write(f"    {counter}.{idx+1}) {questionLoop} {answer}\n")
        root.destroy()

    answers = []
    for question in questions:
        label = tk.Label(root, text=question)
        label.pack()
        answer_entry = tk.Entry(root)
        answer_entry.pack()
        answers.append(answer_entry)

    save_button = tk.Button(root, text="Сохранить ответы", command=save_answers)
    save_button.pack()


def add_question():
    root2 = tk.Toplevel(mainRoot)
    root2.geometry("200x200")
    root2.title("New question")
    label = tk.Label(root2, text="New question")
    label.pack()
    answer_entry = tk.Entry(root2)

    answer_entry.pack()

    def save_quest():
        my_questions.append(answer_entry.get())
        root2.destroy()

    save_button = tk.Button(root2, text="Сохранить", command=save_quest)
    save_button.pack()


def clear_file():
    file_path = "results.txt"
    try:
        open(file_path, "w").close()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Файл очищен")
    except FileNotFoundError:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Файл не найден")


def show_results():
    file_path = "results.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file_contents)
    except FileNotFoundError:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Файл не найден")


mainRoot = tk.Tk()
mainRoot.title("Цифровая анкета для студента")
mainRoot.geometry("500x500")
mainRoot.configure(bg="lightblue")
mainRoot.option_add("*Font", "Arial 10")

button_frame = tk.Frame(mainRoot)
button_frame.pack()

button_style = {'fg': 'black', 'font': ('Arial', 10)}
load_button = tk.Button(button_frame, text="Загрузить ответы", command=show_results)
load_button.config(**button_style)
load_button.pack(side=tk.LEFT, padx=5, pady=10)

clear_file_button = tk.Button(button_frame, text="Очистить", command=clear_file)
clear_file_button.config(**button_style)
clear_file_button.pack(side=tk.LEFT, padx=5, pady=10)

create_button1 = tk.Button(button_frame, text="Создать анкету", command=lambda: create_questionnaire(my_questions))
create_button1.config(**button_style)
create_button1.pack(side=tk.LEFT, padx=5, pady=10)

create_button2 = tk.Button(button_frame, text="Добавить вопрос", command=add_question)
create_button2.config(**button_style)
create_button2.pack(side=tk.LEFT, padx=5, pady=10)

text_area = tk.Text(mainRoot)
text_area.pack(padx=20, pady=10)

mainRoot.mainloop()

mainRoot.quit()

# Главное окно mainRoot
        # Создаем главное окно Tkinter с заголовком "Цифровая анкета для студента".
        # Устанавливает размеры окна 500x500 и цвет фона lightblue.
        # Создаем фрейм для размещения кнопок.
        # Создаем кнопки "Загрузить ответы", "Очистить", "Создать анкету" и "Добавить вопрос" внутри фрейма.
        # Настройки стиля (button_style) применяются ко всем кнопкам.


# create_questionnaire(questions)
        # Создаем окно Tkinter (Toplevel) с анкетой для ввода ответов на вопросы.
        # Отображает вопросы из списка questions и поля ввода для ответов на них.
        # При нажатии кнопки "Сохранить ответы" сохраняет ответы в файл results.txt.


# add_question()
        # Создаем новое диалоговое окно (Toplevel) для добавления нового вопроса.
        # Пользователь может ввести новый вопрос в поле ввода и сохранить его.
        # Новый вопрос добавляется в список my_questions.


# clear_file()
        # Очищает содержимое файла results.txt, если он существует.
        # Выводит сообщение в текстовое поле о том, что файл был очищен.


# show_results()
        # Отображает содержимое файла results.txt в текстовом поле.
        # Если файл не найден, выводит сообщение об ошибке.

