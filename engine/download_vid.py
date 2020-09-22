from __future__ import unicode_literals
import youtube_dl
from pydub import AudioSegment
import os


def get_mp3(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '50',
        }],
    }
    for entry in os.scandir('.'):
        if entry.is_file():
            if os.path.exists('audio.flac'):
                os.remove("audio.flac")

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    for entry in os.scandir('.'):
        if entry.is_file():
            if entry.name.endswith(".flac"):
                os.rename(entry.name, "audio.flac")

    print('uploading')

    # sound = AudioSegment.from_file(r"C:\Programming\Projects\Python\YHack\gui\audio.flac")
    # sound = sound.set_channels(1)
    # sound.export(r"C:\Programming\Projects\Python\YHack\gui\audio.flac")
    x = "C:\\Users\\rocha\\AppData\\Local\\Google\\Cloud_SDK\\google-cloud-sdk\\bin\\gsutil.cmd cp \"C:/Programming/Projects/Python/YHack/audio.flac\" gs://yhack-bucket/"
    os.system(x)
    print("done")


if __name__ == '__main__':
    get_mp3('https://www.youtube.com/watch?v=4WEQtgnBu0I')
