import tkinter as tk
 
class Temp_Msg_Box():
    def __init__(self, title, msg):
#         self.title = title
#         self.msg   = msg
#         
        

        self.root = tk.Tk()
        self.root.title(title)
         
        tk.Label(self.root, text = msg).pack()
        
    def start__no_timeout(self):
        self.root.mainloop()
        
    def destroy(self):
        self.root.destroy()
# 
# root.after(5000, lambda: root.destroy())     # time in ms
# 
# root.mainloop()


if __name__ == "__main__":
    TMB = Temp_Msg_Box('this is title', 'this is msg')
    TMB.start__no_timeout()
    
    import time
    time.sleep(1)
    TMB.destroy()