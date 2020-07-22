import os
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import tensorflow.python.framework.dtypes
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image

# from keras.layers.convolutional import MaxPooling2D, Convolution2D
# from keras.layers.core import Flatten, Dense


classifier = Sequential()
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))
classifier.add(Flatten())
classifier.add(Dense(128, activation = 'relu'))    # hidden layer 



classifier.add(Dense(12, activation = 'softmax'))

classifier.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory('/home/saurav/Desktop/sih/sikkimgov/dataset/training_set', target_size=(64, 64), batch_size=32, class_mode='binary')

test_set = test_datagen.flow_from_directory('/home/saurav/Desktop/sih/sikkimgov/dataset/test_set', target_size=(64, 64), batch_size=32, class_mode='binary')

# training the model 

classifier.fit_generator(train_set,steps_per_epoch=80,epochs=5, validation_data=test_set,validation_steps=800)




def throw_result(path):
    test_image = image.load_img(path, target_size = (64, 64)) 
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict_classes(test_image)
    train_set.class_indices

    if result[0] == 0:
        prediction = 'PHASE_1'
        # print('PHASE_1')
    elif result[0] == 1:
        prediction = 'PHASE_2'
        # print('PHASE_2')
    elif result[0] == 2:
        prediction = 'PHASE_3'
        # print('PHASE_3')
    elif result[0] == 3:
        prediction = 'PHASE_4'
        # print('PHASE_4')
    elif result[0] == 4:
        prediction = 'PHASE_5'
        # print('PHASE_5')
    else:
        prediction = 'PHASE_6'
        # print('PHASE_6')

    return prediction