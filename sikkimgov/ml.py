import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# # Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# # Load the model
model = tensorflow.keras.models.load_model (r'C:\Users\HP\sikkimgov\sikkimgov\keras_model.h5')

# # Create the array of the right shape to feed into the keras model
# # The 'length' or number of images you can put into the array is
# # determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# # Replace this with the path to your image


# #resize the image to a 224x224 with the same strategy as in TM2:
# #resizing the image to be at least 224x224 and then cropping from the center


# #turn the image into a numpy array


# # display the resized image
# # image.show()

# # Normalize the image


# # Load the image into the array


# # run the inference



def throw_result(path):
    image = Image.open(path)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    output = list(prediction[0])
    indx = output.index(max(output))
    print('INDEX', indx)


    if indx == 0:
        prediction = 'PHASE_1'
    elif indx == 1:
        prediction = 'PHASE_2'
    elif indx == 2:
        prediction = 'PHASE_3'
    elif indx == 3:
        prediction = 'PHASE_4'
    elif indx == 4:
        prediction = 'PHASE_5'
    else:
        prediction = 'PHASE_6'
        
    return prediction