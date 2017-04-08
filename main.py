from datetime import datetime
from flask import Flask
from flask import request, render_template

from get_answer import result
app = Flask(__name__)


@app.route('/')
def index():
    error_message = 'Answer is not found'
    username = request.values.get('username')
    if not username:
        return render_template('index.html')
    answer = result(username)
    print (answer)
    if result:
        return render_template('result.html', answer=answer,)
    return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)