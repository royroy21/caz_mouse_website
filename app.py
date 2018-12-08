from flask import Flask, render_template, request, send_from_directory
from user_agents import parse

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def home():
    http_user_agent_string = request.environ['HTTP_USER_AGENT']
    user_agent = parse(http_user_agent_string)

    if user_agent.is_mobile:
        return render_template('mobile_error.html')

    return render_template('home.html')


@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    return send_from_directory(directory='programs', filename=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
