#runs app

from app import app
app.config['SECRET_KEY']='secret_key'
app.run(debug=True)