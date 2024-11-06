import csv 
import matplotlib as plt
import pandas as pd
import matplotlib.pyplot as plt


def create_csv(chronon:int, number_of_fish:int, number_of_sharks:int, average_age_fish:int, average_age_shark:int,
                average_nb_descendants_fish:int,average_nb_descendants_shark:int, average_distance_fish:int, average_distance_shark:int, max_nb_descendants_fish:int, 
                max_nb_descendants_shark:int, max_distance_fish:int, max_distance_shark:int)->None:
    """_summary_ creates a CSV file with the parameters below

    Args:
        chronon (int): _description_
        number_of_fish (int): _description_
        number_of_sharks (int): _description_
        average_age_fish (int): _description_
        average_age_shark (int): _description_
        average_nb_descendants_fish (int): _description_
        average_nb_descendants_shark (int): _description_
        average_distance_fish (int): _description_
        average_distance_shark (int): _description_
        max_nb_descendants_fish (int): _description_
        max_nb_descendants_shark (int): _description_
        max_distance_fish (int): _description_
        max_distance_shark (int): _description_
    """
    with open("data_WaTor.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(["chronon", "nb_fish", "nb_shark", "average_age_fish", "average_age_shark", "nb_descendants_fish", 
                         "nb_descendants_shark", "average_distance_fish", "average_distance_shark", 
                         "max_nb_descendants_fish", "max_nb_descendants_shark", "max_distance_fish", "max_distance_shark"])
        writer.writerow([chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark,
                         average_nb_descendants_fish, average_nb_descendants_shark, average_distance_fish, average_distance_shark, max_nb_descendants_fish,
                         max_nb_descendants_shark, max_distance_fish, max_distance_shark])
        

def update_csv(chronon:int, number_of_fish:int, number_of_sharks:int, average_age_fish:int, average_age_shark:int,
                average_nb_descendants_fish:int,average_nb_descendants_shark:int, average_distance_fish:int, average_distance_shark:int, max_nb_descendants_fish:int, 
                max_nb_descendants_shark:int, max_distance_fish:int, max_distance_shark:int)->None:
    """_summary_ writes a CSV file with the parameters below

    Args:
        chronon (int): _description_
        number_of_fish (int): _description_
        number_of_sharks (int): _description_
        average_age_fish (int): _description_
        average_age_shark (int): _description_
        average_nb_descendants_fish (int): _description_
        average_nb_descendants_shark (int): _description_
        average_distance_fish (int): _description_
        average_distance_shark (int): _description_
        max_nb_descendants_fish (int): _description_
        max_nb_descendants_shark (int): _description_
        max_distance_fish (int): _description_
        max_distance_shark (int): _description_
    """
    with open("data_WaTor.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([chronon, number_of_fish, number_of_sharks, average_age_fish, average_age_shark,
                         average_nb_descendants_fish, average_nb_descendants_shark, average_distance_fish, average_distance_shark, max_nb_descendants_fish,
                         max_nb_descendants_shark, max_distance_fish, max_distance_shark])
    
    
def create_plot()->None:
    """_summary_ creates evolution of animals population plot and Average Distance Traveled plot
    """
    #Evolution of Animals Population plot
    data = pd.read_csv('data_WaTor.csv', sep=',')
    data.rename(index=str, columns={"nb_fish":"number of fish", "nb_shark":"number of sharks"}, inplace=True)
    data["number of animals"]=data["number of fish"]+data["number of sharks"]
    plt.clf()
    plt.stairs(data["number of fish"], color="lightblue", label='Number of fish')
    plt.stairs(data["number of sharks"], color="darkblue", label='Number of sharks')
    plt.title("Evolution of Animals Population")
    plt.xlabel("Time")
    plt.ylabel("Number of animal")
    plt.legend()
    plt.savefig('media/data.png', bbox_inches='tight', dpi=120)
    #Average Distance Traveled plot
    plt.clf()
    plt.title('Average Distance Traveled')
    plt.plot(data["chronon"], data["average_distance_fish"], color="lightblue", label="Fish")
    plt.plot(data["chronon"], data["average_distance_shark"], color="darkblue", label="Shark")
    plt.xlabel('Time')
    plt.ylabel('Distance')
    plt.legend()
    plt.savefig('media/distance.png', bbox_inches='tight', dpi=120)