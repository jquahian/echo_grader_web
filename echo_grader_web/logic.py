import os


video_path = "echo_grader_web/static"

video_list = []
for file in os.listdir(video_path):
	if file[-3:] == "mp4":
		video_list.append(file)

# init_vid = video_list[0]
'''
1) Query the database to see if there is already an entry for this clip for this user

2) if yes, reload all of the data from the database into the grader form

3) if no, start the grader form with default values
'''

# DATABASE QUERY -- CHECK USER + CLIP NAME



