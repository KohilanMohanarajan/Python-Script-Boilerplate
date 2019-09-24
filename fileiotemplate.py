srcFile = 

# For read/write
with open(srcFile, "r") as f:
    data = f.readlines()
f.close()

# search data[i] for a specific line of the file

with open(srcFile, "w") as f:
    for line in data:
        f.write(line)
f.close()

# For read
f = open(srcFile, "r")
# Insert code here
f.close()

# For write
with open(srcFile, "w") as f:
    # Insert code here
    print("temp")
f.close()
