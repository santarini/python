###################
#check if list of values are in string

ext = [".com", ".org", ".net"]
url = "www.google.com"
if any(x in url for x in ext):
     print("Valid URL")

######################
#check if list of values are NOT in string

ext = [".com", ".org", ".net"]
url = "Cinnamon Toast Crunch"
if not(any(x in url for x in ext)):
     print("Invalid URL")
