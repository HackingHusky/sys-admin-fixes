import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

# Check if GPU is available and disable it
if tf.config.list_physical_devices('GPU'):
    tf.config.set_visible_devices([], 'GPU')

# Generate dummy data
X_train = np.random.rand(1000, 20)
y_train = np.random.randint(2, size=(1000, 1))

# Define the model
model = Sequential([
    Dense(64, input_dim=20, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model
loss, accuracy = model.evaluate(X_train, y_train)
print(f'Loss: {loss}, Accuracy: {accuracy}')

# Note: If you're running the model locally without a CPU, use a text dataset in the order of 10 MB.

# Save the model state
import torch
PATH = 'model.pth'
torch.save(model.state_dict(), PATH)
