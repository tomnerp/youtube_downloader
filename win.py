from pytube import YouTube
import os
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from datetime import datetime

welcome = """[green]
$$\   $$\ $$\   $$\ $$\     $$\       $$$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\  $$$$$$\  
$$ |  $$ |$$ |  $$ |\$$\   $$  |      $$  __$$\ $$  __$$\ $$$\  $$ |$$ |  $$ |$$  __$$\ 
$$ |  $$ |$$ |  $$ | \$$\ $$  /       $$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ |  $$ |$$ /  $$ |
$$$$$$$$ |$$ |  $$ |  \$$$$  /        $$$$$$$  |$$$$$$$$ |$$ $$\$$ |$$$$$$$$ |$$$$$$$$ |
$$  __$$ |$$ |  $$ |   \$$  /         $$  ____/ $$  __$$ |$$ \$$$$ |$$  __$$ |$$  __$$ |
$$ |  $$ |$$ |  $$ |    $$ |          $$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |\$$$$$$  |    $$ |          $$ |      $$ |  $$ |$$ | \$$ |$$ |  $$ |$$ |  $$ |
\__|  \__| \______/     \__|          \__|      \__|  \__|\__|  \__|\__|  \__|\__|  \__|[/green]
"""
print(welcome)

def progress(stream, chunk, bytes_remaining):
    contentSize = stream.filesize
    size = contentSize - bytes_remaining

    print('[yellow]\r' + '[Download progress]:[%s%s]	%.2f%%[/yellow]\n' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

def next():
    yt.register_on_progress_callback(progress)

    output = video.download(output_path=dest)

    base, ext = os.path.splitext(output)

    if type == "1":
        newFile = base + str(datetime.now()) + ".mp4"
    else:
        newFile = base + str(datetime.now()) + ".mp3"

    os.rename(output, newFile)

    print("\n\n✓ Saved to : [green]" + newFile + "[/green]")

url = str(input(">> Enter youtube link: "))
dest = str(input(">> Destination directory: ")) or "/Downloads"
yt = YouTube(url)
video = yt

print("\n")
Console().print(Markdown("""# Menu

1. MP4
2. MP3"""))
print(" [red]3 Cancel Downloading[/red]\n")

type = input(">> Enter menu number[1-3]: ")
video_resolutions = []
download_res = ""

if type == "1":
    for res in yt.streams.order_by('resolution').desc():
        if res.resolution not in video_resolutions:
            video_resolutions.append(res.resolution)
    Console().print(Markdown("""# Resolution"""))
    print("\n")
    i = 1
    for resolution in video_resolutions:
        print(str(i) + ". " + resolution)
        i+=1
    print("[red]" + str(i) + ". Cancel Downloading[/red]\n")
    download_res = input("\n>> Enter resolution menu number: ")
    if int(download_res) >= 0 and int(download_res) < i:
        print("\n[cyan]Downloading video with resolution : " + video_resolutions[int(download_res)-1] + "[/cyan]")
        print("[yellow]Downloading MP4: [/yellow][blue]" + yt.title + "[/blue]")
        video = yt.streams.filter(res=video_resolutions[int(download_res)-1]).first()
        next()
elif type == "2":
    video = yt.streams.filter(only_audio=True).first()
    print("[yellow]Downloading MP3: [/yellow][blue]" + yt.title + "[/blue]")
    next()
