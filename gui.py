from tkinter import *

root = Tk()


def send_message():
    send_txt = "User: " + e.get()
    text.insert(END, "\n" + send_txt)


def enter():
    send_message()


# root.geometry("600x700")
root.title("Cheer Up Chat bot")
root.resizable(0, 0)
text = Text(root)
text.grid(row=0, column=0,columnspan=2)
e=Entry(root, width=100)
send_button=Button(root, text="SEND", command=send_message).grid(row=1, column=1)
# send_button.bind('<Return>', enter)
e.grid(row=1, column=0)

# conversation = ["Welcome to Cheer Up Chat bot".center(85)]
# text.set("\n".join(conversation))

# label = tkinter.Label(root, textvariable=text, height=40, width=60, justify=tkinter.LEFT,
#                       anchor='nw', font={"family":"Arial Black", "size":20})
# label.grid(row=0, column=0)
# entry = tkinter.Entry(root, width=72)
# entry.grid(row=5, column=0)
#
#
# def read_message():
#     message = entry.get()
#     conversation.append("User: " + message)
#     text.set("\n".join(conversation))
#     label.update()
#
#
# button = tkinter.Button(root, text="SEND", command=read_message)
# button.grid(row=5, column=40)
root.configure(background='orange')
e.configure(background='orange')
text.configure(background='black', foreground='orange')
# label.configure(background='orange')

root.mainloop()

# import requests
# import tkinter
# import ast
#
# window=tkinter.Tk()
# window.geometry("650X800")
# window.title("Cheer Up Chat bot")
# window.resizable(0,0)
# text = tkinter.StringVar()
# conversation=["  Welcome to Cheer Up Chat bot   ".center(120)]
# text.set("\n".join(conversation))
#
# label = tkinter.Label(window, textVariable=text, height=40, width=60, justify=tkinter.LEFT,
#                       anchor='nw', font={"family":"Arial Black", "size":20})
# label.grid(row=0, column=0)
# entry=tkinter.Entry(window, width=72)
# entry.grid(row=5, column=0)
#
# def read_message():
#     message=entry.get()
#     conversation.append("User: " + message)
#     text.set("\n".join(conversation))
#     label.update()
#
# button=tkinter.Button(window, text="SEND", command=read_message)
# button.grid(row=5, column=40)
# window.configure(background='orange')
# label.configure(background='orange')
#
# window.mainloop()