# Eerst met PCA. Deze resulteert nu in 3 coponenten, waarvoor je dus twee plot nodig hebt
pca = PCA()
pcas = pca.fit_transform(X)
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(121)
plt.scatter(pcas[:, 0], pcas[:, 1], c=color, cmap=plt.cm.Spectral)
ax = fig.add_subplot(122)
plt.scatter(pcas[:, 2], pcas[:, 1], c=color, cmap=plt.cm.Spectral);

print("PCA vindt compenenten die de S projecteren en die loodrecht van boven op de S kijken.")
print("Dit helpt je verder weinig.....")

# Dan een poging met IsoMap en t-SNE 

from sklearn.manifold import Isomap, TSNE
import time 

# Initialiseer vast een plot
fig = plt.figure(figsize=(12, 8))

t0 = time.time()
# Het initialisren, fitten en transformeren kan ook in 1 regel!
# Gebruik n_components=2 als je twee dimensies wilt!
Y = Isomap(n_components=2).fit_transform(X)
# Onderstaande drie regels zouden equivalent zijn aan de regel hierboven:
# mapper = Isomap(n_neighbors=n_neighbors, n_components=n_components)
# mapper.fit(X)
# Y = mapper.transform(X)
t1 = time.time()
ax = fig.add_subplot(121)
plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("Isomap (%.2g sec)" % (t1 - t0))

t0 = time.time()
#t-SNE heeft meerdere hyperparameters, hier kun je mee spelen tot je blij bent!
# Gebruik n_components=2 als je twee dimensies wilt!
Y = TSNE(n_components=2, n_iter=2000).fit_transform(X)
t1 = time.time()
ax = fig.add_subplot(122)
plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("t-SNE (%.2g sec)" % (t1 - t0))

