# ToDo application with GUI 
import tkinter as tk
from tkinter import messagebox
#creating class for adding all its features such as new entry,update, delete,mark as done etc
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Entry for new/update task
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Buttons available 
        tk.Button(root, text="Add Task", command=self.add_task).grid(row=0, column=2)
        tk.Button(root, text="Update Task", command=self.update_task).grid(row=1, column=0)
        tk.Button(root, text="Delete Task", command=self.delete_task).grid(row=1, column=1)
        tk.Button(root, text="Mark as Done", command=self.mark_done).grid(row=1, column=2)
        tk.Button(root, text="View All Tasks", command=self.view_tasks).grid(row=2, column=1)

        # Listbox for displaying tasks
        self.task_listbox = tk.Listbox(root, width=50, height=25)
        self.task_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"text": task, "done": False})
            self.task_entry.delete(0, tk.END)
            self.view_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            new_task = self.task_entry.get().strip()
            if new_task:
                index = selected[0]
                self.tasks[index]["text"] = new_task
                self.tasks[index]["done"] = False  # Reset "done" status on update
                self.task_entry.delete(0, tk.END)
                self.view_tasks()
            else:
                messagebox.showwarning("Input Error", "Enter a new task value.")
        else:
            messagebox.showwarning("Selection Error", "Select a task to update.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.view_tasks()
        else:
            messagebox.showwarning("Selection Error", "Select a task to delete.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = True
            self.view_tasks()
        else:
            messagebox.showwarning("Selection Error", "Select a task to mark as done.")

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task["text"]
            if task["done"]:
                text += " ✔️"
            self.task_listbox.insert(tk.END, text)

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
