from tensorflow.keras import backend as K

# Laat de functie mappen van de input naar de output van de bottleneck-laag
get_middle_layer_output = K.function([nep_encoder.layers[0].input],
                                  [nep_encoder.layers[2].output])

layer_output = get_middle_layer_output([xtr])[0]

print("Shape van de ouput van de functie:", layer_output.shape)

plt.figure(figsize=[12, 12])
plt.scatter(layer_output[:,0], layer_output[:,1], s=10, alpha=0.01, c=ytr)


