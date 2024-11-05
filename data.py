#creation csv, json:
"""with open('data_WaTor.json')as file:
        data = json.load(file)"""
import csv 
import json

def create_csv(chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark, average_nb_descendants_fish, 
               average_nb_descendants_shark, average_distance_fish, average_distance_shark, 
               max_nb_descendants_fish, max_nb_descendants_shark, max_distance_fish, max_distance_shark):
    with open("data_WaTor.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(["chronon", "nb_fish", "nb_shark", "average_age_fish", "average_age_shark", "nb_descendants_fish", 
                         "nb_descendants_shark", "average_distance_fish", "average_distance_shark", 
                         "max_nb_descendants_fish", "max_nb_descendants_shark", "max_distance_fish", "max_distance_shark"])
        writer.writerow([chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark,average_nb_descendants_fish, 
                         average_nb_descendants_shark, average_distance_fish, average_distance_shark, max_nb_descendants_fish
                         ,max_nb_descendants_shark, max_distance_fish, max_distance_shark])
        

def update_csv(chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark,average_nb_descendants_fish, 
               average_nb_descendants_shark, average_distance_fish, average_distance_shark, 
               max_nb_descendants_fish, max_nb_descendants_shark, max_distance_fish, max_distance_shark):
    with open("data_WaTor.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark,
                         average_nb_descendants_fish, average_nb_descendants_shark, average_distance_fish, 
                         average_distance_shark, max_nb_descendants_fish, max_nb_descendants_shark
                         , max_distance_fish, max_distance_shark])
    