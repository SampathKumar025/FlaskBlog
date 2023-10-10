import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, "static/profile_pics", picture_fn)
    img = Image.open(form_picture)
    img.thumbnail((125, 125))
    img.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Password Reset Request", sender="noreply@flaskblog.com", recipients=[user.email])
    msg.body = f'''Hi {user.username}

This mail has been sent form FlaskBlog website.

A password reset request has been made to your flaskblog account, To reset your password please visit the following link:
{url_for("users.password_reset", token=token, _external=True)}

If you did not make this request, simply ignore this email. No changes will be done.

For any issues or queries, please write to support@flaskblog.com
'''
    mail.send(msg)
