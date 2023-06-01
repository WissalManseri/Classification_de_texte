#Tout d'abord, nous importons les modules nécessaires :
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

#Ensuite, nous chargeons les données en utilisant la bibliothèque pandas :
data = pd.read_csv('text_classification_data.csv')

#Nous divisons les données en deux ensembles : un ensemble d'entraînement et un ensemble de test :
train_data = data.sample(frac=0.8, random_state=1)
test_data = data.drop(train_data.index)

#Nous préparons les données d'entraînement et de test en convertissant les textes en vecteurs :
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_data['text'])
y_train = train_data['label']

X_test = vectorizer.transform(test_data['text'])
y_test = test_data['label']

# Ensuite, nous entraînons un classificateur Naive Bayes multinomial sur les données d'entraînement :
clf = MultinomialNB()
clf.fit(X_train, y_train)

#Nous effectuons des prédictions sur les données de test :
y_pred = clf.predict(X_test)


# Enfin, nous évaluons les performances du classificateur en calculant la précision :
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

