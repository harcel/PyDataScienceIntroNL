from sklearn.cluster import KMeans
y_pred = KMeans(n_clusters=3).fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=20)
plt.title("Redelijk waardeloze clustering");

from sklearn.cluster import DBSCAN, AgglomerativeClustering

# De blobs uit het instructienotebook:
X1, y1 = make_blobs(random_state=101, cluster_std=[1, 2, 5], centers=[[0, 10],[-8, 0], [8,-4]], n_samples=1000, )
X2, y2 = make_blobs(random_state=101, centers=[[-8, -8],[0, 0], [2,2]], n_samples=1000, )

plt.figure(figsize=(12,10))
db = DBSCAN()
for i,x in enumerate([X, X1, X2]):
    labels = db.fit_predict(x)
    plt.subplot(2,3,i+1)
    plt.scatter(x[labels>=0, 0], x[labels>=0, 1], c= labels[labels>=0], s=20)
    plt.scatter(x[labels == -1, 0], x[labels == -1, 1], c='red', marker='x', s=40, label="Noise")
    plt.xticks([])
    plt.yticks([])
    plt.legend(frameon=True, fontsize=10, markerscale=2 )
    
hier = AgglomerativeClustering()
for i,x in enumerate([X0, X1, X2]):
    labels = hier.fit_predict(x)
    plt.subplot(2,3,i+4)
    plt.scatter(x[:, 0], x[:, 1], c= labels, s=20)
    plt.xticks([])
    plt.yticks([])
    plt.title("X"+str(i))
    
# Speel vooral nog met de hyperparameters van beide algoritmen en zie wat het doet!
