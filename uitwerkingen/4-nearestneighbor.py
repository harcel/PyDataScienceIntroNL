from sklearn.neighbors import KNeighborsRegressor

# In de uitwerking zal ik meteen de plot maken voor verschillende waarden van k, 
# voel je vrij om dit stapsgewijs te onderzoeken!
ls = ['solid', 'dashed', 'dotted', '-.', 'solid']
plt.figure(figsize=(12,8))
plt.plot(X, y, 'o', markersize=10)
xarr = np.linspace(-3, 3, 1000)[:,np.newaxis]
for k, l in zip((2, 5, 8, 25), ls):
    regr = KNeighborsRegressor(n_neighbors=k)
    regr.fit(X, y)
    score = regr.score(X, y)
    yarr = regr.predict(xarr)
    plt.plot(xarr, yarr, linestyle=l, linewidth=2, label='k = '+str(k)+', R$^2$ = '+str(np.round(score, 2) ))
plt.legend(loc='upper left')

# Let op dat een hoge R**2 niet altijd zomaar betekent dat je een nuttiger model hebt. Zie de bijbehorende huiswerkopgave!


