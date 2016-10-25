# importing necessary libraries

import ConfigParser , os

from flask import Flask, render_template, request, redirect, flash, url_for
app = Flask(__name__)
app.secret_key = 'supersecret'

from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

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


# uploading images function that uses an external library to store files under
# their original name. Addition of a message flashing feature to indicate to the users the successful
# upload of their images


@app.route("/upload/", methods=['POST','GET'])
def upload():
  if request.method == 'POST':
     f= request.files['datafile']
     filename = secure_filename(f.filename)
     f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
     flash('Image uploaded successfully!')
     return redirect(url_for('uploaded'))
  else:
     uploads = os.listdir('static/uploads/')
     page = render_template('upload-service.html', uploads = uploads)
     return page, 200


# function that helps us retrieve the template with the flashed message and
# redirects us again to the upload-service.html template to see the updated
# photo collection after the latest user upload

@app.route('/upload-successful')
def uploaded():
  return redirect(url_for('upload'))



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
