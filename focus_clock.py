import time
import tkinter as tk

def count_down(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timeformat)
        root.update()
        time.sleep(1)
        seconds -= 1

# 创建GUI窗口
root = tk.Tk()
root.title("专注时钟")
root.geometry("300x100")

# 显示倒计时时间
label = tk.Label(root, text="", font=("Helvetica", 48))
label.pack()

# 设置倒计时时长（单位：分钟）
minutes = 25

# 启动倒计时
count_down(minutes)

# 倒计时结束后，显示提示信息
label.config(text="时间到！")
root.update()
time.sleep(2)

# 关闭GUI窗口
root.destroy()
