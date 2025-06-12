import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
class App:
    def __init__(self,root):
        self.root = root
        self.root.title("todolist")
        self.root.geometry("450x450")
        self.root.resizable(width=False,height=False)
        self.root.configure(bg="#f0f4f8")
        
        self.listbox = tk.Listbox(root,width=50,height=15)
        self.listbox.place(x=75,y=100)
        
        self.entrybox = tk.Entry(root,width=30)
        self.entrybox.place(x=75,y=75)
        
        self.btn1 = tk.Button(root,text="add",width=11,height=1,background="#4caf50",foreground="white",command=self.add)
        self.btn1.place(x=290,y=70)
        
        self.btn2 = tk.Button(root,text="upload file",width=11,height=1,background="#4caf50",foreground="white",command=self.uploadfile)
        self.btn2.place(x=187,y=350)
        
        self.btn3 = tk.Button(root,text="delete",width=11,height=1,background="#4caf50",foreground="white",command=self.delete)
        self.btn3.place(x=290,y=350)
        
        self.btn4 = tk.Button(root,text="save",width=11,height=1,background="#4caf50",foreground="white",command=self.save)
        self.btn4.place(x=80,y=350)
        
    def add(self):
        task = self.entrybox.get()
        if task.strip():
            self.listbox.insert(tk.END,task)
            self.entrybox.delete(0,tk.END)
    
    def delete(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("warning","nothing selected")
    
    def save(self):
        tasks = self.listbox.get(0 , tk.END)
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text files","*.txt")])
        if filepath:
            with open(filepath,"w",encoding="utf-8") as f:
                for task in tasks:
                    f.write(task + "\n")
            messagebox.showinfo("saved","list was saved")
            
    def uploadfile(self):
        filepath = filedialog.askopenfilename(filetypes=[("text files","*.txt")])
        if filepath:
            with open(filepath,"r",encoding="utf-8") as f:
                for line in f:
                    task = line.strip()
                    if task:
                        self.listbox.insert(tk.END, task)
                        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()