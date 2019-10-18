import os
import http.server
import socketserver

def readFile(name = 'base.html'):
    f = open(name, 'r')
    data = f.read()
    f.close()
    return data

def writeFile(contents, name= 'index.html'):
    f = open(name, 'w')
    f.write(contents)
    f.close()

def getPhotoList(path = 'pics'):
    pics = os.listdir( os.path.join(os.path.dirname(__file__), path) )
    pics2 = []
    for pic in pics:
        if pic != '.README':
            pics2.append('"%s/%s"'% (path, pic))
    return '[' + ','.join(pics2) + ']'

def confWall():
    html = readFile()
    images = getPhotoList()
    newhtml = html.replace(
        '<script></script>',
        '<script>images = %s;</script>' % images
        )
    writeFile(newhtml)

if __name__ == '__main__':
    confWall()
    port = 8000
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", port)
        httpd.serve_forever()

    print(f"serving at port {port}")
    print("ctrl + c to quit")
    httpd.serve_forever()

