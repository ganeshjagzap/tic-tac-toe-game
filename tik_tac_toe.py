from tkinter import *
from tkinter import messagebox

root=Tk()

root.geometry("385x545")

root.title("Tik Tac Toe")

press=True
count=0

def freez_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)



def checkwhoown():
    global winner
    winner=False


    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')

        winner=True
        messagebox.showinfo("tic tac toe", "X Won.....")

        freez_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg='green')
            b5.config(bg='green')
            b6.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","X Won.....")

            freez_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg='green')
            b8.config(bg='green')
            b9.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","X Won.....")

            freez_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.config(bg='green')
            b4.config(bg='green')
            b7.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","X Won.....")

            freez_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg='green')
            b5.config(bg='green')
            b8.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","X Won.....")

            freez_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.config(bg='green')
            b6.config(bg='green')
            b9.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","X Won.....")

            freez_all_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg='green')
            b5.config(bg='green')
            b9.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","X Won.....")

            freez_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg='green')
            b5.config(bg='green')
            b7.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","X Won.....")

            freez_all_buttons()


    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')

        winner=True
        messagebox.showinfo("tic tac toe", "O Won.....")

        freez_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg='green')
            b5.config(bg='green')
            b6.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","O Won.....")

            freez_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg='green')
            b8.config(bg='green')
            b9.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","O Won.....")

            freez_all_buttons()


    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg='green')
            b4.config(bg='green')
            b7.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","O Won.....")

            freez_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg='green')
            b5.config(bg='green')
            b8.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","O Won.....")

            freez_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg='green')
            b6.config(bg='green')
            b9.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","O Won.....")

            freez_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg='green')
            b5.config(bg='green')
            b9.config(bg='green')

            winner = True
            messagebox.showinfo("tic tac toe","O Won.....")

            freez_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg="green")
            b5.config(bg="green")
            b7.config(bg="green")

            winner = True
            messagebox.showinfo("tic tac toe","O Won.....")

            freez_all_buttons()


    if ((count == 9) and (winner==False)):
        messagebox.showinfo("tic tac toe", "Match draw! ")


def Exit():
    root.destroy()

def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,count
    count=0


    b1 = Button(root, text=" ", font="Arial 20 bold", height=4, width=7, command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font="Arial 20 bold", height=4, width=7, command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font="Arial 20 bold", height=4, width=7, command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font="Arial 20 bold", height=4, width=7, command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font="Arial 20 bold", height=4, width=7, command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font="Arial 20 bold", height=4, width=7, command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font="Arial 20 bold", height=4, width=7, command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font="Arial 20 bold", height=4, width=7, command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font="Arial 20 bold", height=4, width=7, command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def b_click(b):
    global press,count


    if( b["text"]==" " and press==True):
        b["text"]="X"

        press=False
        count+=1
        b.config(bg="skyblue")
        checkwhoown()

    elif (b["text"]==" " and press==False):
        b["text"]="O"
        press=True
        count+=1
        b.config(bg="yellow")

        checkwhoown()





    else:
        messagebox.showinfo("tic tac toe","you can only press on button at once")




b1=Button(root,text=" ",font="Arial 20 bold" ,height=4 , width=7,command=lambda:b_click(b1))
b2=Button(root,text=" ",font="Arial 20 bold" ,height=4 , width=7,command=lambda :b_click(b2))
b3=Button(root,text=" ",font="Arial 20 bold" ,height=4 , width=7,command=lambda :b_click(b3))

b4=Button(root,text=" ",font="Arial 20 bold" ,height=4 , width=7,command=lambda :b_click(b4))
b5=Button(root,text=" ",font="Arial 20 bold" ,height=4 , width=7,command=lambda :b_click(b5))
b6=Button(root,text=" ",font="Arial 20 bold" ,height=4 , width=7,command=lambda :b_click(b6))

b7=Button(root,text=" ",font="Arial 20 bold" ,height=4 , width=7,command=lambda :b_click(b7))
b8=Button(root,text=" ",font="Arial 20 bold" ,height=4 , width=7,command=lambda :b_click(b8))
b9=Button(root,text=" ",font="Arial 20 bold" ,height=4 , width=7,command=lambda :b_click(b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

resetbutton=Button(root,text="Reset ",font="Arial 10",padx=3,pady=4 ,command=reset).place(x=20,y=480)
exit_button=Button(root,text="Exit",font="Arial 10",padx=6,pady=4,command=Exit).place(x=310 ,y=480)


root.mainloop()