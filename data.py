#creation csv, json:
"""with open('data_WaTor.json')as file:
        data = json.load(file)"""
import csv 
import json

def create_csv(chronon, number_of_fish, number_of_sharks):
    with open("data_WaTor.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["chronon", "nb_fish", "nb_shark"])
        writer.writerow([chronon, number_of_fish, number_of_sharks])
        writer.writerow([])
    

def update_csv(chronon, number_of_fish, number_of_sharks):
    with open("data_WaTor.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([chronon, number_of_fish, number_of_sharks])
        writer.writerow([])
    """writer.writerow([f"Taille de la grille :  {height} x {width}"])
        writer.writerow([f"Nombre initial de requin :  {number_of_sharks}"])
        writer.writerow([f"Nombre initial de poisson :  {number_of_fish}"])
        writer.writerow([f"Temps de reproduction :  {reproduction_time}"])
        writer.writerow([f"Temps d' épuisement:  {starvation_time}"])"""