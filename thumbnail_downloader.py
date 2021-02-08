from os import system
url = input('Enter YouTube video Link: ')
url = url.split('/')
url = str(url[3])
system(f'wget -O {url}.jpg http://img.youtube.com/vi/{url}/maxresdefault.jpg > /dev/null 2>&1')
print('Thumbnail Downloaded')
