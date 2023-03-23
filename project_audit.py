# Created by Logan Miller
# 03/22/2023

import os

projectDir = input("Enter the project directory: ")

# Find all of the files within the project directory
projectFiles = os.listdir(projectDir)

# Capture the number of files in the project directory
numFiles = len(projectFiles)

# Capture the number of lines of each file
numLines = 0

for file in projectFiles:
    #ignore git folder and gitignore file
    if file == ".git" or file == ".gitignore" or file == "bin" or file == "node_modules" or file == "package-lock.json" or file == "package.json" or file == "yarn.lock":
        continue
    with open(projectDir + "/" + file, "r+") as f:
        for line in f:
            numLines += 1

# Capture the number of each file type
numPython = 0
numJava = 0
numC = 0
numCpp = 0
numHtml = 0
numCss = 0
numPug = 0
numTxt = 0
numCfg = 0
numCss = 0
numJs = 0
numPhp = 0
numSql = 0
numOther = 0

for file in projectFiles:
    if file.endswith(".py"):
        numPython += 1
    elif file.endswith(".java"):
        numJava += 1
    elif file.endswith(".c"):
        numC += 1
    elif file.endswith(".cpp"):
        numCpp += 1
    elif file.endswith(".html"):
        numHtml += 1
    elif file.endswith(".css"):
        numCss += 1
    elif file.endswith(".pug"):
        numPug += 1
    elif file.endswith(".txt"):
        numTxt += 1
    elif file.endswith(".cfg"):
        numCfg += 1
    elif file.endswith(".js"):
        numJs += 1
    elif file.endswith(".php"):
        numPhp += 1
    elif file.endswith(".sql"):
        numSql += 1
    else:
        numOther += 1

# Print the results of the audit pretty

print("Project Audit Results")
print("Number of files: " + str(numFiles))
print("Number of lines: " + str(numLines))

# Print the number of each file type in a table format
print("File Type\t\tNumber of Files")
print("Python\t\t\t" + str(numPython))
print("Java\t\t\t" + str(numJava))
print("C\t\t\t" + str(numC))
print("C++\t\t\t" + str(numCpp))
print("HTML\t\t\t" + str(numHtml))
print("CSS\t\t\t" + str(numCss))
print("Pug\t\t\t" + str(numPug))
print("Text\t\t\t" + str(numTxt))
print("Config\t\t\t" + str(numCfg))
print("Cfg\t\t\t" + str(numCfg))
print("JavaScript\t\t" + str(numJs))
print("PHP\t\t\t" + str(numPhp))
print("SQL\t\t\t" + str(numSql))
print("Other\t\t\t" + str(numOther))

# Wait for user to close the program
input("Press enter to close the program...")
