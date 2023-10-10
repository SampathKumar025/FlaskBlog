# from flaskblog import *
# from flaskblog.models import *

# with current_app.app_context():
#     db.drop_all()
#     db.create_all()

#     user1 = User(username="Sampath", email="sam@gmail.com", password="sam123")
#     user2 = User(username="Kumar", email="kum@gmail.com", password="kum123")

#     db.session.add(user1)
#     db.session.add(user2)
#     db.session.commit()
#     print(User.query.all())
#     user = User.query.filter_by(username="Sampath").first()
#     post1 = Post(title="Sampath's First Blog", content="Content of the First Blog by Sampath", user_id=user.id)
#     post2 = Post(title="Sampath's Second Blog", content="Content of the Second Blog by Sampath", user_id=user.id)
#     db.session.add(post1)
#     db.session.add(post2)
#     db.session.commit()
#     for post in user.posts:
#         print(post)

# import requests, json

# with open("posts.json") as posts_json:
#     posts = json.load(posts_json)
# response = requests.post("http://127.0.0.1:5000/post/new", json=posts)
# print(response.content)