print("Welcome to your Script boilerplate.  Please choose an option:")

scripttype = ''

while (scripttype != "a" and scripttype != "b"):
    print("(a) Scraper template")
    print("(b) File I/O template")
    scripttype = input("Type 'a' or 'b': ").rstrip()

    if (scripttype != "a" and scripttype != "b"):
        print("Invalid input!  Expected: 'a' or 'b'.")

if (scripttype == 'a'):
    print("User chose: Scraper template")
    srcUrl = input("Please type in the url of the webpage that you wish to scrape: ")
    print("User chose to scrape:" + srcUrl)
    scrapewMonths = ''
    monthsChoice = False
    print("Scrape over multiple months?")
    while (scrapewMonths != "y" and scrapewMonths != "n"):
        print("(y) Yes")
        print("(n) No")
        scrapewMonths = input("Type 'y' or 'n': ").rstrip()

        if (scrapewMonths != "y" and scrapewMonths != "n"):
            print("Invalid input!  Expected: 'y' or 'n'.")
    if (scrapewMonths == 'y'):
        print("User chose to scrape over multiple months")
        monthsChoice = True 
    else:
        print("User chose not to scrape over multiple months")

    fName = input("Please type in the name for your file: ")

    if (".py" not in fName):
        fName = fName + ".py"

    print("Generating " + fName + "...")

    with open("scrapertemplate.py", "r") as f:
        data = f.readlines()
    f.close()

    if ("https://" not in srcUrl):
        if ("http://" not in srcUrl):
            srcUrl = "https://" + srcUrl

    data[5] = data[5][:-2] + " '" + srcUrl + "'\n"

    if (not monthsChoice):
        for i in range(0, 3):
            del data[7]

    with open(fName, "w") as f:
        for line in data:
            f.write(line)
    f.close()

    print("File generated.  Thanks for using boilerplate.")


else:
    print("User chose: File I/O template")
    srcFile = input("Please type in the name of the file that you wish to scrape:")

    ioType = ''

    print("What kind of access would you like?:")
    while (ioType != "a" and ioType != "b" and ioType != "c"):
        print("(a) Read/Write")
        print("(b) Read")
        print("(c) Write")
        ioType = input("Type 'a' or 'b' or 'c': ").rstrip()

        if (ioType != "a" and ioType != "b" and ioType != "c"):
            print("Invalid input!  Expected: 'a' or 'b' or 'c'.")

    fName = input("Please type in the name for your file: ")

    if (".py" not in fName):
        fName = fName + ".py"

    print("Generating " + fName + "...")

    with open("fileiotemplate.py", "r") as f:
        data = f.readlines()
    f.close()

    data[0] = data[0][:-2] + " '" + srcFile + "'\n"

    if (ioType == 'a'):
        for i in range(0, 10):
            del data[14]
    elif (ioType == 'b'):
        for i in range(0, 12):
            del data[2]
        for i in range(0, 5):
            del data[7]
    else:
        for i in range(0, 16):
            del data[14]

    with open(fName, "w") as f:
        for line in data:
            f.write(line)
    f.close()

    print("File generated.  Thanks for using boilerplate.")