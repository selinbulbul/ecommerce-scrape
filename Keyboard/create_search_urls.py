f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.de/-/en/s?k=keyboard+pc&i=computers&crid=H16NJZ6SFTOT&qid=1625652986&sprefix=keyboard%2Caps%2C222&ref=sr_pg_1'
f.write(url)
f.write('\n')


for i in range(2,51):
    url = 'https://www.amazon.de/-/en/s?k=keyboard+pc&i=computers&page=' + str(i) + '&crid=H16NJZ6SFTOT&qid=1625653106&sprefix=keyboard%2Caps%2C222&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()