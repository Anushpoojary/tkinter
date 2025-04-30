import tkinter
import sqlite3
#connecting database
con=sqlite3.connect('sjec.db')
# con.execute("create table department12345(dept_id int,dept_name varchar(20))")
# con.execute("create table employee12345(emp_id int , name varchar(20), salary int, dep_no int references department(dept_id))")
# con.execute("INSERT INTO department12345 VALUES(1,'CSE'),(2,'ICBS'),(3,'ECE'),(4,'MECH'),(5,'EEE'),(6,'CIVIL')")
# con.execute("INSERT INTO employee12345 VALUES(101,'Anush',30000,1),(102,'Glen',20000,1),(103,'Adithya',15000,2),(104,'Thanish',25000,3),(105,'Yashwath',20000,5),(106,'Manish',20000,4),(107,'Sagar',15000,6)")
cur = con.cursor()

from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('LOGIN')
root.geometry('950x500')
root.config(bg='#fff')
root.resizable(False,False)

def signin():
    username=user.get()
    password=passd.get()

    if username=='Anush_poojary' and password=='poojary49':
        root.destroy()
        dtpage()
    
    elif username!='Anush poojary' and password!='poojary49':
        messagebox.showerror('INVALID','INVALID USERNAME AND PASSWORD')
    
    elif username=='Anush poojary' and password!='poojary49':
        messagebox.showerror('INVALID','INVALID PASSWORD')

    elif username!='Anush poojary' and password=='poojary49':
        messagebox.showerror('INVALID','INVALID USERNAME')
    
img=PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)
frame=Frame(root,width=400,height=400,bg='white')
frame.place(x=500,y=50)
heading=Label(frame,text="SIGN IN",fg='#57a1f8',bg='white',font=('Aerial',23,'bold'))
heading.place(x=150,y=5)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    user.get()

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Aerial',11))
user.place(x=80,y=80)
user.insert(0,'USER NAME')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=70,y=107)

def enter(y):
    passd.delete(0,'end')

def leave(y):
    name=passd.get()

passd=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Aerial',11))
passd.place(x=80,y=150)
passd.insert(0,'PASSWORD')
passd.bind('<FocusIn>',enter)
passd.bind('<FocusOut>',leave)

Frame(frame,width=295,height=2,bg='black').place(x=70,y=177)

Button(frame,width=39,pady=7,text='SIGN IN',bg='#57a1f8',fg='white',border=0,command=signin).place(x=80,y=204)
Label(frame,text="DON'T HAVE AN ACCOUNT ?",fg='black',bg='white',font=('Aerial',9)).place(x=110,y=270)

sign_up=Button(frame,width=6,text='SIGN UP',border=0,bg='white',cursor='hand2',fg='#57a1f8').place(x=280,y=270)

def savinfo():
    messagebox.showinfo('showinfo', 'Saved Successfully')

def savinfo1():
    messagebox.showinfo('showinfo', 'Deleted Successfully')

def savinfo2():
    messagebox.showinfo('showinfo', 'Updated Successfully')

