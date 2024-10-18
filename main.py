import tkinter as tk
from tkinter import filedialog
import FileReader
import time
class BossBarApp:
    def __init__(self, master, file_path):
        self.running = True
        self.master = master
        master.title("Boss Bar")
        master.attributes('-topmost', True)

        # Frame to hold the boss bars
        self.boss_frame = tk.Frame(master)
        self.boss_frame.pack()
        
        self.fileReader = FileReader.FileReader(file_path)

        # Bind the window close event
        master.protocol("WM_DELETE_WINDOW", self.on_close)

        # Start the update loop
        self.update_boss_bars()

    def on_close(self):
        self.stop()  # Stop the update loop
        self.master.destroy()  # Close the window

    def stop(self):
        self.running = False
        self.fileReader.stop()

    def update_boss_bars(self):
        creatures = self.fileReader.getCreatures()

        # Clear existing boss bars
        for widget in self.boss_frame.winfo_children():
            widget.destroy()

        for creature in creatures:
            self.create_boss_bar(creature)

        # Schedule the next update
        if self.running:
            self.master.after(100, self.update_boss_bars)

    def create_boss_bar(self, creature: FileReader.Creature):
        # Create a label for the boss's name
        boss_name_label = tk.Label(self.boss_frame, text=creature.name, font=("Helvetica", 14))
        boss_name_label.pack()

        # Create a canvas for the health bar
        health_bar = tk.Canvas(self.boss_frame, width=300, height=30, bg="grey")
        health_bar.pack()

        # Calculate health percentage and draw the bar
        health_percentage = creature.getHpPercent()
        # print(health_percentage)
        if health_percentage > .50:
            health_bar.create_rectangle(0, 0, 300 * health_percentage, 30, fill="green")
        elif health_percentage > .25:
            health_bar.create_rectangle(0, 0, 300 * health_percentage, 30, fill="yellow")
        elif health_percentage > .02:
            health_bar.create_rectangle(0, 0, 300 * health_percentage, 30, fill="red")
        elif health_percentage > 0:
            health_bar.create_rectangle(0, 0, 300 * health_percentage, 30, fill="black")
        else:
            health_bar.create_text(150, 15, text="This Creature is Dead!", font=("Helvetica", 14))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    root = tk.Tk()
    app = BossBarApp(root, file_path)
    root.mainloop()