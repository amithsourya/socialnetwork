import tkinter as tk
from tkcalendar import Calendar, DateEntry
import mysql.connector
from tkinter import *
def follow(db, useridc, connectwin):
    temp = tk.Label(connectwin, text = "Following done!", )
    temp.place(x = 50, y = 50)
    useridc = useridc.get()
    valu = Username.get()
    query = "INSERT INTO FRIENDS VALUES (" + str(valu) + ", " + str(useridc) + ")"
    #cobj = db.cursor()
    db.cursor().execute(query)
    db.commit()
def connect(db):
    connectwin = tk.Toplevel(root)
    connectwin.geometry("300x300")
    connectwin.title("Connect")
    labeluserid = tk.Label(connectwin, text = "Enter userid: ", )
    labeluserid.place(x = 50, y = 20)
    useridc = tk.Entry(connectwin, width = 35)
    useridc.place(x = 150, y=20, width = 100)
    cnctbtn = tk.Button(connectwin, text="Connect", bg='orange', command = lambda: follow(db, useridc, connectwin))
    cnctbtn.place(x = 150, y = 135, width = 55)
    
def friends(db):
    friendswin = tk.Toplevel(root)
    friendswin.geometry("300x300")
    friendswin.title("Following")
    valu = Username.get()
    query = "SELECT FRIEND_ID FROM FRIENDS WHERE USER_ID = "+ valu
    cursorObject = db.cursor()
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    count = cursorObject.rowcount
    res = "People in your Following List are: \n"
    for x in myresult:
        nameretc = db.cursor()
        nameretc.execute("SELECT FIRST_NAME FROM USER WHERE USER_ID = "+ str(x[0]))
        nameret = nameretc.fetchall()
        print(nameret)
        if nameret is None:
            break
        nameret = nameret[0][0]
        res = res + nameret+ '\n'
    print(res)
    res += "Total Following count: " + str(count)
    lblfrstrow = tk.Label(friendswin, text =res, )
    lblfrstrow.place(x = 50, y = 20)
    cnctbtn = tk.Button(friendswin, text="Connect", bg='orange', command = lambda: connect(db))
    cnctbtn.place(x = 150, y = 180, width = 55)
    
def temp(db):
    query = "SELECT * FROM TEMP"
    cursorObject = db.cursor()
    cursorObject.execute(query)
      
    myresult = cursorObject.fetchall()
      
    for x in myresult:
        print(x)
    print("Printing done!!!")
def signupinsert(db, val1, val2):
    cursorObject = db.cursor()
    sql1 = "INSERT INTO User (user_id, first_name, last_name, DOB, age) VALUES (%s, %s, %s, %s, %s)"
    sql2 = "INSERT INTO AUTHENTICATE (user_id, password) VALUES (%s, %s)"
    val1  = (val1[0].get(), val1[1].get(), val1[2].get(), val1[3].get(), val1[4])
    val2 = (val2[0].get(), val2[1].get())
    print(val1)
    print(val2)
    cursorObject.execute(sql1, val1)
    cursorObject.execute(sql2, val2)
    db.commit()
    print("Inserted values!!!")
def signup(db):
    signupwin = tk.Toplevel(root)
    signupwin.geometry("300x300")
    signupwin.title("Signup Page")
    lblfrstrow = tk.Label(signupwin, text ="UserId -", )
    lblfrstrow.place(x = 50, y = 20)
    userid = tk.Entry(signupwin, width = 35)
    userid.place(x = 150, y = 20, width = 100)
    #######
    lblsecrow = tk.Label(signupwin, text ="Password -")
    lblsecrow.place(x = 50, y = 50)
    password = tk.Entry(signupwin, width = 35)
    password.place(x = 150, y = 50, width = 100)
    #######
    lblthdrow = tk.Label(signupwin, text ="FName -", )
    lblthdrow.place(x = 50, y = 80)
    fname = tk.Entry(signupwin, width = 35)
    fname.place(x = 150, y = 80, width = 100)
    #######
    lblfothrow = tk.Label(signupwin, text ="LName -")
    lblfothrow.place(x = 50, y = 110)
    lname = tk.Entry(signupwin, width = 35)
    lname.place(x = 150, y = 110, width = 100)
    #######
    lblfithrow = tk.Label(signupwin, text ="DOB -")
    lblfithrow.place(x = 50, y = 140)
    dob = DateEntry(signupwin, width= 16, background= "magenta3", foreground= "white",bd=2)
    dob.place(x = 50, y=140)
    #######
    val1 = (userid, fname, lname, dob, 20)
    val2 = (userid, password)
    signupbtndn = tk.Button(signupwin, text="Signup", bg='orange', command = lambda: signupinsert(db, val1, val2))
    signupbtndn.place(x = 150, y = 180, width = 55)
    
root = tk.Tk()
root.geometry("300x300")
root.title("Login Page")

db = mysql.connector.connect(host ="localhost", user='root', password='', db='PROJECT')
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login", bg ='yellow', command = lambda: friends(db))

submitbtn.place(x = 150, y = 135, width = 55)
signupbtn = tk.Button(root, text="Signup", bg='orange', command = lambda: signup(db))
signupbtn.place(x = 150, y = 175, width = 55)
root.mainloop()
