<html>
  <body>
    <header><h1></h1></header>
    <div><span><h1 name="title">This is the title.</h1></span></div>
    <footer><h1></h1></footer>
  </body>
</html>

###test if attribute exists

html = soup.find('html')
for element in table.findAll('h1'):
          if element.has_attr('name'):
            print('element')
#>> <h1 name="title">This is the title.</h1>


###isolate tags with specific class

h1 = soup.findAll('h1', {'name': 'title'})
print(h1)
#>> <h1 name="title">This is the title.</h1>


###get tag attribute class

div = soup.find('div')
h1 = div.find('h1'):
print(h1.get('name')))
#>> title
