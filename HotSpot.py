from tkinter import *
from module import start,stop
import win32gui, win32con ,os
from elevate import elevate
def status_check(req):
    if req=="start":
        try:
            start.start()
            file=open("data/data.txt").read()
            file=file.split()
            _status['text']="Started!\n SSID : {} \n Password : {}".format(file[0],file[1])
            _status['fg']="#61f261"
        except:
            _status['text']="Please Set Your SSID And Password First!"
            _status['fg']='#ff3838'
    if req=="stop":
        stop.stop()
        _status['text']="Stoped!\n\n"
        _status['fg']="#61f261"
def data():
    def data_checker():
        SSID=U_entry.get()
        Pass=P_entry.get()
        P_entry['bg']="#fff"
        U_entry['bg']="#fff"
        Status_['text']="\n\n"
        Status_['bg']="#292929"
        currect=True
        if SSID=="" or Pass=="":
            Status_['text']="Please Fill Out All The Blanks!"
            Status_['bg']="#fa7575"
            currect=False
            if SSID=="":
                U_entry['background']="#fa7575"
            if Pass=="":
                P_entry['background']="#fa7575"
        else:
            currect=True
            U_entry['background']="#fff"
            P_entry['background']="#fff"
        if len(Pass)<8 and currect==True:
            currect=False
            P_entry['background']="#fa7575"
            Status_['text']="Password must be at least 8 characters long!"
            Status_['bg']="#fa7575"
        elif SSID!="" and Pass!="":
            currect=True
            P_entry['background']="#fff"
        if currect==True:
            Status_['text']="Submited!"
            Status_['bg']="#61f261"
            return data_save(SSID,Pass)
    def data_save(SSID,Pass):
        os.system("netsh wlan set hostednetwork mode=allow ssid={} key={} keyusage=persistent".format(SSID,Pass))
        file=open("data/data.txt","w")
        file.write("{}\n{}".format(SSID,Pass))
        file.close()
    root=Tk()
    root.title("HotSpot")
    root.geometry("400x350")
    root['background']="#292929"
    root.iconbitmap("data/icon.ico")
    U_label=Label(root,text="SSID",fg="#fff",bg="#292929",font="tahoma 20 bold")
    U_label.pack(pady=20)
    U_entry=Entry(root,justify="center",font="tahoma 15",width=20)
    U_entry.pack()
    P_label=Label(root,text="Password",fg="#fff",bg="#292929",font="tahoma 20 bold")
    P_label.pack(pady=20)
    P_entry=Entry(root,justify="center",font="tahoma 15",width=20)
    P_entry.pack()
    Sub_btn=Button(root,text="Submit",bg="#61f261",font="tahoma 15",width=10,height=1,command=data_checker)
    Sub_btn.pack(pady=15)
    Status_=Label(root,text="",font="tahoma 10",bg="#292929")
    Status_.pack()
    mainloop()
#run as administrator
elevate(show_console=False)
#Hiding console
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
#creating window
window=Tk()
window.title("HotSpot")
window.geometry("500x500")
window.iconbitmap("data/icon.ico")
window['background']="#292929"
#objects
_title=Label(window,text="HotSpot",fg="#fff",bg="#292929",font="tahoma 40 bold")
_title.pack(pady=20)
_databtn=Button(window,text="Set SSID And Password",width="30",font="tahoma 10 bold",height="3",command=data)
_databtn.pack(pady=10)
_startbtn=Button(window,text="Start HotSpot",bg="#61f261",width="30",font="tahoma 10 bold",height="3",command=lambda: status_check("start"))
_startbtn.pack()
_stopbtn=Button(window,text="Stop HotSpot",bg="#fa7575",font="tahoma 10 bold",width="30",height="3",command=lambda: status_check("stop"))
_stopbtn.pack()
_status=Label(window,text="\n\n",bg="#292929",font="tahoma 15")
_status.pack(pady=17)
Dev=Label(window,text="version : 1.0\nDeveloped by Arian\nEmail : Arian_1949@protomail.com\nTelegram : ArianProgrammer",fg="#fa7575",bg="#292929")
Dev.pack()
mainloop()
