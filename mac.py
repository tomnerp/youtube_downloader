from pytube import YouTube
import os

welcome = """\33[94m
$$\   $$\ $$\   $$\ $$\     $$\       $$$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\  $$$$$$\  
$$ |  $$ |$$ |  $$ |\$$\   $$  |      $$  __$$\ $$  __$$\ $$$\  $$ |$$ |  $$ |$$  __$$\ 
$$ |  $$ |$$ |  $$ | \$$\ $$  /       $$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ |  $$ |$$ /  $$ |
$$$$$$$$ |$$ |  $$ |  \$$$$  /        $$$$$$$  |$$$$$$$$ |$$ $$\$$ |$$$$$$$$ |$$$$$$$$ |
$$  __$$ |$$ |  $$ |   \$$  /         $$  ____/ $$  __$$ |$$ \$$$$ |$$  __$$ |$$  __$$ |
$$ |  $$ |$$ |  $$ |    $$ |          $$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |\$$$$$$  |    $$ |          $$ |      $$ |  $$ |$$ | \$$ |$$ |  $$ |$$ |  $$ |
\__|  \__| \______/     \__|          \__|      \__|  \__|\__|  \__|\__|  \__|\__|  \__|\33[0m
"""
print(welcome)

def progress(stream, chunk, bytes_remaining):
    contentSize = stream.filesize
    size = contentSize - bytes_remaining

    print('\33[94m\r' + '[Download progress]:[%s%s]	%.2f%%\33[0m' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

def next():
    yt.register_on_progress_callback(progress)

    output = video.download(output_path=dest)

    base, ext = os.path.splitext(output)

    if type == "1":
        newFile = base + ".mp4"
    else:
        newFile = base + ".mp3"

    os.rename(output, newFile)

    print("\n\nSaved to : \33[92m" + newFile + "\33[0m")

url = str(input("\33[5m>> Enter youtube link: \33[0m"))
dest = str(input("\33[5m>> Destination directory: \33[0m")) or "."
yt = YouTube(url)
video = yt

print("\n\n\33[34m========== Menu ==========")
print("1. MP4\n2. MP3\33[0m\n\33[91m3. Cancel Downloading\33[0m\n\n")
type = input("\33[5m>> Enter menu number[1-2]: \33[0m")
video_resolutions = []
download_res = ""

if type == "1":
    for res in yt.streams.order_by('resolution').desc():
        if res.resolution not in video_resolutions:
            video_resolutions.append(res.resolution)
    print("\n\n\33[34m========== Resolution ==========\n")
    i = 1
    for resolution in video_resolutions:
        print(str(i) + ". " + resolution)
        i+=1
    print("\33[0m\33[91m" + str(i) + ". Cancel Download")
    download_res = input("\n\33[0m\33[5m>> Enter resolution menu number: \33[0m")
    if int(download_res) >= 0 and int(download_res) < i:
        print("\33[93mDownloading video with resolution : " + video_resolutions[int(download_res)-1] + "\33[0m")
        print("\33[92mDownloading MP4: \33[0m\33[104m" + yt.title + "\33[0m")
        video = yt.streams.filter(res=video_resolutions[int(download_res)-1]).first()
        next()
elif type == "2":
    video = yt.streams.filter(only_audio=True).first()
    print("\33[92m>> Downloading MP3 \33[0m\33[104m" + yt.title + "\33[0m")
    next()
