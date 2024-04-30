import os
import random
import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd

# List of attack types
attack_types = ["Syn", "TFTP", "DrDos_NTP", "UDP-lag", "DrDoS_DNS", "UDPLag", "MSSQL", "UDP", "Portmap", "NetBIOS", "DrDoS_UDP", "DrDoS_MSSQL", "LDAP", "WebDDoS", "DrDoS_SNMP", "DrDos_NetBIOS"]

# Placeholder prediction function
def make_predictions(data):
    predictions = []
    for row in data:
        if random.random() < 0.2:
            predictions.append(random.choice(attack_types))
        else:
            predictions.append('BENIGN')
    return predictions

# Function to load CSV file
def load_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path, low_memory=False)  # Set low_memory=False
        data = df.to_dict('records')
        populate_table(data)

# Function to populate the table
def populate_table(data):
    for row in tree.get_children():
        tree.delete(row)

    for i, row_data in enumerate(data):
        values = tuple(row_data.values())
        tree.insert("", "end", text=str(i), values=values)

    make_predictions_and_highlight(data)

# Function to make predictions and highlight attacks
def make_predictions_and_highlight(data):
    predictions = make_predictions(data)
    for i, prediction in enumerate(predictions):
        if prediction != "BENIGN":
            tree.item(tree.get_children()[i], tags=("attack",))
        else:
            tree.item(tree.get_children()[i], tags=())

# Create the main window
root = tk.Tk()
root.title("Dataset Viewer")

# Create a frame for the table
frame = ttk.Frame(root)
frame.pack(pady=10)

# Create a treeview (table) to display the dataset
tree = ttk.Treeview(frame)
tree["columns"] = ("Col 1", "Col 2", "Col 3", "Col 4", "Col 5", "Col 6", "Col 7", "Col 8", "Col 9","Prediction")
tree.heading("#0", text="Index")
tree.column("#0", width=50)

for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack()

# Create a style to highlight attacks
#style = ttk.Style()
#style.configure("attack.Treeview", background="red", foreground="white")
def highlight_attacks(label):
    if label in attack_labels:
        return 'background: yellow'
    else:
        return ''
    
attack_labels = {'Syn', 'TFTP', 'DrDos_NTP', 'UDP-lag', 'DrDoS_DNS', 'UDPLag', 'MSSQL', 'UDP', 'Portmap', 'NetBIOS', 'DrDoS_UDP', 'DrDoS_MSSQL', 'LDAP', 'WebDDoS', 'DrDoS_SNMP', 'DrDos_NetBIOS'}
    

# Function to highlight specified labels
def highlight_labels(df):
    highlight_colors = {label: 'yellow' for label in ['Syn', 'TFTP', 'DrDos_NTP', 'UDP-lag', 'DrDoS_DNS', 'UDPLag', 'MSSQL', 'UDP', 'Portmap', 'NetBIOS', 'DrDoS_UDP', 'DrDoS_MSSQL', 'LDAP', 'WebDDoS', 'DrDoS_SNMP', 'DrDos_NetBIOS']}

# Create a button to browse and load CSV file
button = ttk.Button(root, text="Browse CSV File", command=load_csv_file)
button.pack(pady=10)

# Start the main event loop
root.mainloop()



# Assuming you have a trained model object called 'model'
# and a function 'preprocess_data' to preprocess the data

def make_predictions(data):
    # Preprocess the data
    X = preprocess_data(data)

    # Make predictions using the model
    predictions = model.predict(X)
    

    # Map predictions to attack types
    label_mapping = {0: 'BENIGN', 1: 'Syn', 2: 'TFTP', 3: 'DrDos_NTP', 4: 'UDP-lag', 5: 'DrDoS_DNS', 6: 'UDPLag', 7: 'MSSQL', 8: 'UDP', 9: 'Portmap', 10: 'NetBIOS', 11: 'DrDoS_UDP', 12: 'DrDoS_MSSQL', 13: 'LDAP', 14: 'WebDDoS', 15: 'DrDoS_SNMP', 16: 'DrDos_NetBIOS'}
    predictions = [label_mapping[pred] for pred in predictions]

    return predictions

def make_predictions(label):
    if label in attack_labels:
        return 'background: yellow'
    else:
        return ''
    
attack_labels = {'Syn', 'TFTP', 'DrDos_NTP', 'UDP-lag', 'DrDoS_DNS', 'UDPLag', 'MSSQL', 'UDP', 'Portmap', 'NetBIOS', 'DrDoS_UDP', 'DrDoS_MSSQL', 'LDAP', 'WebDDoS', 'DrDoS_SNMP', 'DrDos_NetBIOS'}
    
    

    # Map predictions to attack types
    #label_mapping = {0: 'BENIGN', 1: 'Syn', 2: 'TFTP', 3: 'DrDos_NTP', 4: 'UDP-lag', 5: 'DrDoS_DNS', 6: 'UDPLag', 7: 'MSSQL', 8: 'UDP', 9: 'Portmap', 10: 'NetBIOS', 11: 'DrDoS_UDP', 12: 'DrDoS_MSSQL', 13: 'LDAP', 14: 'WebDDoS', 15: 'DrDoS_SNMP', 16: 'DrDos_NetBIOS'}
    #predictions = [label_mapping[pred] for pred in predictions]

    #return predictions


