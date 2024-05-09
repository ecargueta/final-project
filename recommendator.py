import pandas as pd
import random as rand
from argparse import ArgumentParser

SongDir = {
            "rap":{"artist":[],"song":[],"album":[]},
            "pop":{"artist":[],"song":[],"album":[]},
            }

def process_data(music_csv):
        data = pd.read_csv(music_csv)
        df = pd.DataFrame(data)
        
        def get_first_genre(genres_string):
            if pd.isna(genres_string):
                return None
            return genres_string.split(',')[0]
        # artists
        for index,row in df.iterrows():
            artist_genre_tuple = (row['track_artist'], row['playlist_genre'])
            if artist_genre_tuple[1] not in SongDir.keys():
                SongDir[artist_genre_tuple[1]] = {"artist":[],"song":[],"album":[]}
            else:
                SongDir[artist_genre_tuple[1]]["artist"].append(artist_genre_tuple[0])

        #songs
        for index,row in df.iterrows():
            genre_song_tuple = (row['track_name'], row['playlist_genre'])
            if genre_song_tuple[1] not in SongDir.keys():
                SongDir[genre_song_tuple[1]] = {"artist":[],"song":[],"album":[]}
            else:
                SongDir[genre_song_tuple[1]]["song"].append(genre_song_tuple[0])
        #albums
        for index,row in df.iterrows():
            albums_genre_tuple = (row['track_album_name'], get_first_genre(row['playlist_genre']))
            if albums_genre_tuple[1] not in SongDir.keys():
                SongDir[albums_genre_tuple[1]] = {"artist":[],"song":[],"album":[]}
            else:
                SongDir[albums_genre_tuple[1]]["album"].append(albums_genre_tuple[0]) 
        return SongDir

class Recommendation:
    """ A class that holds the song, album, artist recommendation per to the user's input."""
  
  
    def __init__(self):
        """ Should define the necessary attributes to their corresponding values.
        """
        self.genre = None
        self.recommendation_type = None


    def user_input(self):
        """ The user will be prompt with a message that asks them to first input 
        genre of music. They will then be asked to input the type of music they want,
        either album, song, or artist. 
        
        Args:

        Return:
        return user input
        """
        self.genre = input("Enter the genre of music: ")
        self.recommendation_type = input("What type of music do you want? (album, song, or artist): ")
        return self.genre, self.recommendation_type
    
    def get_album(self):
        """ If the user inputs that they want a album recommended, this function will
      select a random album based from the album file.
      
      Args:
        album_text: text file to parse for recommended album
         """
        keys = list(SongDir.keys())
        genre = rand.choice(keys)
        recommendations = SongDir[genre]["album"]
        output_recommendation = rand.choice(recommendations)
        return output_recommendation

    def get_song(self):
    
        """ If the user inputs that they want a song recommended, this function will
            select a random song based from the song file.
      
            Args:
                song_text: text file to parse for recommended song
        """

        keys = list(SongDir.keys())
        genre = rand.choice(keys)
        recommendations = SongDir[genre]["song"]
        output_recommendation = rand.choice(recommendations)
        return output_recommendation
    
      
      

    def get_artist(self):
        """ If the user inputs that they want a artist recommended, this function will
        select a random artist based from the artist file.
      
        Args:
            artist_text: text file to parse for recommended artist
        
        """
        keys = list(SongDir.keys())
        genre = rand.choice(keys)
        recommendations = SongDir[genre]["artist"]
        output_recommendation = rand.choice(recommendations)
        return output_recommendation

    def read_file(self):
        """once the user inputs all of the recommendations they want, 
      this function will read the file and output the suggessted recommendation(s).
      
      Args:
      album_file(str): path to album recommnedation(s) file
      song_file(str): path to song recommendaiton(s) file
      artist_file(str): path to artist recommendaiton(s) file
      
        """
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
        except :
                print("the genre is nonexistent in our library")

           
    
        
    def main(self):
        args = parse_args()
        Song_Dir = process_data(args.music_csv)
        recommendation = Recommendation()
        output_rec = recommendation.read_file()
        if output_rec:
            print(f"Your recommended {recommendation.recommendation_type} is: {output_rec}")
        else:
            print("Sorry, no recommendations found.")
        return output_rec
                


def parse_args():
      """Parse command-line arguments.
      
      Args:Args:
        arglist (list of str): list of arguments from the command line.
      """
      parser =  ArgumentParser()
      parser.add_argument("music_csv",type=str, help= "stored data")
      return parser.parse_args()
if __name__== "__main__":
    """"Will print the recommendations to the user
    """
    recommendation = Recommendation()
    song_recommendation = recommendation.main()



