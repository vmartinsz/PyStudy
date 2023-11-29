import random
from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
import connect
import sendemail
import commands as com

cursor = connect.connection.cursor()
connection = connect.connection
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=['GET'])
def home():
  return render_template('home.html')

@app.route('/receivelogin', methods=['POST'])
def receivelogin():
    session["username"] = request.form.get("username")
    password = request.form.get('password')
    result = com.getUser(session['username'], password)
    if result:
      return redirect(f'list/username={session["username"]}')
    else:
        message_erro = "Incorrect Username or Password."
        return render_template('home.html', message_erro=message_erro)

@app.route('/singup', methods=['GET'])
def singup():
  return render_template('singup.html')

@app.route('/receivesignup', methods=['POST'])
def receivesingup():
    session["username"] = request.form.get('username')
    session["password"] = request.form.get('password')
    session["email"] = request.form.get('email')
    session["code"] = random.randint(1000, 5000)
    existing_user = com.specificData('*', 'Users', 'username', session["username"])
    if existing_user:
        message_erro = "User exists."
        return render_template('singup.html', message_erro=message_erro)
    sendemail.sendemail(session["email"], session["code"])
    return redirect('/codemail')

@app.route('/codemail', methods=['GET'])
def codemail():
    return render_template('codemail.html')

# ...
@app.route('/receivecode', methods=['POST'])
def receivecode():
    codeTrue = session["code"]
    code = request.form.get('code')
    if codeTrue == int(code):
        existing_user = com.specificData('*', 'Users', 'username', session["username"])
        
        if not existing_user:
            com.addUser(session["username"], session["password"], session["email"])
            return redirect('/')
        
        else:
            flash('User already exists')
    else:
        flash('Incorrect code')
    
    return redirect('/codemail')

@app.route('/list/username=<username>', methods=['GET'])
def list(username):
   idUser = com.specificData('idUsers', 'Users', 'username', username)
   dic_activities = com.listActivities(idUser)

   return render_template('list.html', dic_activities = dic_activities)

@app.route('/new_activity', methods=['GET'])
def render_newActivity():
   return render_template('activity.html')

@app.route('/receiveactivity', methods=['POST'])
def new_activity():

    username = session["username"]
    idUser = com.specificData('idUsers', 'Users', 'username', username)


    stage = request.form.get('value')

    activityName = request.form.get('activity_name')
    matter = request.form.get('matter')
    com.addActivity(activityName, matter, stage, idUser)


    return redirect(f'/list/username={username}')

@app.route('/deleteActivity/<idActivities>', methods=['POST'])
def deleteActivity(idActivities):
    com.deleteActivity(idActivities)    
    username = session['username']
    return redirect(f'/list/username={username}')

@app.route('/editActivity/<idActivities>', methods=['POST'])
def editActivity(idActivities):
    return render_template('activity.html', idActivities=idActivities)

@app.route('/receiveactivity/<idActivities>', methods=['POST'])
def receiveEditActivity(idActivities):
    username = session["username"]
    stage = request.form.get('value')
    activityName = request.form.get('activity_name')
    matter = request.form.get('matter')
    com.editActivity(activityName, matter, stage, idActivities)
    return redirect(f'/list/username={username}')

if __name__ == '__main__':
    app.run(debug=True)

