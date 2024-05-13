import pandas as pd
import random as rand
from argparse import ArgumentParser

# initalize a dictionary that will be updated in the following functions
SongDir = {
            "rap":{"artist":[],"song":[],"album":[]},
            "pop":{"artist":[],"song":[],"album":[]},
            }

def process_data(music_csv):
        """Define the function to be able to process the data from the csv file
            depending on if the user wants a artist, song, or ablum recommendation.
            
            Args:
                music_csv (file): the file path to the csv file
                
            Returns:
                SongDir (dict): a dictionary that will contain the requested information
                from the data set.
            
            Side effects: 
                Modifies the SongDir dictionary 
        """
        # sets the data from the csv file to a pandas dataframe
        data = pd.read_csv(music_csv)
        df = pd.DataFrame(data)
        # check through the strings to see if something is not available 
        def get_first_genre(genres_string):
            if pd.isna(genres_string):
                return None
            return genres_string.split(',')[0]
        # for loop to search through for artists
        for index,row in df.iterrows():
            artist_genre_tuple = (row['track_artist'], row['playlist_genre'])
            if artist_genre_tuple[1] not in SongDir.keys():
                SongDir[artist_genre_tuple[1]] = {"artist":[],"song":[],"album":[]}
            else:
                SongDir[artist_genre_tuple[1]]["artist"].append(artist_genre_tuple[0])
        # for loop to search through for songs
        for index,row in df.iterrows():
            genre_song_tuple = (row['track_name'], row['playlist_genre'])
            if genre_song_tuple[1] not in SongDir.keys():
                SongDir[genre_song_tuple[1]] = {"artist":[],"song":[],"album":[]}
            else:
                SongDir[genre_song_tuple[1]]["song"].append(genre_song_tuple[0])
        # for loop to search through for albums
        for index,row in df.iterrows():
            albums_genre_tuple = (row['track_album_name'], get_first_genre(row['playlist_genre']))
            if albums_genre_tuple[1] not in SongDir.keys():
                SongDir[albums_genre_tuple[1]] = {"artist":[],"song":[],"album":[]}
            else:
                SongDir[albums_genre_tuple[1]]["album"].append(albums_genre_tuple[0]) 
        # return the now updated dictionary
        return SongDir

class Recommendation:
    """ A class that holds the song, album, artist recommendation per to the user's input."""
  
    def __init__(self):
        """ Should define the necessary attributes to their corresponding values.
        """
        self.genre = None
        self.recommendation_type = None
        self.genre_list = None

    def user_input(self):
        """The user will be prompt with a message that asks them to first input 
            genre of music. They will then be asked to input the type of music 
            they want,ceither album, song, or artist. 
        
            Args:
                self: a reference to the class
            
            Return:
                return user input
        """
        # initial prompt to ask the user the genre and type of music wanted
        genre_list = rand.sample(list(SongDir.keys()), 4)
        self.genre = input(f"Here are some genres to consider: {', '.join(genre_list)}\nEnter the genre of music: ")
        self.recommendation_type = input("What type of music do you want? (album, song, or artist): ")
        return self.genre.lower(), self.recommendation_type.lower()
    
    def get_album(self):
        """ If the user inputs that they want a album recommended, this function will
            select a random album based from the album file.
      
            Args:
                self: a reference to the class
                
            Return: 
                output_recommendation: the random recommendation if an album is wanted
        """
        # ensure that the recommendation from the SongDir is randomized
        keys = list(SongDir.keys())
        genre = rand.choice(keys)
        recommendations = SongDir[genre]["album"]
        output_recommendation = rand.choice(recommendations)
        return output_recommendation

    def get_song(self):
        """ If the user inputs that they want a song recommended, this function will
            select a random song based from the song file.
      
            Args:
                self: a reference to the class
                
            Return:
                output_recommendation: the random recommendation if a song is wanted
        """
        # ensure that the recommednation from SongDir is random for the song
        keys = list(SongDir.keys())
        genre = rand.choice(keys)
        recommendations = SongDir[genre]["song"]
        output_recommendation = rand.choice(recommendations)
        return output_recommendation
    
    def get_artist(self):
        """ If the user inputs that they want a artist recommended, this function 
            will select a random artist based from the artist file.
      
            Args:
                self: a reference to the class
            
            Return:
                output_recommendation: the random recommendation if an artist is wanted
        """
        # for the artist, use random to pick a recommendation
        keys = list(SongDir.keys())
        genre = rand.choice(keys)
        recommendations = SongDir[genre]["artist"]
        output_recommendation = rand.choice(recommendations)
        return output_recommendation

    def read_file(self):
        """Define a function where once the user inputs all of the recommendations 
            they want, it will read the file and output the suggessted 
            recommendation(s).
      
            Args:
                self: a reference to the class
                
            Returns:
                output_recommendation: will connect to the required function 
                depending on what the user wants
        """
        # use a try to ensure that the wanted genre & music type is correct
        try:
            Desired_Genre,Desired_recommedation = self.user_input()
            if Desired_recommedation == "song" and Desired_Genre == "any":
                output_recommendation = self.get_song()
            elif Desired_recommedation == "artist" and Desired_Genre == "any":
                output_recommendation = self.get_artist()
            elif Desired_recommedation == "album" and Desired_Genre == "any":
                output_recommendation = self.get_album()
            else:
                if Desired_Genre in SongDir.keys():
                    recommendations = SongDir[Desired_Genre][Desired_recommedation]
                    if recommendations: 
                        output_recommendation = rand.choice(recommendations)
            return output_recommendation
        # if the inputted information is not correct the message wll be printed
        except:
            print("You may have selected a recommendation type or genre that does not exist.")

    def main(self):
        """Define a function that will connect the necessary functions and print
            out the recommendation to the user.
            
            Args: 
                self: a reference to the class
            Returns:
                output_rec (str): the randomized recommendation 
        """
        # use the parse_args so that the user can use the command line
        args = parse_args()
        # call the process_data to process the file placed in the command line
        Song_Dir = process_data(args.music_csv)
        # call the Recommendation() class and read_file() function 
        recommendation = Recommendation()
        output_rec = recommendation.read_file()
        # if the random recommendation is true, print it out, and if not, state that
        if output_rec:
            print(f"Your recommended {recommendation.recommendation_type} is: {output_rec}")
        else:
            print("Sorry, no recommendations found.")
        return output_rec
                
def parse_args():
      """Parse command-line arguments.

            Returns:
                the ArgumentParser() object that was made
      """
      parser =  ArgumentParser()
      parser.add_argument("music_csv", type = str, help = "data from csv file")
      return parser.parse_args()
  
if __name__== "__main__":
    """"Will print the recommendations to the user
    """
    # call the Recommendation() class and then the results from the main function
    recommendation = Recommendation()
    song_recommendation = recommendation.main()
