import sys

from pprint import pprint

def parse_relationships(relations):
    if relations == 'None':
        return []
    return relations.split(',')

def parse_file(file_path):
    plants = {}
    with open(file_path, 'r') as f:
        for line in f.readlines():
            num, plant_info = line.strip().split(' ', 1)
            plant_name, friends, enemies = plant_info.split('|')
            plants[plant_name] = {
                'positive': parse_relationships(friends),
                'negative': parse_relationships(enemies),
            }
    return plants

if __name__ == '__main__':
    plants = parse_file('plantdata.txt')
    pprint(plants)

