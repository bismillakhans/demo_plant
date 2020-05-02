import os
from keras.models import model_from_json

from flask import Flask, render_template, request, jsonify,send_from_directory

from image_classifier import classify
import cv2


# create flask instance
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))




# main route
@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/search', methods=['POST'])
def search():

    
    if request.method == "POST":

        # get url
        
        image_url = APP_ROOT+request.form.get('img')
        print(image_url)



        results=classify(image_url)
        return jsonify(results=results)



@app.route("/uploads", methods=["POST","GET"])
def upload():
    if request.method == "POST":
        target = os.path.join(APP_ROOT, 'uploads/')
        print(target)
        if not os.path.isdir(target):
            os.mkdir(target)
        else:
            print("Couldn't create upload directory: {}".format(target))
        print(request.files.getlist("file"))
        for upload in request.files.getlist("file"):
            print(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            destination = "/".join([target, filename])
            print("Accept incoming file:", filename)
            print("Save it to:", destination)
            upload.save(destination)

    image_names = os.listdir('./uploads')
    print(image_names)
    return render_template("index.html", image_names=image_names)


@app.route('/uploads/<filename>')
def send_image(filename):
    return send_from_directory("uploads", filename)


# run!
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
