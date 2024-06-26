from tkinter import *
from PIL import Image,ImageTk
import speech_to_text
import actions
root=Tk()
root.title("AI ASSISTANT")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#3baea0")

#ask
def ask():
    user_val=speech_to_text.speech_to_text()
    bot_val=actions.Actions(user_val)
    text.insert(END,'User--->'+user_val+"\n")
    if bot_val!=None:
        text.insert(END,"BOT<---"+str(bot_val)+"\n")
    if bot_val=="ok sir":
        root.destroy()
        
def send():
    send=entry.get()
    bot=actions.Actions(send)
    text.insert(END,'User--->'+send+"\n")
    if bot!=None:
        text.insert(END,"BOT<---"+str(bot)+"\n")
    if bot=="ok sir":
        root.destroy()
    
def del_text():
    text.delete('1.0',"end")


# frame
frame=LabelFrame(root,padx=100,pady=0,borderwidth=3,relief="raised")
frame.config (bg="#3baea0")
frame.grid(row=0,column=1,padx=55,pady=20)

#textlabel

text_label=Label(frame,text="AI assistant",font=("comic Sans ms",14,"bold"),bd="5")
text_label.grid(row=0,column=0,padx=20,pady=10)

# image
image=ImageTk.PhotoImage(Image.open("images/assistant-robots.png"))
image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)

#adding a text

text=Text(root,font=('courier 10 bold'),bg="#118a7e")
text.grid(row=2,column=0)
text.place(x=100,y=375,width=375,height=100)

# entry widget
entry=Entry(root,justify=CENTER)
entry.place(x=100,y=500,width=350,height=30)

# button
Button1=Button(root,text="ASK",bg="#118a7e",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=575)

#button2
Button2=Button(root,text="SEND",bg="#118a7e",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=400,y=575)

#button3
Button3=Button(root,text="DELETE",bg="#118a7e",pady=16,padx=40,borderwidth=3,relief=SOLID,command=del_text)
Button3.place(x=225,y=575)


root.mainloop()