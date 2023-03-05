from numpy import loadtxt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import model_from_json

dataset =loadtxt ('pima-indians-diabetes.csv', delimiter=',')
x = dataset [:,0:8]
y = dataset [:,8]

#loading the model file:
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model= model_from_json(loaded_model_json)
model.load_weights("model.h5")
print ("loaded")

predictions= model.predict_classes(x)#pred for complete dataset
for i in range (5,10): #5th tp 10th row
    print ('%s=> %d (expected %d)' % (x[i].tolist(), predictions[i], y[i]))

