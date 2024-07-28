from tkinter import*
from PIL import Image , ImageTk
import listen
import tasks


def ask():
    send=listen.listen()
    bot=tasks.work(send)
    text.insert(END, 'User---->'+send+"\n")
    if bot!=None:
        text.insert(END, 'AI_assistant---->'+bot+"\n")
    if bot=="ok sure":
        root.destroy()


def User_send():
    send = entry1.get()
    bot = tasks.work(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()  



def delete_text():
    text.delete('1.0',"end")



root=Tk()
root.title("AI Assistant")
root.geometry("600x720")
root.resizable(False,False)
root.config(bg="#bcaaa4")


#frame

frame=LabelFrame(root, padx=100, pady=7, relief="raised")
frame.grid(row=0,column=1,padx=55,pady=10)
frame.config(bg="#bcaaa4")

#text label

text_label=Label(frame,  text="AI ASSISTANT", font=("sans-serif", 14, "bold") , bg="#8d6e63")
text_label.grid(row=0,column=0,padx=20,pady=10)


# Add a text widget

text=Text(root , font= ('Courier 10 bold') , bg = "#8d6e63")
text.grid(row = 5,  column= 5)
text.place(x=120, y=450, width= 375, height= 100) 


Display_Image = ImageTk.PhotoImage(Image.open("image/assistant.png"))
Image_Lable = Label(frame, image= Display_Image)
Image_Lable.grid(row = 1 ,  column=0 , pady=20)







# Add a entry widget
entry1 = Entry(root, justify = CENTER)
entry1.place(x=120 , y = 570 , width= 350, height= 30)

# Add a text button1
button1 =  Button(root,  text="ASK" , bg="#8d6e63" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 70, y= 625)

# Add a text button2
button2 =  Button(root,  text="Send" , bg="#8d6e63" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
button2.place(x= 400, y= 625)

# Add a text button3
button3 = Button(root, text="Delete", bg="#8d6e63" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x= 225, y= 625)

root.mainloop()


