# CADE_ANALYSE_ALGO

## Description

Projet d'analyse comparative des performances d'algorithmes d'optimisation sur les fonctions de benchmark BBOB. Ce projet fournit une analyse rigoureuse et reproductible des algorithmes PSO (Particle Swarm Optimization), GA (Genetic Algorithm) et Random Search sur des fonctions BBOB sélectionnées en dimension 20.

## Contexte et Objectif

Ce projet a été développé dans le cadre d'un séminaire de recherche pour évaluer et comparer les performances de différents algorithmes d'optimisation sur des problèmes de benchmark standardisés (BBOB - Black-Box Optimization Benchmarking). L'objectif principal est de produire des analyses statistiques et visuelles permettant de comprendre la convergence, l'efficacité et les caractéristiques de chaque algorithme sur diverses fonctions de test.

## Fonctionnalités Principales

- **Parsing automatique** des fichiers de données bruts (.dat) issus de COCO
- **Agrégation des runs expérimentaux** pour une analyse statistique robuste
- **Visualisation de la convergence** avec courbes de performance
- **Comparaisons statistiques** entre algorithmes (tests de Wilcoxon, écarts-types, etc.)
- **Génération de figures** pour rapports scientifiques et présentations
- **Validation des chemins** et gestion des erreurs de fichiers

## Stack Technique

- **Langage** : Python 3
- **Environnements** : Jupyter Notebook pour l'analyse interactive
- **Bibliothèques principales** :
  - `numpy` : calculs numériques
  - `pandas` : manipulation et analyse de données
  - `matplotlib` : visualisation des données
  - `scipy` : statistiques et interpolation
- **Données** : Fichiers BBOB au format .dat (COCO framework)

## Structure du Projet

```
code_analyse_algo/
├── Analyse-data.ipynb          # Notebook principal d'analyse
├── Analyse-data-backup.ipynb   # Version de sauvegarde
├── repair_notebook.py          # Script de réparation du notebook
├── data_archive_pso/           # Données expérimentales PSO
├── data_archive-GA/            # Données expérimentales GA
├── data_archive_RANDOMSEARCH-5/ # Données expérimentales Random Search
└── .venv/                      # Environnement virtuel Python
```

## Installation

### Prérequis

- Python 3.7+
- Jupyter Notebook
- Git (pour le versioning)

### Étapes d'installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre-username/CADE_ANALYSE_ALGO.git
   cd CADE_ANALYSE_ALGO
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install numpy pandas matplotlib scipy jupyter
   ```

## Configuration

Le projet utilise des chemins relatifs configurés dans le notebook principal. Assurez-vous que la structure des dossiers `data_archive_*` reste inchangée.

### Paramètres configurables

- **Algorithmes** : PSO, GA, RANDOMSEARCH-5
- **Fonctions BBOB** : f1, f8, f15, f20, f24
- **Dimension** : 20 (fixe pour ce projet)
- **Budgets d'évaluation** : petit (2000), moyen (20000), grand (200000)

## Utilisation

1. **Activer l'environnement virtuel** :
   ```bash
   source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
   ```

2. **Lancer Jupyter** :
   ```bash
   jupyter notebook
   ```

3. **Ouvrir et exécuter** `Analyse-data.ipynb` :
   - Le notebook guide pas à pas l'analyse complète
   - Commencer par vérifier les chemins des fichiers
   - Exécuter les sections dans l'ordre pour reproduire l'analyse

### Commande de lancement rapide

```bash
jupyter notebook Analyse-data.ipynb
```

## Exemples d'Usage

Le notebook fournit des exemples d'analyse pour :
- Visualisation des courbes de convergence par fonction
- Comparaison des performances moyennes entre algorithmes
- Analyse statistique des écarts-types et distributions
- Génération de tableaux récapitulatifs pour rapports

## Choix Techniques et Architecture

- **Modularité** : Fonctions dédiées pour le parsing, l'agrégation et la visualisation
- **Reproductibilité** : Utilisation de seeds et chemins configurables
- **Robustesse** : Gestion des erreurs et validation des fichiers d'entrée
- **Performance** : Optimisation des calculs avec numpy et interpolation scipy

## Améliorations Futures

- Extension à d'autres algorithmes d'optimisation
- Support de dimensions variables
- Interface web pour l'exploration interactive des résultats
- Intégration de tests statistiques supplémentaires
- Automatisation du pipeline d'analyse

## Auteur

[Votre nom] - Projet développé dans le cadre d'un séminaire de recherche en optimisation.

## Licence

Ce projet est fourni tel quel pour usage académique et de recherche. Veuillez citer la source si utilisé dans des publications.