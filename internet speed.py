from tkinter import *
#mport speedtest

def speedchcek():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) +"Mbps"
    up = str(round(sp.upload()/(10**6),3)) +"Mbps"
    lab_down.config(text=down)
    lab_up.config(test=up)


sp = Tk()
sp.title("Internet speed Test")
sp.geometry("500x500")
sp.config(bg="Blue")

lab = Label(sp,text="Internet Speed Test", font=("Time New Roman",20,"bold"),bg="Blue",fg = "White")
lab.place(x=50,y=40,height = 30,width=380)

lab = Label(sp,text="Dowload Speed Test", font=("Time New Roman",20,"bold"),bg="Blue",fg = "White")
lab.place(x=50,y=130,height=50,width=380)

lab_down = Label(sp,text="00", font=("Time New Roman",20,"bold"),bg="Blue",fg = "White")
lab_down.place(x=50,y=200,height=50,width=380)

lab = Label(sp,text="upload Speed Test", font=("Time New Roman",20,"bold"),bg="Blue",fg = "White")
lab.place(x=50,y=290,height=50,width=389)

lab_up = Label(sp,text="00", font=("Time New Roman",20,"bold"),bg="Blue",fg = "White")
lab_up.place(x=50,y=40,height=50,width=380)

button = Button(sp,text="CHECK Speed", font=("Time New Roman",20,"bold"),relief =RAISED,command=speedcheck)
button.place(x=50,y=290,height=50,width=389)


sp.mainloop()