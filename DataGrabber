import requests
from pip._vendor.distlib.compat import raw_input

def requestSummonerData(region, summonerName, APIKey):
    URL = "https://"+region+"1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName+"?api_key="+APIKey
    response = requests.get(URL)
    return response.json()
def requestSummonerRanked(region,ID,APIKey):
    URL = "https://"+region+"1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+ID+"?api_key="+APIKey
    response = requests.get(URL)
    return response.json()
def main():
    region = (str)(raw_input("Enter Region: "))
    summonerName = (str)(raw_input("Enter Summoner Name: "))
    APIKey = (str)(raw_input("Enter API Key: "))
    responseJSON = requestSummonerData(region,summonerName,APIKey)
    ID = str(responseJSON['id'])
    print("ID IS"+ID)
    responseJSON2 = requestSummonerRanked(region,ID,APIKey)
    print(responseJSON2)
    print(responseJSON2[1]['tier'])
    print(responseJSON2[1]['rank'])
    print(responseJSON2[1]['leaguePoints'])
if __name__ == "__main__":
    main()