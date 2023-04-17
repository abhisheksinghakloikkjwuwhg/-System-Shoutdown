from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 10")


def shutdown():
    os.system("shutdown /s /t 1")


st =Tk()
st.title(" ShutDown App")
st.geometry("480x400")
st.config(bg="Blue")

r_button =Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart )
r_button.place(x=150,y=60,height=50,width=200)


rt_button =Button(st,text="Restart TIME",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=180,height=50,width=200)

St_button =Button(st,text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
St_button.place(x=150,y=300,height=50,width=200)




st.mainloop()