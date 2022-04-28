#coding: utf-8

"""

@Ryad Lotfi MAHTAL
"""

import sys 
sys.path.insert(1, './utils') 

from data_processor import * 
from data_collector import *
from write_data_mongodb import *
import argparse

parser = argparse.ArgumentParser(description='Web Scraping from Instagram')

parser.add_argument('--username','-U',type=str, default=None, help='Provide instagram username to log in')
parser.add_argument('--subject','-S',type=str, default=None, help='Provide the subject')
parser.add_argument('--database','-DB', type=str, default="insta_scrap", help='Provide the name of the database')
parser.add_argument('--db_username','-dbU', type=str, default="Ryad", help='Provide the dabatabase username')
parser.add_argument('--db_password','-dbP', type=str, default=None, help='Provide the dabatabase password')
parser.add_argument('--max_count','-C', type=int, default=5, help='Maxcount of data retrieved')


args = parser.parse_args()

if args.username is None:
    raise Exception(f'You must provide username to log in and scrap data from Instagram')
if args.subject is None:
    raise Exception('You must provide subject')
if args.db_password is None:
    raise Exception('You must provide database password')


def lunch_scraping(username : str, subject : str, db_username, db_password, max_count):
	hashtags = clean_text(subject)
	folder_name = hashtags[0]
	print("hashtags are : ", hashtags)
	print("Begin Scraping ... !!!")
	DataScraper(hashtags, username, max_count)
	write_data(args.database, db_username, db_password, files_dir=f"./#{folder_name}")
	
	
if __name__ == '__main__':
	lunch_scraping(username = args.username, subject = args.subject, db_username = args.db_username, db_password = args.db_password, max_count = args.max_count)
	 
