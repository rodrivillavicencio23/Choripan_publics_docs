pilotes = [
    ['p', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['p', '-', '-', 'p', '-', '-', '-', '-', '-', '-'],
    ['p', '-', '-', 'p', '-', '-', '-', '-', 'p', '-'],
    ['p', '-', '-', 'p', '-', 'p', '-', 'p', 'p', 'p'],
    ['p', '-', '-', 'p', '-', 'p', '-', 'p', 'p', 'p'],
    ['p', '-', '-', 'p', '-', 'p', '-', 'p', 'p', 'p'],
]
def emparejar_pilotes(pilotes):
    example = ['-']*len(pilotes[0])
    fla = pilotes[len(pilotes)-1]
    a = len(pilotes)

    for b in range(len(pilotes)):
        print(pilotes[b])
        print(example)
        if pilotes[b] != fla:
            pilotes[b] = example

emparejar_pilotes(pilotes)

print("cabrontunove")
for c in pilotes:
    print(c)
