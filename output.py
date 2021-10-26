import os


os.chdir(os.getcwd())


files = os.listdir(".")
buffer = ""
for file in files:
    if file is "output.py" or file is "addresses.txt":
        pass
    else:
        with open(".\\"+str(file), "r") as NFILE:
            for lines in NFILE.readlines():
                buffer+= str(lines)
    # print(file)
    # print(buffer)
    with open("addresses.txt", 'a') as NFILE:
        NFILE.writelines("\t\t\t\t"+str(file) + "\t\t\t\t\n\n\n\n")
        NFILE.writelines(buffer)
    buffer = ""

