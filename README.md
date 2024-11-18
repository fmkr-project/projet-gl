Semaine 1  
Création de Personas et Scénarios d'Utilisation  
Objectif : Créer deux personas et des scénarios qui représentent les principaux utilisateurs de l'application.  
Activité : L'équipe doit développer des personas basées sur le public cible et créer des scénarios détaillés décrivant les interactions de ces utilisateurs avec le système.  
Livrables : Personas, scénarios et une liste initiale des fonctionnalités  

**Persona 1** : Lucie, Chef de Projet  
<ins>Profil :</ins>   
  Âge : 35 ans  
  Profession : Chef de Projet Technique  
<ins>Contexte :</ins>   
  Lucie travaille dans une entreprise de développement logiciel et gère plusieurs équipes sur différents projets.   
  Elle est expérimentée en gestion de projet agile et utilise des outils de suivi pour contrôler l'avancement des projets, assigner des tâches, et s'assurer que les échéances sont respectées.  
<ins>Objectifs :</ins> 
  Suivre l’avancement des tâches et des projets.  
  Assigner les tâches aux membres de l’équipe et ajuster les priorités en fonction des urgences.  
  Obtenir des rapports de productivité et analyser les problèmes...    
<ins>Motivations :</ins>  
  Améliorer la productivité de l’équipe en ayant une vision claire de chaque projet.  
  Réduire les retards en identifiant les problèmes potentiels tôt.  
<ins>Connaissances Techniques :</ins>  
  Très à l’aise avec les outils de gestion de projet (Jira).  
  Connaissances en méthodologies agiles (Scrum et Kanban).  
<ins>Scénario d'Utilisation :</ins>  
  Début du projet : Lucie crée un nouveau projet dans le logiciel et définit les tâches principales.   
                    Elle attribue chaque tâche aux membres de l'équipe en fonction de leurs spécialités.  
  Suivi des progrès : Elle utilise le tableau Kanban intégré pour voir les tâches en cours, en attente, ou terminées.   
                      Elle fait des ajustements pour équilibrer la charge de travail.  
  Rapports : À la fin de chaque sprint, elle génère un rapport sur la productivité de l’équipe pour évaluer le respect des délais et des objectifs.   
             Elle partage ensuite ces rapports avec les parties prenantes.  

**Persona 2** : Antoine, Développeur Frontend  
<ins>Profil :</ins>   
  Âge : 28 ans  
  Profession : Développeur Frontend  
<ins>Contexte :</ins>   
  Antoine est développeur dans l’équipe de Lucie et se concentre principalement sur le développement d’interfaces utilisateur.  
  Il collabore étroitement avec les concepteurs et les développeurs backend.  
<ins>Objectifs :</ins>  
  Visualiser ses tâches de façon claire et organisée.  
  Mettre à jour l’état de ses tâches rapidement et facilement.  
  Communiquer efficacement sur ses blocages avec les autres membres de l’équipe.  
<ins>Motivations :</ins>  
  Livrer un travail de qualité en respectant les délais.  
  Minimiser les interruptions et gérer les priorités de manière fluide.  
<ins>Connaissances Techniques :</ins>  
  Familiarisé avec les outils de suivi de tâches et de gestion de versions.  
  Maîtrise les technologies de frontend (JavaScript, CSS, React).  
<ins>Scénario d'Utilisation :</ins>  
  Revue des tâches quotidiennes : Chaque matin, Antoine consulte le tableau des tâches pour voir les priorités de la journée et les nouvelles affectations.  
  Mise à jour d’état : Il passe sa tâche de « en cours » à « terminée » dès qu’il termine un développement et laisse des commentaires pour les réviseurs.  
  Collaboration : En cas de blocage, il mentionne Lucie pour obtenir de l’aide et notifie l'équipe des autres tâches potentiellement affectées.  


**Liste Initiale des Fonctionnalités**  
Création et gestion de projets : gestion de multiples projets avec des tâches spécifiques.  
Attribution des tâches : assignation de tâches aux utilisateurs, avec des dates d’échéance et des priorités.  
Tableaux Kanban et vues de calendrier : visualisation des tâches sous plusieurs formats pour le suivi et l’organisation.  
Rapports de productivité : génération de rapports de performance, avec graphiques et statistiques.  
Notifications et communication : système de commentaires et notifications pour une meilleure collaboration.  
Mise à jour d’état des tâches : passage d’une tâche par différents statuts (ex. : à faire, en cours, terminé).  
Historique des modifications : suivi des changements pour chaque tâche et chaque utilisateur.  


----------
Semaine 2   
Histoires d'Utilisateur et Prototypage Initial  
Objectif : Créer des histoires d'utilisateur basées sur les scénarios et développer un prototype initial.  
Activité : Pour chaque scénario, créer au moins quatre histoires d'utilisateur et commencer le prototype de base de l'application.  
Livrables : Liste d'histoires d'utilisateur et un prototype fonctionnel initial.  

**Histoires d'Utilisateur**     
  
Persona 1 : Lucie, Chef de Projet  
<ins>Créer et gérer un projet</ins>    
En tant que chef de projet, je veux créer un projet et y ajouter des tâches, afin de planifier les travaux de mon équipe de manière structurée.  
<ins>Attribuer des tâches aux membres de l’équipe</ins>     
En tant que chef de projet, je veux assigner chaque tâche à un membre spécifique de mon équipe, afin que chacun sache clairement ce qu’il doit accomplir.  
<ins>Suivre l'avancement des tâches</ins>     
En tant que chef de projet, je veux visualiser l’avancement de chaque tâche sur un tableau Kanban, afin de voir les tâches en cours, terminées, et celles qui sont bloquées.  
<ins>Générer des rapports de productivité</ins>     
En tant que chef de projet, je veux générer un rapport de productivité basé sur les tâches accomplies et leur statut, afin de présenter ces données aux parties prenantes.  

