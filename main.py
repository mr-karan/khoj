from datetime import datetime
from flask import Flask
from flask import request, render_template, session

from get_answer import result
app = Flask(__name__)

@app.route('/')
def index():
    error_message = 'Answer is not found'
    username = request.values.get('username')
    if not username:
        return render_template('index.html')
    answer = result(username)[0]
    query_text = result(username)[1]
    session['query_text'] = query_text

    if result:
        return render_template('result.html', answer=answer, query_text=query_text)
    return render_template('index.html', error_message=error_message)

@app.route('/query')
def check():
    query_text = session.get('query_text', None)
    return render_template('query.html', query_text=query_text)

@app.route('/about')
def blah():
    return render_template('about.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
