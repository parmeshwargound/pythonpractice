from lxml import html
import requests





page = requests.get("http://www.megavenues.com/pune/wedding-halls")
tree = html.fromstring(page.content)

print(tree)
