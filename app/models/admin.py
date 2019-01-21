from moderator import Moderator
from user import User, users
from comment import Comment, comments


class Admin(Moderator, User):

    def __init__(self, name):
        super().__init__(name)

    def delete_comment(self, comment_id):
        for comment in comments:
            if comment.id == comment_id:
                comments.remove(comment)
                message = "Commment has been deleted"
                return message
                
        
