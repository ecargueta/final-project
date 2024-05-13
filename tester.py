from recommendator import Recommendation

def test1():
    """use assert to test from the Recommendation(), the user's want for artist""" 
    random_recommendation = Recommendation()
    assert random_recommendation.user_input() == ("pop", "artist")

def test2():
    """use assert to test from the Recommendation(), the user's want for song"""
    random_recommendation = Recommendation()
    assert random_recommendation.user_input() == ("rap", "song")
    
def test3():
    """use assert to test from the Recommendation(), the user's want for an album"""
    random_recommendation = Recommendation()
    assert random_recommendation.user_input() == ("rock", "album")
    
def test4():
    """use assert to test the get_song() function and its connection to the 
        user's input
    """
    random_recommendation = Recommendation()
    random_recommendation.genre = "pop"
    random_recommendation.recommendation_type = "song"
    random_recommendation.read_file()
    assert isinstance(random_recommendation.get_song(), str)
    
def test5():
    """use assert to test the get_artist() function and its connection to the 
        user's input
    """
    random_recommendation = Recommendation()
    random_recommendation.genre = "pop"
    random_recommendation.recommendation_type = "artist"
    random_recommendation.read_file()
    assert isinstance(random_recommendation.get_artist(), str)
    
def test6():
    """use assert to test the get_album() function and its connection to the 
        user's input
    """
    random_recommendation = Recommendation()
    random_recommendation.genre = "pop"
    random_recommendation.recommendation_type = "album"
    random_recommendation.read_file()
    assert isinstance(random_recommendation.get_album(), str)