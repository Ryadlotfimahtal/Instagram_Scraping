#coding: utf-8

"""
@Ryad Lotfi MAHTAL
"""
#import sys 
#sys.path.insert(1, './utils') 

from mongodb_connection import *
import gridfs
import argparse
import os 
#from bson import json_util

parser = argparse.ArgumentParser(description='Retrieve Data from MongoDB database')


parser.add_argument('--database','-DB', type=str, default="insta_scrap", help='Provide the name of the database')
parser.add_argument('--db_username','-dbU', type=str, default="Ryad", help='Provide the dabatabase username')
parser.add_argument('--db_password','-dbP', type=str, default=None, help='Provide the dabatabase password')


args = parser.parse_args()
	 

if args.db_password is None:
    raise Exception('You must provide database password')


class retrieve_data():

	def __init__(self, fs, database):
		self.fs = fs
		self.database = database
	
	def retrieve_image (self):
		output_dir = "./pictures"

		try:
			os.makedirs(output_dir)
		except FileExistsError:
			pass

		data = self.database.fs.files.find({})
		for image in data:
			image_id = image['_id']
			image_name = image['filename']
			
			retrieved_image = self.fs.get(image_id).read()
			download_location = f"{output_dir}/{image_name}.jpg"
			with open(download_location, "wb") as d:
				d.write(retrieved_image)

	def retrieve_text(self):
		output_dir = "./text"
		
		try:
			os.makedirs(output_dir)
		except FileExistsError:
			pass

		data = self.database.text.find({})
		for text in data:
		
			text_name = text['file_name']
			retrieved_text = text['contents']
			download_location = f"{output_dir}/{text_name}.txt"
			with open(download_location, "wb") as d:
				d.write(retrieved_text)
		
	def retrieve_comments(self):
		output_dir = "./comments"
		
		try:
			os.makedirs(output_dir)
		except FileExistsError:
			pass

		data = self.database.comments.find({})
		
		for comment in data:

			comment_name = comment['file_name']
			retrieved_comment = comment['contents']
			download_location = f"{output_dir}/{comment_name}.json"
			with open(download_location, "wb") as d:
				d.write(retrieved_comment)


if __name__ == '__main__':
	connection = mongodb_connect(args.db_username, args.db_password)
	db = connection[args.database]
	fs = gridfs.GridFS(db)
	
	data = retrieve_data(fs, db)
	data.retrieve_image()
	data.retrieve_text()
	data.retrieve_comments()
	
	print("Download Done!!!")


