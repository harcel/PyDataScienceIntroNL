iris = sns.load_dataset('iris')

fig, ax = plt.subplots(1, 3)
sns.boxplot(data=iris, x='species', y='petal_width', ax=ax[0])
sns.violinplot(data=iris, x='species', y='petal_width', ax=ax[1])
sns.distplot(iris.petal_width[iris.species == "setosa"], rug=True, hist=False, ax=ax[2])
sns.distplot(iris.petal_width[iris.species == "versicolor"], kde=False, norm_hist=True, ax=ax[2])
sns.distplot(iris.petal_width[iris.species == "virginica"], ax=ax[2])
fig.set_size_inches(18, 6)
