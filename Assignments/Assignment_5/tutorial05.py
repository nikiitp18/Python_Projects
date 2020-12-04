
import re
import os 

# How I Met Your Mother!! seires episode renaming logic is implemented

def rename_HIMYM(series_selected):
	webseries_file = os.path.join('Subtitles',series_selected)
	director_list = os.listdir(webseries_file)
	for each_dir in director_list:
		try:
			# seprating using regular expression
			name_in_parts = re.findall(r'\d+',each_dir)
			# segregating season and episode number
			episode_number = (name_in_parts[1]).strip()
			season_number = (name_in_parts[0]).strip()
			# season particular have been restored
			name_in_parts = re.split('-',each_dir)
			name_of_episode = (re.split(r'\.',name_in_parts[2])[0]).strip()
			used_extension = (re.split(r'\.',each_dir)[-1]).strip()
			webseries_file = os.path.join(os.getcwd(),webseries_file)
			while(len(episode_number) < int(selected_episode)):
				episode_number = '0' + episode_number
			while(len(season_number) < int(selected_season)):
				season_number = '0' + season_number
			os.chdir(webseries_file)
			# renaming of file is done here
			os.rename(each_dir,'How I Met Your Mother - Season '+ season_number + ' Episode ' + episode_number + '- ' + name_of_episode + '.' + used_extension) 
		except:
			os.remove(each_dir)			

# Suits!! seires episode renaming logic is implemented.

def rename_Suits(series_selected):
	webseries_file = os.path.join('Subtitles',series_selected)
	director_list = os.listdir(webseries_file)
	for each_dir in director_list:
		try:
			# seprating using regular expression
			name_in_parts = re.findall(r'\d+',each_dir)
			# segregating season and episode number
			episode_number = (name_in_parts[1]).strip()
			season_number = (name_in_parts[0]).strip()
			# season particular have been restored
			name_in_parts = re.split('-',each_dir)
			name_of_episode = (re.split(r'\.',name_in_parts[2])[0]).strip()
			used_extension = (re.split(r'\.',each_dir)[-1]).strip()
			webseries_file = os.path.join(os.getcwd(),webseries_file)
			while(len(episode_number) < int(selected_episode)):
				episode_number = '0' + episode_number
			while(len(season_number) < int(selected_season)):
				season_number = '0' + season_number
			os.chdir(webseries_file)
			# renaming of file is done here
			os.rename(each_dir,'Suits - Season '+ season_number + ' Episode ' + episode_number + '- ' + name_of_episode + '.' + used_extension)    
		except:
			os.remove(each_dir)

# Sherlock!! seires episode renaming logic is implemented

def rename_Sherlock(series_selected):
	webseries_file = os.path.join('Subtitles',series_selected)
	director_list = os.listdir(webseries_file)
	for each_dir in director_list:
		try:
			# seprating using regular expression
			name_in_parts = re.findall(r'\d+',each_dir)
			# segregating season and episode number
			season_number = (name_in_parts[0]).strip()
			episode_number = (name_in_parts[1]).strip()
			# season particular have been restored
			used_extension = (re.split(r'\.',each_dir)[-1]).strip()
			webseries_file = os.path.join(os.getcwd(),webseries_file)
			while(len(episode_number) < int(selected_episode)):
				episode_number = '0' + episode_number
			while(len(season_number) < int(selected_season)):
				season_number = '0' + season_number	
			os.chdir(webseries_file)
			# renaming of file is done here
			os.rename(each_dir,'Sherlock- Season '+ season_number + ' Episode ' + episode_number + '.' + used_extension) 
		except:
			os.remove(each_dir)	

# FIR seires episode renaming logic is implemented

def rename_FIR(series_selected):
	webseries_file = os.path.join('Subtitles',series_selected)
	director_list = os.listdir(webseries_file)
	for each_dir in director_list:
		try:
			# seprating using regular expression
			name_in_parts = re.findall(r'\d+',each_dir)
			# segregating season and episode number
			episode_number = (name_in_parts[0]).strip()
			# season particular have been restored
			used_extension = (re.split(r'\.',each_dir)[-1]).strip()

			webseries_file = os.path.join(os.getcwd(),webseries_file)
			while(len(episode_number) < int(selected_episode)):
				episode_number = '0' + episode_number

			os.chdir(webseries_file)
			# renaming of file is done here
			os.rename(each_dir,'FIR-' + ' Episode ' + episode_number + '.' + used_extension) 
		except:
			os.remove(each_dir) 

# Game of Thrones seires episode renaming logic is implemented

def rename_GOT(series_selected):
	webseries_file = os.path.join('Subtitles',series_selected)
	director_list = os.listdir(webseries_file)
	for each_dir in director_list:
		try:
			# seprating using regular expression
			name_in_parts =  re.split('-',each_dir)
			# segregating season and episode number
			season_number=re.findall(r'\d+',name_in_parts[1])[0]
			episode_number=re.findall(r'\d+',name_in_parts[1])[1]
			# season particular have been restored
			name_of_episode = (re.split(r'\.',name_in_parts[2])[0]).strip()
			used_extension = (re.split(r'\.',name_in_parts[2])[-1]).strip()

			webseries_file = os.path.join(os.getcwd(),webseries_file)
			while(len(episode_number) < int(selected_episode)):
				episode_number = '0' + episode_number
			while(len(season_number) < int(selected_season)):
				season_number = '0' + season_number

			os.chdir(webseries_file)
			# renaming of file is done here
			os.rename(each_dir,'Game of Thrones- Season '+ season_number + ' Episode ' + episode_number + '- ' + name_of_episode + '.' + used_extension)  
		except:
			os.remove(each_dir)	



# mapping webseries name with their code 
season = {1:'FIR',2:'Game of Thrones',3:'How I Met Your Mother',4:'Sherlock',5:'Suits'}

# webseries to be choose, list of webseries is displayed
webseries_choice = int(input("Webseries we have in our system:\n1. FIR \n2. Game of Thrones \n3. How I Met Your Mother \n4. Sherlock \n5. Suits \nEnter a number corresponding to a series: "))

# season is selected for the above specified webseries
selected_season = input(f"Enter season number of {season[webseries_choice]} webseries: ")

# episode number is for the specified season of the given webseries
selected_episode = input(f"Enter episode number of season {selected_season} of {season[webseries_choice]} webseries: ")



# logic part of executing function depending upon the input of the user
if webseries_choice == 3:
	rename_HIMYM(season[3])
elif webseries_choice == 5:
	rename_Suits(season[5])
elif webseries_choice == 4:
	rename_Sherlock(season[4])
elif webseries_choice == 1:
	rename_FIR(season[1])
elif webseries_choice == 2:
	rename_GOT(season[2])
else:
    print(f"\nwarning:  make sure to write the code of the webseries as given. \ninvalid choice!! webseires with code '{webseries_choice}' doesn't exist in our system.")    



