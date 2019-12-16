import os
from flask import Flask, render_template, request, redirect, url_for, abort, session, flash
import pandas as pd 
import random
import collections
import copy

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.no_of_chance = 4



#### La page d'accueil #####
@app.route('/')
def home():
    return render_template('index.html')


#### s'inscrire #####


@app.route('/signup', methods=['POST'])
def signup():
    session['username'] = request.form['username']
    #df.iloc[-1]["user"] = request.form['username']
    return redirect(url_for('bienvenue'))


#### page de bienvenue une fois l'inscription faite #####

@app.route('/bienvenue')
def bienvenue():
    if not 'username' in session:
        return abort(403)        
    return render_template('message.html', username=session['username'])
    

#### le questionnaire #####
T=[[[0,[],'un scientifique']],[[1,['oui'],'une femme'],[1,['non'],'un sportif']],[[2,['oui','oui'],'Marie Curie'],[2,['oui','non'],'Pasteur'],[2,['non','oui'],'Zinédine Zidane'],[2,['non','non'],'Jean-Jacques Goldman']]]
R1=[]
A=[]
    
@app.route('/questionnaire/', methods=['GET', 'POST'])
def questionnaire():
    print(request.method)
    #print(session.get("question", "a"))
    ans=[]
    n=2
    quest=T[0][0][2]
    c=1
    if request.method == "POST":
       rep=request.form.get('answer', '')
       ans.append(rep)
       R1.append(rep)
       c=c+1
       print(ans)
       for k in range(n+1):
           for i in range(2*k):
               if T[k][i][1]==R1:
                  p=T[k][i][2]
                  quest=p
   
    if len(R1)==n: #cas où il n'y a plus de question
       session.pop('username', None)
       session.clear()
       A.append(quest)
       return redirect(url_for('logout'))

    return render_template("quiz.html", question="Votre personnage est : " + quest +" ?", question_number=c,
                             options=['oui','non'])
    



@app.route('/logout')
def logout():
    # réinitialiser la session
    #Cette fonction a un petit problème il faudrait pouvoir rénitialiser R1, mais nous n'arrivons pas à le faire

    session.pop('username', None)
    session.clear()
    return render_template("fin_quizz.html", reponse="Vous pensez à : "+A[-1])    





if __name__ == '__main__':
    app.run(debug = True)