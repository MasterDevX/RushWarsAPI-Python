# RushStatsAPI-Python
A simple, clear-code, easy-to-use wrapper for RushStatsAPI (Rush Wars API) written in Python 3!
### Requirements
- OS: Windows / Linux / Android / MacOS
- Python version: 3.x
- Python modules: json, requests
### Note
Because the project is just a script for now, it means you will have to manually download it and put the ```rushstats.py``` file into directory of your project you are going to use this wrapper in. Then you can simpy import it as you are doing it with any other modules: ```import rushstats```.
### Authorization
```rushstats.session('token')```
### Getting player info
```rushstats.get_player('tag')```
### Getting team info
```rushstats.get_team('tag')```
### Searching teams by keyword
```rushstats.team_search('keyword')```
### Getting player leaderboard
```rushstats.top_players(count)```
