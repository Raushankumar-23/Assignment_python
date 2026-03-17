import socket
import threading
from tkinter import *

connected = True

def receive():
    global connected
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if not message:
                break

            if message.lower() == "bye":
                listbox.insert(END, "Client disconnected")
                connected = False
                client.close()
                break

            listbox.insert(END, "Client: " + message)

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

    listbox.insert(END, "Server: " + message)

    try:
        client.send(message.encode("utf-8"))
    except:
        listbox.insert(END, "Send failed")
        connected = False
        return

    if message.lower() == "bye":
        connected = False
        client.close()
        root.quit()


def on_closing():
    global connected
    try:
        if connected:
            client.send("bye".encode("utf-8"))
            client.close()
    except:
        pass
    root.destroy()


# GUI
root = Tk()
root.title("Server Chat")

listbox = Listbox(root, width=50)
listbox.pack()

entry = Entry(root, width=40)
entry.pack(side=LEFT)

button = Button(root, text="Send", command=send)
button.pack(side=LEFT)

root.protocol("WM_DELETE_WINDOW", on_closing)

# Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 12345))
server.listen(1)

print("Waiting for client...")
client, addr = server.accept()
print("Connected:", addr)

threading.Thread(target=receive, daemon=True).start()

root.mainloop()