import socket
import threading
from tkinter import *

connected = True

def receive():
    global connected
    while True:
        try:
            message = s.recv(1024).decode("utf-8")

            if not message:
                break

            if message.lower() == "bye":
                listbox.insert(END, "Server disconnected")
                connected = False
                s.close()
                break

            listbox.insert(END, "Server: " + message)

        except:
            connected = False
            break


def send():
    global connected

    if not connected:
        listbox.insert(END, "Connection closed. Cannot send.")
        return

    message = entry.get()
    entry.delete(0, END)

    if message.strip() == "":
        return

    listbox.insert(END, "Client: " + message)

    try:
        s.send(message.encode("utf-8"))
    except:
        listbox.insert(END, "Send failed")
        connected = False
        return

    if message.lower() == "bye":
        connected = False
        s.close()
        root.quit()


def on_closing():
    global connected
    try:
        if connected:
            s.send("bye".encode("utf-8"))
            s.close()
    except:
        pass
    root.destroy()


# GUI
root = Tk()
root.title("Client Chat")

listbox = Listbox(root, width=50)
listbox.pack()

entry = Entry(root, width=40)
entry.pack(side=LEFT)

button = Button(root, text="Send", command=send)
button.pack(side=LEFT)

root.protocol("WM_DELETE_WINDOW", on_closing)

# Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 12345))

threading.Thread(target=receive, daemon=True).start()

root.mainloop()