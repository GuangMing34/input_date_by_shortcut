import keyboard
import datetime
import sys

# 定义快捷键为 Ctrl+Shift+D
hotkey = 'ctrl+shift+d'

# 定义快捷键的回调函数
def print_date():
    # 阻止快捷键的默认行为
    # e.preventDefault()
    # 获取当前日期并格式化
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    # 将日期粘贴到剪贴板
    keyboard.write(current_date, delay=0.05)
    sys.stdout.flush()
    # keyboard.send(current_date)

# 注册快捷键
keyboard.add_hotkey(hotkey, print_date)

# 程序持续运行
print("按 Ctrl+Shift+D 快捷键在任意文本框中输出当前日期。")
keyboard.wait('esc')  # 按 'esc' 键退出程序