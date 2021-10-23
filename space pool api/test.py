import requests
import time

alertPlotSizeTib = 150
lineToken = 'your line token'
userAgent = "your userAgent"
spacePoolId = "your Spacepool ID"

def lineNotifyMessage(token, msg):
    lineHeaders = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    linePayload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = lineHeaders, params = linePayload)
    return r.status_code

def lineShowStatistics(eachProfile):
    statistic ="\n"
    for i in eachProfile:
        statistic += i+"\n"
    lineNotifyMessage(lineToken, statistic)
    time.sleep(2)

def lineShowWarning(estimatedPlotSizeTiB,alertPlotSizeTib,lineToken):
    if estimatedPlotSizeTiB <= alertPlotSizeTib:
        warningMessage = "\nWarning! Your Plotsize is about "+str(estimatedPlotSizeTiB)+"TiB,and is under "+str(alertPlotSizeTib)+"TiB !"
        lineNotifyMessage(lineToken, warningMessage)
    time.sleep(2)

def getInfo():
    # response = requests.request("GET", url, headers=spacePoolHeaders)
    # farmsprofile = response.text
    farmsprofile = "{\"launcherId\":\"aa44f53b655e33a2d565786bfc5537f992d90ca48e28a01695994e38c004b15c\",\"unpaidBalanceInXCH\":0.010195044194,\"totalPaidInXCH\":1.933626358547,\"blocksFound\":1,\"estimatedPlotSizeTiB\":130.17791755759362,\"estimatedPlots\":1454,\"tenureDateTimeUtc\":\"2021-07-07T08:20:29.0000000Z\",\"pendingPoints\":1785,\"accountDisplayName\":\"uufarm\",\"rank\":6314,\"difficulty\":21}"
    k = farmsprofile.find("estimatedPlotSizeTiB")
    estimatedPlotSizeTiB = float(farmsprofile[k+22:k+27])
    eachProfile = farmsprofile[1:-2].split(",")
    return estimatedPlotSizeTiB,eachProfile

url = "https://developer.pool.space/api/v1/farms/"+spacePoolId
spacePoolHeaders = {
    "Accept": "text/plain",
    "Developer-Key": "O0jlUJr1Es2lEsqdQmSZTTnfc5Q2pxCUc8pKWXQ3Czz18EmTANYvnVoAjIyX3EYT",
    "User-Agent": userAgent
}
localtime = time.localtime()
localtime2 = time.localtime()
while(1):
    now = time.localtime()
    if now.tm_hour-localtime.tm_hour ==1 or now.tm_hour-localtime.tm_hour ==-23:
        estimatedPlotSizeTiB,eachProfile = getInfo()
        lineShowWarning(estimatedPlotSizeTiB,alertPlotSizeTib,lineToken)
        localtime = now
    if abs(now.tm_hour-localtime2.tm_hour) ==12:
        estimatedPlotSizeTiB,eachProfile = getInfo()
        lineShowStatistics(eachProfile)
        localtime2 = now
    







