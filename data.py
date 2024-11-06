#creation csv, json:
"""with open('data_WaTor.json')as file:
        data = json.load(file)"""
import csv 
import json
import matplotlib as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_csv(chronon, number_of_fish, number_of_sharks):
    with open("data_WaTor.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow([f"Taille de la grille :  {height} x {width}"])
        #writer.writerow([])
        writer.writerow(["chronon", "nb_fish", "nb_shark"])
        writer.writerow([chronon, number_of_fish, number_of_sharks])
        

def update_csv(chronon, number_of_fish, number_of_sharks):
    with open("data_WaTor.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([chronon, number_of_fish, number_of_sharks])
    
def create_plot():
    
    data = pd.read_csv('data_WaTor.csv', sep=',')
    data.rename(index=str, columns={"nb_fish":"number of fish", "nb_shark":"number of sharks"}, inplace=True)
    data["number of animals"]=data["number of fish"]+data["number of sharks"]
    plt.clf()
    
    plt.stairs(data["number of fish"], color="lightblue", label='Number of fish')
    plt.stairs(data["number of sharks"], color="darkblue", label='Number of sharks')
    plt.title("Evolution of animals population")
    plt.xlabel("Chronons")
    plt.ylabel("Number of animal")
    plt.legend() # a revoir pour ajouter
   
    plt.savefig('data.png', bbox_inches='tight', dpi = 150) #bbox_inches pour éviter des marges trop grandes
   