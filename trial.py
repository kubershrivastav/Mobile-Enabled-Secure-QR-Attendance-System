import numpy as np
from keras.preprocessing import image
import os
save_path = '.'
from tensorflow.keras.models import load_model
import math

model = load_model(os.path.join(save_path,"liveness.h5"))
print(model)
# Load the image taken from camera
img_path = 'C:/Users/singh/OneDrive/Documents/Mobile_Integrated Attandence system/received.jpg'
img = image.load_img(img_path, target_size=(128, 128))

# Preprocess the image
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normalize the image

# Make prediction
prediction = model.predict(img_array)

# Print prediction
if prediction<0.5:
    print("Real")
    print("Probability of being a real image:", round(100*(1 - prediction[0][0]),2),'%')
else:
    print("Spoof")
    print("Probability of being a spoofed image:", round(100*(prediction[0][0]),2),'%')