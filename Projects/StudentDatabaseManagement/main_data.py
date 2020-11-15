from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview
import mysql.connector
import time

root = Tk()
root.title('Student Database Application')
root.config(bg='white')
root.geometry('1500x900+200+50')
root.iconbitmap('student.ico')
root.resizable(False, False)


####################ConnectDatabaseFunction##############
def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = pswdval.get()
        print(host, user, password)
        try:
            con = mysql.connector.connect(host=host, user=user,
                                          password=password,port = 3306)
            mycursor = con.cursor()
            print('Database Connected')
        except:
            messagebox.showerror('Notifications', 'Data is incorrect\nPlease Try Again')
            print('Database NOT Connected')
            return
        try:
            strr = 'create database StudentDatabaseSystem'
            mycursor.execute(strr)
            strr = 'use StudentDatabaseSystem'
            mycursor.execute(strr)
            strr = 'create table StudentData(id int,name varchar(20),mobile varchar(12),email varchar(25),address varchar(30),gender varchar(10),dob varchar(20),date varchar(20), time varchar(20))'
            mycursor.execute(strr)
            strr = 'alter table StudentData modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table StudentData modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Connected To The Student Database!', parent=dbroot)
            print('Student DataBase Created')
        except:
            strr = 'use StudentDatabaseSystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Connected To The Student Database!',parent=dbroot)
            print('StudentDatabase Updated')
        dbroot.destroy()


    dbroot = Toplevel()
    dbroot.title('Connect To Database')
    dbroot.grab_set()
    dbroot.geometry('470x300+800+230')
    dbroot.iconbitmap('database.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='white')

    # ---------Db Labels--------
    hostlabel = Label(dbroot, text='Enter Host :', bg='white',
                      font=('times', 18, 'bold'), width=10, anchor='n')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text='Enter User :', bg='white',
                      font=('times', 18, 'bold'), width=10, anchor='n')
    userlabel.place(x=10, y=70)

    pswdlabel = Label(dbroot, text='Enter\nPassword :', bg='white',
                      font=('times', 18, 'bold'), width=10, anchor='n')
    pswdlabel.place(x=10, y=130)

    # ---------Entry Boxes------- #
    hostval = StringVar()
    userval = StringVar()
    pswdval = StringVar()

    hostentry = Entry(dbroot, font=('times', 12, 'bold'), bd=3, textvariable=hostval)
    hostentry.place(x=235, y=15)
    userentry = Entry(dbroot, font=('times', 12, 'bold'), bd=3, textvariable=userval)
    userentry.place(x=235, y=75)
    pswdentry = Entry(dbroot, font=('times', 12, 'bold'), bd=3, textvariable=pswdval)
    pswdentry.place(x=235, y=170)

    # ---------SubmitButton-------
    submitbtn = Button(dbroot, text='Submit !', font=('times', 15, 'bold'), bg='white',
                       relief=RIDGE, borderwidth=3, bd=5,
                       width=12, activebackground='black', activeforeground='white',
                       command=submitdb)
    submitbtn.place(x=145, y=225)
    dbroot.mainloop()


####################TimeFunction#################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :' + date_string + '\nTime :' + time_string)
    clock.after(200, tick)


