# importing necessary libraries

import ConfigParser

from flask import Flask, render_template, request
app = Flask(__name__)

# routing to individual pages

@app.route("/")
def root():
  return render_template('pamela-love.html'), 200


@app.route("/pamela-love/")
def pl():
  return render_template('pamela-love.html'), 200


@app.route("/mania-mania/") 
def mm():
  return render_template('mania-mania.html'), 200


@app.route("/eilisain-jewelry/")
def ej():
  return render_template('eilisain.html'), 200


@app.route("/blood-milk-jewels/")
def bmj():
  return render_template('blood-milk-jewels.html'), 200


@app.route("/omnia-oddities/")
def oo():
  return render_template('omnia-oddities.html'), 200

# custom error handling

@app.errorhandler(404)
def page_not_found(error):
  return render_template('errorPage.html'), 404

# GET-POST requests using a feedback form

@app.route("/contactUs/", methods=['POST','GET'])
def contactUs():
  if request.method == 'POST':
    print request.form
    name = request.form['first_name']
    return render_template('POST-response.html', name = name)
  else:
    page = render_template('contactUs.html')
    return page


# parsing configuration details from an external file

def init (app):
  config = ConfigParser.ConfigParser()
  try:
    config_location = "etc/defaults.cfg"
    config.read(config_location)

    app.config['DEBUG'] = config.get("config", "debug")
    app.config['ip_address'] = config.get("config", "ip_address")
    app.config['port'] = config.get("config", "port")
    app.config['url'] = config.get("config", "url")
  except:
    print "Could not read configuration file from: " , config_location


# initialisation function

if __name__ == "__main__":
  init(app)
  app.run(
    host = app.config['ip_address'],
    port = int(app.config['port']))
