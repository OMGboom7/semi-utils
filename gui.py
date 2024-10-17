import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("消息", "按钮被点击了！")

# 创建主窗口
root = tk.Tk()
root.title("我的第一个 GUI 应用")
root.geometry("300x200")  # 设置窗口大小

# 创建按钮
button = tk.Button(root, text="点击我", command=on_button_click)
button.pack(pady=20)  # 添加按钮并设置间距

# 进入主事件循环
root.mainloop()
