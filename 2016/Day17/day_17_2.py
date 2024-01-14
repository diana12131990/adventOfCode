import hashlib

Open = ["b","c","d","e","f"]
longest_path = 0

def FindPath(string,i,j):
    global longest_path
    
    if i == 3 and j == 3:
        if longest_path < len(string) - original_length:
            longest_path = len(string) - original_length
    else:
        code = hashlib.md5(string).hexdigest()
        if code[0] in Open and i != 0:
            FindPath(string+"U",i-1,j)
        if code[1] in Open and i < 3:
            FindPath(string+"D",i+1,j)
        if code[2] in Open and j != 0:
            FindPath(string+"L",i,j-1)
        if code[3] in Open and j < 3:
            FindPath(string+"R",i,j+1)

passcode = "udskfozm"
original_length = len(passcode)
FindPath(passcode,0,0)
print(longest_path)