import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data  
y = iris.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
basari_orani = model.score(X_test, y_test)
print(f"Modelin doğruluk oranı: %{basari_orani * 100}")
yeni_cicek = [[5.1, 3.5, 1.4, 0.2]]
tahmin = model.predict(yeni_cicek)
print(f"Yeni çiçeğin tahmini türü: {iris.target_names[tahmin][0]}")