Persona 2 : Antoine, Développeur Frontend  
<ins>Consulter mes tâches assignées</ins>     
En tant que développeur, je veux pouvoir consulter les tâches qui me sont assignées, afin de savoir sur quoi je dois travailler en priorité.  
<ins>Mettre à jour l’état d’une tâche</ins>     
En tant que développeur, je veux pouvoir changer l’état de mes tâches (par exemple, de « En cours » à « Terminé »), afin de tenir mon équipe informée de ma progression.  
<ins>Recevoir des notifications en cas de changement</ins>     
En tant que développeur, je veux recevoir des notifications quand une tâche qui me concerne est modifiée ou lorsque j’en reçois une nouvelle, afin de rester informé en temps réel.  
<ins>Partager un commentaire sur une tâche</ins>     
En tant que développeur, je veux pouvoir commenter les tâches pour poser des questions ou signaler des blocages, afin de faciliter la collaboration avec mon équipe.  


**Prototype Initial de l’Application**    
Pour le prototype de base, nous pouvons envisager les éléments suivants :  
<ins>Tableau de bord principal :</ins>  
  Vue d’ensemble des projets pour les chefs de projet.  
  Accès rapide aux tâches assignées pour les développeurs.  
<ins>Page de projet :</ins>  
  Création de nouvelles tâches et assignation aux membres de l’équipe.  
  Visualisation des tâches par statut (ex. : tableau Kanban avec colonnes « À faire », « En cours », « En révision », « Terminé »).  
<ins>Page de tâche :</ins>  
  Détail de la tâche avec description, responsable, statut actuel, date d’échéance et commentaires. 
  Boutons pour changer le statut de la tâche (e.g., "Commencer", "Terminé", etc.).  
<ins>Section de rapports et statistiques :</ins>  
  Vue d’ensemble des tâches par état (nombre de tâches terminées, en cours, bloquées).  
  Graphiques simples montrant la productivité de l’équipe sur une période.  
<ins>Notifications et messagerie interne :</ins>  
  Notifications dans le tableau de bord pour informer des mises à jour de tâches.  
  Zone de commentaire sous chaque tâche pour permettre les échanges entre les membres.  

----------
Semaine 3  
Développement Incrémental et Création du Backlog  
Objectif : Définir les fonctionnalités essentielles et souhaitables, et commencer l'implémentation.  
Activité : Organiser le backlog sur GitHub avec les fonctionnalités divisées entre essentielles (obligatoires) et souhaitables (facultatives). 
Commencer l'implémentation des fonctionnalités essentielles comme la création de tâches et l'authentification.
Livrables : Première version fonctionnelle avec les fonctionnalités essentielles implémentées et backlog organisé  

----------

Semaine 4
Implémentation des Fonctionnalités Essentielles  
Objectif : Finaliser l'implémentation complète des fonctionnalités essentielles pour assurer le bon fonctionnement de l'application. 
Activité : Terminer les fonctionnalités critiques telles que la gestion des tâches, la connexion et la visualisation de l'avancement. Si le temps le permet, commencer à travailler sur les fonctionnalités souhaitables comme la personnalisation de l'interface.  
Livrables : Fonctionnalités essentielles terminées et, si possible, progrès sur les fonctionnalités souhaitables.   


----------
Semaine 5   
Tests Basique et Affinement  
Objectif : Introduire des tests simples pour garantir la stabilité du système et affiner les fonctionnalités déjà implémentées.  
Activité : Mettre en place des tests basiques pour les fonctionnalités principales (création de tâches, connexion). Affiner le code en fonction des retours initiaux.  
Livrables : Tests basiques implémentés et affinement de l'application.  

----------
Semaine 6 
Fonctionnalités Souhaitables et Collaboration (Optionnel)  
Objectif : Ajouter les fonctionnalités souhaitables et, pour les équipes qui le souhaitent, implémenter la fonctionnalité de collaboration.  
Activité : Ajouter des fonctionnalités souhaitables comme la personnalisation des tâches ou des filtres avancés. Les équipes qui souhaitent relever un défi supplémentaire peuvent implémenter la fonctionnalité de collaboration, permettant à plusieurs utilisateurs de gérer des tâches partagées.  
Livrables : Fonctionnalités souhaitables implémentées et, optionnellement, la fonctionnalité de collaboration.  


----------
Semaine 7 
Présentation Finale  
Objectif : Présenter la version finale du projet en expliquant le processus de développement, les personas, les scénarios et les histoires d'utilisateur.  
Activité : Préparer une présentation mettant en avant les personas, scénarios, backlog, développement incrémental et la distinction entre fonctionnalités essentielles et souhaitables.  
Livrables : Présentation finale du projet.  


----------
Critères d'évaluation
Personas et Scénarios : Qualité et pertinence des personas et scénarios créés.  
Histoires d'Utilisateur : Clarté des histoires et leur contribution à l'orientation du développement.  
Développement Incrémental : Efficacité dans le développement incrémental et la livraison des prototypes.  
Fonctionnalités Indispensables vs. Souhaitables : Mise en œuvre réussie des fonctionnalités essentielles, avec un bonus pour ceux qui implémentent des fonctionnalités souhaitables et la collaboration.  
Travail d'Équipe et Gestion du Code : Utilisation de systèmes de contrôle de version et collaboration efficace entre les membres de l'équipe.  


