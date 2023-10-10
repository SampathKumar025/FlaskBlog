import os
from flaskblog.models import User
from flaskblog import create_app

app = create_app()
path = "flaskblog\static\profile_pics"
pp_list_fs = os.listdir(path)
with app.app_context():
    for pic in pp_list_fs:
        if User.query.filter_by(image_file=pic).first() is None:
            os.remove(os.path.join(path, pic))