from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.messagebox as tm
import sqlite3
import smtplib, ssl
from email.mime.text import MIMEText
import os
import math, random
import time

def generateOTP() :
    global onetimepass
 
    string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@£#$%^&*()_-+=[{]}:;|'~`?!"
    OTP = ""
    length = len(string)
    for i in range(12) :
        OTP += string[math.floor(random.random() * length)]
    return OTP


if __name__ == "__main__" :
     
    onetimepass=generateOTP()
    print("Your one time password is", onetimepass)




def sendemail():
    global onetimepass
    global username
    global USERNAME
    global user_string
    #SMTP details needed to connect to mail server
    smtp_ssl_host = '****'
    smtp_ssl_port = 465
 #SMTP details  username and password  credentials replace *'s with appropriate credentials
    username1 = '****'
    password = '****'

    from_addr = ****'
    to_addrs = ((USERNAME.get()))

    message = MIMEText("Your OTP is:\n" + str(onetimepass))
    message['subject'] = 'One Time Password for QMUL project'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

#connects to server using SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

    server.login(username1, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()


root = Tk()
root.title("QMUL: Ryan Opoku New Login Protocol")
 
width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


#=======================================VARIABLES=====================================
USERNAME = StringVar()
MEMWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
EMAIL = StringVar()
user_string=USERNAME
#=======================================METHODS=======================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("qmulProject_db.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, memword TEXT, firstname TEXT, lastname TEXT)")




def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

     
def LoginForm():
    global LoginFrame, lbl_result1
    global username
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(LoginFrame, text="Email Address:", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_memword = Label(LoginFrame, text="Memorable Word:", font=('arial', 25), bd=18)
    lbl_memword.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    memword = Entry(LoginFrame, font=('arial', 20), textvariable=MEMWORD, width=15, show="*")
    memword.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', ToggleToRegister)
    

def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lbl_username = Label(RegisterFrame, text="Email Address:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_memword = Label(RegisterFrame, text="Memorable Word:", font=('arial', 18), bd=18)
    lbl_memword.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="First Name:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Last Name:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=5, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    memword = Entry(RegisterFrame, font=('arial', 20), textvariable=MEMWORD, width=15, show="*")
    memword.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
    btn_login.grid(row=7, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)

def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()

def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()

def Register():
    Database()
    if USERNAME.get == "" or MEMWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Unfortunately, that username has already been taken", fg="red")
        else:
            cursor.execute("INSERT INTO `member` (username, memword, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(MEMWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
            conn.commit()
            USERNAME.set("")
            MEMWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            EMAIL.set("")
            lbl_result2.config(text="You have successfully registered. Please login now.", fg="black")
        cursor.close()
        conn.close()


def onetimepassword():
    global username
    one_pass = Tk()
    one_pass.title("Generate One Time password")
    one_pass.configure(bg='purple')
    one_pass.geometry('650x500')

    generate_pass = Button (one_pass, text = "Generate OTP", height = 5, width = 30,bg="green",command=enter_pass)
    generate_pass.place(x = 70, y = 40)
    back_button = Button (one_pass, text="Exit", bg="green",
width=30, height=4, command=one_pass.destroy).place(x=200, y= 300)


def enter_pass():
     global onetimepass
     global enter_box
     global enter_main
     global username
     sendemail()
     print("One Time Password has been sent to your email. Please check all folders including junk!, and if you haven't received it, please retry to login again.")
     enter_main = Tk()
     enter_main.title('Enter Password')
     enter_main.geometry('399x390')
     enter_main.configure(bg='purple')


     enter_box = Entry(enter_main)
     enter_box.grid(row=2)

     enterpass = Label (enter_main, text = "Enter Your One Time Password:")
     enterpass.grid(row=1)

     enter_button = Button(enter_main, text = 'Login', bg="blue",
  width=10, height=2, command=entry)
     enter_button.grid(row=3, columnspan=2, pady=20)

     back_button = Button (enter_main, text="Exit", bg="green",
width=30, height=4, command=enter_main.destroy).grid(row=4, columnspan=2, pady=20)


def entry():
    global onetimepass
    global enter_box
    global enterpass
    if  enter_box.get() == onetimepass:
                 print ("Correct OTP!")
                 tm.showinfo("Welcome","You have successfully passed security!")
                 print ('OTP was: ' + enter_box.get())
                 balance_page()
    
def balance_page():
     balance = Tk()
     balance.title("Welcome!")
     balance.configure(bg='purple')
     balance.geometry('650x500')
     balance_label = Label(balance, text= "Hello, You have successfully authenticated and logged into my new Login and Authentication protocol!")
     balance_label.pack() 

     back_button = Button (balance, text="Exit", bg="green",
width=30, height=4, command=balance.destroy).place(x=200, y= 300)





def Login():
    global username
    Database()
    if USERNAME.get == "" or MEMWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `memword` = ?", (USERNAME.get(), MEMWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You've successfully logged in.", fg="blue")
            onetimepassword()
        else:
            lbl_result1.config(text="Invalid Username or memorable word", fg="red")
LoginForm()





#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
