import os

from flask import Flask, render_template, request, jsonify

from image_classifier import classify
# from pyimagesearch.colordescriptor import ColorDescriptor
# from pyimagesearch.searcher import Searcher


# create flask instance
app = Flask(__name__)


Model = os.path.join(os.path.dirname(__file__), 'model_weights.h5')
Model_weights = os.path.join(os.path.dirname(__file__), 'model_architecture.json')

# INDEX = os.path.join(os.path.dirname(__file__), 'index.csv')

# main route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    
    if request.method == "POST":

        # get url
        image_url = request.form.get('img')
        print(image_url)

        

        try:
            results=classify(Model_weights,Model,image_url)
            return jsonify(results=results)

           
            


        except:

            # return error
            return jsonify({"sorry": "Sorry, no results! Please try again."})







# run!
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
