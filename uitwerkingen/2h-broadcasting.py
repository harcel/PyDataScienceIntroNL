X = np.random.random(size=(20, 3)) * 3
X *= np.array([1, 2, 1])
X_mean = X.mean(axis=0)
print((X-X_mean).mean(axis=0))

# De vermenigvuldiging met 3 is broadcasting (elk element wordt met 3 vermenigvuldigd, dus de 3 wordt gebroadcast tot een 20x3 array van drieen) 
# Het vermeniguldigen met de array [1, 2, 1] is broadcasting (deze array wordt 20x herhaald)
# Het aftrekken van de gemiddelden is broadcasting, die array van 3 getallen wordt steeds 20x herhaald.
