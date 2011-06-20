import os
import SimpleHTTPServer
import SocketServer

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
	html = []
	for pic in pics:
		if pic != '.README':
			html.append('<img width="100%%" src="%s/%s" />'% (path, pic))
	return ''.join(html)

def confWall():
	html = readFile()
	images = getPhotoList()
	print images
	newhtml = html.replace(
			'<div class="slideshow"></div>', 
			'<div class="slideshow">%s</div>' % images)
	print newhtml
	writeFile(newhtml)

if __name__ == '__main__':
	confWall()
	port = 8000
	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer(("", port), Handler)

	print "serving at port %s"% port
	print "ctrl + c to quit"
	httpd.serve_forever()

