from flask import Flask, render_template, request, jsonify
from forms import MyForm
from data import find_recommendations
from api_request import find_album_details

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_key'


@app.route('/', methods=['GET', 'POST'])
def index():
	form = MyForm()
	if request.method == 'GET':
		return render_template("index.html", form=form)
	elif request.method == 'POST':
		album_name = request.form['album_name']
		album_list = find_recommendations(album_name)
		album_choice = find_album_details(album_name)
		new_album_list = []
		for alb in album_list:
			new = find_album_details(alb)
			new_album_list.append(new)
		return render_template("index.html", form=form, entry=album_choice, recommendations=new_album_list)


@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500


@app.route("/recommendations/<album_name>")
def get_recommendation(album_name):
	recommendations = find_recommendations(album_name)
	new_album_list = []
	for alb in recommendations:
		new = find_album_details(alb)
		new_album_list.append(new)
	return jsonify(new_album_list), 200