######################EntryButtonFunctions###########################
def addstudent():
    print('Student Added')

    def submitadd():
        print('added')

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x490+220+200')
    addroot.title('Student Database')
    addroot.config(bg='white')
    addroot.iconbitmap('student.ico')
    addroot.resizable(False, False)
    # -----------------------Add Student Labels---------------------
    idlabel = Label(addroot, text='Enter Id : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                    width=12, anchor='e')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                      width=12, anchor='e')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                        width=12, anchor='e')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                       width=12, anchor='e')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                         width=12, anchor='e')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                        width=12, anchor='e')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B. : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                     width=12, anchor='e')
    doblabel.place(x=10, y=370)

    # --------------------------Add Student Entry Boxes---------------------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    identry = Entry(addroot, font=('times', 12, 'bold'), bd=5, textvariable=idval)
    identry.place(x=230, y=10)

    nameentry = Entry(addroot, font=('times', 12, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=230, y=70)

    mobileentry = Entry(addroot, font=('times', 12, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=230, y=130)

    emailentry = Entry(addroot, font=('times', 12, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=230, y=190)

    addressentry = Entry(addroot, font=('times', 12, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=230, y=250)

    genderentry = Entry(addroot, font=('times', 12, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=230, y=310)

    dobentry = Entry(addroot, font=('times', 12, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=230, y=370)

    # -----------------------------Submit Button----------------------------------
    submitbtn = Button(addroot, text='Submit !', font=('times', 15, 'bold'), bg='white',
                       relief=RIDGE, borderwidth=3, bd=5,
                       width=12, activebackground='black', activeforeground='white',
                       command=submitadd)
    submitbtn.place(x=140, y=420)

    addroot.mainloop()


def searchstudent():
    print('Student Searched')

    def search():
        print('search')

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x550+220+200')
    searchroot.title('Student Database')
    searchroot.config(bg='white')
    searchroot.iconbitmap('student.ico')
    searchroot.resizable(False, False)
    # -----------------------Add Student Labels---------------------
    idlabel = Label(searchroot, text='Enter Id : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                    width=12, anchor='e')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                      width=12, anchor='e')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                        width=12, anchor='e')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                       width=12, anchor='e')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                         width=12, anchor='e')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                        width=12, anchor='e')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter D.O.B. : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                     width=12, anchor='e')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                      width=12, anchor='e')
    datelabel.place(x=10, y=430)

    # --------------------------Add Student Entry Boxes---------------------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    identry = Entry(searchroot, font=('times', 12, 'bold'), bd=5, textvariable=idval)
    identry.place(x=230, y=10)

    nameentry = Entry(searchroot, font=('times', 12, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=230, y=70)

    mobileentry = Entry(searchroot, font=('times', 12, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=230, y=130)

    emailentry = Entry(searchroot, font=('times', 12, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=230, y=190)

    addressentry = Entry(searchroot, font=('times', 12, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=230, y=250)

    genderentry = Entry(searchroot, font=('times', 12, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=230, y=310)

    dobentry = Entry(searchroot, font=('times', 12, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=230, y=370)

    dateentry = Entry(searchroot, font=('times', 12, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=230, y=430)

    # -----------------------------Submit Button----------------------------------
    submitbtn = Button(searchroot, text='Submit !', font=('times', 15, 'bold'), bg='white',
                       relief=RIDGE, borderwidth=3, bd=5,
                       width=12, activebackground='black', activeforeground='white',
                       command=search)
    submitbtn.place(x=140, y=480)

    searchroot.mainloop()


def deletestudent():
    print('Student Delete')


def updatestudent():
    print('Student Update')

    def update():
        print('update')

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x610+220+200')
    updateroot.title('Student Database')
    updateroot.config(bg='white')
    updateroot.iconbitmap('student.ico')
    updateroot.resizable(False, False)
    # -----------------------Add Student Labels---------------------
    idlabel = Label(updateroot, text='Enter Id : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                    width=12, anchor='e')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                      width=12, anchor='e')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                        width=12, anchor='e')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                       width=12, anchor='e')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                         width=12, anchor='e')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                        width=12, anchor='e')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter D.O.B. : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                     width=12, anchor='e')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                      width=12, anchor='e')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time : ', bg='white', font=('times', 18, 'bold'), borderwidth=3,
                      width=12, anchor='e')
    timelabel.place(x=10, y=490)

    # --------------------------Add Student Entry Boxes---------------------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    identry = Entry(updateroot, font=('times', 12, 'bold'), bd=5, textvariable=idval)
    identry.place(x=230, y=10)

    nameentry = Entry(updateroot, font=('times', 12, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=230, y=70)

    mobileentry = Entry(updateroot, font=('times', 12, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=230, y=130)

    emailentry = Entry(updateroot, font=('times', 12, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=230, y=190)

    addressentry = Entry(updateroot, font=('times', 12, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=230, y=250)

    genderentry = Entry(updateroot, font=('times', 12, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=230, y=310)

    dobentry = Entry(updateroot, font=('times', 12, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=230, y=370)

    dateentry = Entry(updateroot, font=('times', 12, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=230, y=430)

    timeentry = Entry(updateroot, font=('times', 12, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=230, y=490)

    # -----------------------------Submit Button----------------------------------
    submitbtn = Button(updateroot, text='Submit !', font=('times', 15, 'bold'), bg='white',
                       relief=RIDGE, borderwidth=3, bd=5,
                       width=12, activebackground='black', activeforeground='white',
                       command=update)
    submitbtn.place(x=140, y=540)

    updateroot.mainloop()


def showstudent():
    print('Student Show')


def exportstudent():
    print('Student Exported')


def exitstudent():
    print('Student Exit')
    res = messagebox.askyesno('Notification', 'Do You Want To Exit?')
    if res:
        root.destroy()


#####################frames######################
# ---------------------Entry Buttons-----------------------#
DataEntryFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=40, y=150, width=340, height=700)

addbtn = Button(DataEntryFrame, text='Add Student', font=('times', 15, 'bold'),
                bg='white', relief=RIDGE, borderwidth=3, bd=5,
                width=15, activebackground='black', activeforeground='white',
                command=addstudent)
addbtn.pack(side=TOP, expand=True)

searchbtn = Button(DataEntryFrame, text='Search Student', font=('times', 15, 'bold'),
                   bg='white', relief=RIDGE, borderwidth=3, bd=5,
                   width=15, activebackground='black', activeforeground='white',
                   command=searchstudent)
searchbtn.pack(side=TOP, expand=True)

deletebtn = Button(DataEntryFrame, text='Delete Student', font=('times', 15, 'bold'),
                   bg='white', relief=RIDGE, borderwidth=3, bd=5,
                   width=15, activebackground='black', activeforeground='white',
                   command=deletestudent)
deletebtn.pack(side=TOP, expand=True)

updatebtn = Button(DataEntryFrame, text='Update Student', font=('times', 15, 'bold'),
                   bg='white', relief=RIDGE, borderwidth=3, bd=5,
                   width=15, activebackground='black', activeforeground='white',
                   command=updatestudent)
updatebtn.pack(side=TOP, expand=True)

showbtn = Button(DataEntryFrame, text='Show All Students', font=('times', 15, 'bold'),
                 bg='white', relief=RIDGE, borderwidth=3, bd=5,
                 width=15, activebackground='black', activeforeground='white',
                 command=showstudent)
showbtn.pack(side=TOP, expand=True)

exportbtn = Button(DataEntryFrame, text='Export Student Data', font=('times', 15, 'bold'),
                   bg='white', relief=RIDGE, borderwidth=3, bd=5,
                   width=15, activebackground='black', activeforeground='white',
                   command=exportstudent)
exportbtn.pack(side=TOP, expand=True)

exitbtn = Button(DataEntryFrame, text='Exit Application', font=('times', 15, 'bold'),
                 bg='white', relief=RIDGE, borderwidth=3, bd=5,
                 width=15, activebackground='black', activeforeground='white',
                 command=exitstudent)
exitbtn.pack(side=TOP, expand=True)
# ----------------------Show------------------------#
ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=420, y=150, width=1020, height=700)

# -------------------------------Show Data frame------------------
style = ttk.Style()
style.configure('Treeview.Heading', font=('Times', 15, 'bold'))
style.configure('Treeview', font=('Times', 15, 'bold'), foreground='black', background='cyan')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable = Treeview(ShowDataFrame, columns=(
    'Id', 'Name', 'Mobile No.', 'Email', 'Address', 'Gender', 'D.O.B.', 'Added Date', 'Added Time'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile No.', text='Mobile No.')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B.', text='D.O.B.')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id', width=150)
studenttable.column('Name', width=300)
studenttable.column('Mobile No.', width=200)
studenttable.column('Email', width=250)
studenttable.column('Address', width=300)
studenttable.column('Gender', width=100)
studenttable.column('D.O.B.', width=200)
studenttable.column('Added Date', width=200)
studenttable.column('Added Time', width=200)
studenttable.pack(fill=BOTH, expand=1)

#####################Heading######################
SliderLabel = Label(root, text='Student Database System',
                    font=('TkHeadingFont', 32, 'italic bold'),
                    relief=SOLID, borderwidth=7, width=22, bg='white')
SliderLabel.place(x=295, y=10)
#####################clock#######################
clock = Label(root, font=('times', 15, 'bold'), bg='white')
clock.place(x=40, y=10)
tick()
#####################DatabeaseButton############
connectbtn = Button(root, text='Connect\nTo Database', width=23,
                    font=('TkHeadingFont', 15, 'italic bold'),
                    relief=RIDGE, borderwidth=4, bg='white',
                    activebackground='black', activeforeground='white',
                    command=Connectdb)
connectbtn.place(x=1080, y=10)

root.mainloop()
