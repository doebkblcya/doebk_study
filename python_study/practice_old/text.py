from tkinter import *
from tkinter import filedialog, messagebox

class Read_text():
    def __init__(self,title = '哦耶',geometry = '600x400'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometry)

        self.text_box = Text(self.root,wrap=WORD,)
        self.text_box.pack(fill=BOTH, expand=True,)

        self.open_button = Button(self.root, text="Open File", command=self.open_file)
        self.open_button.pack()

        self.root.mainloop()
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), 
                    ("Markdown Files", "*.md"), 
                    ("Log Files", "*.log"), 
                    ("All Files", "*.*")]
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                self.text_box.delete(1.0, END)
                self.text_box.insert(END, text)
        except Exception as e:
             messagebox.showerror("Error", f"无法打开文件:\n{e}")

if __name__ == '__main__':
    Read_text()
