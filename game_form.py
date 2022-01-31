import tkinter as tk
from tkinter import ttk


def save_entry():
    print(string_game_name.get())
    print(string_game_price.get())
    print(string_game_year.get())


# 1. Make a root window
root = tk.Tk()
root.title('Game Form')
root.geometry('320x220')

# 2. Make the main frame
root_frame = ttk.Frame(root)
root_frame.pack(fill=tk.BOTH, expand=True)

# 3. Make labels
ttk.Label(root_frame, text="Welcome To Game Form", justify='center').grid(column=2, row=1, pady=(10, 10), padx=(10, 10))
ttk.Label(root_frame, text=" Game Name:").grid(column=1, row=2, pady=(10, 10), padx=(10, 10))
ttk.Label(root_frame, text=" Price of Game:").grid(column=1, row=4, pady=(10, 10), padx=(10, 10))
ttk.Label(root_frame, text=" Game Made On:").grid(column=1, row=6, pady=(10, 10), padx=(10, 10))

# 4. Make input box
string_game_name = tk.StringVar()
ttk.Entry(root_frame, width=30, textvariable=string_game_name).grid(column=2, row=2, pady=(10, 10))

string_game_price = tk.StringVar()
ttk.Entry(root_frame, width=30, textvariable=string_game_price).grid(column=2, row=4, pady=(10, 10))

string_game_year = tk.StringVar()
ttk.Entry(root_frame, width=30, textvariable=string_game_year).grid(column=2, row=6, pady=(10, 10))

# 5. Make the Enter Button
ttk.Button(root_frame, text="ENTER", command=save_entry).grid(column=1, row=10, columnspan=2, pady=(10, 10))

root.mainloop()
