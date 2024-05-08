import pandas as pd
import random as rand
from argparse import ArgumentParser

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
      
      self.genre = print(input("Enter the genre of music: "))
      self.recommendation_type = print(input("What type of music do you want? (album, song, or artist): "))
      return self.genre, self.recommendation_type

      
  def get_album(album_text):
      """ If the user inputs that they want a album recommended, this function will
      select a random album based from the album file.
      
      Args:
        album_text: text file to parse for recommended album
      """
      df = pd.read_csv(album_text)
      albums_list = df["Album"].tolist()
      return rand.choice(albums_list)

  def get_song(songs_text):
    
      """ If the user inputs that they want a song recommended, this function will
      select a random song based from the song file.
      
      Args:
        song_text: text file to parse for recommended song
      """
      df = pd.read_csv("songs.csv")
      song_list = df["title"].tolist()
      return rand.choice(song_list)
    
  def get_artist(artist_text):
      """ If the user inputs that they want a artist recommended, this function will
      select a random artist based from the artist file.
      
      Args:
        artist_text: text file to parse for recommended artist
        
      """
      df = pd.read_csv(artist_text, usecols = ['Artist','artist_count','bpm'])
      artist_name = df['Artist'].str.split(',', expand=True)[0]
      artist_list = artist_name.tolist()
      return rand.choice(artist_list)

  def read_file(self, album_text, song_text, artist_text):
      """once the user inputs all of the recommendations they want, 
      this function will read the file and output the suggessted recommendation(s).
      
      Args:
      album_file(str): path to album recommnedation(s) file
      song_file(str): path to song recommendaiton(s) file
      artist_file(str): path to artist recommendaiton(s) file
      
      """
      wanted_recommedation = self.user_input()
      if wanted_recommedation == "song":
        output_recommedation = self.get_song(song_text)
      elif wanted_recommedation == "artist":
        output_recommedation = self.get_artist(artist_text)
      elif wanted_recommedation == "album":
        output_recommedation = self.get_album(album_text)
      return output_recommedation

  def parse_args():
      """Parse command-line arguments.
      
      Args:Args:
        arglist (list of str): list of arguments from the command line.
      """
      parser = ArgumentParser()
      parser.add_argument("album_csv",type=str, help= "stored data")
      parser.add_argument("songs_csv", type=str, help= "stored data")
      parser.add_argument("Artist_csv", type=str, help= "stored data")
      return parser.parse_args()
    
  def main():
      """ Will open the text_file or specifc recommendation(s) based on the user's input and desired output
      
      Args: 
      path: Gets the paths to the text_file
      
      Return:
        a tuple containing the wanted type of recommendation by the user and then
        the recommendation made
      """
      args = Recommendation.parse_args()
      recommender = Recommendation()
      recommender = recommender.user_input()
      recommendation = recommender.read_file(args.album_csv, args.songs_csv, args.Artist_csv)
      print("Recommended:", recommendation)

  if __name__== "main":
    """"Will print the recommendations to the user
    """
    main()  