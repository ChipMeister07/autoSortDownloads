# Importing required modules
import glob
import os 
import re

# Gets the user to input the location of their download folder
downloadFolder = input("Please input the location of your download folder: ")

# Gets all the files within the download folder before its been sorted
initialFiles = glob.glob(downloadFolder + "\\*")

# removes the download link from the start so we only have the file
count = 0

for x in initialFiles:
    initialFiles[count] = x.removeprefix(downloadFolder + "\\")
    count += 1

# creates an array to keep track of all stored and discovered file types.
fileTypes = []

# Looping through the intialfiles to extract their file types using regular expressions.
for x in initialFiles:
    try:
        match = re.search("\.[0-9a-zA-Z]+$", x).group()
    except:
        print("Found a folder instead of a file")
        pass

    if match in fileTypes:
        pass
    else:
        fileTypes.append(match)

# create the folders for the file types
for x in range(len(fileTypes)):
    # try to create the directory, if it already exists then pass
    try:
        os.mkdir(downloadFolder + "\\" + fileTypes[x])
        pass
    except Exception as e:
        pass

# move the file to the folder that matches their file type
for x in initialFiles:
    try: 
        os.rename(downloadFolder + "\\" + x, downloadFolder + "\\" + re.search("\.[0-9a-zA-Z]+$", x).group() + "\\" + x)
    except Exception as e:
        print(e)


# if the above runs without error it prints a success message
print("Successful")

# the program will now constantly run until the while loop is breaked
while True:

    amountOfFiles = len(initialFiles)
    initialFiles = glob.glob(downloadFolder + "\\*")

    print(initialFiles)

    if len(initialFiles) > amountOfFiles:
        for x in initialFiles:
            print(x)
            if re.search("\.[0-9a-zA-Z]+$", x) == None:
                pass
            else:
                match = re.search("\.[0-9a-zA-Z]+$", x).group()
                if match in fileTypes:
                    os.rename(x, downloadFolder + "\\" + re.search("\.[0-9a-zA-Z]+$", x).group() + "\\" + x.removeprefix(downloadFolder + "\\"))
                    pass
                else:
                    fileTypes.append(match)
                    os.mkdir(downloadFolder + "\\" + match)
                    os.rename(x, downloadFolder + "\\" + match + "\\" + x.removeprefix(downloadFolder + "\\"))
                    break
    else:
        pass

#Either remove prefix from file or work around it you mong!