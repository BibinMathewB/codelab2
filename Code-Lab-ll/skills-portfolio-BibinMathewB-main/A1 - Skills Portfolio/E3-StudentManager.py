import tkinter as tk
from tkinter import messagebox, ttk

# Function to read student data from file
def load_student_data(file_path="skills-portfolio-BibinMathewB-main/A1 - Skills Portfolio/A1 - Resources/studentMarks.txt"):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        no_students = int(lines[0].strip())
        students = []
        for line in lines[1:]:
            student_id, name, mark1, mark2, mark3, exam = line.strip().split(',')
            total_coursework = int(mark1) + int(mark2) + int(mark3)
            total_marks = total_coursework + int(exam)
            percentage = (total_marks / 160) * 100
            if percentage >= 70:
                grade = 'a'
            elif percentage >= 60:
                grade = 'b'
            elif percentage >= 50:
                grade = 'c'
            elif percentage >= 40:
                grade = ''
            else:
                grade = 'f'
            students.append({
                "ID": student_id,
                "Name": name,
                "Total Coursework": total_coursework,
                "Exam Mark": int(exam),
                "Total Marks": total_marks,
                "Percentage": percentage,
                "Grade": grade
            })
        return students
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")
        return []

# Function to display all student records
def view_all_students():
    display_text = ""
    total_percentage = 0
    for student in student_data:
        display_text += (
            f"ID: {student['ID']}, Name: {student['Name']}, "
            f"Coursework: {student['Total Coursework']}, Exam: {student['Exam Mark']}, "
            f"Percentage: {student['Percentage']:.2f}%, Grade: {student['Grade']}\n"
        )
        total_percentage += student['Percentage']
    average_percentage = total_percentage / len(student_data)
    display_text += f"\nTotal Students: {len(student_data)}, Average Percentage: {average_percentage:.2f}%"
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, display_text)

# Function to view an individual student record
def view_individual_student():
    selected_name = student_combo.get()
    for student in student_data:
        if student['Name'] == selected_name:
            display_text = (
                f"ID: {student['ID']}, Name: {student['Name']}, "
                f"Coursework: {student['Total Coursework']}, Exam: {student['Exam Mark']}, "
                f"Percentage: {student['Percentage']:.2f}%, Grade: {student['Grade']}"
            )
            text_box.delete('1.0', tk.END)
            text_box.insert(tk.END, display_text)
            return
    messagebox.showinfo("Not Found", "No studen found.")

# Function to display the student with the highest marks
def show_highest():
    highest_student = max(student_data, key=lambda s: s["Total Marks"])
    display_text = (
        f"ID: {highest_student['ID']}, Name: {highest_student['Name']}, "
        f"Coursework: {highest_student['Total Coursework']}, Exam: {highest_student['Exam Mark']}, "
        f"Percentage: {highest_student['Percentage']:.2f}%, Grade: {highest_student['Grade']}"
    )
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, display_text)

# Function to display the student with the lowest marks
def show_lowest():
    lowest_student = min(student_data, key=lambda s: s["Total Marks"])
    display_text = (
        f"ID: {lowest_student['ID']}, Name: {lowest_student['Name']}, "
        f"Coursework: {lowest_student['Total Coursework']}, Exam: {lowest_student['Exam Mark']}, "
        f"Percentage: {lowest_student['Percentage']:.2f}%, Grade: {lowest_student['Grade']}"
    )
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, display_text)

# Load student data
student_data = load_student_data()

# Create main window
root = tk.Tk()
root.title("Student Manager")
root.configure(bg="lightblue")  # Light blue background

# Create frame for options
frame = tk.Frame(root, bg="lightblue")  # Frame with the same background color
frame.pack(pady=10)

# Add buttons
btn_view_all = tk.Button(frame, text="View All Students", command=view_all_students, bg="white")
btn_view_all.grid(row=0, column=0, padx=5)

btn_view_individual = tk.Button(frame, text="View Individual Student", command=view_individual_student, bg="white")
btn_view_individual.grid(row=0, column=1, padx=5)

btn_highest = tk.Button(frame, text="Highest Marks", command=show_highest, bg="white")
btn_highest.grid(row=0, column=2, padx=5)

btn_lowest = tk.Button(frame, text="Lowest Marks", command=show_lowest, bg="white")
btn_lowest.grid(row=0, column=3, padx=5)

# Dropdown menu for individual student
student_names = [student["Name"] for student in student_data]
student_combo = ttk.Combobox(frame, values=student_names, state="readonly")
student_combo.grid(row=1, column=1, columnspan=2, pady=10)

# Text box for output
text_box = tk.Text(root, height=15, width=80, bg="cyan")  # Alice blue for text box
text_box.pack(pady=10)

# Run the app
root.mainloop()
