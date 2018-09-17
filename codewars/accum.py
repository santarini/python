def leopard(string):
     i = 0
     y = ""
     while i < len(string):
          if i < len(string) -1:
               x = string[i]*(i+1) + "-"
               y = y + x.capitalize()
               i += 1
          else:
               x = string[i]*(i+1)
               y = y + x.capitalize()
               i += 1
     return y
