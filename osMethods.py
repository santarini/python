import os

#os.makedirs()
#creates a path (ie. creates a directories and/or files)

#os.path.join()
#creates a path formatted for your OS
#print(os.path.join('Users', 'UserName', 'Desktop')) and os.path.join('Users', 'UserName', 'Desktop') return two entirely seperate values
os.path.join('Users', 'UserName', 'Desktop')

#os.getcwd()
#gets current working directory
print(os.getcwd())

#os.chdir()
#changes current working directory

#os.path.basename(path)
#returns path base name (end file or directory)
#everything after the last slash

#os.path.relpath(finish, start)
#returns the relative path from two points

#os.path.dirname(path)
#returns path directory names (parent folders)
#everything before the last slash

#os.path.exists(path)
#tests if path exists

#os.path.isfile(path)
#tests if path leads to file

#os.path.isdir(path)
#tests if path leads to directory