def add_dept():
    add_d = Tk()
    add_d.title('Add Details(dept)')
    add_d.geometry('950x500')
    add_d.config(bg='#fff')
    add_d.resizable(False,False)

    id_d=Label(add_d,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER ID :',bg='#57a1f8',fg='black',border=2)
    id_d.place(x=280, y=50)
    name_d=Label(add_d,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER DEPARTMENT NAME :',bg='#57a1f8',fg='black',border=2)
    name_d.place(x=280, y=150)
    id_inp_d=Entry(add_d,width=25,fg='black',border=3,bg='silver')
    id_inp_d.place(x=380,y=110)
    name_inp_d=Entry(add_d,width=25,fg='black',border=3,bg='silver')
    name_inp_d.place(x=380,y=210)

    def save_dept():
        try:
            cur.execute("SELECT 1 FROM department12345 WHERE dept_id = ?", (id_inp_d.get(),))
            if cur.fetchone() is not None:
                messagebox.showerror('Error', "ID already exists!")
            else:
                cur.execute("INSERT INTO department12345(dept_id, dept_name) VALUES (?,?)", (id_inp_d.get(), name_inp_d.get()))
                con.commit()
                savinfo()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def cancel_dept():
        id_inp_d.delete(0, END)
        name_inp_d.delete(0, END)

    savbtn = Button(add_d,width=15,height=2,font=('Aerial',13,'bold'),text='SAVE',bg='#57a1f8',fg='black',border=0, command=save_dept)
    savbtn.place(x=200, y=420)
    candbtn = Button(add_d,width=15,height=2,font=('Aerial',13,'bold'),text='CLEAR',bg='#57a1f8',fg='black',border=0, command=cancel_dept)
    candbtn.place(x=400, y=420)
    backbtn = Button(add_d,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [add_d.destroy(), dept_page()])
    backbtn.place(x=600, y=420)

    add_d.mainloop() 

def delete_dept():
    del_d = Tk()
    del_d.title('Delete')
    del_d.geometry('950x500')
    del_d.config(bg='#fff')
    del_d.resizable(False,False)

    id_d=Label(del_d,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER DEPT_ID TO DELETE :',bg='#57a1f8',fg='black',border=2)
    id_d.place(x=280, y=50)
    id_inp_d=Entry(del_d,width=25,fg='black',border=3,bg='silver')
    id_inp_d.place(x=380,y=100)

    def save_dept():
        try:
            cur.execute("SELECT 1 FROM department12345 WHERE dept_id = ?", (id_inp_d.get(),))
            if cur.fetchone() is None:
                messagebox.showerror('Error', "ID not Found!")
            else:
                cur.execute("DELETE FROM department12345 WHERE dept_id = ?", (id_inp_d.get(),))
                con.commit()
                savinfo1()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def cancel_dept():
        id_inp_d.delete(0, END)

    savbtn = Button(del_d,width=15,height=2,font=('Aerial',13,'bold'),text='SAVE',bg='#57a1f8',fg='black',border=0, command=save_dept)
    savbtn.place(x=200, y=420)
    candbtn = Button(del_d,width=15,height=2,font=('Aerial',13,'bold'),text='CLEAR',bg='#57a1f8',fg='black',border=0, command=cancel_dept)
    candbtn.place(x=400, y=420)
    backbtn = Button(del_d,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [del_d.destroy(), dept_page()])
    backbtn.place(x=600, y=420)

    del_d.mainloop()

def update_dept():
    def ask_id():
        ask_id = Tk()
        ask_id.title('Ask ID (dept)')
        ask_id.geometry('950x500')
        ask_id.config(bg='#fff')
        ask_id.resizable(False,False)

        id_ask=Label(ask_id,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER DEPT_ID TO UPDATE :',bg='#57a1f8',fg='black',border=2)
        id_ask.place(x=280, y=50)
        id_ask_in=Entry(ask_id,width=25,fg='black',border=3,bg='silver')
        id_ask_in.place(x=380,y=100)

        def check(dept_id):
            cur.execute('SELECT 1 FROM department12345 WHERE dept_id = ?', (dept_id,))
            return cur.fetchone() is not None

        def proceed():
            dept_id = id_ask_in.get()
            if check(dept_id):
                ask_id.destroy()
                update_details(dept_id)
            else:
                messagebox.showerror('Error', 'ID not found in the database.')

        proceedbtn = Button(ask_id,width=15,height=2,font=('Aerial',13,'bold'),text='PROCEED',bg='#57a1f8',fg='black',border=0, command=proceed)
        proceedbtn.place(x=200, y=420)
        cancelbtn = Button(ask_id,width=15,height=2,font=('Aerial',13,'bold'),text='CLEAR',bg='#57a1f8',fg='black',border=0, command=ask_id.destroy)
        cancelbtn.place(x=400, y=420)
        backbtn = Button(ask_id,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [ask_id.destroy(), dept_page()])
        backbtn.place(x=600, y=420)

        ask_id.mainloop()

    def update_details(dept_id):
        update_d = Tk()
        update_d.title('Update Details (dept)')
        update_d.title('Delete')
        update_d.geometry('950x500')
        update_d.config(bg='#fff')
        update_d.resizable(False,False)

        name_d=Label(update_d,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER DEPTARTMENT NAME :',bg='#57a1f8',fg='black',border=2)
        name_d.place(x=280, y=50)
        name_inp=Entry(update_d,width=25,fg='black',border=3,bg='silver')
        name_inp.place(x=380,y=100)

        def save_dept():
            try:
                cur.execute("UPDATE department12345 SET dept_name = ? WHERE dept_id = ?", (name_inp.get(), dept_id))
                con.commit()
                savinfo2()
            except Exception as e:
                messagebox.showerror('Error', str(e))

        def cancel_dept():
            name_inp.delete(0, END)

        savbtn = Button(update_d,width=15,height=2,font=('Aerial',13,'bold'),text='SAVE',bg='#57a1f8',fg='black',border=0, command=save_dept)
        savbtn.place(x=200, y=420)
        candbtn = Button(update_d,width=15,height=2,font=('Aerial',13,'bold'),text='CLEAR',bg='#57a1f8',fg='black',border=0, command=cancel_dept)
        candbtn.place(x=400, y=420)
        backbtn = Button(update_d,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [update_d.destroy(), dept_page()])
        backbtn.place(x=600, y=420)

        update_d.mainloop()

    ask_id()

def dept_page():
    dept_page1= Tk()
    dept_page1.title('Department')
    dept_page1.geometry('950x500')
    dept_page1.config(bg='#fff')
    dept_page1.resizable(False,False)

    res = [('DEPT_ID', 'DEPT_NAME')]
    cur.execute("SELECT DEPT_ID,DEPT_NAME FROM department12345")
    res.extend(cur.fetchall())

    trows = len(res)
    tcolumns = len(res[0])
    table_frame = Frame(dept_page1, bg='#fff')
    table_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    class Table:
        def __init__(self, root):
            for i in range(trows):
                for j in range(tcolumns):
                    self.e = Entry(root, font=('Arial', 12))
                    self.e.grid(row=i, column=j, padx=5, pady=5)
                    self.e.insert(END, res[i][j])

    t = Table(table_frame)
 
    addbtn = Button(dept_page1,width=15,height=2,font=('Aerial',13,'bold'),text='ADD',bg='#57a1f8',fg='black',border=0,command=lambda: [dept_page1.destroy(),add_dept()])
    addbtn.place(x=80, y=420)
    delbtn = Button(dept_page1,width=15,height=2,font=('Aerial',13,'bold'),text='DELETE',bg='#57a1f8',fg='black',border=0, command=lambda: [dept_page1.destroy(),delete_dept()])
    delbtn.place(x=300, y=420)
    updbtn = Button(dept_page1,width=15,height=2,font=('Aerial',13,'bold'),text='UPDATE',bg='#57a1f8',fg='black',border=0,command=lambda: [dept_page1.destroy(),update_dept()])
    updbtn.place(x=500, y=420)
    backbtn = Button(dept_page1,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [dept_page1.destroy(), dtpage()])
    backbtn.place(x=715, y=420)

    dept_page1.mainloop()

def add_emp():
    add_e= Tk()
    add_e.title('Add Details(emp)')
    add_e.geometry('950x500')
    add_e.config(bg='#fff')
    add_e.resizable(False,False)

    id_e=Label(add_e,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER ID :',bg='#57a1f8',fg='black',border=2)
    id_e.place(x=280, y=10)
    name_e=Label(add_e,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER NAME :',bg='#57a1f8',fg='black',border=2)
    name_e.place(x=280, y=100)
    salary_e=Label(add_e,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER SALARY :',bg='#57a1f8',fg='black',border=2)
    salary_e.place(x=280, y=200)
    dept_no_e=Label(add_e,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER DEPARTMENT NO :',bg='#57a1f8',fg='black',border=2)
    dept_no_e.place(x=280, y=300)

    id_inp_e=Entry(add_e,width=25,fg='black',border=3,bg='silver')
    id_inp_e.place(x=380,y=60)
    name_inp_e=Entry(add_e,width=25,fg='black',border=3,bg='silver')
    name_inp_e.place(x=380,y=160)
    salary_inp_e=Entry(add_e,width=25,fg='black',border=3,bg='silver')
    salary_inp_e.place(x=380,y=260)
    dept_no_inpe=Entry(add_e,width=25,fg='black',border=3,bg='silver')
    dept_no_inpe.place(x=380,y=360)
    
    def save_emp():
        try:
            cur.execute("SELECT 1 FROM employee12345 WHERE emp_id = ?", (id_inp_e.get(),))
            if cur.fetchone() is not None:
                messagebox.showerror('Error', "ID already exists!")
            else:
                cur.execute("INSERT INTO employee12345(emp_id, name, salary, dep_no) VALUES (?,?,?,?)", (id_inp_e.get(), name_inp_e.get(), salary_inp_e.get(), dept_no_inpe.get()))
                con.commit()
                savinfo()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def cancel_emp():
        id_inp_e.delete(0, END)
        name_inp_e.delete(0, END)
        salary_inp_e.delete(0, END)
        dept_no_inpe.delete(0, END)

    savbtn = Button(add_e,width=15,height=2,font=('Aerial',13,'bold'),text='SAVE',bg='#57a1f8',fg='black',border=0, command=save_emp)
    savbtn.place(x=200, y=420)
    candbtn = Button(add_e,width=15,height=2,font=('Aerial',13,'bold'),text='CLEAR',bg='#57a1f8',fg='black',border=0, command=cancel_emp)
    candbtn.place(x=400, y=420)
    backbtn = Button(add_e,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [add_e.destroy(), emp_page()])
    backbtn.place(x=600, y=420)

    add_e.mainloop()

def update_emp():
    def ask_id():
        ask_id = Tk()
        ask_id.title('Ask ID (emp)')
        ask_id.geometry('950x500')
        ask_id.config(bg='#fff')
        ask_id.resizable(False,False)

        id_ask=Label(ask_id,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER ID :',bg='#57a1f8',fg='black',border=2)
        id_ask.place(x=280, y=50)
        id_ask_inp=Entry(ask_id,width=25,fg='black',border=3,bg='silver')
        id_ask_inp.place(x=380,y=100)

        def check(emp_id):
            cur.execute('SELECT 1 FROM employee12345 WHERE emp_id = ?', (emp_id,))
            return cur.fetchone() is not None

        def proceed():
            emp_id = id_ask_inp.get()
            if check(emp_id):
                ask_id.destroy()
                update_details(emp_id)
            else:
                messagebox.showerror('Error', 'ID not found in the database.')

        proceedbtn = Button(ask_id,width=15,height=2,font=('Aerial',13,'bold'),text='PROCEED',bg='#57a1f8',fg='black',border=0, command=proceed)
        proceedbtn.place(x=200, y=420)
        cancelbtn = Button(ask_id,width=15,height=2,font=('Aerial',13,'bold'),text='CLEAR',bg='#57a1f8',fg='black',border=0, command=ask_id.destroy)
        cancelbtn.place(x=400, y=420)
        backbtn = Button(ask_id,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [ask_id.destroy(), dept_page()])
        backbtn.place(x=600, y=420)

        ask_id.mainloop()

    def update_details(emp_id):
        update_e = Tk()
        update_e.title('Update Details (emp)')
        update_e .geometry('950x500')
        update_e .config(bg='#fff')
        update_e .resizable(False,False)

        name_e=Label(update_e,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER NAME :',bg='#57a1f8',fg='black',border=2)
        name_e.place(x=280, y=50)
        salary_e=Label(update_e,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER SALARY :',bg='#57a1f8',fg='black',border=2)
        salary_e.place(x=280, y=150)
        dept_e=Label(update_e,width=40,height=2,font=('Aerial',11,'bold'),text='ENTER DEPARTMENT :',bg='#57a1f8',fg='black',border=2)
        dept_e.place(x=280, y=250)

        name_inp=Entry(update_e ,width=25,fg='black',border=3,bg='silver')
        name_inp.place(x=380,y=100)
        salary_inp=Entry(update_e ,width=25,fg='black',border=3,bg='silver')
        salary_inp.place(x=380,y=200)
        dept_inp=Entry(update_e ,width=25,fg='black',border=3,bg='silver')
        dept_inp.place(x=380,y=300)

        def save_emp():
            try:
                cur.execute("UPDATE employee12345 SET name = ?, salary = ?, dep_no = ? WHERE emp_id = ?", (name_inp.get(), salary_inp.get(), dept_inp.get(), emp_id))
                con.commit()
                savinfo2()
            except Exception as e:
                messagebox.showerror('Error', str(e))

        def cancel_emp():
            name_inp.delete(0, END)
            salary_inp.delete(0, END)
            dept_inp.delete(0, END)

        savbtn = Button(update_e ,width=15,height=2,font=('Aerial',13,'bold'),text='SAVE',bg='#57a1f8',fg='black',border=0, command=save_emp)
        savbtn.place(x=200, y=420)
        candbtn = Button(update_e ,width=15,height=2,font=('Aerial',13,'bold'),text='CLEAR',bg='#57a1f8',fg='black',border=0, command=cancel_emp)
        candbtn.place(x=400, y=420)
        backbtn = Button(update_e ,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [update_e.destroy(), emp_page()])
        backbtn.place(x=600, y=420)

        update_e.mainloop()

    ask_id()

def delete_emp():
    del_e = Tk()
    del_e.title('Delete')
    del_e.geometry('950x500')
    del_e.config(bg='#fff')
    del_e.resizable(False,False)

    eid_e = Label(del_e, width=40, height=2, font=('Arial', 11, 'bold'),text='ENTER EMP_ID TO DELETE :', bg='#57a1f8', fg='black', border=2)
    eid_e.place(x=280, y=50)

    eid_inp_e = Entry(del_e, width=25, fg='black', border=3, bg='silver')
    eid_inp_e.place(x=380, y=100)
    def save_emp():
        try:
            cur.execute("SELECT 1 FROM employee12345 WHERE emp_id = ?", (eid_inp_e.get(),))
            if cur.fetchone() is None:
                messagebox.showerror('Error', "ID not Found!")
            else:
                cur.execute("DELETE FROM employee12345 WHERE emp_id = ?", (eid_inp_e.get(),))
                con.commit()
                savinfo1()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def cancel_emp():
        eid_inp_e.delete(0, END)

    savbtn = Button(del_e,width=15,height=2,font=('Aerial',13,'bold'),text='SAVE',bg='#57a1f8',fg='black',border=0, command=save_emp)
    savbtn.place(x=200, y=420)
    candbtn = Button(del_e,width=15,height=2,font=('Aerial',13,'bold'),text='CLEAR',bg='#57a1f8',fg='black',border=0, command=cancel_emp)
    candbtn.place(x=400, y=420)
    backbtn = Button(del_e,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [del_e.destroy(), emp_page()])
    backbtn.place(x=600, y=420)

    del_e.mainloop()


def emp_page():
    emp_page1= Tk()
    emp_page1.title('Employee')
    emp_page1.geometry('950x500')
    emp_page1.config(bg='#fff')
    emp_page1.resizable(False,False)

    res = [('EMP_ID', 'NAME', 'SALARY', 'DEP_NO')]
    cur.execute("SELECT emp_id, name, salary, dep_no FROM employee12345")
    res.extend(cur.fetchall())

    trows = len(res)
    tcolumns = len(res[0])

    table_frame = Frame(emp_page1, bg='#fff')
    table_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    class Table:
        def __init__(self, root):
            for i in range(trows):
                for j in range(tcolumns):
                    self.e = Entry(root, font=('Arial', 12))
                    self.e.grid(row=i, column=j, padx=5, pady=5)
                    self.e.insert(END, res[i][j])

    t = Table(table_frame)

    addbtn = Button(emp_page1,width=15,height=2,font=('Aerial',13,'bold'),text='ADD',bg='#57a1f8',fg='black',border=0,command=lambda: [emp_page1.destroy(),add_emp()])
    addbtn.place(x=80, y=420)
    delbtn = Button(emp_page1,width=15,height=2,font=('Aerial',13,'bold'),text='DELETE',bg='#57a1f8',fg='black',border=0,command=lambda: [emp_page1.destroy(),delete_emp()])
    delbtn.place(x=300, y=420)
    updbtn = Button(emp_page1,width=15,height=2,font=('Aerial',13,'bold'),text='UPDATE',bg='#57a1f8',fg='black',border=0, command=lambda: [emp_page1.destroy(),update_emp()])
    updbtn.place(x=500, y=420)
    backbtn = Button(emp_page1,width=15,height=2,font=('Aerial',13,'bold'),text='BACK',bg='#57a1f8',fg='black',border=0, command=lambda : [emp_page1.destroy(), dtpage()])
    backbtn.place(x=715, y=420)

    emp_page1.mainloop()


def dtpage():
    dt_root=Tk()
    dt_root.title('TABLE')
    dt_root.geometry('950x500')
    dt_root.config(bg='#fff')
    dt_root.resizable(False,False)

    deptxt=Label(dt_root,width=39,height=3,font=('Aerial',13,'bold'),text='DEPARTMENT DETAILS:',fg='black',border=2)
    deptxt.place(x=280, y=50)
    emptxt=Label(dt_root,width=39,height=3,font=('Aerial',13,'bold'),text='EMPLOYEE DETAILS:', fg='black',border=2)
    emptxt.place(x=280, y=290)
    deptbtn=Button(dt_root,width=39,height=3,font=('Aerial',13,'bold'),text='DEPARTMENT',bg='#57a1f8',fg='black',border=0,command=lambda: [dt_root.destroy(),dept_page()])
    deptbtn.place(x=280, y=130)
    empbtn=Button(dt_root,width=39,height=3,font=('Aerial',13,'bold'),text='EMPLOYEE',bg='#57a1f8',fg='black',border=0,command=lambda: [dt_root.destroy(),emp_page()])
    empbtn.place(x=280, y=370)

    dt_root.mainloop()
root.mainloop() 