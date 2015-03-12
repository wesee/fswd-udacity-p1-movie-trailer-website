# import required modules
import webbrowser

# define movie class which has attributes and methods
# 	properties: title, storyline, poster_image_url, trailer_youtube_url, release_date
# 	methods: show_trailer()

class Movie():
    def __init__(self, m_title, m_storyline, m_poster_url, m_youtube_url, m_release_date):
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = m_poster_url
        self.trailer_youtube_url = m_youtube_url
        self.release_date = m_release_date

    # open web browser with the trailer url		
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
