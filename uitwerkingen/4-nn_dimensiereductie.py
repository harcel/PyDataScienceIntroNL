# De eigenlijk-niet-encoder wordt getraind als voorspeller van labels
# Gebruik dus in ieder geval softmax als laatste activation function.

nep_encoder = tf.keras.models.Sequential([
  tf.keras.layers.Dense(200, activation=tf.nn.relu),
  tf.keras.layers.Dense(50, activation=tf.nn.relu),
  tf.keras.layers.Dense(2, activation=tf.nn.relu),
  tf.keras.layers.Dense(50, activation=tf.nn.relu),
  tf.keras.layers.Dense(200, activation=tf.nn.softmax)
])

# Instellingen voor compilatie zoals in het oorspronkelijk voorbeeld
# van de voorspeller werken prima.
nep_encoder.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train het netwerk om de labels te reproduceren!
nep_encoder.fit(xtr, ytr, epochs=10)
print("Training performance:", nep_encoder.evaluate(xtr, ytr))
print("Test performance:", nep_encoder.evaluate(x, y))

# Een summary kan gegenereerd worden voor netwerken gemaakt met Keras:
nep_encoder.summary()

