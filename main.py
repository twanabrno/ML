import operator
import sys
import time
import random
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import cv2
from gtts import gTTS
import playsound


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
engine.setProperty('rate', 150)
n = 0

def speak(audio, lang="en"):
    if lang == "tr":
        global n
        n += 1
        file = f"{n}.mp3"
        tts = gTTS(text=audio, lang="tr", slow=False)
        try:
            tts.save(file)
            print(audio)

            playsound.playsound(file)
            os.remove(file)
        except Exception as e:
            print(e)
    else:
        print(audio)
        engine.say(audio)
        engine.runAndWait()


def wishMe(lang="en"):
    hour = int(datetime.datetime.now().hour)
    if lang == "tr":
        if 0 <= hour < 12:
            speak("günaydın", "tr")

        elif 12 <= hour < 18:
            speak("iyi günler", "tr")

        else:
            speak("iyi akşamlar", "tr")

        speak("nasıl yardımcı olablirim?", "tr")
    else:
        if 0 <= hour < 12:
            speak("good morning sir")

        elif 12 <= hour < 18:
            speak("good afternoon")

        else:
            speak("good evening")

        speak("ready to comply. What can i do for you ?")


def takeCommand(lang="en"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if lang == "tr":
            print("dinliyor...")
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                print("tanımlıyor...")
                query = r.recognize_google(audio, language='tr-TR')
                print(f"kullanıcı: {query}\n")
            except Exception:
                print("anlayamadım tekrarlarmısın?")
                return "None"

        else:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                print("recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said: {query}\n")
            except Exception:
                print("say that again please?")
                return "None"

    return query


def turkish():
    wishMe("tr")
    while True:
        query = takeCommand("tr").lower()
        if 'mila' in query:
            speak("sizi dinliyorum", "tr")
        elif "nasılsın" in query:
            speak("iyim teşekürler, sen nasılsın", "tr")
            qry = takeCommand("tr").lower()
            if ("iyi değilim" in qry) or ("kötüyüm" in qry):
                speak("çok üzüldüm, seni nasıl mutlu edebilirim", "tr")
            elif ("iyi" in query) or ("harika" in query):
                speak("iyi olmana sevindim, sana nasıl yarcımcı olablirim?", "tr")
            else:
                speak("seni ne yazik ki anlayamadığım", "tr")
        elif ("sen kimsin" in query) or ("kimsin sen" in query):
            speak("benim adım mila", "tr")
            speak('beni kodlayan ne öğrettiyse onu yapabilirim', "tr")
        elif ("ustan kim" in query) or ("seni kodlayan kim" in query) or ("seni kim kodladı" in query):
            speak("beni kodlayan enes ve tuana", "tr")
        elif ("nedir" in query) or ("ne için" in query):
            speak("vikipedyada arıyorum...", "tr")
            query = query.replace("nedir", "")
            query = query.replace("ne için", "")
            result = wikipedia.summary(query, sentences=2)
            speak("vikipedyaya göre...", "tr")
            speak(result, "tr")
        elif ("kim" in query) or ("kimdir" in query):
            speak("vikipedyada arıyorum...", "tr")
            query = query.replace("who is", "")
            result = wikipedia.summary(query, sentences=2)
            speak("vikipedyaya göre...", "tr")
            speak(result, "tr")
        elif "google aç" in query:
            speak("senin için ne arama mı istersin ?", "tr")
            qry = takeCommand("tr").lower()
            if "sadece aç" in qry:
                webbrowser.open("google.com")
            else:
                webbrowser.open(f"{qry}")
        elif "youtube aç" in query:
            speak("ne izlemek istersin?", "tr")
            qry = takeCommand("tr").lower()
            wk.playonyt(f"{qry}")
        elif "youtube'da arar mısın" in query:
            query = query.replace("youtube'da arar mısın", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        elif "tarayıcıyı kapat" in query:
            os.system("taskkill /f /im chrome.exe")
        ################################################
        elif "painti aç" in query:
            npath = "C:\Windows\system32\mspaint.exe"
            os.startfile(npath)
        elif "painti kapat" in query:
            os.system("taskkill /f /im mspaint.exe")
        elif ("çiz" in query) or ("ev" in query):
            speak("çiziyorum", "tr")
            pyautogui.moveTo(365, 255, duration=1)
            pyautogui.dragTo(365, 380, duration=2)
            pyautogui.dragTo(490, 380, duration=2)
            pyautogui.dragTo(490, 255, duration=2)
            pyautogui.dragTo(365, 255, duration=2)
            pyautogui.dragTo(427, 155, duration=2)
            pyautogui.dragTo(490, 255, duration=2)

            pyautogui.moveTo(385, 275, duration=1)
            pyautogui.dragTo(415, 275, duration=1)
            pyautogui.dragTo(415, 305, duration=1)
            pyautogui.dragTo(385, 305, duration=1)
            pyautogui.dragTo(385, 275, duration=1)

            pyautogui.moveTo(440, 275, duration=1)
            pyautogui.dragTo(470, 275, duration=1)
            pyautogui.dragTo(470, 305, duration=1)
            pyautogui.dragTo(440, 305, duration=1)
            pyautogui.dragTo(440, 275, duration=1)

            pyautogui.moveTo(415, 380, duration=1)
            pyautogui.dragTo(415, 340, duration=1)
            pyautogui.dragTo(440, 340, duration=1)
            pyautogui.dragTo(440, 380, duration=1)

            pyautogui.moveTo(435, 360, duration=1)
            pyautogui.dragTo(433, 360, duration=1)
            pyautogui.moveTo(4305, 3060, duration=1)




        elif "notpadı aç" in query:
            npath = "C:\Windows\system32\notepad.exe"
            os.startfile(npath)
        elif "notpadı kapat" in query:
            os.system("taskkill /f /im notepad.exe")

        elif ("komut istemini aç" in query) or ("cmd aç" in query):
            os.startfile("start cmd")
        elif ("komut istemini kapat" in query) or ("cmd kapat" in query):
            os.system("taskkill /f /im cmd.exe")
        elif "saat kaç" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" saat {strTime}", "tr")
        elif "sistemi yeniden başlat" in query:
            os.system("restart /r /t 5")
        elif "sistemi uykuya al" in query:
            os.system("rundll32.exe poweroff.dll, SetSuspendState 0,1,0")
        #############################################
        elif "kamerayı aç" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Input', img)
                k = cv2.waitKey(1)
                if k == 27 & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif ("kendini kapat" in query) or ("sessiz ol" in query) or ("tamamdır teşekkür ederim" in query):
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour < 21:
                speak("tamam o zaman, iyi günler", "tr")
            else:
                speak("tamam o zaman, iyi akşamlar", "tr")
            sys.exit()
        elif "ekran görüntüsü" in query:
            speak("aldığım ekran görüntüsünün ismi ne olsun", "tr")
            name = takeCommand("tr").lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f'{name}.png')
            speak("ekran görüntüsü kaydedildi", "tr")
        elif "hesapla" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("hazırım...", "tr")
                print("dinliyorum...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            myString = r.recognize_google(audio)
            print(myString)

            def get_op(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    'divided': operator.__truediv__,
                }[op]

            def evalBinbaryExpre(op1, op, op2):
                op1, op2 = int(op1), int(op2)
                return get_op(op)(op1, op2)

            speak("sonuç: ", "tr")
            speak(evalBinbaryExpre(*(myString.split())), "tr")


        elif "ip adresimi öğrenebilir misin?" in query:
            speak('bakıyorum...', "tr")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                speak("senin ip adresin :", "tr")
                speak(ipAdd, "tr")
            except Exception as ex:
                speak("internetin kötü, daha sonra tekrar dene", "tr")
        elif "sesi aç" in query:
            pyautogui.press("volumeup")
        elif "sesi kıs" in query:
            pyautogui.press("volumedown")
        elif "sustur" in query:
            pyautogui.press("volumemute")
        elif "susturma" in query:
            pyautogui.press("volumeunmute")
        elif "en yükses sesi aç" in query:
            for i in range(50):
                pyautogui.press("volumeup")
        elif "en düşük sesi aç" in query:
            for i in range(50):
                pyautogui.press("volumedown")
            pyautogui.press("volumeup")
        #################################################
        elif "abone ol" in query:
            speak(
                "burdaki olan herkes lütfen bizim youtube kanalımıza abone olun, twana ahmed brno, size göstereyim", "tr")
            pyautogui.hotkey("win")
            time.sleep(1)
            speak("tarayıcıyı aç", "tr")
            pyautogui.typewrite("chrome", 0.2)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(3)
            speak("youtube.com yaz", "tr")
            pyautogui.typewrite("youtube.com", 0.2)
            time.sleep(1)
            speak("entere bas", "tr")
            pyautogui.press("enter")
            time.sleep(3)
            youtubeSearch = pyautogui.locateCenterOnScreen('./imgs/youtubeSearch.png')
            pyautogui.moveTo(youtubeSearch, duration=0.2)
            pyautogui.click()
            pyautogui.press("enter")
            time.sleep(1)
            speak("twana ahmed brno'yu yaz", "tr")
            pyautogui.typewrite("twana ahmed brno", 0.2)
            time.sleep(1)
            speak("entere bas", "tr")
            pyautogui.press("enter")
            time.sleep(2)
            youtubeName = pyautogui.locateCenterOnScreen('./imgs/youtubeName.png')
            pyautogui.moveTo(youtubeName, duration=0.3)
            speak("burda bizim kanalımızı görebilirsiniz", "tr")
            subscribe = pyautogui.locateCenterOnScreen('./imgs/subscribe.png')
            pyautogui.moveTo(subscribe, duration=0.4)
            speak("burayı tıklayarak bize abone olabilirsiniz", "tr")

        elif "kaç dil biliyorsun" in query:
            speak("ben türkçe ve ingilizce konuşabiliyorum", "tr")

        elif ("ingilizce konuşabilir misin" in query) or ("ingilizce" in query):
            speak("ben ingilizce konuşabiliyorum, ingilizce konuşmamı ister misin?", "tr")
            qry = takeCommand("tr").lower()
            if ("evet" in qry) or ("neden olmasın" in qry) or ("hadi" in qry) or ("tamam" in qry):
                speak("ingilizceye çevriliyor", "tr")
                break;

            else:
                speak("nasıl istersen", "tr")

        else:
            speak("anlayamadım, tekrarlar mısın ?", "tr")
################################################################################
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "mila" in query:
            speak("yes sir")
        elif "how are you" in query:
            speak("i am good thanks, what about you?")
            qry = takeCommand().lower()
            if "not good" in qry:
                speak("oh sorry, Is there anything i can do for you?")
            elif "good" or "excellent" or "fine" in query:
                speak("i am glad that you are good, how can i help you?")
            else:
                speak("i couldn't understand sorry, how can i help you?")
        ###########################################
        elif ("who you are" in query) or ("who are you" in query):
            speak("my name is mila")
            speak('i can do anything that my creator programmed me to do, i created with python Language in pycharm')
        ###########################################
        elif ("who is your master" in query) or ("who created you" in query) or ("who is your creator" in query):
            speak("i have been created by Twana and enes in Kahramanmarash sutchu imam")
        ###########################################
        elif ("what is" in query) or ("what's" in query):
            speak("searching wikipedia...")
            query = query.replace("what is", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia...")
            speak(result)
        ###########################################
        elif ("who is" in query) or ("who's" in query):
            speak("searching wikipedia...")
            query = query.replace("who is", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia...")
            speak(result)
        ###########################################
        elif "open google" in query:
            speak("what do you want me to search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
        elif "open youtube" in query:
            speak("what you will like to watch ?")
            qry = takeCommand().lower()
            wk.playonyt(f"{qry}")
        elif "search on youtube" in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        elif "close browser" in query:
            os.system("taskkill /f /im iexplore.exe")
        ################################################
        elif "open paint" in query:
            npath = "C:\Windows\system32\mspaint.exe"
            os.startfile(npath)
        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")
        elif ("draw" in query) or ("house" in query):
            speak("drawing")
            pyautogui.moveTo(365, 255, duration=0.5)
            pyautogui.dragTo(365, 380, duration=0.5)
            pyautogui.dragTo(490, 380, duration=0.5)
            pyautogui.dragTo(490, 255, duration=0.5)
            pyautogui.dragTo(365, 255, duration=0.5)
            pyautogui.dragTo(427, 155, duration=0.5)
            pyautogui.dragTo(490, 255, duration=0.5)
            # first window
            pyautogui.moveTo(385, 275, duration=0.5)
            pyautogui.dragTo(415, 275, duration=0.5)
            pyautogui.dragTo(415, 305, duration=0.5)
            pyautogui.dragTo(385, 305, duration=0.5)
            pyautogui.dragTo(385, 275, duration=0.5)
            # second window
            pyautogui.moveTo(440, 275, duration=0.5)
            pyautogui.dragTo(470, 275, duration=0.5)
            pyautogui.dragTo(470, 305, duration=0.5)
            pyautogui.dragTo(440, 305, duration=0.5)
            pyautogui.dragTo(440, 275, duration=0.5)
            # door
            pyautogui.moveTo(415, 380, duration=0.5)
            pyautogui.dragTo(415, 340, duration=0.5)
            pyautogui.dragTo(440, 340, duration=0.5)
            pyautogui.dragTo(440, 380, duration=0.5)
            pyautogui.moveTo(435, 360, duration=0.5)
            pyautogui.dragTo(433, 360, duration=0.5)

            pyautogui.moveTo(500, 500, duration=0.5)
        ###########################################
        elif "open notepad" in query:
            speak("what do you want to write in")
            qryText = takeCommand().lower()
            npath = "C:\Windows\system32\\notepad.exe"
            os.startfile(npath)
            time.sleep(2)
            pyautogui.typewrite(qryText, 0.1)
        elif "close notepad" in query:
            speak("do you want to save it?")
            save = takeCommand().lower()
            fileName = str(random.randint(1, 100))
            if "yes" in save:
                pyautogui.hotkey("ctrl", "s")
                time.sleep(1)
                pyautogui.typewrite(fileName, 0.1)
                time.sleep(1)
                pyautogui.press("enter")
                os.system("taskkill /f /im notepad.exe")
            else:
                os.system("taskkill /f /im notepad.exe")
        ###########################################
        elif ("open command prompt" in query) or ("open cmd" in query):
            os.startfile("start cmd")
        elif ("close cmd" in query) or ("close command prompt" in query):
            os.system("taskkill /f /im cmd.exe")
        ###########################################
        elif "what time is it" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        ###########################################
        elif "refresh" in query:
            pyautogui.hotkey('win', 'd')
            pyautogui.hotkey('win', 'd')
        elif "restart" in query:
            os.system("restart /r /t 5")
        elif "lock" in query:
            print("locking")
            os.system("rundll32.exe poweroff.dll, SetSuspendState 0,1,0")
        ############################################
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Input', img)
                k = cv2.waitKey(1)
                if k == 27 & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
        ###########################################
        elif "screenshot" in query:
            speak("tell the name for the file")
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f'{name}.png')
            speak("screenshot saved")
        #################################################
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready...")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            myString = r.recognize_google(audio)
            print(myString)


            def get_op(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    'divided': operator.__truediv__,
                }[op]


            def evalBinbaryExpre(op1, op, op2):
                op1, op2 = int(op1), int(op2)
                return get_op(op)(op1, op2)
            speak("your result is: ")
            speak(evalBinbaryExpre(*(myString.split())))
        #################################################
        elif "my ip address" in query:
            speak('checking...')
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                speak("your ip address is :")
                speak(ipAdd)
            except Exception as ex:
                speak("bad internet, please try again later")
        #################################################
        elif "volume up" in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif "unmute" in query:
            pyautogui.press("volumeunmute")
        elif "volume max" in query:
            for i in range(50):
                pyautogui.press("volumeup")
        elif "volume min" in query:
            for i in range(50):
                pyautogui.press("volumedown")
        #################################################
        elif "subscribe" in query:
            speak("everyone who are watching this video, please subscribe our channel twana ahmed brno, let me show you how to do that")
            pyautogui.hotkey("win")
            time.sleep(1)
            speak("open your browser")
            pyautogui.typewrite("chrome", 0.2)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(3)
            speak("type youtube.com")
            pyautogui.typewrite("youtube.com", 0.2)
            time.sleep(1)
            speak("press enter")
            pyautogui.press("enter")
            time.sleep(3)
            youtubeSearch = pyautogui.locateCenterOnScreen('./imgs/youtubeSearch.png')
            pyautogui.moveTo(youtubeSearch, duration=0.2)
            pyautogui.click()
            pyautogui.press("enter")
            time.sleep(1)
            speak("type on search bar twana ahmed brno")
            pyautogui.typewrite("twana ahmed brno", 0.2)
            time.sleep(1)
            speak("press enter")
            pyautogui.press("enter")
            time.sleep(2)
            youtubeName = pyautogui.locateCenterOnScreen('./imgs/youtubeName.png')
            pyautogui.moveTo(youtubeName, duration=0.3)
            speak("here you will see our channel")
            subscribe = pyautogui.locateCenterOnScreen('./imgs/subscribe.png')
            pyautogui.moveTo(subscribe, duration=0.4)
            speak("click here to subscribe")
            # time.sleep(1)
            # speak("if you do not see our channel here, click on filter")
            # youtubeFilter = pyautogui.locateCenterOnScreen('./imgs/youtubeFilters.png')
            # pyautogui.moveTo(youtubeFilter)
            # pyautogui.click()
            # time.sleep(1)
            # speak("now click on channel")
            # youtubeChannel = pyautogui.locateCenterOnScreen('./imgs/youtubeChannel.png')
            # pyautogui.moveTo(youtubeChannel)
            # pyautogui.click()
            # time.sleep(1)
            # speak("here you will surely see our channel")
            # subscribe = pyautogui.locateCenterOnScreen('./imgs/subscribe.png')
            # pyautogui.moveTo(subscribe)
            # speak("click here to subscribe our channel")
            # pyautogui.click()
        #################################################
        elif "languages" in query:
            speak("i can speak English and Turkish")
        elif ("speake Turkish" in query) or ("turkish" in query):
            speak("i can speak turkish, do you want me to speake turkish?")
            qry = takeCommand().lower()
            if ("yes" in qry) or ("why not" in qry) or ("lets try" in qry) or ("yeap" in qry):
                speak("translating to turkish")
                turkish()
                speak("translated to English, how can i help you")

            else:
                speak("as you wish ")

        #################################################
        elif ("go to sleep" in query) or ("be quiet" in query) or ("okay thank you" in query):
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour < 21:
                speak("alright then, have a nice day")
            else:
                speak("alright then, good night")
            sys.exit()
        else:
            speak("i have no idea what you are saying")






# import os
# import time
# import playsound
# import speech_recognition as sr
# from gtts import gTTS
#
# def speak(text):
#     tts = gTTS(text=text, lang='en')
#     filename = "voice.mp3"
#     tts.save(filename)
#     playsound.playsound(filename)
#     os.remove(filename)
#
#
# def get_audio():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         said = ""
#
#         try:
#             said = r.recognize_google(audio)
#             print(said)
#         except Exception as e:
#             print("Exeption: " + str(e))
#
#     return said
#
#
# speak("hello its BRNO virtual assistant")
# get_audio()


# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia
# import pyjokes

# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
#
#
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
#
#
# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print('listening...')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'alexa' in command:
#                 command = command.replace('alexa', '')
#                 print(command)
#
#     except:
#         pass
#     return command
#
#
# def run_alexa():
#     command = take_command()
#     print(command)
#     if 'play' in command:
#         song = command.replace('play', '')
#         talk('playing ' + song)
#         pywhatkit.playonyt(song)
#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         talk('Current time is ' + time)
#     elif 'who is' in command:
#         person = command.replace('who is', '')
#         info = wikipedia.summary(person, 1)
#         print(info)
#         talk(info)
#     elif 'date' in command:
#         talk('sorry, I have a boyfriend')
#     elif 'are you single' in command:
#         talk('I am in a relationship with wifi')
#     elif 'joke' in command:
#         talk(pyjokes.get_joke())
#     else:
#         talk('Please say the command again.')
#
#
# while True:
#     run_alexa()
