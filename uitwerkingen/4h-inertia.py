from sklearn.cluster import KMeans

plt.figure(figsize=(12,8))
plt.subplot(221)
plt.scatter(X[:,0], X[:,1], c=y, s=20)

plt.subplot(222)
# In een loopje over verschillende clusteraantallen sla ik steeds inertia_ op.
inertia = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, 
                random_state=0)
    km.fit(X)
    inertia.append(km.inertia_)
# Die kun je vervolgens plotten
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Aantal clusters')
plt.ylabel('intertia_')
plt.tight_layout()


plt.subplot(223)
plt.scatter(X2[:,0], X2[:,1], c=y2, s=20)

plt.subplot(224)
inertia = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, 
                random_state=0)
    km.fit(X2)
    inertia.append(km.inertia_)
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Aantal clusters')
plt.ylabel('intertia_')
plt.tight_layout()


# Wanneer de clusters heel dicht bij elkaar liggen is het niet duidelijk of het er 1 of twee zijn.
# Dit geldt, tot op zekere hoogte ook voor niet-sferische clusters.
# 4 en 2 zouden wat mij betreft de ellebogen zijn.