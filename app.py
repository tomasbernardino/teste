from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/birthday', methods=['GET'])
def birthday():
    message = """
	╮╭╭╮┏╮┏╮╮╭
	┣┫┣┫┣╯┣╯╰┫  ☆
	╯╯╯╯╯╯╯╯╰╯╭━┻━╮
	┏╮┊┏╮╭╮╮╭╭┻━━━┻╮
	┣┫┊┃┃┣┫╰┫┣╮╭╮╭╮┃
	┗╯┊┗╯╯╯╰╯┃╰╯╰╯╰┫
	━━━━━━━━━╯╳╳╳╳╳╰
	━━━━━━━┏━━━┓━━━━━━┏┓━━━━━━━┏━━━┓┏┓━━━━━━━━━━━━━━━
	━━━━━━━┃┏━┓┃━━━━━━┃┃━━━━━━━┃┏━┓┃┃┃━━━━━━━━━━━━━━━
	┏┓┏┓┏━┓┃┃━┃┃┏━┓━┏━┛┃┏━┓┏━━┓┃┗━┛┃┃┃━┏━━┓━┏┓━┏┓┏━━┓
	┃┗┛┃┃┏┛┃┗━┛┃┃┏┓┓┃┏┓┃┃┏┛┃┏┓┃┃┏━━┛┃┃━┗━┓┃━┃┃━┃┃┃━━┫
	┃┃┃┃┃┃━┃┏━┓┃┃┃┃┃┃┗┛┃┃┃━┃┃━┫┃┃━━━┃┗┓┃┗┛┗┓┃┗━┛┃┣━━┃
	┗┻┻┛┗┛━┗┛━┗┛┗┛┗┛┗━━┛┗┛━┗━━┛┗┛━━━┗━┛┗━━━┛┗━┓┏┛┗━━┛
	━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━┛┃━━━━━
	━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┗━━┛━━━━━
    """
    # Converte quebras de linha para <br> e espaços para &nbsp;
    message_html = message.replace(" ", "&nbsp;").replace("\n", "<br>")
    return jsonify(message=message_html)

if __name__ == '__main__':
    app.run(debug=False)

