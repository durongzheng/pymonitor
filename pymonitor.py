#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, subprocess, argparse
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

application = ''
path = ''
process = None

class MyFileSystemEventHandler(FileSystemEventHandler):

    def __init__(self, fn):
        super(MyFileSystemEventHandler, self).__init__()
        self.restart = fn

    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            logging.info('Python source file changed: %s' % event.src_path)
            self.restart()

def start_process():
    global application, process
    command = 'python ' + application
    logging.info('Start process %s...' % command)
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

def kill_process():
    global process
    if process:
        logging.info('Kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        logging.info('Process ended with code %s.' % process.returncode)
        process = None

def restart_process():    
    kill_process()
    start_process()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('application',help='your python source file need to debug.')
    parser.add_argument('-p', dest='path', default='.', help='specify directory to monitor.')
    args = parser.parse_args()
    if os.path.exists(args.application)==False or os.path.isdir(args.path)==False:
        print('parameters error!')
        sys.exit()

    global application, path
    application = args.application
    path = args.path

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    parse_args()
    event_handler = MyFileSystemEventHandler(restart_process)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    start_process()
    
    try:
        while observer.isAlive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()