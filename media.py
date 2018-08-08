#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser


class Movie():
    """Essa classe define o objeto Movie (Filme)"""
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_poster_image,
                 movie_trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

    def show_trailer(self):
        """Abre o video do Movie"""
        webbrowser.open(self.trailer_youtube_url)
