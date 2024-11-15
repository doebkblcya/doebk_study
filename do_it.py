import tkinter as tk
from pathlib import Path

root = tk.Tk()
root.title('study and study')
root.geometry('500x400')

text_box = tk.Text(root,wrap=tk.WORD,width=60,height=20)
text_box.pack(fill=tk.BOTH, expand=True,)

path = Path('do_it.txt')

def open_file():
    try:
        content = path.read_text(encoding='utf-8')
        text_box.delete(1.0,tk.END)
        text_box.insert(tk.END,content)
    except Exception as e:
        text_box.delete(1.0,tk.END)
        text_box.insert(tk.END, f"Error: {e}")

open_file()
root.mainloop()