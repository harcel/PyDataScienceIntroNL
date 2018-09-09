from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
import tensorflow as tf

mnist = fetch_mldata("MNIST original", data_home='./data/')  
features, labels = mnist.data / 255., mnist.target

xtr, x, ytr, y = train_test_split(features, labels, test_size=0.3)

print("Dimensies van xtr:", xtr.shape)
print("Dimensies van ytr:", ytr.shape)
print("Dimensies van x:", x.shape)
print("Dimensies van y:", y.shape)

# Maak ruis op de test set
n_pixels = np.product(x.shape)

# Als ruis gebruik ik uniform verdeelde random getallen tussen -4 en 0. 
# Deze zijn de logaritme van de ruiswaarde in elke pixel.
logruis = np.random.uniform(-4, 0, n_pixels).reshape(x.shape)
xruis = x + 10**logruis

# De array kan nu van 0 tot 2 lopen, dus ik "clip" de waarden van 0 tot 1
xruis = np.clip(xruis, 0, 1)

# Even een random serie voorbeelden laten zien:
imsize = 28

# Bekijk van elk getal een random voorbeeld. Als je deze cell meerdere keren uitvoert krijg je steeds een nieuwe serie. 
plt.figure(figsize=[12, 5])
for target in range(10):
    deze = np.random.choice(np.where(y == target)[0])
    number = np.reshape(np.array(xruis[deze]), [imsize, imsize])
    pp = plt.subplot(2, 5, target+1)
    pp.imshow(number, cmap='Greys')
    pp.set_xticklabels([])
    pp.set_yticklabels([])
    
# We trainen dezelfde auto-encoder als in de instructie:
auto_encoder = tf.keras.models.Sequential([
  tf.keras.layers.Dense(784, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(128, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  tf.keras.layers.Dense(784, activation=tf.nn.relu)
])
auto_encoder.compile(loss=tf.keras.losses.mean_squared_error,
             optimizer=tf.keras.optimizers.RMSprop(lr=0.0001, rho=0.9, epsilon=None, decay=0.0),
             metrics = ['accuracy'])

auto_encoder.fit(xtr, xtr, epochs=10, batch_size=256)


# Vergelijk dan een input met ruis met de reconstructie van het netwerk
# Alle gereconstrueerde images:
reconstructed = auto_encoder.predict(xruis)

# Als je meerdere voorbeelden wil zien, maak dan van het stuk hieronder een aparte cell 
# (met "split cell" onder "Edit" of ctrl-shift-- als je cursor op de goed plek staat)
aantal_im = len(xruis)
deze = np.random.randint(0, aantal_im)

plt.figure(figsize=(12, 24))
pp = plt.subplot(121)
number = np.reshape(reconstructed[deze], [imsize, imsize])
pp.imshow(number, cmap='Greys')
pp.set_xticklabels([])
pp.set_yticklabels([])
pp.set_title("Gereconstrueerd")

pp = plt.subplot(122)
number = np.reshape(xruis[deze], [imsize, imsize])
pp.imshow(number, cmap='Greys')
pp.set_xticklabels([])
pp.set_yticklabels([])
pp.set_title("Oorspronkelijke digit met ruis");
