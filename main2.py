import get_words
import dictionary
import trial
import sys
import docx2txt


s = str(sys.argv[1])
content = ""
if s.endswith(".txt"):
    with open(s, "r") as file:
        content = file.read()
elif s.endswith(".doc"):
    content = docx2txt.process(s)
elif s.endswith(".docx"):
    content = docx2txt.process(s)
else:
    sys.exit(1)

with open("input.txt", "w") as file:
    file.write("%s" % content)
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
