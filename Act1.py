from tkinter import *
import tkinter.font as font
import random

root=Tk()
root.title("Rock Paper Scissors")
root.geometry("700x300")
#game logic
player_score=0
comp_score=0
options= [("rock",0), ("paper",1), ("scissors",2)]


#designing
app_font=font.Font(size=12)

title=Label(text="Rock Paper Scissors",font=font.Font(size=20),fg='gray')
title.pack()

winner=Label(text="Let's Start the Game...",font=font.Font(size=15),fg="red",pady=8)
winner.pack()

frame=Frame(root)
frame.pack()

options=Label(frame,text="Your Options:",font=app_font,pady=8)
options.grid(row=0,column=0)

rock=Button(frame,text="Rock",width=15,bd=0,bg="pink",pady=5)
rock.grid(row=1,column=1,padx=8)

paper=Button(frame,text="Paper",width=15,bd=0,bg="cyan",pady=5)
paper.grid(row=1,column=2,padx=8)

scissors=Button(frame,text="Scissors",width=15,bd=0,bg="lime",pady=5)
scissors.grid(row=1,column=3,padx=8)

score=Label(frame,text="Score:",font=app_font,pady=8)
score.grid(row=2,column=0)

pchoice=Label(frame,text="Your Selected:",font=app_font,pady=8)
pchoice.grid(row=3,column=1,padx=8)

pscore=Label(frame,text="Your Score:",font=app_font,pady=8)
pscore.grid(row=3,column=2,padx=8)

cochoice=Label(frame,text="Computer Selected:",font=app_font,pady=8)
cochoice.grid(row=4,column=1,padx=8)

coscore=Label(frame,text="Computer Score:",font=app_font,pady=8)
coscore.grid(row=4,column=2,padx=8)



root.mainloop()