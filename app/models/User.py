#class User(db.Model):
#   id = db.Column(db.Integer, primary_key = True)
#   username = db.Column(db.String(64), unique = True)
#   email = db.Column(db.String(120), unique = True)
#   role = db.Column(db.SmallInteger, default = ROLE_USER)
#
#   def is_authenticated(self):
#   return True
#
#   def is_active(self):
#   return True
#
#   def is_anonymous(self):
#   return False
#
#   def get_id(self):
#   return unicode(self.id)
#
#   def __repr__(self):
#   return '<User %r>' % (self.username)
