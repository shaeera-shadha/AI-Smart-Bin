import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Dataset path (update with your dataset folder)
train_dir = "data/train"
val_dir = "data/val"

img_size = (128, 128)

train_gen = ImageDataGenerator(rescale=1./255)
val_gen = ImageDataGenerator(rescale=1./255)

train_data = train_gen.flow_from_directory(train_dir, target_size=img_size, batch_size=32, class_mode="categorical")
val_data = val_gen.flow_from_directory(val_dir, target_size=img_size, batch_size=32, class_mode="categorical")

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation="relu", input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(5, activation="softmax")  # 5 categories
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(train_data, validation_data=val_data, epochs=10)

model.save("waste_model.h5")
