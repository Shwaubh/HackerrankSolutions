import  math
def designerPdfViewer(h, word):
    ma = 0
    for i in word:
       # print(ord(i) - 65)
        if i.islower():
            ma = max(ma , h[ord(i) - 97])
        else:
            ma = max(ma , h[ord(i) - 65])
    return ma*len(word)


h = list(map(int, input().rstrip().split()))
word = input()
result = designerPdfViewer(h, word)
print(result)