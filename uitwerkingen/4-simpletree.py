for a, b in zip(features_dummies.columns, tree.feature_importances_):
    print("Importance of %12s : %5.4f" %(a, b))
print()
# De interpretatie is niet eenduidig, want sommige features komen op meerdere plekken terug in de boom en dat zie je niet terug in deze lijst.

# Deze boom is de afgebeelde:
simpletree = DecisionTreeClassifier(max_depth=3, max_leaf_nodes=3)
simpletree.fit(decent_data, labels)
print(simpletree.score(decent_data, labels))

for a, b in zip(features_dummies.columns, simpletree.feature_importances_):
    print("Importance of %12s : %5.4f" %(a, b))

    