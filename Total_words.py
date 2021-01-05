def total_words(contents):
    with open(contents,"r") as f:
        count = f.read()
        count.replace(","," ")
        print("Total number of words:{}" .format(len(count.split())))

total_words("File1.txt")
total_words("File2.txt")

    