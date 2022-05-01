# Different modules were imported from python as well as with the pre-made dictionaries
# for the story texts, decisions, and dialogue for the text-based adventure game
import tkinter as tk
import story_text
from PIL import ImageTk, Image
import winsound as wn
import sys
import os


# The pre-made dictionaries were called from another file and assigned to variables for convenience 
story_dict = story_text.main_text()
choice_dict = story_text.main_decisions()
route = story_text.decision_outcome()
story_cut_text = story_text.game_cut_story()
# Choice buttons is an empty list were the decisions will be appended, as well as for easy access to create and destroy
choice_buttons = []

def game_over_determiner(choice_key,frame3):
    # This function displays what ending the user gets from playing the game, pre-determined by the choices the user made 
    # throughout the story-game
    if choice_key == "Call the police":
        end = tk.Label(frame3, text = "Ending:\nARRESTED",font = ("Something Strange",20), fg = "red")
        wn.PlaySound("police siren", wn.SND_FILENAME|wn.SND_ASYNC)
        end.pack()
        play_again_button()
    elif choice_key == "Run":
        wn.PlaySound("Bat hit", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nHARD HEADED GIRL",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key == "Call police":
        wn.PlaySound("Another OST - Track 06", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nSILENT FALL",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key=="CONTINUE":
        wn.PlaySound("multibang", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nBULLET HEADACHE",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key=="Interact with them":
        wn.PlaySound("police siren", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nYOU WERE SET UP.",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key=="This is it! Follow him":
        wn.PlaySound("multibang", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nYOU DIED.",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key == "You find some place to jump":
        wn.PlaySound("Bat hit", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nHome Run.",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key == "No time to jump":
        wn.PlaySound("scream1", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nDID YOU HAVE A GOOD SLEEP?...",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key == "Take the opposite direction":
        wn.PlaySound("Another OST - Track 06", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nDON'T WORRY, THE DOCTOR IS COMING.",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key == "Continue walking towards the store":
        wn.PlaySound("Another OST - Track 06", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nYOU SHOULD DRINK YOUR MEDICINE REGULARLY.",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key == "Go out and take the risk to listen":
        wn.PlaySound("Evangelion 3.33 ost - Long Slow Pain", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nYOU ARE GOING TO PAY THE PRICE\n(for someone else)",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key == "Stay inside the closet until the voices are gone":
        wn.PlaySound("Evangelion 3.33 ost - Long Slow Pain", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nYOU SHOULD HAVE STAYED INSIDE...",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()
    elif choice_key == "NO,go back":
        wn.PlaySound("Evangelion 3.33 ost - Long Slow Pain", wn.SND_FILENAME|wn.SND_ASYNC)
        end = tk.Label(frame3, text = "Ending:\nYou should have followed your instincts.",font = ("Something Strange",20), fg = "red")
        end.pack()
        play_again_button()


# s_t_c is set to -1 since the function to display the text increments s_t_c by 1 automatically, and the text starts at key 0 
s_t_c = -1
def story_cut(choice_key,frame3,mainnum,canvas,canvas_text):
    global s_t_c
    s_t_c += 1
    if s_t_c ==5:
        # When s_t_c has the value of 5, it will go to display a mini game (pass code minigame)
        for i in choice_buttons:
            i.destroy()
        text_string = story_cut_text[s_t_c]
        canvas.itemconfigure(canvas_text, text=text_string)
        paswrd = tk.Entry(frame3)
        paswrd.pack()
        button = tk.Button(frame3, text="Enter", command = lambda: entry_check(choice_key,frame3,mainnum,canvas,canvas_text,paswrd.get(),paswrd,button))
        button.pack()

    # Each value of these s_t_c has corresponding texts to display so prevent an out of border text display
    if s_t_c==2 or s_t_c==8 or s_t_c==11 or s_t_c==18 or s_t_c==21 or s_t_c==25 or s_t_c==28 or s_t_c==31:
        display_text_for_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    else:
        for i in choice_buttons:
            i.destroy()
        text_string = story_cut_text[s_t_c]
        canvas.itemconfigure(canvas_text, text=text_string)
        next_cut(choice_key,frame3,mainnum,canvas,canvas_text)

# This function displays the text for a storyline per few sentences to avoid an out of border text display
def display_text_for_cut(choice_key,frame3,mainnum,canvas,canvas_text):
    global s_t_c
    for i in choice_buttons:
        i.destroy()
    text_string = story_cut_text[s_t_c]
    canvas.itemconfigure(canvas_text, text=text_string)
    display_choices2(choice_key,frame3,mainnum,canvas,canvas_text)

# This button is for the cut story texts so the user can proceed to the next sentence
def next_cut(choice_key,frame3,mainnum,canvas,canvas_text):
    global s_t_c
    next_but = tk.Button(frame3, text = "Next", font = (10),command = lambda:[story_cut(choice_key,frame3,mainnum,canvas,canvas_text),next_but.destroy()])  
    next_but.pack(side= "left", padx = 10)
    if s_t_c == 5:
        next_but.destroy() 

# Entry check function checks the entry of the user for the password minigame and determines if the user proceeds or not
def entry_check(choice_key,frame3,mainnum,canvas,canvas_text,x,paswrd,button):
    if x == "password":
        paswrd.destroy()
        button.destroy()
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)

# This function displays the text according to the flow of the user's game
def choices_and_stories2(choice_key,frame3,mainnum,canvas,canvas_text):
    global s_t_c
    # When the choice of the user is in one of these conditions, it will display the cut story texts
    # and changes the value of the s_t_c accordingly
    if choice_key == "Take the risk and go upstairs":
        s_t_c = 2
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    elif choice_key =="Go out and find another place to hide":
        s_t_c = 8
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    # Choice-key interact with them does not have a set value for s_t_c as the value of s_t_c is already at negative 1
    # incrementing it by one will change the value to zero which is already a corresponding key to the dictionary of cut texts
    elif choice_key =="Interact with them":
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    elif choice_key =="Take precautions by staying inside":
        s_t_c = 11
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    elif choice_key =="CONTINUE":
        s_t_c = 18
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    elif choice_key =="Wait for him to go":
        s_t_c = 21
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    elif choice_key =="No time to jump":
        s_t_c = 25
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    elif choice_key =="Take the opposite direction":
        s_t_c = 28
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    elif choice_key =="Go in warehouse":
        choice_key = "Take the risk and go upstairs"
        s_t_c = 4
        story_cut(choice_key,frame3,mainnum,canvas,canvas_text)
    else:
        # The buttons that were appended in the display_choices function will be destroyed so as to give way
        # for the new decisions that the user will be provided with
        for i in choice_buttons:
                i.destroy()
        text_string = route[choice_key]
        canvas.itemconfigure(canvas_text, text=text_string)
        display_choices2(choice_key,frame3,mainnum,canvas,canvas_text)

# This function serves to display the first main story line/text at the start of the game
def choices_and_stories1(mainnum,canvas,canvas_text,frame3,next_click,back_click):
    text_string = story_dict[mainnum]
    # key -1 has the value of the instructions for the game, which will be displayed with a red color
    if mainnum == -1:
        canvas.itemconfigure(canvas_text, text=text_string, fill = "red", justify = "center")
    else:
        canvas.itemconfigure(canvas_text, text=text_string,fill = "white")
    # Once mainnum is equal to four, it proceeds to the next function where the decision based outcome gameplay
    # will start
    if mainnum == 4:
        next_click.destroy()
        back_click.destroy()
        display_choices(frame3,mainnum,canvas,canvas_text)

# choice_dict has values of a list where each elemment is a choice of the user, the number of choices determines the number of buttons
# Both display choices functions will display the decisions to be chosen by the user. One is for the first three decisions and the other is
# for the gameplay itself where the story branches out.
def display_choices(frame3,mainnum,canvas,canvas_text):
    for choice in choice_dict[0]:
        decide = tk.Button(frame3, text = choice, font = (10),pady = 10,command = lambda choice = choice: choices_and_stories2(choice,frame3,mainnum,canvas,canvas_text))
        choice_buttons.append(decide) 
        decide.pack(side = "left", padx = 10)

def display_choices2(choice_key,frame3,mainnum,canvas,canvas_text):
    game_over_determiner(choice_key,frame3)
    for choice in choice_dict[choice_key]:
        choice = tk.Button(frame3, text = choice, font = (10),pady = 10,command = lambda choice = choice: choices_and_stories2(choice,frame3,mainnum,canvas,canvas_text))
        choice_buttons.append(choice) 
        choice.pack(side = "left", padx = 10)

# mainnum is set to negative two to enable the first text value at key -1 to appear first
mainnum = -2
def next_button(canvas,frame2,canvas_text,frame3,next_click,back_click):
    global mainnum
    mainnum+=1
    choices_and_stories1(mainnum,canvas,canvas_text,frame3,next_click,back_click)

def back_button(canvas,frame2,canvas_text,frame3,next_click,back_click):
    global mainnum
    if mainnum >= 1:
        mainnum-=1
        choices_and_stories1(mainnum,canvas,canvas_text,frame3,next_click,back_click)


def repeat():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def play_again_button():
    play_again = tk.Button(window, text="PLAY AGAIN", font = ("Fixedsys",7),fg = "red",command=repeat)
    play_again.place(x=300,y=300)

    exit_button = tk.Button(window, text="EXIT", font = ("Fixedsys",7),fg = "red",command=window.destroy)
    exit_button.place(x=500,y=300)

#Function to give credits to the artist's work that we used in developing our game
def credits():
    frame0 = tk.LabelFrame(window,text="CREDITS",font = ("Fixedsys",20),fg = "red",bg="black",width=850,height=500)
    frame0.pack()
    Label1 = tk.Label(frame0,text="Music:",font = ("Fixedsys",20),fg = "red",bg="black", anchor = tk.N)
    Label1.place(x = 370, y=30)
    Label2 = tk.Label(frame0,text="Crime Thriller background Music for videos -Unsolved Murder Suspenseful Film Noir Scene Sound: Youtube\nEvangelion 3.33 ost - Long Slow Pain\nAnother OST - Track 06\nWoman Scream Jump Scare Sound Effect: Youtube\nHead hit with bat, foley take..: Youtube\nmore M16A1 sound effects: Youtube\nPolice Siren: Youtube",font = ("Fixedsys",14),fg = "red",bg="black", anchor = tk.N)
    Label2.place(x=20,y=80)
    Label1 = tk.Label(frame0,text="Art:",font = ("Fixedsys",20),fg = "red",bg="black", anchor = tk.N)
    Label1.place(x = 387, y=200)
    Label2 = tk.Label(frame0,text="Manriel:'Hanged Anime Man': https://whvn.cc/0w1y27",font = ("Fixedsys",14),fg = "red",bg="black", anchor = tk.N)
    Label2.place(x=240,y=240)

    back_click = tk.Button(frame0, text = "Back", font = ("Fixedsys",20),fg = "red",bg="black",highlightthickness = 0, bd = 0,command = lambda:frame0.forget())  
    back_click.place(x=10,y=380)


# Main screen display when playing the game    
def main_screen():
    #Frame is made to separate the window into three parts, one for text and the other for the choices and buttons
    #Frame1 is propagated so as to disable any unecessary movements when the texts adjusts due to their length
    frame1 = tk.Frame(window,width = 100, height = 100)
    frame1.pack(fill = "both",ipady = 80)
    frame1.propagate(0)
    #Frame2 and frame3 is built for the display of the buttons and choices
    frame2 = tk.LabelFrame(window,text = "Options",font = ("Fixedsys",7))
    frame2.pack(fill="both", ipady = 20)
    frame3 = tk.LabelFrame(window,text = "Choices",font = ("Fixedsys",7))
    frame3.pack(fill="both", ipady = 75)
    
    #Canvas as well as canvas_text, is built into frame1 to display the text for the story
    canvas = tk.Canvas(frame1,width = 850)
    canvas.configure(bg = "black")
    canvas.pack()

    canvas_text = canvas.create_text(425, 100, text='',font = ("Fixedsys",5),fill = "white",justify = "center",width = 600)

    back_click = tk.Button(frame2, text = "Back", font = (10),command = lambda:back_button(canvas,frame2,canvas_text,frame3,next_click,back_click))  
    back_click.pack(side= "left", padx = 10)

    next_click = tk.Button(frame2, text = "Next", font = (10),command = lambda: next_button(canvas,frame2,canvas_text,frame3,next_click,back_click))
    next_click.invoke() 
    next_click.pack(side= "left") 

#====Main Code====#
window = tk.Tk()
window.title("Everyone's Game")
window.geometry("850x500")
window.configure(bg = "light grey")

# This line of code will display an image for the title screen of the game
img1 = Image.open("pierce.gif")
img2 = img1.resize((500,750), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img2)
panel = tk.Label(window, image = img)
panel.place(x = 185) 

# Play music continuously while the user plays the game
wn.PlaySound("Thriller Music", wn.SND_FILENAME|wn.SND_LOOP|wn.SND_ASYNC)

# Configures the game title of the application
title = tk.Label(window, text = "Everyone's Game", font= ("Something Strange",15), fg = "red")
title.place(x=375,y=30)


# Start button to initiate the game
start_button = tk.Button(window, text="START", font = ("Fixedsys",17),fg = "red",highlightthickness = 0, bd = 0,command=lambda:main_screen())
start_button.place(x =260 ,y = 250)


#Quit button whenever the user wants to exit the game
quit_button = tk.Button(window, text="QUIT", font = ("Fixedsys",17),fg = "red",highlightthickness = 0, bd = 0,command=lambda:window.destroy())
quit_button.place(x=560, y=310)

#credit button whenever the user wants to view credits for the assests that was used in the game
credits_button = tk.Button(window, text="Credits", font = ("Fixedsys",17),fg = "red",highlightthickness = 0, bd = 0,command=lambda:credits())
credits_button.place(x=210, y=420)

window.resizable(False,False)
# Mainloop of GUI
window.mainloop()