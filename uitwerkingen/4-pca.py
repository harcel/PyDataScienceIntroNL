from sklearn.decomposition import PCA
# Initialiseer een instantie
pca = PCA()
# Gebruik de fit methode om op de dataset te fitten
pca.fit(X_blob)
# Transformeer de oorspronkelijke dataset met het zojuist gefitte object
X_pca = pca.transform(X_blob)

# Plot de resultaten.
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, linewidths=0, s=30)
plt.xlabel("first principal component")
plt.ylabel("second principal component")
plt.axvline(0, linestyle='dotted')
plt.axhline(0, linestyle='dotted')
plt.title("Je hoeft PCA niks te vertellen over verbanden, deze worden gevonden!");

print("Na de PCA wordt de classificatie nog net iets simpeler.")
