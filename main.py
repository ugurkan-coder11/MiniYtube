from youtubesearchpython import Search #pip install youtube-search-python
from pytube import YouTube #pip install pytube
from moviepy.editor import VideoFileClip #pip install moviepy
import os

class Engine:
    def __init__(self):
        def clear():
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        clear()
        text = """
        ###################################################
        - MiniYTUBE'A HOSGELDİN
            - Istediğin gibi arama yapıp,istediğin videoyu indirebilirsin
            - Mp3 ve Mp4 formatları
            - Yüksek kalite
        ###################################################
        
        """
        print(text)
    
    def searchMotor(self):
        try:
            arama_limiti = int(input("Arama Limitini giriniz: "))
            self.search = input("Arama: ")
            self.allSearch = Search(self.search, limit = arama_limiti)
            results = self.allSearch.result()["result"]
            for i in range(arama_limiti):
                self.url = results[i]["link"]
                self.title = results[i]["title"]
                self.channel = results[i]["channel"]["name"]
                view = results[i]["viewCount"]["text"]
                print(f"[{i}] {self.title}, Channel: {self.channel}, VIEW: {view}")
            print("-"*100)
            selectt = int(input("Seçimin: "))
            if selectt > arama_limiti:
                print("### LİMİTİ AŞMA! ###")
            else:
                text_two = f"""
                *********************************************************
                ---------------------------------------------------------
                Video:
                    - Ismi : {results[selectt]['title']}
                    - Kanal adı : {results[selectt]['channel']['name']}
                    - Izlenme : {results[selectt]['viewCount']['text']}
                    - URL : {results[selectt]["link"]}
                Indirme:
                    1 - Mp4 olarak indir
                    2 - Mp3 olarak indir
                    3 - Çıkış yap
                ---------------------------------------------------------
                *********************************************************
                """
                print(text_two)
                download = int(input("Seçimin: "))
                if download == 1:
                    self.motor(results[selectt]["link"],"mp4")
                    print("INDIRME ISLEMI BASARILI!")
                elif download == 2:
                    self.motor(results[selectt]["link"],"mp3")
                    print("INDIRME ISLEMI BASARILI!")
                elif download == 3:
                    print("Yine Bekleriz..")
                    exit()
        except ValueError:
            print("INT ERROR")

    def motor(self,url,format = "mp4"):
        if format == "mp4":
            mp4 = YouTube(url).streams.get_highest_resolution().download()
                                      
        elif format == "mp3":
            mp4 = YouTube(url).streams.get_highest_resolution().download()
            mp3 = mp4.split(".mp4",1)[0] + ".mp3"
                
            video_clip = VideoFileClip(mp4)
            audio = video_clip.audio
            audio.write_audiofile(mp3)
                
            audio.close()
            video_clip.close()
                
            os.remove(mp4)


e = Engine()
e.searchMotor()
