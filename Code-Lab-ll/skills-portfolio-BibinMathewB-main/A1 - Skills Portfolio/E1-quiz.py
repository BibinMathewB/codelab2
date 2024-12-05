import tkinter as tk
from tkinter import messagebox
import random

#displaying the menu
def display_menu():
    menu_label.config(text="Choose A Difficulty Level:\n1. Easy\n2. Moderate\n3. Advanced", bg="blue", font="Italic")

def start_quiz():
    global difficulty_level, score, question_number
    
    #getting the user difficulty level
    try:
        difficulty_level = int(difficulty_input.get())
        if difficulty_level not in [1, 2, 3]:
            raise ValueError("Invalid level")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid difficulty level (1, 2, or 3).")
        return

    score = 0
    question_number = 1
    generate_question()

def generate_question():
    global num1, num2, operation, answer
    
    min_max = {
        1: (1, 9),
        2: (10, 99),
        3: (1000, 9999)
    }

    min_val, max_val = min_max[difficulty_level]
    num1 = random.randint(min_val, max_val)
    num2 = random.randint(min_val, max_val)
    operation = random.choice(['+', '-'])
    
    if operation == '+':
        answer = num1 + num2
    else:
        answer = num1 - num2

    question_label.config(text=f"Question {question_number}: {num1} {operation} {num2} = ?")
    user_answer_input.delete(0, tk.END)

def check_answer():
    global score, question_number

    try:
        user_answer = int(user_answer_input.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a numeric number answer.")
        return

    if user_answer == answer:
        if attempts_left.get() == 2:
            score += 10
        elif attempts_left.get() == 1:
            score += 5

        messagebox.showinfo("Correct!", "That's the correct answer!")
        next_question()
    else:
        attempts_left.set(attempts_left.get() - 1)
        if attempts_left.get() == 0:
            messagebox.showinfo("Out of attempts", f"The correct answer is {answer}.")
            next_question()
        else:
            messagebox.showerror("Incorrect", "Try again!")

def next_question():
    global question_number
    
    if question_number < 10:
        question_number += 1
        attempts_left.set(2)
        generate_question()
    else:
        display_results()

def display_results():
    grade = ""
    if score > 90:
        grade = "A+"
    elif score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"
    else:
        grade = "F"

    messagebox.showinfo("You completed the quiz!", f"Your total score is: {score}/100\nYour grade is: {grade}")
    play_again()

def play_again():
    if messagebox.askyesno("Play Again?", "Would you like to play again?"):
        display_menu()
    else:
        root.destroy()

# Tkinter window setup
root = tk.Tk()
root.title("Math Quiz")

menu_label = tk.Label(root, text="", font=("Helvetica", 14))
menu_label.pack(pady=10)

difficulty_input = tk.Entry(root)
difficulty_input.pack()

start_button = tk.Button(root, text="Start Quiz", command=start_quiz, bg="red")
start_button.pack(pady=10)

question_label = tk.Label(root, text="", font=("Helvetica", 14))
question_label.pack(pady=10)

user_answer_input = tk.Entry(root)
user_answer_input.pack()

submit_button = tk.Button(root, text="Submit Answer", command=check_answer,bg="red")
submit_button.pack(pady=10)

attempts_left = tk.IntVar(value=2)

#run the code/app
display_menu()
root.mainloop()
