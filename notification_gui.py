import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.models import load_model
from plyer import notification
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
from tensorflow.keras.preprocessing import image


# This is the Function to predict animal name and emotion (attempt 5)
def predict_emotion():
    file_path = filedialog.askopenfilename()
    img = image.load_img(file_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    animal_name = file_path.split('/')[-2]
    emotion = class_to_emotion[predicted_class]
    result_label.config(text=f"{animal_name.capitalize()} is {emotion.capitalize()}")

# Tkinter part
root = tk.Tk()
root.title("Animal Type and Emotion Recognition By Wasim")
select_button = tk.Button(root, text="Click to Upload the image ", command=predict_emotion)
select_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# model loading
model = load_model('animal_emotion_model.h5')

class_to_emotion = {0: 'Angry', 1: 'Sad', 2: 'Other', 3: 'Happy'}

root.mainloop()
