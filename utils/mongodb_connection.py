import pymongo
from pymongo import MongoClient
import gridfs


def mongodb_connect(username: str, 
		 password:  str):
	try:
		cluster = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.hkv6j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") #connect to cluster
		print("MongoDb connected ...")
	except Exception as e:
		print("MongoDb failed connection", e)
		
	return cluster
	

