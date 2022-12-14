import tkinter
import sqlite3
from tkinter import messagebox
def login():
    db=sqlite3.connect('login.sqlite')
    db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT,password TEXT')
    #db.execute("INSERT INTO login(username, password) VALUES('admin', 'admin')")
    db.execute("INSERT INTO login(username, password) VALUES('user', 'admin')")
    cursor=db.cursor()
    cursor.execute("SELECT * FROM login where username=? AND password=?" ,(userinput.get(), pass_input.get()))
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('info','login success')

    else:
        messagebox.showinfo('info','login failed')

main_window=tkinter.Tk()
main_window.title('Login App')
main_window.geometry('500 * 400')
padd=20
main_window['padx']=padd
user_input=tkinter.stringVar()
pass_input=tkinter.stringVar()
info_label=tkinter.Label(main_window,text='login Application')
info_label.grid(row=0,column=0,pady=20)

info_user=tkinter.label(main_window, text='Username')
info_user.grid(row=1, column=0)
userinput=tkinter.Entry(main_window, textvarible=user_input)
userinput.grid(row=1, column=1)

info_pass=tkinter.label(main_window, text='Password')
info_user.grid(row=2, column=0, pady=20)
passinput=tkinter.Entry(main_window, textvarible=pass_input)
passinput.grid(row=2, column=1)

login_btn=tkinter.Button(main_window,text='login', command=login)
login_btn.grid(row=2, column=1)

main_window.mainloop()



