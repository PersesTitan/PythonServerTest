def op(file_name):
    total = ""
    file = open("html/" + file_name, "r")
    for line in file.readlines():
        total += line
    file.close()
    return total

