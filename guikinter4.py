#
'''
from tkinter import *
root=Tk()
root.geometry("500x500")

gender=IntVar()
country=IntVar()

def xyz():
    L=[]
    if gender.get()==1:
        L.append("male")
    elif gender.get()==2:
        L.append("female")
    else:
        print("neutral")
        
    if country.get()==1:
        L.append("India")
    else:
        L.append("Usa")

    print(L)

Label(root,text="Select gender",bg="black",fg="red",
      font=(20)).pack()

r1=Radiobutton(root,text="male",variable=gender,value=1,bg="yellow",fg="green",font=(15),width=10)
r2=Radiobutton(root,text="female",variable=gender,value=2,bg="yellow",fg="green",font=(15),width=10)
r1.pack()
r2.pack()

Label(root,text="Select Country",bg="black",fg="red",
      font=(20)).pack()

Radiobutton(root,text="India",variable=country,value=1,bg="yellow",fg="green",font=(15),width=10).pack()
Radiobutton(root,text="Usa",variable=country,value=2,bg="yellow",fg="green",font=(15),width=10).pack()

Button(root,text="Submit",command=xyz).pack()

root.mainloop()
'''

#
from tkinter import *
root=Tk()
root.geometry("500x500")

root.config(bg="yellow")
'''
header=Frame(root,width=200,height=200,bg="red",relief="sunken",bd=30)
foot=Frame(root,width=200,height=200,bg="green",relief="solid",bd=3)


header.pack(side="top",fill="x")
foot.pack(side="bottom",fill="x")
'''
f=Frame(root,bg="red",padx=300,pady=300)
f.pack()

Button(root,text="in root").pack()
Button(f,text="in frame").pack()




