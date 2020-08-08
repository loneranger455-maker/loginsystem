from tkinter import ttk
from tkinter import *
from csv import DictReader,DictWriter
root=Tk()
class pujan:
    Yearv = IntVar()
    Monthv = StringVar()
    Namev = StringVar()
    Emailv=StringVar()
    Pass1v = StringVar()
    Pass2v = StringVar()
    Dayv = IntVar()
    info=StringVar()
    def submit(self,func1):
        bool1 =bool2=bool3=bool4=False
        if len(pujan.Namev.get())<3:
            p.name.focus()
            pujan.info.set("*Name must be at least 3 character long")
        elif pujan.Emailv.get()[-9:]!="gmail.com":
            p.Email.focus()
            pujan.info.set("*Invalid Email Format must be {}".format(pujan.Emailv.get()[-10:]))
        elif len(pujan.Pass1v.get())==0:
            p.pas1.focus()
            pujan.info.set("Please Enter a valid password")
        else:
            for i in pujan.Pass1v.get():
                if(i.isupper()):
                    bool1=True
                if (i.islower()):
                    bool2=True
                if i.isalpha()!=True:
                    if i.isdigit()==True:
                        bool3=True
            if len(pujan.Pass1v.get())<8 or (bool1==False or bool2==False or bool3==False):
                pujan.info.set("Password must contain at least 8 character with a digit a Capital\nand aSmall letter")
            elif pujan.Pass1v.get()!=pujan.Pass2v.get():
                pujan.info.set(f"password are not matching:{pujan.Pass1v} annd {pujan.Pass2v.get()}")
            else:
                kk=open("data.txt","r")
                dk=DictReader(kk)
                for a in dk:
                    if a['Name']==pujan.Namev.get():
                        pujan.info.set(f"Name {pujan.Namev.get()} is already taken")
                        bool4=True
                        break
                    elif a['Email']==pujan.Emailv.get():
                        pujan.info.set(
                            "Email is already registered..Please Signin")
                        bool4=True
                        break
                kk.close()
                if bool4==False:
                    pujan.save(self)
    def save(self):
        with open("data.txt","a") as file1:
            read1=DictWriter(file1,fieldnames=["Name","Email","BirthYear","BirthMonth","BirthDay","Password"])
            read1.writerow({"Name":pujan.Namev.get(),"Email":pujan.Emailv.get(),"BirthYear":pujan.Yearv.get(),"BirthMonth":pujan.Monthv.get(),"BirthDay":pujan.Dayv.get(),"Password":pujan.Pass1v.get()})
        p.frame1.destroy()
        p1=login()
root.geometry("1400x800")
dictmonth={"January":30,"February":28,"March":31,"April":30,"May":31,"June":30,"July":30,"August":31,"September":30,
           "October":31,"November":31,"December":30}
checkleap=lambda a: 28 if (a % 4 == 0 and (a % 100 != 0 or a % 400==0))  else 29
frame=Frame(root,height=800,width=1250,bg="orange")
frame.place(x=50,y=20)
class signin:
    def __init__(self):
        self.frame1 = Frame(frame, height=450, width=600, bg="gray")
        self.frame1.place(x=400, y=160)
        Label(self.frame1, bg="gray", text="            SIGN-IN                ", font=("Georgia", 30, "italic")).place(x=50,
                                                                                                                   y=10)
        pk = pujan()
        Label(self.frame1, bg="gray", text="Name:", font=("Georgia", 15, "bold")).place(x=10, y=80)
        self.name = ttk.Entry(self.frame1, font=("Georgia", 15, "bold"), textvariable=pujan.Namev)
        self.name.place(x=250, y=80)
        Label(self.frame1, bg="gray", text="Email:", font=("Georgia", 15, "bold")).place(x=10, y=130)
        self.Email = Entry(self.frame1, font=("Georgia", 12, "bold"), textvariable=pujan.Emailv, width=25)
        self.Email.place(x=250, y=130)
        Label(self.frame1, bg="gray", text="Age", font=("Georgia", 15, "bold")).place(x=10, y=180)
        self.Year = ttk.Combobox(self.frame1, font=("Georgia", 10, "bold"), width=6, state="readonly", textvariable=pujan.Yearv)
        self.Year["values"] = tuple(reversed(range(1975, 2020)))
        self.Year.current(20)
        self.Year.place(x=250, y=180)
        self.Month = ttk.Combobox(self.frame1, font=("Georgia", 10, "bold"), width=10, state="readonly",
                             textvariable=pujan.Monthv)
        self.Month["values"] = tuple(a for a in dictmonth)
        self.Month.current(5)
        self.Month.place(x=340, y=180)
        self.Day = ttk.Combobox(self.frame1, font=("Georgia", 10, "bold"), width=6, state="readonly", textvariable=pujan.Dayv)
        if (checkleap(pujan.Yearv.get()) == 29):
            dictmonth["February"] = 29
        self.Day["values"] = tuple(reversed(range(1, dictmonth[pujan.Monthv.get()])))
        self.Day.current(20)
        self.Day.place(x=460, y=180)
        Label(self.frame1, bg="gray", text="New Password:", font=("Georgia", 15, "bold")).place(x=10, y=230)
        self.pas1 = Entry(self.frame1, font=("Georgia", 12, "bold"), width=25,
