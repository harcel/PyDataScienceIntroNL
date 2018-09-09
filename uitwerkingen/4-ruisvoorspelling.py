# De uitwerking van 4-autoencoder.py moet hiervoor gedraaid worden!

voorspeller = tf.keras.models.Sequential([
  tf.keras.layers.Dense(200, activation=tf.nn.relu),
  tf.keras.layers.Dense(50, activation=tf.nn.relu),
  tf.keras.layers.Dense(50, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

voorspeller.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

voorspeller.fit(xtr, ytr, epochs=10)
print(voorspeller.evaluate(xtr, ytr))
print("Performance op ruizige getallen:")
print(voorspeller.evaluate(xruis, y))
print("Performance van hetzelfde netwerk op door auto-encoder gereconstrueerde getallen:")
print(voorspeller.evaluate(reconstructed, y))
print("Als het goed is, flinke winst!")
