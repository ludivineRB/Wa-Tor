from Fish import Fish
from class_shark import Shark
import data
from printworld import print_world
import list_creation

height = 40
width = 40

#initialize number of animals
number_of_sharks = 25
number_of_fish = 200
number_of_animals = number_of_sharks + number_of_fish
list_of_fish, list_of_sharks, list_positions_fish, list_positions_shark = list_creation.list_creation(height, width, number_of_sharks, number_of_animals)
#initialize time
chronon = 0
#initialize the csv
data.create_csv(chronon, number_of_fish, number_of_sharks, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

#launch simulation
while len(list_of_fish) != 0 or len(list_of_sharks)!=0:
    print_world(list_positions_fish, list_positions_shark, height, width)
    temp_list_positions_fish = []
    temp_list_positions_shark = []
    temp_list_of_fish = []
    temp_list_of_shark = []
    temp_positions_babyshark = []
    temp_positions_babyfish = []
    list_of_shared_positions= [] 
    average_age_fish = 0
    average_age_shark = 0
    average_nb_descendants_fish = 0
    average_nb_descendants_shark = 0
    average_distance_fish = 0
    average_distance_shark = 0

    #loop to move sharks 
    for j in range(len(list_of_sharks)):
        x_old = list_of_sharks[j].x_coordinate
        y_old = list_of_sharks[j].y_coordinate
        list_of_sharks[j].move(list_positions_fish, list_positions_shark, temp_positions_babyshark)
        list_of_sharks[j].age += 1
        #checks starvation time of sharks
        if list_of_sharks[j].starvation_time == 0:
            pass
        else:
            temp_list_positions_shark.append((list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate))
            temp_list_of_shark.append(list_of_sharks[j])
            list_positions_shark[j] =(list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate)
            if list_of_sharks[j].x_coordinate != x_old or list_of_sharks[j].y_coordinate != y_old:
                list_of_sharks[j].distance += 1
            #reproduction of sharks
            if list_of_sharks[j].reproduction_time > 6:
                if list_of_sharks[j].x_coordinate != x_old or list_of_sharks[j].y_coordinate != y_old:
                    list_of_sharks[j].distance += 1
                    temp_list_of_shark.append(Shark(height, width, x_old,y_old, 0, 2, 0, 0, 0))
                    temp_list_positions_shark.append((x_old, y_old))
                    list_of_sharks[j].reproduction_time = 0
                    temp_positions_babyshark.append((x_old,y_old))
                    list_of_sharks[j].nb_descendants += 1
            #checks if shark eats a fish
            if list_of_sharks[j].starvation_time==3:
                list_of_shared_positions.append((list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate))

    #loop to move fish
    for i in range(len(list_of_fish)):
        if (list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate) in list_of_shared_positions:      
            pass
        else:
            x_old = list_of_fish[i].x_coordinate
            y_old = list_of_fish[i].y_coordinate
            list_of_fish[i].move(list_positions_fish, list_positions_shark, temp_positions_babyshark, temp_positions_babyfish)
            #refresh list of fish and list of fish positions    
            temp_list_positions_fish.append((list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate))
            list_positions_fish[i] = (list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate)
            temp_list_of_fish.append(list_of_fish[i])
            if list_of_fish[i].x_coordinate != x_old or list_of_fish[i].y_coordinate != y_old:
                    list_of_fish[i].distance += 1
            #reproduction of fish
            if list_of_fish[i].reproduction_time > 1:
                if list_of_fish[i].x_coordinate != x_old or list_of_fish[i].y_coordinate != y_old:
                    list_of_fish[i].distance += 1
                    temp_list_of_fish.append(Fish(height, width, x_old,y_old, 0, 0, 0, 0))
                    temp_list_positions_fish.append((x_old, y_old))
                    list_of_fish[i].reproduction_time = 0
                    temp_positions_babyfish.append((x_old,y_old))
                    list_of_fish[i].nb_descendants += 1

    #update list
    list_positions_shark = temp_list_positions_shark
    list_of_sharks = temp_list_of_shark
    list_of_fish = temp_list_of_fish   
    list_positions_fish = temp_list_positions_fish
    chronon += 1
    max_nb_descendants_fish = 0
    max_nb_descendants_shark = 0
    max_distance_fish = 0
    max_distance_shark = 0

    #calculate the sharks datas and statistics
    for shark in list_of_sharks:
        average_age_shark+=shark.age
        average_nb_descendants_shark += shark.nb_descendants
        average_distance_shark += shark.distance
        if shark.nb_descendants > max_nb_descendants_shark:
            max_nb_descendants_shark = shark.nb_descendants
        if shark.distance > max_distance_shark:
            max_distance_shark = shark.distance
    average_age_shark = int(average_age_shark/len(list_of_sharks))
    average_nb_descendants_shark = int(average_nb_descendants_shark/len(list_of_sharks))
    average_distance_shark = int(average_distance_shark/len(list_of_sharks))

    #calculate the fish datas and statistics
    for fish in list_of_fish:
        average_age_fish+=fish.age
        average_nb_descendants_fish += fish.nb_descendants
        average_distance_fish += fish.distance
        if fish.nb_descendants > max_nb_descendants_fish:
            max_nb_descendants_fish = fish.nb_descendants
        if fish.distance > max_distance_fish:
            max_distance_fish = fish.distance
    average_age_fish = int(average_age_fish/len(list_of_fish))
    average_nb_descendants_fish = int(average_nb_descendants_fish/len(list_of_fish))
    average_distance_fish = int(average_distance_fish/len(list_of_fish))

    data.update_csv(chronon, len(list_positions_fish), len(list_positions_shark), average_age_fish, average_age_shark,average_nb_descendants_fish, 
               average_nb_descendants_shark, average_distance_fish, average_distance_shark, 
               max_nb_descendants_fish, max_nb_descendants_shark, max_distance_fish, max_distance_shark)

    data.create_plot()

