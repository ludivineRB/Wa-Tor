#creation csv, json:
"""with open('data_WaTor.json')as file:
        data = json.load(file)"""
import csv 
import json
import matplotlib as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def create_csv(chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark, average_nb_descendants_fish,average_nb_descendants_shark, average_distance_fish, average_distance_shark, max_nb_descendants_fish, max_nb_descendants_shark, max_distance_fish, max_distance_shark):
    with open("data_WaTor.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(["chronon", "nb_fish", "nb_shark", "average_age_fish", "average_age_shark", "nb_descendants_fish", 
                         "nb_descendants_shark", "average_distance_fish", "average_distance_shark", 
                         "max_nb_descendants_fish", "max_nb_descendants_shark", "max_distance_fish", "max_distance_shark"])
        writer.writerow([chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark,average_nb_descendants_fish, average_nb_descendants_shark, average_distance_fish, average_distance_shark, max_nb_descendants_fish,max_nb_descendants_shark, max_distance_fish, max_distance_shark])
        

def update_csv(chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark,average_nb_descendants_fish, 
               average_nb_descendants_shark, average_distance_fish, average_distance_shark, 
               max_nb_descendants_fish, max_nb_descendants_shark, max_distance_fish, max_distance_shark):
    with open("data_WaTor.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark,
                         average_nb_descendants_fish, average_nb_descendants_shark, average_distance_fish, 
                         average_distance_shark, max_nb_descendants_fish, max_nb_descendants_shark
                         , max_distance_fish, max_distance_shark])
    
    
def create_plot():
    
    data = pd.read_csv('data_WaTor.csv', sep=',')
    data.rename(index=str, columns={"nb_fish":"number of fish", "nb_shark":"number of sharks"}, inplace=True)
    data["number of animals"]=data["number of fish"]+data["number of sharks"]
    plt.clf()
    plt.stairs(data["number of fish"], color="lightblue", label='Number of fish')
    plt.stairs(data["number of sharks"], color="darkblue", label='Number of sharks')
    plt.title("Evolution of animals population")
    plt.xlabel("Time")
    plt.ylabel("Number of animal")
    plt.legend() # a revoir pour ajouter
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('data.png', bbox_inches='tight', dpi = 120) #bbox_inches pour éviter des marges trop grandes
    
    plt.clf()
    plt.title('Average Distance Traveled')
    plt.plot(data["chronon"], data["average_distance_fish"], color="lightblue", label = "Fish")
    plt.plot(data["chronon"], data["average_distance_shark"], color="darkblue", label = "Shark")
    plt.xlabel('Time')
    plt.ylabel('Distance')
    plt.legend()
    plt.savefig('distance.png', bbox_inches='tight', dpi = 120)