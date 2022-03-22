from tkinter import *
import pygame
from tkinter import  filedialog
music_player=Tk()
music_player.title("My music player")
#music_player.iconbitmap('')
music_player.geometry("500x500")

# Initialize pygame mixer
pygame.mixer.init()

# add song function
def add_song():
    song=filedialog.askopenfilename(initialdir='audio/',title="Choose A Song",filetype=(('mp3 files',"*.mp3"),))
    # strip out the directory info and the .mp3 from the song name
    song = song.replace("C:/Users/Rajnish tripathi/Music/music_player/", "")
    song = song.replace(".mp3", "")
    song_list.insert(END,song)
# add many songs function
def add_many_song():
    songs=filedialog.askopenfilenames(initialdir='audio/',title="Choose A Song",filetype=(('mp3 files',"*.mp3"),))

    # loop through the song list replace info and the mpeg
    for song in songs:
        song=song.replace("C:/Users/Rajnish tripathi/Music/music_player/","")
        song=song.replace(".mp3","")

        #inssert many songs
        song_list.insert(END,song)
# play selected song
def play():
    song=song_list.get(ACTIVE)
    song=f'C:/Users/Rajnish tripathi/Music/music_player/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
# stop the song
def stop():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)

# create global pause variable
global paused
paused=False
# pause and unpause the current song
def pause(is_paused):
    global  paused
    paused= is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

# function for forward
def forward():
    # get the current song tuple number
    next_one=song_list.curselection()
    # add one the the current song for the next song
    next_one=(next_one[0]+1)
    # grab song title from the playlist
    song=song_list.get(next_one)
    song = f'C:/Users/Rajnish tripathi/Music/music_player/{song}.mp3'
    print(song)
    # load and play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # move the active bar in playlist listbox
    song_list.selection_clear(0,END)

    # add new song bar
    song_list.activate(next_one)

    # set active bar to nex song bar
    song_list.selection_set(next_one,last=None)
def pre_song():
    # get the current song tuple number
    next_one = song_list.curselection()
    # add one the the current song for the next song
    next_one = (next_one[0] - 1)
    # grab song title from the playlist
    song = song_list.get(next_one)
    song = f'C:/Users/Rajnish tripathi/Music/music_player/{song}.mp3'
    print(song)
    # load and play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # move the active bar in playlist listbox
    song_list.selection_clear(0, END)

    # add new song bar
    song_list.activate(next_one)

    # set active bar to nex song bar
    song_list.selection_set(next_one, last=None)

def delete_song():
    song_list.delete(ANCHOR)
    pygame.mixer.music.stop()
def delete_all_song():
    song_list.delete(0,END)
    pygame.mixer.music.stop()



# create playlist box
# fg for the text color
song_list=Listbox(music_player,bg="black",fg="red",width=80,height=20,selectbackground="yellow",selectforeground="black")
song_list.pack(pady=10)

# Define player control Buttons Images
back_img=PhotoImage(file='C:\\Users\\Rajnish tripathi\\OneDrive\\Pictures\\buttons\\backward.png')
play_img=PhotoImage(file='C:\\Users\\Rajnish tripathi\\OneDrive\\Pictures\\buttons\\play.png')
forward_img=PhotoImage(file='C:\\Users\\Rajnish tripathi\\OneDrive\\Pictures\\buttons\\forward.png')
pause_img=PhotoImage(file='C:\\Users\\Rajnish tripathi\\OneDrive\\Pictures\\buttons\\pause.png')
stop_img=PhotoImage(file='C:\\Users\\Rajnish tripathi\\OneDrive\\Pictures\\buttons\\stop.png')

# create player control frame
Controls_frame= Frame(music_player)
Controls_frame.pack()

# create player control button

back_btn=Button(Controls_frame,image=back_img,borderwidth=0,command=pre_song)
play_btn=Button(Controls_frame,image=play_img,borderwidth=0,command=play)
forward_btn=Button(Controls_frame,image=forward_img,borderwidth=0,command=forward)
pause_btn=Button(Controls_frame,image=pause_img,borderwidth=0,command=lambda: pause(paused))
stop_btn=Button(Controls_frame,image=stop_img,borderwidth=0,command=stop)

play_btn.grid(row=0,column=0,padx=10)
back_btn.grid(row=0,column=1,padx=10)
forward_btn.grid(row=0,column=2,padx=10)
pause_btn.grid(row=0,column=3,padx=10)
stop_btn.grid(row=0,column=4,padx=10)

# create menu
my_menu=Menu(music_player)
music_player.config(menu=my_menu)

# Add song menu
add_song_menu= Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist",command=add_song)
add_song_menu.add_command(label="Add Many song to playlist",command=add_many_song)

# Create delete song menu
remove_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Remove Songs",menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song from palylist",command=delete_song)
remove_song_menu.add_command(label="Delete all song from palylist",command=delete_all_song)

# create status Bar


music_player.mainloop()