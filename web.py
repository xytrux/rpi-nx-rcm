from flask import Flask, render_template, flash, jsonify
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage
from tinydb import TinyDB, Query
import sys
import os
class WebServer:
  app = Flask(__name__, static_folder='static')
  app.config.from_json(os.path.realpath('./config.json'))
  _port = 8181
  db = TinyDB(os.path.realpath('./database.json'), storage=CachingMiddleware(JSONStorage))
  def __init__(self, port=8181):
    self.port = port
    @self.app.route('/')
    def index():
      return render_template('page.html', lol=True)
    @self.app.route('/api/payloads')
    def get_payloads():
      payloads = self.db.all()
      return jsonify(payloads)
  def listen(self):
    self.app.run(host='0.0.0.0', port=self.port)

server = WebServer(port=8181)

def main():
  print('starting web server')
  server.listen()

if __name__ == "__main__":
  #print("This is meant to be run by the main watchdog script of nx-rcm.")
  #print("Please don\'t run this file directly.")
  #sys.exit(1)
  main()