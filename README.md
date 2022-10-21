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
- [TroubleShooting](#troubleshooting)
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

## Usage

```bash
git clone 'git@github.com:calopessoa/log-quake.git'
```

```bash
cd log-quake
```
Install Venv environment for Python:
```bash
source .venv/bin/activate
```

Run the following to show all game matches from the main function:
```bash
python3 -m main.py
```

## Testing

Firstly, install Pytest dependency:
```bash
python3 -m pip install pytest
```

The, run the following command to get all tests, with the verbose tag:
```bash
python3 -m pytest -v
```

## Author

- LinkedIn - [Carlos Augusto Lopes de Oliveira](https://www.linkedin.com/in/carlos-augusto-lopes-de-oliveira-2602458b/)
