import webbrowser
from tkinter import Button, Tk

root = Tk( )

root.title('Meu software com Tkinter')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

def linkedin():
    webbrowser.open('https://www.linkedin.com/in/elizeu-barbosa-abreu-69965b218/')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
mylinkedin = Button(root, text='Abrir o Linkedin', command=linkedin).pack(pady=20)

root.mainloop()