import tkinter as tk

class Watch():
    def __init__(self):
self.enter_ip = tk.Toplevel(self.window)
self.enter_ip.geometry('350x200')
self.enter_ip.title('ip&port')

new_ip = tk.StringVar()
new_ip.set('')
tk.Label(self.enter_ip, text='ip:').place(x=80, y=10)
entry_new_ip = tk.Entry(self.enter_ip, textvariable=new_ip)
entry_new_ip.place(x=150, y=10)

new_port = tk.StringVar()
tk.Label(self.enter_ip, text='port:').place(x=80, y=50)
entry_port = tk.Entry(self.enter_ip, textvariable=new_port, show='*')
entry_port.place(x=150, y=50)

btn_set = tk.Button(self.enter_ip, text='确定',
                    command=lambda: self.getPort(new_ip, new_port))
btn_set.place(x=160, y=130)