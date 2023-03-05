from numpy import loadtxt #handles excel
from tensorflow.keras import Sequential #creates empty layers (hidden layers)
from tensorflow.keras.layers import Dense #type of layer
from tensorflow.keras.models import model_from_json #save the model

dataset =loadtxt ('pima-indians-diabetes.csv', delimiter=',')
x = dataset [:,0:8]
y = dataset [:,8]
#print (x)
model = Sequential()#empty layer stacks
model.add(Dense(12, input_dim=8, activation='relu'))#12-no of nuerons, 8 inputs
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
#model.summmary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])#compiles
model.fit(x,y, epochs=5, batch_size=10)#trains the model,better accuracy epoch inc
_, accuracy = model.evaluate(x,y)#for better overall accuracy
print ('accuracy=%.2f'%(accuracy*100))

#saving the model:
model_json=model.to_json()
with open ("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print ("saved")
