from django.db import models



class Resolution:
    def __init__(self):
        self.resolution = []
        self.mistakes = Mistakes()


class Mistakes:
    def __init__(self):
        self.mistakes = {}


class Link:
    def __init__(self):
        self.link = ''

