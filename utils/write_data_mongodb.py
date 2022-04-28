import gridfs
from mongodb_connection import *
import glob
import os

def save_file_to_db(collection, fname):
	"""save file to mongodb
	args:
		collection : collection of the database
		fname : iterator, all the filenames
	return:
		void
	"""
	for file in fname:
		with open(file, "rb") as f:
			content_file = f.read()
		file_name = os.path.basename(file).rsplit('.', 1)[0]	
		file_dict = {"file_name":file_name, "contents" : content_file}
		collection.insert_one(file_dict)
		
def save_image_to_db(database, images_fname):
	"""save image to mongodb
	args:
		database : collection of the database
		images_fname : iterator, all the image filenames
	return:
		void
	"""
	fs = gridfs.GridFS(database)
	
	for image in images_fname:
		with open(image, "rb") as f:
			content_image = f.read()
		image_name = os.path.basename(image).rsplit('.', 1)[0]
		fs.put(content_image, filename = image_name)
	


def write_data(database : str,
		username: str,
		password: str,
		files_dir: str):
 
    connection = mongodb_connect(username, password)
    db = connection[database] #connect to db
    comment_collection = db["comments"] #collection to store comments
    text_collection    = db["text"]     #collection to store text

    images_fname   = glob.glob(f"{files_dir}/*.jpg")
    comments_fname = glob.glob(f"{files_dir}/*.json")
    text_fname     = glob.glob(f"{files_dir}/*.txt")

    save_file_to_db(comment_collection, comments_fname)
    save_file_to_db(text_collection, text_fname)
    save_image_to_db(db, images_fname)

    print("upload completed...")



