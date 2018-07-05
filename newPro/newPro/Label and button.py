import tkinter as tk
w = tk.Tk()               # 主窗口
w.title('My Window')    # 窗口标题
w.geometry('200x100')   # 窗口尺寸
var = tk.StringVar()     # 标签
l = tk.Label(w, textvariable=var, bg='pink', font=('Arial',12), width=15, height=12)
l.pack()
on_hit = False          # 按钮的响应事件
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('来打我啊')
    else:
        on_hit = False
        var.set('还真打啊')
b = tk.Button(w,text ='hit me',width = 5, height = 3, command = hit_me)   # 按钮
b.pack()
w.mainloop()   # 主事件循环








