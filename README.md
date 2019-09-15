# RushStatsAPI-Python
The simplest ever, clear-code, easy-to-use wrapper for RushStatsAPI (Rush Wars API) written in Python 3!
### Requirements
- OS: Windows / Linux / Android / MacOS
- Python version: 3.x
- Python modules: json, requests
### Note
Because the project is just a script for now, it means you will have to manually download it and put the ```rushstats.py``` file into directory of your project you are going to use this wrapper in. Then you can simply import it as you are doing it with any other modules: ```import rushstats```.
### Authorization
To connect to the API you will need an access token. If you will try to retrieve any info without authorization, you will receive an error. So, if you still don't have any token, you can get a new one here: https://api.rushstats.com/dashboard <br>
Then authenticate using this function (don't forget to replace ```token``` with your token): ```rushstats.session('token')```
### Retrieving information
All of the functions below are returning requested data as a ```Json``` object.
- Information about player: ```rushstats.get_player('tag')```
- Information about team: ```rushstats.get_team('tag')```
- Searching teams by keyword: ```rushstats.team_search('keyword')``` <br>
(This will return only first 64 results beacause of in-game limit.)
- Getting player leaderboard: ```rushstats.top_players(count)``` <br>
(A ```count``` argument here specifies how many players from the leaderboard will be returned. It should be an integer and should be equal to any number in range 0-200.)
