import requests
import time

def lineNotifyMessage(msg):
    '''
    Line的通知傳送，將找token寫在裡面，所以會用較少空間
    '''
    #讀取config.txt 動態調整參數
    filePath = './config.txt'
    file = open(filePath, 'r')
    config=[]
    allLines = file.readlines()
    for i in allLines:
        config.append(i.strip().split("=")[1])
    token = config[1]
    lineHeaders = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    linePayload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = lineHeaders, params = linePayload)
    return r.status_code

def lineShowStatistics(eachProfile):
    '''
    將SpacePool的個人統計數據回傳給Line做通知
    '''
    statistic ="\n"
    for i in eachProfile:
        statistic += i+"\n"
    lineNotifyMessage(statistic)

def lineShowWarning(estimatedPlotSizeTiB,alertPlotSizeTib):
    '''
    警示提醒功能
    '''
    if estimatedPlotSizeTiB <= float(alertPlotSizeTib):
        warningMessage = "\nWarning! Your Plotsize is about "+str(estimatedPlotSizeTiB)+"TiB,and is under "+str(alertPlotSizeTib)+"TiB !"
        lineNotifyMessage(warningMessage)

def getInfo():
    filePath = './config.txt'
    file = open(filePath, 'r')
    config=[]
    allLines = file.readlines()
    for i in allLines:
        config.append(i.strip().split("=")[1])
    alertPlotSizeTib,lineToken,userAgent,spacePoolId = config[0:4]

    url = "https://developer.pool.space/api/v1/farms/"+spacePoolId
    spacePoolHeaders = {
        "Accept": "text/plain",
        "Developer-Key": "O0jlUJr1Es2lEsqdQmSZTTnfc5Q2pxCUc8pKWXQ3Czz18EmTANYvnVoAjIyX3EYT",
        "User-Agent": userAgent
    }
    response = requests.request("GET", url, headers=spacePoolHeaders)
    farmsprofile = response.text
    k = farmsprofile.find("estimatedPlotSizeTiB")
    estimatedPlotSizeTiB = float(farmsprofile[k+22:k+27])
    eachProfile = farmsprofile[1:-1].split(",")
    currentBlockFound = int(eachProfile[3][14:])
    return estimatedPlotSizeTiB,eachProfile,currentBlockFound,alertPlotSizeTib

def initialize():
    estimatedPlotSizeTiB,eachProfile,currentBlockFound,alertPlotSizeTib=getInfo()
    lineShowStatistics(eachProfile)
    lineShowWarning(estimatedPlotSizeTiB,alertPlotSizeTib)

def isFoundBlock(currentBlockFound,block):
    if currentBlockFound > block:
        Message = "\nCongratulations! You win a block!\nYou now have found "+str(currentBlockFound)+" blocks! "
        lineNotifyMessage(Message)
        block = currentBlockFound
    return block

# print("start notice! press \"ctrl+c\" to exit...")
# cnt=0
# block=1
# initialize()
# while(1):
#     estimatedPlotSizeTiB,eachProfile,currentBlockFound = getInfo()
#     block = isFoundBlock(currentBlockFound,block)
#     lineShowWarning(estimatedPlotSizeTiB,alertPlotSizeTib,lineToken)
#     cnt+=1
#     if cnt==12:
#         lineShowStatistics(eachProfile)
#         cnt=0
#     time.sleep(3600) #check every hour
# print("end notice!")
