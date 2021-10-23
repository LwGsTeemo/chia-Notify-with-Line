# chia-Notify-with-Line 警示程式
It's an .exe file that can notify your chia profit and warning message every time automatically.<br><br>
>這是我自行設計的小程式，有轉成.exe檔了，可以在沒有安裝python的電腦下執行<br>
>其功能為透過LineNotify與SpacePool作連動<br>
>若是收割機離線，能夠在LINE上面收到通知!，就可以及早排除問題<br>
>還可以定時收到SpacePool即時的統計數據:D<br>

# Installing 安裝
https://github.com/LwGsTeemo/chia-Notify-with-Line/releases/tag/v1.0.0

# How to Use 使用說明

解壓縮後 在./main/裡面有一個叫做 config.txt 的檔案<br>
須將個人的四項參數設定好<br><br>
alertPlotSizeTib為設定在多少TiB以下會發出警訊<br><br>
lineToken為LineNotify的個人權杖，獲取權杖步驟如以下敘述:<br>
1.打開 LINE Notify 的網站 ( https://notify-bot.line.me/zh_TW/ )，使用自己的 LINE 帳號登入。<br>
2.在個人頁面可以發行「權杖」<br>
3.點選「發行」，會出現一段權杖代碼，這段代碼「只會出現一次」，複製這段代碼，先找個地方貼上並儲存這段代碼，就可以點選下方按鈕「關閉」。<br>
4.完成後就會發現連動的服務裡，出現了我們自訂的服務。<br>
![Linetoken](https://user-images.githubusercontent.com/72924522/138567011-74a0da56-aa29-47c7-897c-78d1aea19ae5.jpg)
<br><br><br>
userAgent為個人的用戶代理，可以在F12下獲取<br>
![useragent](https://user-images.githubusercontent.com/72924522/138566588-669877fb-7705-4c1b-bfe0-16ab7ff65b71.png)
<br><br><br>
spacePoolId為個人在spacepool的ID<br>
![spacepoolid](https://user-images.githubusercontent.com/72924522/138566651-8d0b648d-7037-48bb-aaa2-4d8be821b7bf.png)
<br>
設定好四項參數後，就可以開啟main.exe了!<br>



>!!happy farming!!
>成功後main.exe就可以打開了!!

