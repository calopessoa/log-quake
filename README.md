# Quake 3 Arena - Match Log Viewer

Check the viewer application here!
<a href="http://quake3-log-viewer.vercel.app/">Quake Log Application</a>
<b>

A Single-Page-App (SPA) to render the results of each match from a session of Quake 3 Arena.
Please proceed to the Documentation for a guide:
<a href="http://documentation-quake-log.vercel.app/">Quake Log Documentation</a>

## Table of contents

- [General view](#general-view)
  - [The Challenge](#the-challenge)
  - [Images](#images)
  - [Links](#links)
- [The development process](#the-development-process)
  - [Tools used](#tools-used)
  - [Lessons learned](#lessons-learned)
- [Usage](#usage)
- [Testing](#testing)
- [Jenkins Pipeline](#jenkins-pipeline)
- [Author](#author)

## General view

### The challenge

Quake 3 Arena - Match Log Viewer is a project that parse a Quake 3 Arena session log into two data files, 
where a user can:

**consult info about each match**, showing:

- participant players,
- total kills made (whereas by the scenario or by the players),
- individual score, considering penalties,
- the top-3 players of each match,
- the causes of death (in the second card).

Our pattern-search engine should return an output like this:
```bash
game_1: {
    total_kills: 45
    players: ["Dono da bola", "Isgalamido", "Zeh"]
    kills: {
      "Dono da bola": 5,
      "Isgalamido": 18,
      "Zeh": 20
    }
  }
```
And everytime a player is killed by the 'world', that player should receive a score penalty.
The pattern is like this:
```bash
  21:42 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
```

Finally, as a bonus, a second pattern-search engine should return something like this,
That is the Causes of Death card (the right-corner card in the application):
```bash
"game-1": {
  "kills_by_means": {
    "MOD_SHOTGUN": 10,
    "MOD_RAILGUN": 2,
    "MOD_GAUNTLET": 1,
    ...
  }
}
```


## Images

<div align="center">
  <img width="330px" height="252px" src="/front-end/src/assets/game1.png" />
  <img width="330px" height="252px" src="/front-end/src/assets/game8.png" />
  <img width="330px" height="252px" src="/front-end/src/assets/game6mixed.png" />
</div>

## The development process

### Tools used

#### Front-end

- JavaScript
- React (Context API)
- Free Formatter - to format JSON files
- SASS - CSS
- Cypress

#### Log Parsing

- Python
- Venv
- Pytest - Testing framework for Python

#### Deployment & Documentation

- Vercel
- Docusaurus

### Lessons learned

In this project I could improve my knowledge in both front-end and Python, by:

- Using and learning about new frameworks and its applicabilities, namely Pytest framework.
- Creating a fake database to make unitary tests for the pattern-search functions.
- Rendering a dynamic card based on the option selected in a page.
- Using the basics of cypress to test the main page (front-end).

## Usage

```bash
git clone 'git@github.com:calopessoa/log-quake.git'
```

```bash
cd log-quake
```
Install Venv environment for Python:
```bash
python3 -m venv .venv
```

Go into the virtual environment
```bash
source .venv/bin/activate
```

Run the following to show all game matches from the main function:
```bash
python3 main.py
```

## Testing
  
Testing the parsing functions: 

Firstly, install Pytest dependency:
```bash
python3 -m pip install pytest
```

Then, run the following command to get all tests, with the verbose tag:
```bash
python3 -m pytest -v
```

Testing the main page, within the front-end:

(Install the dependencies, after moving to the project's folder):
```bash
cd front-end
```  
  
```bash
npm install
```
Now, to run cypress:
  
```bash
npx cypress open
```
or, withouth the GUI:

```bash
npm run test:chrome
```


## Jenkins Pipeline

- Install Docker on your local machine.
- Run this command:
```bash
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11
```
- Write down the password that's created for you during the set up, like:
"9061757e890a4e81802c4b54399adaba"
- Now visit *localhost:8080* and you'll be prompted the above password
- If you run into problems connecting with Jenkins, try removing the container and redoing the above steps all over again; resetting the container should also work.
- Go to "New Task"
- Add to the configuration tab the setup included in Jenkinsfile
- While the docker container is running, run cmd: docker ps to see what containers are running - copy the container ID for Jenkins, like: *440b198de7be*
- Run this command to go to Docker container as root (user 0):
```bash
docker exec -it -u 0 YourContainerIdHere /bin/bash
```
- Run the following commands to get python and pip within Docker container:
```bash
apt-get update
```
```bash
apt-get install python3
```
```bash
apt-get install python3-pip
```

- Then, run this to install the pytest package:
```bash
pip install pytest
```

- Back to the Main Board in Jerkins, press "Build now" to run the pipelines

## Author

- LinkedIn - [Carlos Augusto Lopes de Oliveira](https://www.linkedin.com/in/carlos-augusto-lopes-de-oliveira-2602458b/)
