import requests
from pip._vendor.distlib.compat import raw_input
APIKey = ""
def requestSummonerData(region, summonerName):
    URL = "https://"+region+"1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName+"?api_key="+APIKey
    response = requests.get(URL)
    return response.json()
def requestSummonerRanked(region,ID):
    URL = "https://"+region+"1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+ID+"?api_key="+APIKey
    response = requests.get(URL)
    return response.json()
def divisionAverages(region,division,tier):
    URL = "https://"+region+"1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/"+division+"/"+tier+"?page=1"+"?api_key="+APIKey
    response = requests.get(URL)
    summJSON = response.json
    print("size of page 1 is : " + len(summJSON))
    #for i in range(len(summJSON
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
    divisionAverages(region,division,tier):
if __name__ == "__main__":
    main()
