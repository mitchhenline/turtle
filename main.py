import csv

class Enemy():
    def __init__(self, enemy_id, name, enemy_rank, image_url, bio):
        self.enemy_id = enemy_id
        self.name = name
        self.enemy_rank = enemy_rank
        self.image_url = image_url
        self.bio = bio

    def __repr__(self):