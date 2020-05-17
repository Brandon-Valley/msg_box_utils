# import tkinter as tk
# from threading import Thread
#  
# class Temp_Msg_Box():
#     def __init__(self, title, msg):
# #         self.title = title
# #         self.msg   = msg
# #         
#         
# 
#         self.root = tk.Tk()
#         self.root.title(title)
#          
#         tk.Label(self.root, text = msg).pack()
#         
#         
#         
#     def show__with_timeout(self, timeout):
#         self.root.after(timeout * 1000, lambda: self.root.destroy())
#         self.root.mainloop()
#         
#         
#     def start__no_timeout(self):
# #         thread = Thread(target = self.root.mainloop)
# #         thread.start()
# #         thread.join()
# 
#         self.root.mainloop()
#         
#     def show_while__(self, func, show_while = True):
#         
#         
#         
#     def destroy(self):
#         self.root.destroy()
# 
# 
# def get_Temp_Msg_Box_after_starting_with_no_timeout(title, msg):
#     def get_Temp_Msg_Box_after_starting_with_no_timeout__threaded(title, msg):
#         TMB = Temp_Msg_Box(title, msg)
#         TM






# import tkinter as tk
# 
# root = tk.Tk()
# root.title("info")
# 
# tk.Label(root, text="This is a pop-up message").pack()
# 
# root.after(5000, lambda: root.destroy())     # time in ms
# 
# root.mainloop()



import time
import tkinter as tk
# from threading import Thread
import tkinter, time, threading

x = 0

def test_func():
    global x
    if x > 3:
        print('should end now')
        return False
    else:
        print('adding to x')
        x += 1
        
    


def show_temp_msg_box_until__(text, func, show_until = False):
    window = tkinter.Tk()#Tkinter.Toplevel() # or tkinter.Tk()
    # code before computation starts
    label = tkinter.Label(window, text = text)
    label.pack()
    done = []
    def call():
        result = func()
        
        while(result != show_until):
            result = func()
            
        done.append(result)

    thread = threading.Thread(target = call)
    thread.start() # start parallel computation
    while thread.is_alive():
        # code while computing
        window.update()
        time.sleep(0.001)
    # code when computation is done
    label['text'] = str(done)


# show_temp_msg_box_until__('waiting 2 seconds...', lambda: time.sleep(2))
show_temp_msg_box_until__('waiting 2 seconds...', test_func)




# 
# if __name__ == "__main__":
#     TMB = Temp_Msg_Box('this is title', 'this is msg')
# #     TMB.start__no_timeout()
# #      
# #     import time
# #     time.sleep(1)
# #     TMB.destroy()
# 
# 
#     thread = Thread(target = self.root.mainloop)
#     thread.start()
# 
# 
# #     TMB.start__with_timeout(3)