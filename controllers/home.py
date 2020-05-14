
'''
Preset controller by torn for / route
'''
from .modules import *

class homeHandler(tornado.web.RequestHandler):
	"""CRUD CYCLE"""
	#READ
	def get(self):
		posts_record=session.query(post).all()
		self.write(tornado.escape.json_encode([str(post.__dict__) for post in posts_record]))
	#Create
	def post(self):
		post_data=tornado.escape.json_decode(self.request.body)
		session.add(post(id=post_data['id'],title=post_data['title'],body=post_data['body']))
		session.commit()
		self.get()
	#DELETE
	def delete(self):
		to_delte=session.query(post).filter(post.id ==tornado.escape.json_decode(self.request.body)['id']).one()
		session.delete(to_delte)
		session.commit()
		self.get()
	#UPDATE
	def put(self):
		session.query(post).filter(

			post.id==tornado.escape.json_decode(self.request.body)['id']

		).update({
			"title":tornado.escape.json_decode(self.request.body)['title'],
			"body":tornado.escape.json_decode(self.request.body)['body']
			})
		
		session.commit()
		self.get()
