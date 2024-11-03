# Projet Wator / Wator Project

> **Un projet cosigné par David, Maxime et Ludivine / A project co-signed by David, Maxime, and Ludivine**

Ce projet implémente une simulation de l'écosystème Wator en **programmation orientée objet**. Il s'agit d'une modélisation de vie marine peuplée de poissons et de requins, où chaque entité agit de manière autonome, se déplaçant en fonction d'une liste d'objets environnants. La simulation est développée en Python avec deux modes d'affichage :
1. Une version console pour une visualisation simple et rapide.
2. Une version graphique avec Pygame pour une expérience interactive.

This project implements a simulation of the Wator ecosystem using **object-oriented programming**. It models a marine ecosystem populated by fish and sharks, where each entity acts autonomously, moving based on a list of surrounding objects. The simulation is developed in Python and offers two display modes:
1. A console version for a quick, simple visualization.
2. A graphical version using Pygame for an interactive experience.

---

## Table des matières / Table of Contents
- [Description du projet / Project Description](#description-du-projet--project-description)
- [Fonctionnalités / Features](#fonctionnalités--features)
- [Installation](#installation)
- [Utilisation / Usage](#utilisation--usage)
- [Contributeurs / Contributors](#contributeurs--contributors)
- [Licence / License](#licence--license)
- [Notes supplémentaires / Additional Notes](#notes-supplémentaires--additional-notes)

---

## Description du projet / Project Description

### Français
Wator est une simulation de vie marine où deux types d'espèces interagissent dans un environnement fermé :
- Les **poissons** se déplacent librement et se reproduisent après un certain nombre de cycles.
- Les **requins** chassent les poissons pour survivre, se déplacent, et se reproduisent également après plusieurs cycles. En l'absence de nourriture, les requins meurent.

Chaque espèce utilise la programmation orientée objet pour suivre des règles simples :
- **Déplacement** : Les poissons et requins se déplacent en fonction des objets environnants.
- **Reproduction** : Les espèces peuvent se reproduire après un certain nombre de cycles.
- **Prédation** : Les requins chassent les poissons proches. Sans nourriture, ils meurent après plusieurs cycles.

### English
Wator is a marine life simulation where two types of species interact in a closed environment:
- **Fish** move freely and reproduce after a certain number of cycles.
- **Sharks** hunt fish to survive, move around, and also reproduce after several cycles. Without food, sharks eventually die.

Each species uses object-oriented programming to follow simple rules:
- **Movement**: Fish and sharks move based on nearby objects.
- **Reproduction**: Both species reproduce after a specified number of cycles.
- **Predation**: Sharks hunt nearby fish. Without food, they die after several cycles.

---

## Fonctionnalités / Features

### Version Console
- **Français** : Affichage simplifié de la grille avec des symboles pour chaque espèce.
- **English** : Simplified grid display with symbols for each species.
  
### Version Pygame
- **Français** : Interface graphique avec une grille animée illustrant les déplacements.
- **English** : Graphical interface with an animated grid showing movements.

---

## Installation

### Prérequis / Prerequisites
- **Python** (version >= 3.9)
- **Pygame** : Installez Pygame avec / Install Pygame with:
  ```bash
  pip install pygame

### Clonage du projet / Project Cloning
  ```bash```
git clone https://github.com/votre-utilisateur/projet-wator.git
cd projet-wator

### Lancer la simulation / Running the simulation
- **Version Console**
python wator_console.py #A changer
- **Version Pygame**
python wator_pygame.py

## Utilisation / Usage

## Contributeurs / Contributors
Ce projet a été conçu et réalisé par / This project was created by:

    David
    Maxime
    Ludivine

## Licence / License


## Notes supplémentaires / Additional Notes

Ce projet est un exemple de modélisation multi-agents et de simulation stochastique.

This project serves as an example of multi-agent modeling and stochastic simulation.