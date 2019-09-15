import json
import requests

def session(token):
    global headers, url
    url = 'https://api.rushstats.com/v1/'
    headers = {'Authorization': token}

def get_player(tag):
    return getdata('player/', tag)

def get_team(tag):
    return getdata('team/', tag)

def team_search(keyword):
    return getdata('search/team/', keyword)

def top_players(count):
    return getdata('leaderboard/players?count=', count)

def getdata(end, arg):
    if 'headers' in globals():
        return requests.get(url + end + str(arg), headers=headers).json()
    else:
        print('Please authenticate using your token!')
