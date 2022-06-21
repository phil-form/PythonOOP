#!/bin/python3

import cgi
from lxml.html.clean import clean_html

page = """
<!DOCTYPE html>
<html>
    <body>
        <h1>Balthazr Picsou super form!!!!</h1>
        <form action="form.py" method="post">
            <input type="text" name="myInput" value=""/>
        </form>
"""

print("Content-type: text/html; charset=utf-8\n")
print(page)

formData = cgi.FieldStorage()
# unsafe 
# print("<p>" + formData.getvalue('myInput') + "</p>")
# safe
# print("<p>" + clean_html(formData.getvalue('myInput')) + "</p>")
sanitziedData = str(formData.getvalue('myInput'))
# sanitize html characters
sanitziedData = sanitziedData.replace('<', '&lt;')
sanitziedData = sanitziedData.replace('>', '&gt;')
# remove <script> only
# sanitziedData = sanitziedData.replace('<script>', '&lt;script&gt;')
# sanitziedData = sanitziedData.replace('</script>', '&lt;/script&gt;')
print("<p>" + sanitziedData + "</p>")

print("""
    </body>
</html>
""")



