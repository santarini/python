
#prints all TRs in a table
table = soup.findAll('table')[3]
for row in table.findAll('tr'):
  print(row)
 
#prints each TR and each child tag in TR
table = soup.findAll('table')[3]
for row in table.findAll('tr'):
  for line in row.findAll():
    print(line)
