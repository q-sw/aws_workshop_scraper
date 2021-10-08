# AWS_WORKSHOP_SCRAPER
Aws propose un site avec des workshops, [https://workshops.aws](https://workshops.aws), sur ces différents services pour monter en compétence.  
Le site n'offre pas dans l'état de moyen simple de filtrer par niveau les workshops ou par centre d'intérêt.  

Ce projet est une simple CLI développé en Python pour réaliser ces filtres.  

## Installation des prerequis
Si vous ne voulez pas installer les prerequis directement un version Docker est disponible [Docker](#Docker)
```
python3 -m pip install -r requirement.txt
```
## Utilisation de la CLI:  
```
python script.py --help
````
```
Usage: script.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  by-level  filtre l'ensemble des workshops par niveau
  filtred   filtre les workshops par centre d'interet cf:tag.json

```

### by-level utilisation
cette Option permet de retourner les workshops par niveau.  
les niveau des workshops vont de 100 à 400

```
python script.py by-level --help
Usage: script.py by-level [OPTIONS]

  filtre l'ensemble des workshops par niveau

Options:
  --level TEXT  indiquer un niveau entre 100 et 400  [required]
  --help        Show this message and exit.
```
exemple d'utilisation:  
```
python script.py by-level --level 100
```

### filtred utilisation
```
python script.py filtred --help
Usage: script.py filtred [OPTIONS]

  filtre les workshops par centre d'interet cf:tag.json

Options:
  --all-wks           Recupére tous les workshop par centre d'interet
  --by-level INTEGER  Recupere les workshop par niveau et par centre d'interet
                      value: entre 100 et 400
  --help              Show this message and exit.
```
exemple d'utilisation:
```
python script.py filtred --all-wks
```
outputs:
```
...
{'level': '400',
  'tag': 'ec2, spot, eks, emr, sagemaker, jenkins, nextflow, spark',
  'time': '1.5 hours',
  'titre': ' EC2 Spot Workshops ',
  'url': 'https://ec2spotworkshops.com/'},
 {'level': '300',
  'tag': 'ec2, auto scaling',
  'time': '4 hours',
  'titre': ' Migrate Webapps ',
  'url': 'https://migrate-webapps.workshop.aws'}]

133
```
```
python script.py filtred --by-level 100
```
outputs:
```
...
{'level': '100',
  'tag': 'amazon s3, amazon cloudfront, amazon lex, amazon rekognition, amazon '
         'cognito, amazon cloudfront',
  'time': '6 hours',
  'titre': ' Work Placement Workshop ',
  'url': 'https://work-placement.workshop.aws'},
 {'level': '100',
  'tag': 'eks, kubernetes, eksctl, helm, x-ray, appmesh, elasticsearch, kibana',
  'time': '8 hours',
  'titre': ' Amazon EKS Workshop ',
  'url': 'https://www.eksworkshop.com/'}]
5
```

Pour changer les filtres, il suffit de modifier le fichier tag.json.
> l'ensemble des tags présents sur le site sont référencés dans le fichier all_tag.json

## Docker
Un version Docker est disponible

### Build de l'image
```
docker build -f Dockerfile -t aws_workshop:1.0 .
````

### Utilisation avec l'images
```
docker run aws_workshop:1.0 --help
```
```
docker run aws_workshop:1.0 by-level --help
```
````
```
docker run aws_workshop:1.0 filtred --help
```
