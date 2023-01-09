

import random
from tkinter import *

root = Tk()
root.geometry("564x317")    # dimensions for the window
root.config(bg='#A66CFF')   # color for the window

bg=PhotoImage(file="req/Bg1.png")

d1='''

           /\```````````\   
          /  \      O    \
         /    \           \
        /  O   \           \ 
        \      /```````````/
         \    /           /
          \  /     O     /
           \/           /
            ```````````` 
     '''

d2='''   
           /\```````````\   
          /  \     O     \
         /    \     O     \
        /   O  \           \ 
        \   O  /```````````/
         \    /     O     /
          \  /     O     /
           \/           /
            ````````````  
      '''

d3='''   

           /```````````/\   
          /         o /  \
         /     o     /    \  
        /  o        /   o  \ 
        \```````````\  o o /  
         \  o        \    /
          \    o      \  /    
           \       o   \/
            ```````````
      '''

d4='''          
           /```````````/\   
          /     o     /  \
         /   o    o  /  o \  
        /      o    /  o o \ 
        \```````````\   o  /  
         \     o     \    /
          \  o    o   \  /    
           \     o     \/
            ```````````
      '''

d5='''           
           /\```````````\   
          /  \     O     \
         / O  \  O  O  O  \
        /O O O \     O     \ 
        \  O   /```````````/
         \    /     O     /
          \  /  O  O  O  /
           \/     O     /
            ```````````` 
     '''

d6='''

           /\```````````\   
          /O \   O O O   \
         /O O \   O O O   \
        /O O O \   O O O   \ 
        \ O O  /```````````/
         \ O  /    O O O  /
          \  /    O O O  /
           \/   O O O   /
            ````````````  
   '''

# Create Canvas
canvas1=Canvas(root, width=1366, height=768)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg , anchor='nw')

l1 = Label(canvas1,text='',font=("times",70))

# roll command for the dice
def roll():
    # ascii code of numbers on the dice
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}',bg='#62de49')
    l1.place(x=30,y=100)

# button
b1 = Button(root,text='LETS ROLL...',activebackground='black',activeforeground='white',bd='4',bg='#58fc58',command=roll)
b1.place(x=30,y=20)

root.mainloop()