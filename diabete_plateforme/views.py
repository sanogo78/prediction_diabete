# Importer toute la bibliothèque
from unittest import result
from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Les vues du projet

# Vue de la page d'accueil
def home(request):
    return render(request, 'home.html')

# Vue de la page de prédiction
def predict(request):
    return render(request, 'predict.html')

# Chargement des données
def result(request):
    data = pd.read_csv('diabetes.csv')
    X = data.drop('Outcome', axis=1)
    Y = data['Outcome']
    # Division des données en donnée d'entrainement
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    # Créeation du modèle
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    
    # les names du formulaire de prediction
    val1 = float(request.POST['n1'])
    val2 = float(request.POST['n2'])
    val3 = float(request.POST['n3'])
    val4 = float(request.POST['n4'])
    val5 = float(request.POST['n5'])
    val6 = float(request.POST['n6'])
    val7 = float(request.POST['n7'])
    val8 = float(request.POST['n8'])
    
    # Faire la prédiction
    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    
    result1 = ""
    if pred == [1]:
        result1 = "OUPS! Vous êtes diabétique."
    else:
        result1 = "FÉLICITATIONS! Vous n'êtes pas diabétique."
    return render(request, 'predict.html', {'result2': result1})
