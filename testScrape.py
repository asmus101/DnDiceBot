import openpyxl, requests, bs4, os

url = 'http://thebombzen.com/grimoire/spells/abi-dalzims-horrid-wilting'

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

for script in soup(['script', 'style']):
    script.extract()

text = soup.get_text()
print(text)

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
