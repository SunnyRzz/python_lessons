file = open("teams.txt", "w")

teams=["Manchester united", "Arsenal","Man City", "Chelsea", "Liverpool"]

for x in teams:
    newline = x + " FC" + "\n"
    #print(newline)
    file.write(newline)

file.close

file = open("teams.txt", "r")

lines = file.readlines()
print(lines[0].strip("\n"))
print(lines[3].strip("\n"))

lines[0] = "This is a newline\n"

file = open("teams.txt", "w")
file.writelines(lines)

file.close()

file= open("teams.txt", "r")
print(file)

file.close
