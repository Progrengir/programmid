import customtkinter
import tkinter
from pytube import YouTube
from tkinter import  filedialog

def startDownload(): ## Download function
    try:
        ytLink = link.get()
        global selected_directory ## veendun et see globaalne
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()  
        title.configure(text=ytObject.title , text_color="white")
        textbox.configure(text=f"{ytObject.views} -Views" , text_color="white")
        textbox2.configure(text=f"{ytObject.author} -Author", text_color="white")
        finishLabel.configure(text="")
        destination_folder = selected_directory
        print("Directory", selected_directory)
        video.download(output_path=destination_folder)
        finishLabel.configure(text="Download complete!", text_color="white")

    except:
        finishLabel.configure(text="Download failed", text_color="red")




def on_progress(stream, chunk, bytes_remaining): #Progressbar
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #Progress bar

    progressBar.set(float(percentage_of_completion) / 100)



#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Youtube Downloader")


#UI Elements

title = customtkinter.CTkLabel(app, text = "Insert YouTube link here!")  # tiitelleht
title.pack(padx=20, pady=20)

#Download button

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=20, pady=20)

#YouTube link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=30, textvariable=url_var)
link.pack(padx=50,pady=0)


#App directory

def selected_directory():
    global selected_directory
    selected_directory = filedialog.askdirectory()
    print(selected_directory)
    if selected_directory:
        directory_label.configure(text=selected_directory, text_color="white")


#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Progress
pPercentage = customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=300)
progressBar.set(0)
progressBar.pack(padx=20,pady=20)

#Directory button
directory_button = customtkinter.CTkButton(app, text="Change directory", command=selected_directory)
directory_button.pack(padx=0,pady=10)
directory_label = customtkinter.CTkLabel(app, text="")
directory_label.pack(padx=0,pady=0)

#Run app

app.mainloop()