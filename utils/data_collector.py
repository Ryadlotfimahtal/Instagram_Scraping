"""
@Ryad Lotfi MAHTAL

This code aim to wrap data related to the subject giver. The data consist of the text description, images & comments. 
"""

import instaloader


def DataScraper(subject : list,
		username : str,
		max_count: int):

    """Function to wrap data from Instagram related to a subject and save text, comments & pictures related to that subject
	Args :
		subject : list of strings
		username : string 
		max_count : int
	Return :
		void
	"""
    L = instaloader.Instaloader(
			download_pictures=True,
			download_videos=False, 
			download_video_thumbnails=False,
			compress_json=False, 
			download_geotags=False, 
			save_metadata=False,
			post_metadata_txt_pattern=None, 
			max_connection_attempts=0,
			download_comments=True,) #To set all the parameters
			

    L.interactive_login(username) #asks for password 

    hashtag = subject.pop(0) #take the first elemnt
    posts = L.get_hashtag_posts(hashtag)

    count = 0
	#key_words = ["covid19", "china"]
    for post in posts:
        if all(x in post.caption_hashtags for x in subject): #take post that cite all the subject key words at the same time
            L.download_post(post, f"#{hashtag}")
        else:
            continue
        count += 1
        if (count > max_count):
            break
