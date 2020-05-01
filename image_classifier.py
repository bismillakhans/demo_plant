from keras.models import model_from_json
import cv2
import numpy as np


def classify(model_json,model,im):
	# Model reconstruction from JSON file
	with open(model_json, 'r') as f:
		model_from = model_from_json(f.read())

	# Load weights into the new model
	model_from.load_weights(model)

	image=cv2.imread(im)
	default_image_size = tuple((256, 256))
	image=cv2.resize(image,default_image_size)


	x = np.expand_dims(image, axis=0)
	pp=model_from.predict(x)
	clas = np.argmax(pp,axis=1)
	arr=['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
	       'Potato___Early_blight', 'Potato___Late_blight',
	       'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight',
	       'Tomato_Late_blight', 'Tomato_Leaf_Mold',
	       'Tomato_Septoria_leaf_spot',
	       'Tomato_Spider_mites_Two_spotted_spider_mite',
	       'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus',
	       'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
	return arr[clas[0]]
