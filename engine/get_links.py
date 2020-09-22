from googlesearch import search


def fix(s):
    s = str(s)
    s = s.replace(r'"', r'\"')
    return s


def text_format(file_name):
    file = open(file_name, "r")
    string = file.read().strip()
    # string = "".join([s for s in string.splitlines(True) if s.strip("\r\n")])
    l = string.split('\n')
    query = []
    definition = []
    links = []

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


if __name__ == '__main__':
    text_format('dictionary.txt')
