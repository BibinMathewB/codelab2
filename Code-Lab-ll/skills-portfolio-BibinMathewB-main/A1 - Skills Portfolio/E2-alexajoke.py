import tkinter as tk
from tkinter import messagebox
import random

# Load jokes from a file
def load_jokes(filename):
    try:
        with open(filename, "r") as file:
            jokes = file.readlines()
        return [joke.strip() for joke in jokes if "?" in joke]
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' not found.")
        return []

# Display a new joke
def show_new_joke():
    if jokes:
        global current_joke
        current_joke = random.choice(jokes).split("?")
        joke_label.config(text=current_joke[0] + "?")
        punchline_button.config(state=tk.NORMAL)
        punchline_label.config(text="")
    else:
        joke_label.config(text="No jokes available.")

# show the punchline
def show_punchline():
    if current_joke:
        punchline_label.config(text=current_joke[1])
        punchline_button.config(state=tk.DISABLED)

# Quit the application
def quit_app():
    root.destroy()

# Load jokes
jokes = load_jokes("D:/Code-Lab-ll/skills-portfolio-BibinMathewB-main/A1 - Skills Portfolio/A1 - Resources/randomJokes.txt")  # Replace with the path to your jokes file
current_joke = None

#setup
root = tk.Tk()
root.title("Alexa Tell a Joke")

# Widgets
joke_label = tk.Label(root, text="Click 'A New Joke' to begin.", font=("Arial", 14), wraplength=400, pady=20, bg="yellow")
joke_label.pack()

punchline_label = tk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=400, fg="green", pady=10)
punchline_label.pack()

punchline_button = tk.Button(root, text="Show the joke", state=tk.DISABLED, command=show_punchline, bg="pink")
punchline_button.pack(pady=10)

new_joke_button = tk.Button(root, text="A New Joke", command=show_new_joke, bg="pink")
new_joke_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_app, bg="pink")
quit_button.pack(pady=10)

joke_label=tk.Label(root, bg="yellow")
joke_label.pack()


# Start the application
root.mainloop()
