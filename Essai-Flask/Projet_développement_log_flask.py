import os
from flask import Flask, render_template, request, redirect, url_for, abort, session, flash
import pandas as pd 
import random
import collections
import copy

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.no_of_chance = 4

file_csv = "./projet_dev_log_flask.csv"

# Avoir les infos sur les pokemons et les technologies big data



######### On définit le nombre de questions du questionnaire

longueur_questionnaire = 10

####### On définit les éléments du questitonnaire

liste_choice = ['Femme',
 'Homme',
 'Artiste',
 'Scientifique',
 'Sportif',
 'Acteur',
 'Politique',
 'Jeune',
 'Chauve',
 'Sculpteur']
    

questions = {}    
for x in range(1, longueur_questionnaire + 1) : 
    item = liste_choice[x-1]
    questions[str(x)] = {"question" : "Votre personnage est : {} ?".format(item), "options" :["oui", "non"]}


# Ici on vérifie si le fichier qui conserve les réponses existe ou pas

if not os.path.isfile(file_csv):
    df = pd.DataFrame({'user' : [], 'score' : []})
    #for question in questions.keys() :
    for x in range(1, longueur_questionnaire+ 1 ) : 
        df[str(x)] = []
    df.to_csv(file_csv, index = False)


#### La page d'accueil #####
@app.route('/')
def home():
    return render_template('index.html')


#### s'inscrire #####

liste = [None] * (longueur_questionnaire + 2)

@app.route('/signup', methods=['POST'])
def signup():
    session['username'] = request.form['username']
    liste[0] = request.form['username']
    #df.iloc[-1]["user"] = request.form['username']
    return redirect(url_for('bienvenue'))


#### page de bienvenue une fois l'inscription faite #####

@app.route('/bienvenue')
def bienvenue():
    if not 'username' in session:
        return abort(403)        
    return render_template('message.html', username=session['username'])
    
#### le questionnaire #####
    
@app.route('/questionnaire/', methods=['GET', 'POST'])
def questionnaire():
    print(request.method)
    print(session.get("question", "a"))

    if request.method == "POST":
        if "question" in session:
            entered_answer = request.form.get('answer', '')
            liste[int(session["question"])] = entered_answer
            print(questions.get(session["question"],False))
            if questions.get(session["question"],False):
                if entered_answer != "oui":
                    mark = 0
                else:
                    mark = 4
                session["mark"] += mark
                session["question"] = str(int(session["question"])+1)
        else:
            print("question missing")
  
    if "question" not in session:
        session["question"] = "1"
        session["mark"] = 0
    elif session["question"] not in questions: #cas où il n'y a plus de question
        session.pop('username', None)
        session.clear()        
        return render_template("message2.html")
    return render_template("quiz.html", question=questions[session["question"]]["question"], question_number=session["question"],
                             options=questions[session["question"]]["options"])


@app.route('/logout')
def logout():
    # réinitialiser la session
    session.pop('username', None)
    session.clear()
    return redirect(url_for('home'))    





if __name__ == '__main__':
    app.run(debug = True)