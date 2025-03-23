import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Banking App")
        self.geometry("600x400")

        self.balance = 0.0
        self.scoreboard = {}
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        # Balance Display
        self.balance_label = ttk.Label(self, text="Balance: $0.00")
        self.balance_label.pack(pady=10)

        # Deposit/Withdraw
        self.amount_label = ttk.Label(self, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = ttk.Entry(self)
        self.amount_entry.pack()

        self.deposit_button = ttk.Button(self, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)
        self.withdraw_button = ttk.Button(self, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        # Scoreboard
        self.scoreboard_label = ttk.Label(self, text="Scoreboard:")
        self.scoreboard_label.pack(pady=10)
        self.scoreboard_text = tk.Text(self, height=5, width=30)
        self.scoreboard_text.pack()

        # Task List
        self.tasklist_label = ttk.Label(self, text="Task List:")
        self.tasklist_label.pack(pady=10)
        self.tasklist = tk.Listbox(self, height=5, width=30)
        self.tasklist.pack()

        # Add Task Button
        self.task_label = ttk.Label(self, text="Task:")
        self.task_label.pack()
        self.task_entry = ttk.Entry(self)
        self.task_entry.pack()
        self.add_task_button = ttk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Check Task Button
        self.check_task_button = ttk.Button(self, text="Check Task", command=self.check_task)
        self.check_task_button.pack(pady=5)

        # Add Player Button
        self.player_label = ttk.Label(self, text="Player Name:")
        self.player_label.pack()
        self.player_entry = ttk.Entry(self)
        self.player_entry.pack()
        self.add_player_button = ttk.Button(self, text="Add Player", command=self.add_player)
        self.add_player_button.pack(pady=5)

    def deposit(self):
     try:
        amount = float(self.amount_entry.get())
        if amount > 30:
            messagebox.showerror("Error", "Task is not worth this high of an amount. Please enter a lower amount.")
        elif amount > 0:
            self.balance += amount
            self.update_balance_label()
            self.amount_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a positive amount.")
     except ValueError:
        messagebox.showerror("Error", "Invalid amount.")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    self.update_balance_label()
                    self.amount_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Insufficient balance.")
            else:
                messagebox.showerror("Error", "Please enter a positive amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

    def update_balance_label(self):
        self.balance_label.config(text="Balance: ${:.2f}".format(self.balance))

    def add_player(self):
        player_name = self.player_entry.get()
        if player_name:
            self.scoreboard[player_name] = 0
            self.update_scoreboard()
            self.player_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a player name.")

    def update_scoreboard(self):
        self.scoreboard_text.delete("1.0", tk.END)
        for player, score in self.scoreboard.items():
            self.scoreboard_text.insert(tk.END, "{}: {}\n".format(player, score))

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasklist()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def check_task(self):
        try:
            index = self.tasklist.curselection()[0]
            self.tasks.pop(index)
            self.update_tasklist()
            self.add_points_to_scoreboard()
        except IndexError:
            messagebox.showerror("Error", "Please select a task to check.")

    def update_tasklist(self):
        self.tasklist.delete(0, tk.END)
        for task in self.tasks:
            self.tasklist.insert(tk.END, task)

    def add_points_to_scoreboard(self):
        for player in self.scoreboard:
            self.scoreboard[player] += 10
        self.update_scoreboard()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()