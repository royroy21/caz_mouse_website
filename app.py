from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    return send_from_directory(directory='programs', filename=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
