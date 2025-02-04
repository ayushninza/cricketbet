import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing, svm, neighbors
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import data as d
from sklearn.model_selection import train_test_split
teamsDF = pd.read_csv('../data/Team.csv')

matchesTeamsDF = pd.read_csv("../data/gen/match_team.csv")
data = matchesTeamsDF.drop(['Match_Id'],1)
data = data.drop(['Unnamed: 0'],1)
X = data.drop(['Match_Won'],1)
Y = data['Match_Won']

X = preprocessing.scale(X)

X_train, X_test, y_train, y_test =train_test_split(X, Y, test_size = 0.25)
print("Team_Id,Team_Name,Team_Short_Code")
print("1,WEST INDIES,WI")
print("2,SOUTH AFRICA,SA")
print("3,ENGLAND,ENG")
print("4,AUSTRALIA,AUS")
print("5,PAKISTAN,PAK")
print("6,AFGANISTAN,AFG")
print("7,INDIA,IND")
print("8,NEPAL,NEP")
print("9,BANGALADESH,BAN")
print("10,SRI LANKA,SL")
print("11,IRELAND,IRE")
print("12,UNITED ARAB EMIRATES,UAE")
print("13,NEW ZEALAND,NZ")


def predict():
    print("Enter Team A Id")
    teamId = input()
    while(len(teamsDF[teamsDF["Team_Id"] == int(teamId)]) == 0):
        print("Please Enter valid Team Id")
        teamId = input()
    print("Enter Team B Id")
    opponentId = input()
    while(len(teamsDF[teamsDF["Team_Id"] == int(opponentId)]) == 0):
        print("Please Enter valid Team Id")
        opponentId = input()
    print("Which team won the toss?Enter Id")
    tossWon = input()
    while((tossWon != teamId) & (tossWon != opponentId)):
        print("Please Enter valid Team Id. %s or %s" % (teamId,opponentId))
        tossWon = input()
    print("Which team bat first?Enter Id")
    batFirst = input()
    while((batFirst != teamId) & (batFirst != opponentId)):
        print("Please Enter valid Team Id. %s or %s" % (teamId,opponentId))
        batFirst = input()
    px = d.generatePredictData(int(teamId),int(opponentId),int(tossWon),int(batFirst))
    px = px.drop(['Match_Id'],1)
    px = px.drop(['Match_Won'],1)

    px = preprocessing.scale(px)

    lin_svm = svm.LinearSVC()
    lin_svm.fit(X_train, y_train)
    pred = lin_svm.predict(px)
    if(pred[0] == 1):
        print("Team A Wins")
    else:
        print("Team B Wins")



def fitModels():

    print("Linear SVM")
    lin_svm = svm.LinearSVC()
    lin_svm.fit(X_train, y_train)
    accu = lin_svm.score(X_test,y_test)
    print(accu)

    print("SVC SVM")
    svc_svm = svm.SVC()
    svc_svm.fit(X_train, y_train)
    accu = svc_svm.score(X_test,y_test)
    print(accu)

    print("Naive Bayes")
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    accu = gnb.score(X_test,y_test)
    print(accu)

    print("Random Forest")
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    accu = rf.score(X_test,y_test)
    print(accu)

#fitModels()
predict()
