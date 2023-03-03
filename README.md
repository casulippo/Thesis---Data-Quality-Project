# Thesis - Data-Quality

### Step 1 - Build dell'immagine
E' possibile creare ambiente su cui utilizzare il progetto di Data Quality:
sarà necessario buildare l'immagine dal prompt dei comandi con il codice: ``` docker build -t thesis . ``` 

### Step 2 - Attivazione del contaneir
Una volta completato il primo step sarò possibile avere immagine del nome ```Thesis```, per utilizzarla digitare una dei due seguenti comandi:
1. ```docker run --rm -d -p 9000:8888 -p 4041:4040 -e DOCKER_STACKS_JUPYTER_CMD=nbclassic --user root -e GRANT_SUDO=yes  -v ${PWD}:/home/jovyan/ --name container_thesis thesis ```

2. ```docker run --rm -d -p 9000:8888 -p 4040:4040 -e DOCKER_STACKS_JUPYTER_CMD=nbclassic --user root -e GRANT_SUDO=yes  -v %cd%:/home/jovyan/ --name container_thesis thesis```

### Step 3 - Apertura del local-host
Se tutti gli step sono stati completati nel modo giusto sarà possibile accedere al link http://localhost:9000/ accedendo così al progetto.
La password settata è 'DQ2022'


Data Ingestion Workflow

![image](https://user-images.githubusercontent.com/58252186/222507141-706b9436-6407-4ebb-8e78-b1fc70e53a51.png)
