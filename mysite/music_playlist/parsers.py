"""
All the websites parsers should fall as a part of a class Parser
"""

class MusicParser(song_url):
    self.song_name = None
    self.artist_name = None
    self.media_url = None
    self.song_url = song_url
    
    def parse_webpage(self, song_url):
        pass

    def guess_artist_song_from_link(self, song_url):
        """
        A rough estimation of what a song's artist / could be, got by splitting
        the string from the url.
        """
        song_name = link.split('/')[-1] #the object name
        artist = song_name.split('-')[0]
        song_name = song_name.split('-')[1].split('.')[0]
        return artist, song_name

    def get_artist_song_from_file(self, media_url):
        """
        Get info by running through the metadata of the media file.
        """
        pass

    
