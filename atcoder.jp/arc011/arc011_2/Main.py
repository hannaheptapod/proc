N = int(input())
w = list(input().split(' '))

dic = {
    'b': '1', 'B': '1', 'c': '1', 'C': '1',
    'd': '2', 'D': '2', 'w': '2', 'W': '2',
    't': '3', 'T': '3', 'j': '3', 'J': '3',
    'f': '4', 'F': '4', 'q': '4', 'Q': '4',
    'l': '5', 'L': '5', 'v': '5', 'V': '5',
    's': '6', 'S': '6', 'x': '6', 'X': '6',
    'p': '7', 'P': '7', 'm': '7', 'M': '7',
    'h': '8', 'H': '8', 'k': '8', 'K': '8',
    'n': '9', 'N': '9', 'g': '9', 'G': '9',
    'z': '0', 'Z': '0', 'r': '0', 'R': '0',
    'a': '', 'e': '', 'i': '', 'o': '', 'u': '', 'y': '',
    'A': '', 'E': '', 'I': '', 'O': '', 'U': '', 'Y': '', '.': '', ',': '',
    ' ': ' '
}

ans = []
for wi in w:
    s = ''
    for wij in wi: s += dic[wij]
    
    if s: ans.append(s)

print(*ans)
