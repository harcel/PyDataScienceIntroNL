# Maak twee curven en plak ze naast elkaar.
from sklearn.datasets import samples_generator
from mpl_toolkits.mplot3d import Axes3D

n_points = 1000
X, color = samples_generator.make_s_curve(n_points, random_state=0)
X1 = np.array([X[:, 0]+5, X[:, 1], X[:, 2]]).T
# Numpy geeft handige functionaliteiten voor het aan elkaar hangen van arrays.
Z = np.concatenate([X, X1])
zcolor = np.concatenate([color, color])

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Z[:, 0], Z[:, 1], Z[:, 2], c=zcolor, cmap=plt.cm.Spectral)
ax.view_init(10, -72)

# Ik onderzoek hier een groot scala aan manifold learners. 
# Als je er zelf minder had is dat uiteraard prima.
n_neighbors = 10
n_components = 2

fig = plt.figure(figsize=(18, 12))
plt.suptitle("Manifold Learning with %i points, %i neighbors"
             % (n_points, n_neighbors), fontsize=14)


from sklearn.manifold import LocallyLinearEmbedding, Isomap, MDS, SpectralEmbedding, TSNE
from time import time

methods = ['standard', 'ltsa', 'hessian', 'modified']
labels = ['LLE', 'LTSA', 'Hessian LLE', 'Modified LLE']

for i, method in enumerate(methods):
    t0 = time()
    Y = LocallyLinearEmbedding(n_neighbors, n_components,
                                        eigen_solver='auto',
                                        method=method).fit_transform(Z)
    t1 = time()
    print("%s: %.2g sec" % (methods[i], t1 - t0))

    ax = fig.add_subplot(252 + i)
    plt.scatter(Y[:, 0], Y[:, 1], c=zcolor, cmap=plt.cm.Spectral)
    plt.title("%s (%.2g sec)" % (labels[i], t1 - t0))
    plt.axis('tight')

t0 = time()
Y = Isomap(n_neighbors, n_components).fit_transform(Z)
t1 = time()
print("Isomap: %.2g sec" % (t1 - t0))
ax = fig.add_subplot(257)
plt.scatter(Y[:, 0], Y[:, 1], c=zcolor, cmap=plt.cm.Spectral)
plt.title("Isomap (%.2g sec)" % (t1 - t0))
plt.axis('tight')


t0 = time()
mds = MDS(n_components, max_iter=100, n_init=1)
Y = mds.fit_transform(Z)
t1 = time()
print("MDS: %.2g sec" % (t1 - t0))
ax = fig.add_subplot(258)
plt.scatter(Y[:, 0], Y[:, 1], c=zcolor, cmap=plt.cm.Spectral)
plt.title("MDS (%.2g sec)" % (t1 - t0))
plt.axis('tight')


t0 = time()
se = SpectralEmbedding(n_components=n_components,
                                n_neighbors=n_neighbors)
Y = se.fit_transform(Z)
t1 = time()
print("SpectralEmbedding: %.2g sec" % (t1 - t0))
ax = fig.add_subplot(259)
plt.scatter(Y[:, 0], Y[:, 1], c=zcolor, cmap=plt.cm.Spectral)
plt.title("SpectralEmbedding (%.2g sec)" % (t1 - t0))
plt.axis('tight')

t0 = time()
tsne = TSNE(n_components=n_components, init='pca', random_state=0)
Y = tsne.fit_transform(Z)
t1 = time()
print("t-SNE: %.2g sec" % (t1 - t0))
ax = fig.add_subplot(2, 5, 10)
plt.scatter(Y[:, 0], Y[:, 1], c=zcolor, cmap=plt.cm.Spectral)
plt.title("t-SNE (%.2g sec)" % (t1 - t0))
plt.axis('tight');

# t-SNE duurt wat langer, maar geeft in deze iets gecompliceerdere situatie wel het zinnigste antwoord.
