import tkinter as tk
from tkinter import messagebox

class CricketScoringGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Scoring System")

        # Initialize teams
        self.team1 = {"name": "", "score": 0, "wickets": 0, "overs": 0.0}
        self.team2 = {"name": "", "score": 0, "wickets": 0, "overs": 0.0}
        self.current_team = self.team1  # Start with team1 batting

        # Input fields for team names
        tk.Label(root, text="Team 1 Name:").grid(row=0, column=0, padx=10, pady=5)
        self.team1_name_entry = tk.Entry(root, width=20)
        self.team1_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Team 2 Name:").grid(row=1, column=0, padx=10, pady=5)
        self.team2_name_entry = tk.Entry(root, width=20)
        self.team2_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(root, text="Set Teams", command=self.set_teams).grid(row=2, column=0, columnspan=2, pady=10)

        # Action buttons
        tk.Label(root, text="Actions:").grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Update Score", command=self.update_score_gui).grid(row=4, column=0, padx=10, pady=5)
        tk.Button(root, text="Update Wickets", command=self.update_wickets).grid(row=4, column=1, padx=10, pady=5)
        tk.Button(root, text="Switch Team", command=self.switch_team).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Display Score", command=self.display_score).grid(row=6, column=0, columnspan=2, pady=5)

        # Current Status Display
        self.status_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="center")
        self.status_label.grid(row=7, column=0, columnspan=2, pady=10)

    def set_teams(self):
        self.team1["name"] = self.team1_name_entry.get()
        self.team2["name"] = self.team2_name_entry.get()

        if not self.team1["name"] or not self.team2["name"]:
            messagebox.showwarning("Warning", "Please enter names for both teams!")
        else:
            self.current_team = self.team1
            self.update_status(f"Team names set! {self.team1['name']} will bat first.")

    def update_score_gui(self):
        score_window = tk.Toplevel(self.root)
        score_window.title("Update Score")

        tk.Label(score_window, text="Runs:").grid(row=0, column=0, padx=10, pady=5)
        runs_entry = tk.Entry(score_window)
        runs_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(score_window, text="Balls:").grid(row=1, column=0, padx=10, pady=5)
        balls_entry = tk.Entry(score_window)
        balls_entry.grid(row=1, column=1, padx=10, pady=5)

        def update_score_action():
            try:
                runs = int(runs_entry.get())
                balls = int(balls_entry.get())
                self.update_score(runs, balls)
                score_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers for runs and balls.")

        tk.Button(score_window, text="Update", command=update_score_action).grid(row=2, column=0, columnspan=2, pady=10)

    def update_score(self, runs, balls):
        self.current_team["score"] += runs
        self.current_team["overs"] += balls / 6
        if balls % 6 == 0:
            self.current_team["overs"] = round(self.current_team["overs"], 1)
        self.update_status("Score updated!")

    def update_wickets(self):
        if self.current_team["wickets"] < 10:
            self.current_team["wickets"] += 1
            self.update_status("Wicket added!")
        else:
            messagebox.showinfo("Info", "All wickets are already down!")

    def switch_team(self):
        self.current_team = self.team2 if self.current_team == self.team1 else self.team1
        self.update_status(f"Switched to {self.current_team['name']} for batting.")

    def display_score(self):
        score_text = (
            f"{self.team1['name']}: {self.team1['score']}/{self.team1['wickets']} in {self.team1['overs']} overs\n"
            f"{self.team2['name']}: {self.team2['score']}/{self.team2['wickets']} in {self.team2['overs']} overs"
        )
        messagebox.showinfo("Score", score_text)

    def update_status(self, text):
        self.status_label.config(text=text)

# Main program
root = tk.Tk()
app = CricketScoringGUI(root)
root.mainloop()
