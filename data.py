#creation csv, json:
"""with open('data_WaTor.json')as file:
        data = json.load(file)"""
import csv 
import json

def create_csv(chronon, number_of_fish, number_of_sharks, width, height):
    with open("data_WaTor.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"Taille de la grille :  {height} x {width}"])
        writer.writerow([])
        writer.writerow(["chronon", "nb_fish", "nb_shark"])
        writer.writerow([chronon, number_of_fish, number_of_sharks])
        

def update_csv(chronon, number_of_fish, number_of_sharks):
    with open("data_WaTor.csv", mode='of', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([chronon, number_of_fish, number_of_sharks])
    