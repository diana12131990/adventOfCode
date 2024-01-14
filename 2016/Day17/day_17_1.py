import hashlib

Open = ["b","c","d","e","f"]
shortest_path_length = -1
shortest_path = ""

def FindPath(string,i,j):
    global shortest_path_length
    global shortest_path
    
    if i == 3 and j == 3:
        if shortest_path_length == -1 or shortest_path_length > len(string) - original_length + 1:
            shortest_path_length = len(string) - original_length + 1
            shortest_path = string[original_length:]
    else:
        if shortest_path_length == -1 or shortest_path_length > len(string) - original_length + 1:
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
print(shortest_path)