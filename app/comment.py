from models.user import users
import datetime
comments = []

class Comment:
	def __init__(self, author,message, _id):
		self.id = _id
		self.author = author
		self.message = message
		self.timestamp = datetime.datetime.utcnow()


	def save_comment(comment):
		return comments.append(comment)


	def edit_comment(comment_id, message):
		if user.role = 'admin':
			for comment in comments:
				if comment.id == comment_id:
					comment.message =message


