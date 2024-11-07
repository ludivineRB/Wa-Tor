# Wa-tor Project / Projet Wa-tor

> **A project co-signed by David, Maxime, and Ludivine /Un projet cosigné par David, Maxime et Ludivine**
 
This project implements a simulation of the Wator ecosystem using **object-oriented programming**. It models a marine ecosystem populated by fish and sharks, where each entity acts autonomously, moving based on a list of surrounding objects. The simulation is developed in Python and offers two display modes:
1. A console version for a quick, simple visualization.
2. A graphical version using Pygame for an interactive experience.

Ce projet implémente une simulation de l'écosystème Wator en **programmation orientée objet**. Il s'agit d'une modélisation de vie marine peuplée de poissons et de requins, où chaque entité agit de manière autonome, se déplaçant en fonction d'une liste d'objets environnants. La simulation est développée en Python avec deux modes d'affichage :
1. Une version console pour une visualisation simple et rapide.
2. Une version graphique avec Pygame pour une expérience interactive.


---

## Table des matières / Table of Contents
- [Description du projet / Project Description](#description-du-projet--project-description)
- [Fonctionnalités / Features](#fonctionnalités--features)
- [Installation](#installation)
- [Utilisation / Usage](#utilisation--usage)
- [Contributeurs / Contributors](#contributeurs--contributors)
- [Notes supplémentaires / Additional Notes](#notes-supplémentaires--additional-notes)

---

## Project Description / Description du projet 

### English
Wator is a marine life simulation where two types of species interact in a closed environment:
- **Fish** move freely and reproduce after a certain number of cycles.
- **Sharks** hunt fish to survive, move around, and also reproduce after several cycles. Without food, sharks eventually die.

Each species uses object-oriented programming to follow simple rules:
- **Movement**: Fish and sharks move based on nearby objects.
- **Reproduction**: Both species reproduce after a specified number of cycles.
- **Predation**: Sharks hunt nearby fish. Without food, they die after several cycles.

### Français
Wator est une simulation de vie marine où deux types d'espèces interagissent dans un environnement fermé :
- Les **poissons** se déplacent librement et se reproduisent après un certain nombre de cycles.
- Les **requins** chassent les poissons pour survivre, se déplacent, et se reproduisent également après plusieurs cycles. En l'absence de nourriture, les requins meurent.

Chaque espèce utilise la programmation orientée objet pour suivre des règles simples :
- **Déplacement** : Les poissons et requins se déplacent en fonction des objets environnants.
- **Reproduction** : Les espèces peuvent se reproduire après un certain nombre de cycles.
- **Prédation** : Les requins chassent les poissons proches. Sans nourriture, ils meurent après plusieurs cycles.

---

## Features / Fonctionnalités 

### Version Console
- **English** : Simplified grid display with symbols for each species ('\U0001F420' pour fish et 'S' pour shark).
  
- **Français** : Affichage simplifié de la grille avec des symboles pour chaque espèce('f' pour fish et 'S' pour shark).

### Version Pygame
- **English** : Graphical interface showing interactions between different objects on the grid.

- **Français** : Interface graphique représentant les intéractions des objets entre eux au sein de la grille.

---

## Installation

### Prerequisites / Prérequis 
- **Python** (version >= 3.9)
- **Pygame** : Installez Pygame avec / Install Pygame with:
  ```bash
  pip install pygame

### Project Cloning / Clonage du projet 
  ```bash```
git clone https://github.com/ludivineRB/Wa-Tor.git
cd projet-wator

### Running the simulation / Lancer la simulation 
- **Version Console**
python main.py 
- **Version Pygame**
python app.py 

## Usage / Utilisation 

Wa-Tor closed environment simulation including two species sharks and fish, and a predation relationship between the two. For a stable simulation, the optimal criteria are:
-grid size: 40*40
-shark population: ~25
-fish population: ~200
-shark reproduction time: 6 chronons
-fish reproduction time: 1 chronon
-starvation time: 2 chronons


Simulation d'environnement clos Wa-Tor comprenant deux espèces requins et poissons, et une relation de prédation entre les deux. Pour une simulation stable, les critères optimaux sont:
-taille de la grille : 40*40
-population de requins: ~25
-population de poissons: ~200
-temps de reproduction requins: 6 chronons
-temps de reproduction poissons : 1 chronon
-temps de famine : 2 chronons

## Contributors / Contributeurs 
This project was created by: / Ce projet a été conçu et réalisé par 

    David (Daviddavid-sudo)
    Maxime (TheMaxfly)
    Ludivine (ludivineRB)

## Additional Notes /Notes supplémentaires 

This project serves as an example of multi-agent modeling and stochastic simulation.
Ce projet est un exemple de modélisation multi-agents et de simulation stochastique.

