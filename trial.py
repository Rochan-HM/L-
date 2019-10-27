import pygsheets
import pandas as pd
from googlesearch import search

gc = pygsheets.authorize(client_secret=r"C:/Programming/Projects/Python/YHack/credentials.json",
                         service_file=r"C:/Programming/Projects/Python/YHack/credentials_2.json")

df = pd.DataFrame()

query = []
definition = []
links = []


def fix(s):
    s = str(s)
    s = s.replace(r'"', r'\"')
    return s


def formatter(file_name):
    file = open(file_name, "r")
    string = file.read().strip()
    # string = "".join([s for s in string.splitlines(True) if s.strip("\r\n")])
    l = string.split('\n')

    for i in range(len(l)):
        s = l[i].split(": ")
        print(s)
        query.append(s[0])
        definition.append(s[1])
        temp = []
        for j in search(query[i], tld="com", num=3, start=0, stop=3, pause=2.0):
            temp.append(j)
        links.append(temp)
        print(links)

    open(r"C:\Programming\Projects\Python\YHack\input.json", "w").close()
    with open(r"C:\Programming\Projects\Python\YHack\input.json", 'a+') as file:
        for z in range(0, len(query)):
            if z == 0:
                file.write("[" + '\n' + "{\n"
                                        '"' + query[z] + '"' + ": " + '"' + fix(definition[z]) + "|" + links[z][
                               0] + "|" +
                           links[z][1] + "|" +
                           links[z][
                               2] + '"\n},' + '\n')
            elif z == len(query) - 1:
                file.write("{\n" +
                           '"' + query[z] + '"' + ": " + '"' + fix(definition[z]) + "|" + links[z][0] + "|" + links[z][
                               1] + "|" +
                           links[z][
                               2] + '"\n}' + '\n' + "]")
            else:
                file.write("{\n" +
                           '"' + query[z] + '"' + ": " + '"' + fix(definition[z]) + "|" + links[z][0] + "|" + links[z][
                               1] + "|" +
                           links[z][
                               2] + '"\n},' + '\n')


def text_format(file_name):
    formatter(file_name)
    link1 = []
    link2 = []
    link3 = []
    for x in links:
        link1.append(x[0])
        link2.append(x[1])
        link3.append(x[2])
    df['Word'] = query
    df['Meaning'] = definition
    df['Link 1'] = link1
    df['Link 2'] = link2
    df['Link 3'] = link3

    sh = gc.open('Converted Sheet')

    wks = sh[0]
    wks.set_dataframe(df, (1, 1))


if __name__ == '__main__':
    text_format("dictionary.txt")
