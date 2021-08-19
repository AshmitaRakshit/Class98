f = open("demoFile.txt", "rt")

#f = open("demoFile.txt", "r")
#print(f.read())

#f = open("demofile.txt", "r")
#print(f.readline())

#f = open("demofile.txt", "r")
#print(f.readline())
#print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)