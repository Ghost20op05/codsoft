import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x600")

        self.listbox = tk.Listbox(root, width=40, height=20)
        self.listbox.pack(pady=10, padx=10)

        self.task_entry = tk.Entry(root, width=45)
        self.task_entry.pack(pady=5)

        # Consolidate button creation for task management and sorting
        button_specs = [
            ("Add a task", self.add_task),
            ("Remove a task", self.remove_task),
            ("Clear all the tasks", self.clear_tasks),
            ("Sort in ascending", lambda: self.sort_tasks(ascending=True)),
            ("Sort in descending", lambda: self.sort_tasks(ascending=False))
        ]
        for text, command in button_specs:
            tk.Button(root, text=text, command=command).pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task.")

    def remove_task(self):
        if selection := self.listbox.curselection():
            self.listbox.delete(selection[0])
        else:
            messagebox.showwarning("Warning", "Select a task.")

    def clear_tasks(self):
        self.listbox.delete(0, tk.END)

    def sort_tasks(self, ascending=True):
        tasks = sorted(self.listbox.get(0, tk.END), reverse=not ascending)
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, *tasks)

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            f.writelines(task + "\n" for task in self.listbox.get(0, tk.END))

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.listbox.insert(tk.END, *map(str.strip, f))
        except FileNotFoundError:
            pass

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()