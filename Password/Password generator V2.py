import string
from tkinter import *
import hashlib
import os


def verify():
    verif = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for x in password_entry.get():
        for i in str(string.ascii_lowercase):
            if x == i:
                a = 1
        for h in str(string.ascii_uppercase):
            if x == h:
                b = 1
        for j in str(string.punctuation):
            if x == j:
                c = 1
        for k in str(string.digits):
            if x == k:
                e = 1
        d += 1
    if d >= 8 and d <= 20:
        if a == 1:
            if b == 1:
                if c == 1:
                    if e == 1:
                        label3.config(text="Mot de passe bon (vous pouvez le chiffrer)", bg="black", fg="green", font=("Courrier", 15))
                        verif = 1
                    else:
                        label3.config(text="Il manque un chiffre", bg="black", fg="green", font=("Courrier", 15))
                else:
                    label3.config(text="Il manque un symbole de ponctuation", bg="black", fg="green", font=("Courrier", 15))
            else:
                label3.config(text="Il manque une lettre majuscule", bg="black", fg="green", font=("Courrier", 15))
        else:
            label3.config(text="Il manque une lettre minuscule", bg="black", fg="green", font=("Courrier", 15))
    else:
        label3.config(text="Mot de passe trop court (8 char min)", bg="black", fg="green", font=("Courrier", 15))
    return verif


def clear():
    password_entry.delete(0, END)


def read():
    os.startfile("password.txt")


def encrypt_password(password):
    if verify() == 1:
        password_bytes = password.encode()
        sha256 = hashlib.sha256()
        sha256.update(password_bytes)
        encrypted_password = sha256.hexdigest()
        if check(encrypted_password) == True:
            write(encrypted_password)
            label3.config(text="Le mot de passe chiffré a été envoyé dans password.txt", bg="black", fg="green",
                          font=("Courrier", 15))
        else:
            label3.config(text="Le mot de passe existe déja", bg="black", fg="green",
                          font=("Courrier", 15))
    else:
        label3.config(text="Veuillez vérifier votre mot de passe", bg="black", fg="green",
                      font=("Courrier", 15))


def check(pw):
    result = True
    file = open('password.txt', "r")
    for line in file:
        if str(pw) == str(line.strip()):
            result = False
        else:
            result = 1
    return result


def write(password):
    file = open('password.txt', "a")
    file.write(f"{password}\n")
    file.close()


window = Tk()
window.title("Passeword generator")
window.geometry("710x400")
window.resizable(FALSE, FALSE)
window.config(background='black')

# bg
width = 720
height = 480
bg = PhotoImage(file="pngwing.png")
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

# title
label2 = Label( window, text = "Password generator", bg="black", fg="green", font=("Courrier", 30))
label2.pack(pady=40)

# frame

frame3 = Frame(window)
frame1 = Frame(window)
frame2 = Frame(window)


# entry
password_entry = Entry(frame3, font=("Courrier",15),width=19)
password_entry.place(x=0,y=0)
password_entry.grid(row=0, column=0, sticky=W)
# password verify

label3 = Label(window, text="", bg="black", fg="green")
label3.pack()

# button
button2 = Button(frame2,text="Chiffrer",bg="black",fg="green",font=("Courrier",15),command=lambda: encrypt_password(password_entry.get()))
button2.grid(row=0, column=1, sticky=W)

button3 = Button(frame2,text="Clear",bg="black",fg="green",font=("Courrier",15),command=clear)
button3.grid(row=0, column=2, sticky=W)

button4 = Button(frame2,text="Verify",bg="black",fg="green",font=("Courrier",15),command=verify)
button4.grid(row=0, column=0, sticky=W)

button5 = Button(window,text="Voir les precedents mdp",bg="black",fg="green",font=("Courrier",15),command=read)
button5.pack(side=BOTTOM,pady=3)

button1 = Button(frame1,text="Exit",bg="black" ,fg="green",font=("Courrier",15),command=exit)
button1.pack()

frame3.pack()
frame1.pack(side=BOTTOM, pady=10)
frame2.pack()


window.mainloop()
