titanic = pd.read_csv(os.path.join('data', 'titanic3.csv'))
print(titanic.head())

labels = titanic.survived.values
features = titanic[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']]
features_dummies = pd.get_dummies(features, columns=['pclass', 'sex', 'embarked'])
features_dummies.head()

data = features_dummies.values

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import Imputer

imp = Imputer()
# Fitten en transformeren kan in 1 stap!
decent_data = imp.fit_transform(data)
# Wat anders ook werkt
# imp.fit(data)
# decent_data = imp.transform(data)


tree = DecisionTreeClassifier()
tree.fit(decent_data, labels)

print("R**2 van de decision tree:", tree.score(decent_data, labels))



