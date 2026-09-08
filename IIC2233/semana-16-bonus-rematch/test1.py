import wikipedia


text = wikipedia.page("Gulf War", auto_suggest=False).content

try:
    print(text[:3000], '...')
except Exception:
    print("no existe . . .")

print("-" * 30, "\n" ,"-" * 30 )


try:
    count = 1
    for line in text.split('\n'):
        for sentence in line.split('.'):
            x = sentence.find("Iraq ")
            if x != -1:
                for pais in ["Kuwait", "Iran"]:
                    y = sentence.find(pais, x)
                    if y != -1:
                        print("{}. {}".format(count, sentence))
                        count += 1
                        break
except Exception:
    print("error")

    