#Rock, paper, scisscor 
from tkinter import * # import everything from tkinter module
from PIL import ImageTk, Image 
from tkinter import messagebox
import random
window = Tk() # instantiate an instant of window
window.title("Rock-Paper-Scissor Game")
window.geometry("350x350")
window.config(background="#Ffb6c1")
label = Label(window,text="Make a choice_Click on one of option",background="white",font=('50'))
label.pack()
List = ["rock","paper","scissor"]

# Load images
rock_img = ImageTk.PhotoImage(Image.open(r"C:\Users\gsm computeronix\Downloads\Rock.png").resize((80, 80)))
paper_img = ImageTk.PhotoImage(Image.open(r"C:\Users\gsm computeronix\Downloads\paper.jpeg").resize((80, 80)))
scissor_img = ImageTk.PhotoImage(Image.open(r"C:\Users\gsm computeronix\Downloads\scissor.jpeg").resize((80, 80)))

# Function to play a round
def play(user_choice):
    computer_choice = random.choice(List)
    if user_choice == computer_choice:
        result = "It's a Draw!"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        result = "You Win!"
    else:
        result = "You Lose!"    
    messagebox.showinfo(title="Result",
         message=f"Computer chose: {computer_choice}\nYou chose: {user_choice}\n{result}")

# Buttons with images
Button(window, image=rock_img, command=lambda: play("rock")).pack(pady=5)
Button(window, image=paper_img, command=lambda: play("paper")).pack(pady=5)
Button(window, image=scissor_img, command=lambda: play("scissor")).pack(pady=5)


window.mainloop() # place window on screen 
