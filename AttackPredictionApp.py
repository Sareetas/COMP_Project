import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import random
from rf_wrapper import *

class AttackPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATTACK PREDICTION APPLICATION FOR DATASET")
        self.full_screen = False

        self.data = None
        self.predictions = None

        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the top buttons
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.X)

        # Load dataset button
        self.load_button = tk.Button(top_frame, text="Load Dataset", command=self.load_dataset)
        self.load_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Next dataset button
        self.next_button = tk.Button(top_frame, text="Next Dataset", command=self.load_dataset)
        self.next_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Predict attacks button
        self.predict_button = tk.Button(top_frame, text="Predict Attacks", command=self.predict_attacks)
        self.predict_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Full screen toggle button
        self.full_screen_button = tk.Button(top_frame, text="Full Screen", command=self.toggle_full_screen)
        self.full_screen_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create a frame for the table and scrollbars
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True)

        # Create the table (Text widget) and scrollbars
        self.table = tk.Text(table_frame, wrap="none")
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.v_scrollbar = tk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.table.yview)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.h_scrollbar = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.table.xview)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.table.config(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

    def toggle_full_screen(self):
        self.full_screen = not self.full_screen
        self.root.attributes("-fullscreen", self.full_screen)
        if not self.full_screen:
            self.root.geometry("800x600")  # Reset to default size when exiting full screen

    def load_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                self.display_data()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load dataset:\n{str(e)}")

    def display_data(self):
        self.table.delete(1.0, tk.END)
        self.table.insert(tk.END, self.data.to_string(index=False))

    def predict_attacks(self):
        if self.data is None:
            messagebox.showwarning("Warning", "Please load a dataset first.")
            return

        # Placeholder function to predict attacks
        self.predictions = {}
        for index, _ in self.data.iterrows():
            self.predictions[index] = random.choice(['Syn', 'TFTP', 'DrDos_NTP', 'UDP-lag', 'DrDoS_DNS', 'UDPLag', 'MSSQL', 'UDP', 'Portmap', 'NetBIOS', 'DrDoS_UDP', 'DrDoS_MSSQL', 'LDAP', 'WebDDoS', 'DrDoS_SNMP', 'DrDos_NetBIOS'])

        self.highlight_predictions()

    def highlight_predictions(self):
        self.table.tag_configure("attack", background="red")

        for index, prediction in self.predictions.items():
            if prediction in ['Syn', 'TFTP', 'DrDos_NTP', 'UDP-lag', 'DrDoS_DNS', 'UDPLag', 'MSSQL', 'UDP', 'Portmap', 'NetBIOS', 'DrDoS_UDP', 'DrDoS_MSSQL', 'LDAP', 'WebDDoS', 'DrDoS_SNMP', 'DrDos_NetBIOS']:
                start = f"{index + 1}.0"
                end = f"{index + 1}.end"
                self.table.tag_add("attack", start, end)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttackPredictionApp(root)
    root.mainloop()
