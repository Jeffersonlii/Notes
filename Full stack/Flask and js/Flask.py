#what is Flask? a way to run python code on each user navigation, a good backend

Set Up:
1. Start by importing flask
2. app= Flask(__name__)
   #app is the actual web app, has lots of settings
3. 
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', blah = "")# blah accessed in index.html as "{{ blah }}" 

db connection:
1. app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'#connect db
2. db = SQLAlchemy(app) # initiates the db
DB MODS:
1. sql = '''sql command here'''
2. db.engine.exicute(text(sql))

GET VS POST, sent through <form> or AJAX/jquery
1. GET - send small chunks of data through URL
2. POST - send large chunks of data through JSON/AJAX

#When a app.route is ran through GET or POST, we can access HTML data through request.form['JSON NAME({this: stuff}) or html element NAME']

ajax for asym data transfers
#FRONT: must use jquery
$.ajax({#sends the request 
  type: "POST",#or get
  url: url,#app.route url
  data: {hey: 1, hi:2},#JSON DATA
  success: function(response){
  	response.key
  	response.lib
  },#what to do when python send a response
  dataType: dataType #idk
});

#BACK
@app.route('/url',methods=['POST'])
def func():
	#access request data by 
	request.form['hey'];

	#send back data by
	return jsonify({'lib': hey});

SESSIONS
#used for login services, stores login in cache
fill by 
session['anything']=stuff;
EX:
if user logs in:
	session['username']=name
if user logs off:
	session.pop('username')
