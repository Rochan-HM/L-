import get_words
import Speech2Text
import download_vid
import dictionary
import trial
import sys

# s = input("Please input Youtube URL: ")
# s = r"https://www.youtube.com/watch?v=Ay1DYoeg9tc"
s = sys.argv[1]

with open("C:/Programming/Projects/Python/YHack/gui/link.txt", "w+") as file:
    file.write(s)

download_vid.get_mp3(s)
transcript = Speech2Text.sample_long_running_recognize("gs://yhack-bucket/audio.flac")
with open("input.txt", "w") as file:
    file.write("%s" % transcript)
words = get_words.main()
open("dictionary.txt", "w").close()
with open("dictionary.txt", "a+") as file:
    for word in words:
        t = dictionary.main(word)
        if t is not None:
            file.write(word + ": " + t + "\n")
            print(word + ": " + t)
    file.close()

trial.text_format(r"C:\Programming\Projects\Python\YHack\dictionary.txt")
print("done json")
