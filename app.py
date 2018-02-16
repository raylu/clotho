#!/usr/bin/env python3

import fast_lib
import slow_lib

def app(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/plain')])
	return [('cow = %s\n' % fast_lib.cow).encode('utf-8')]

def main():
	import wsgiref.simple_server
	server = wsgiref.simple_server.make_server('0.0.0.0', 8000, app)
	print('listening on port 8000')
	server.serve_forever()

if __name__ == '__main__':
	main()
