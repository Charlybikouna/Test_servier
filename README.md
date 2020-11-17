# Pipeline de traitement de données

Il s'agit d'un pipeline de traitement de données à travers des jobs d'extraction , de traitement et de stockage 



### Prerequis

Ubuntu 18.04
docker


### Installation

```bash

    cd Test_servier
    sudo su 
    docker pull python:3.7.1
    docker build -t pipeline:v1 .

```

### Exécution 

```bash
    docker run -ti -v output:/code/output pipeline:v1
```
Chemin du dossier contenant le fichier (data.json) de sortie du pipeline est :

/var/lib/docker/volumes/output/_data

Le résultat de la fonction qui mentionne le plus de médicaments différents apparait en console à l'exécution de la commande bash ci-dessus

### Version

1.0.0

## Auteur

* **Atangana Bikouna Charles**


