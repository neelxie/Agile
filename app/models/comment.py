from models import User
comments = []
class Comment:
	def __init__(self, username,comment):
		self.id = 0
		self.username = username
		self.comment = comment

	def write_comment(self):
		self.id =self.id+1
		if user.role = 'admin':
			return "you cannot create comment"
		self.comment = input("add a comment :                ")
		new_comment ={
		'_id'=self.id,
		'username'=self.username
		'comment'=self.comment

		}
		comments.append(new_comment)
		return new_comment

	def edit_comment():
		if username.role = 'admin':

