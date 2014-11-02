#Login Form
#Uses OpenID to authenticate users

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, validators


class LoginForm(Form):
	openid = TextField('openid', [validators.Required()])
	remember_me = BooleanField('remember_me', default = False)

#DataRequired is a validator, a function that performs validation that field not empty
