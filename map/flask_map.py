# parse a text file and send that data to the javascript
import flask
from flask import request
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY


###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
	app.logger.debug("Main page entry")
	# A list of dictionaries
	points = []
	file = open("Points_of_Interest.txt", "r")
	# Parse file
	for line in file:
		line_parts = line.split(',')
		title = line_parts[0].strip('\n').strip(' ')
		lat = line_parts[1].strip('&#39;').strip('\n').strip(' ')
		lon = line_parts[2].strip('&#39;').strip('\n').strip(' ')
		points.append({'title': title, 'lat': lat, 'lon': lon});
	# Send dev_key and points list to client side
	flask.g.points = points
	flask.g.dev_key = CONFIG.DEV_KEY

	return flask.render_template('map.html')



if __name__ == "__main__":
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT, host="127.0.0.1")




