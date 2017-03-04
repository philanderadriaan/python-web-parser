import urllib.request
import re
links = re.findall('<a href="(.*?)".*?>(.*?)</a>', str(urllib.request.urlopen('http://www.tacoma.uw.edu/institute-technology/institute-technology').read()))
file = open('output.csv', 'w')
file.write('Link,Text\n')
for i in range(0, len(links)):
    file.write(links[i][0] + ',' + links[i][1] + '\n') if len(links[i][0]) > 0 and len(links[i][1]) > 0 else None
file.close()
