import requests
import time

filePath = './config.txt'
file = open(filePath, 'r')
config=[]
allLines = file.readlines()
for i in allLines:
    config.append(i.strip().split("=")[1])
alertPlotSizeTib,lineToken,userAgent,spacePoolId = config[0:4]

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

def lineShowWarning(estimatedPlotSizeTiB,alertPlotSizeTib,lineToken):
    if estimatedPlotSizeTiB <= float(alertPlotSizeTib):
        warningMessage = "\nWarning! Your Plotsize is about "+str(estimatedPlotSizeTiB)+"TiB,and is under "+str(alertPlotSizeTib)+"TiB !"
        lineNotifyMessage(lineToken, warningMessage)

def getInfo():
    response = requests.request("GET", url, headers=spacePoolHeaders)
    farmsprofile = response.text
    k = farmsprofile.find("estimatedPlotSizeTiB")
    estimatedPlotSizeTiB = float(farmsprofile[k+22:k+27])
    eachProfile = farmsprofile[1:-1].split(",")
    return estimatedPlotSizeTiB,eachProfile

def initialize():
    estimatedPlotSizeTiB,eachProfile=getInfo()
    lineShowStatistics(eachProfile)
    lineShowWarning(estimatedPlotSizeTiB,alertPlotSizeTib,lineToken)

url = "https://developer.pool.space/api/v1/farms/"+spacePoolId
spacePoolHeaders = {
    "Accept": "text/plain",
    "Developer-Key": "O0jlUJr1Es2lEsqdQmSZTTnfc5Q2pxCUc8pKWXQ3Czz18EmTANYvnVoAjIyX3EYT",
    "User-Agent": userAgent
}
print("start notice!")
cnt=0
initialize()
while(1):
    estimatedPlotSizeTiB,eachProfile = getInfo()
    lineShowWarning(estimatedPlotSizeTiB,alertPlotSizeTib,lineToken)
    cnt+=1
    if cnt==12:
        lineShowStatistics(eachProfile)
        cnt=0
    time.sleep(3600) #check every hour
print("end notice!")







