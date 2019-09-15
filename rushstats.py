import json
import requests

def session(token):
    global headers
    headers = {'Authorization': token}

def get_player(tag):
    return requests.get('https://api.rushstats.com/v1/player/' + tag, headers=headers).json()

def get_team(tag):
    return requests.get('https://api.rushstats.com/v1/team/' + tag, headers=headers).json()

def team_search(keyword):
    return requests.get('https://api.rushstats.com/v1/search/team/' + keyword, headers=headers).json()

def top_players(count):
    return requests.get('https://api.rushstats.com/v1/leaderboard/players?count=' + str(count), headers=headers).json()
