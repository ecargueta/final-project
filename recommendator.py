import pandas as pd
import random as rand

class Recommendation:
  """ A class that holds the song, album, artist recommendation per to the user's input.
  """
  def __init__(self):
      """ Should define the necessary attributes to their corresponding values.
      """
      pass

  def user_input():
      """ The user will be prompt with a message that asks them to first input 
      genre of music. They will then be asked to input the type of music they want,
      either album, song, or artist. 
      
      Args:

      Return:
        return user input
      """
      pass

  def get_album(album_text):
      """ If the user inputs that they want a album recommended, this function will
      select a random album based from the album file.
      
      Args:
        album_text: text file to parse for recommended album
      """
      df = pd.read_csv(album_text)
      albums_list = df["Album"].tolist()
      return rand.choice(albums_list)

  def get_song(song_text):
      """ If the user inputs that they want a song recommended, this function will
      select a random song based from the song file.
      
      Args:
        song_text: text file to parse for recommended song
      """
      pass

  def get_artist(artist_text):
      """ If the user inputs that they want a artist recommended, this function will
      select a random artist based from the artist file.
      
      Args:
        artist_text: text file to parse for recommended artist
        
      """
      pass

  def read_file(self):
      """once the user inputs all of the recommendations they want, 
      this function will read the file and output the suggessted recommendation(s).
      
      Args:
      album_file(str): path to album recommnedation(s) file
      song_file(str): path to song recommendaiton(s) file
      artist_file(str): path to artist recommendaiton(s) file
      
      """
      wanted_recommedation = self.user_input()
      if wanted_recommedation == "song":
        output_recommedation = self.get_song()
      elif wanted_recommedation == "artist":
        output_recommedation = self.get_artist()
      elif wanted_recommedation == "album":
        output_recommedation = self.get_album()
      return output_recommedation

  def main():
      """ Will open the text_file or specifc recommendation(s) based on the user's input and desired output
      
      Args: 
      path: Gets the paths to the text_file
      
      Return:
        a tuple containing the wanted type of recommendation by the user and then
        the recommendation made
      """
      pass

  def parse_args():
      """Parse command-line arguments.
      
      Args:Args:
        arglist (list of str): list of arguments from the command line.
      """
      pass

  if __name__== "main":
    """"Will print the recommendations to the user
    """
  pass