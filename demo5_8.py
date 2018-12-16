from demo5_7 import db
from demo5_7 import Role, User


db.create_all()
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')

user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)

print(admin_role.id)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)

db.session.commit()

print(admin_role.id)

# admin_role.name = 'Administrator'
# db.session.add(admin_role)
# db.session.commit()

# db.session.delete(mod_role)
# db.session.commit()

Role.query.all()
User.query.all()

User.query.filter_by(role=user_role).all()
str(User.query.filter_by(role=user_role))

user_role = Role.query.filter_by(name='User').first()


users = user_role.users
users
users[0].role
