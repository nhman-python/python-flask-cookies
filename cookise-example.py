from datetime import datetime, timedelta
from flask import Flask, make_response, request,send_file
import os
app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    # Set expiration date to one year from now
    expires = datetime.now() + timedelta(days=365)

    # Create response with message and set cookie with expiration date
    resp = make_response('Cookie has been set!')
    resp.set_cookie('1234', 'abcd', expires=expires)

    return resp

@app.route('/check_cookie')
def check_cookie():
    if '1234' in request.cookies:
        return send_file(os.path.join(app.root_path, 'img.png'))
    else:
        return 'You do not have the access_token cookie.'


if __name__ == '__main__':
    app.run(debug=False)
