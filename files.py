with open("File1.txt","w") as f:
    f.write("A text file is a computer file that only contains text and has no special formatting such as bold text, italic text, images, etc. With Microsoft Windows computers text files are identified with the .txt file extension, as shown in the example picture")


with open("File1.txt","r") as f:
    content = f.read().splitlines()
    print(content)

