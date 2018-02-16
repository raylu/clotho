#!/usr/bin/env python3

import os
import sys
import wsgiref.simple_server
import _thread

import inotify
from inotify import IN

def slow_imports():
	import slow_lib

def main():
	slow_imports()
	while True:
		worker_pid = os.fork()
		if worker_pid == 0:
			worker()
		os.waitpid(worker_pid, 0)
		print('respawning worker...')

def worker():
	import app

	server = wsgiref.simple_server.make_server('0.0.0.0', 8000, app.app)
	_thread.start_new_thread(watcher, ())
	print('listening on port 8000')
	server.serve_forever()

def watcher():
	fd = inotify.init()
	wds = {}
	for name, mod in sys.modules.items():
		try:
			filepath = mod.__file__
		except AttributeError:
			continue
		wd = inotify.add_watch(fd, filepath, IN.CLOSE_WRITE)
		wds[wd] = filepath

	for event in inotify.get_events(fd):
		print(wds[event.wd], 'changed')
	print('reloading...')
	os._exit(0)

if __name__ == '__main__':
	main()
