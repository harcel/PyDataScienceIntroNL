# Dit is weer een encoder, dus gebruik instellinen die daarbij horen.
real_encoder = tf.keras.models.Sequential([
  tf.keras.layers.Dense(784, activation=tf.nn.relu),
  tf.keras.layers.Dense(128, activation=tf.nn.relu),
  tf.keras.layers.Dense(2, activation=tf.nn.relu),
  tf.keras.layers.Dense(128, activation=tf.nn.relu),
  tf.keras.layers.Dense(784, activation=tf.nn.relu)
])
real_encoder.compile(loss=tf.keras.losses.mean_squared_error,
             optimizer=tf.keras.optimizers.RMSprop(lr=0.0001, rho=0.9, epsilon=None, decay=0.0),
             metrics = ['accuracy'])

# Dus ook: trainen op de input.
real_encoder.fit(xtr, xtr, epochs=10, batch_size=256)
print("Training performance:", real_encoder.evaluate(xtr, xtr))


# Zoals wellicht verwacht wanneer er niet wordt getraind op de labels, 
# is het veel moeilijker de verschillend gelabelde plaatjes te onderscheiden 
# in de bottleneck-laag. De performance van het model lijkt ook heel laag. 
# Dit is echter niet zo'n betekenisvol getal: het is een maat voor hoe goed 
# afzonderlijke pixels worden gereconstrueerd, en voor het eventueel kunnen 
# herkennen van een plaatje kunnen die nog behoorlijk anders zijn, zoals we 
# hieronder zullen zien.

# Predict de output, gegeven de input en laat ze beiden naast elkaar zien.
real_constructed = real_encoder.predict(xtr)

imsize = 28
aantal_im = len(xtr)
deze = np.random.randint(0, aantal_im)

plt.figure(figsize=(12, 24))
pp = plt.subplot(121)
number = np.reshape(real_constructed[deze], [imsize, imsize])
pp.imshow(number, cmap='Greys')
pp.set_xticklabels([])
pp.set_yticklabels([])
pp.set_title("Gereconstrueerd")

pp = plt.subplot(122)
number = np.reshape(xtr[deze], [imsize, imsize])
pp.imshow(number, cmap='Greys')
pp.set_xticklabels([])
pp.set_yticklabels([])
pp.set_title("Oorspronkelijke digit");
