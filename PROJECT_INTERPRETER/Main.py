"""
Nama Program    : QueTube (Antrian lagu yang terintegrasi dengan API Youtube Music)
Dibuat oleh     : Kelompok 11
                  2017051008 - Kayla Atsila Ivanka 
                  2017051035 - Irfan Saputra
Dibuat pada     : Kamis, 9 Desember 2021, 23:34:55
Selesai pada    : Sabtu, 11 Desember 2021, 03:23:00
Revisi pada     : Minggu, 12 Desember 2021, 22:37:00

install pip install --upgrade YouTubeMusicAPI
install pip3 install bs4 (jika ada error bs4 not found)
"""
# t adalah class table
import os
# from YouTubeMusicAPI import YouTubeMusicAPI
import table as t

song = ('Kenshi Yonezu ~ Lemon', 
        'Official Hige Dandism ~ Pretender', 
        'Yuuri ~ Dry Flower',
        'Aimer ~ Kataomoi',
        'King Gnu ~ Hakujitsu',
        'Masaki Suda ~ Machigaisagashi',
        'Kana-Boon ~ Silhouette',
        'YOASOBI ~ Yoru ni Kakeru',
        'Mrs. GREEN APPLE ~ Inferno',
        'LiSA ~ homura')

class Action:
    que = []

    def isEmpty(self):
        return len(self.que) == 0

    def addQueue(self):  
        os.system('cls')

        t.header('RECOMMENDATION', 60)
        t.spaceRow(60)
        for l in song :
            t.addIterRow(song.index(l)+1, l, 55)
        t.spaceRow(60)
        t.endRow(60)

        n = input('Choose song number ➤  ').split()

        which = [int(i) for i in n]

        for i in which:
            i -= 1

            if i >= 0 and i <= len(song)-1:
                self.que.append(song[i])
                t.messageBox((str(song[i]) + ' is added ♪'), 60)
            else:
                t.warningBox('! No song found !', 60)

    def showPlaying(self):
        os.system('cls')

        """ 
            Konsep Queue adalah First In First Out.
            Oleh karena itu, secara default, lagu yang pertama akan 
            dimainkan adalah lagu yang pertama kali ditambahkan
            dalam antrian.
        """

        track = YouTubeMusicAPI(str(self.que[0])).track()

        t.messageBox('🎜 Playing '+ self.que[0] + '🎜', 60)

        print()
        t.header('► Youtube Music Description', 60)
        t.spaceRow(60)
        t.addSpecialRow(track["name"], 60)
        t.addCenterRow(track["datePublished"], 60)               
        t.addCenterRow(track["url"], 60)               
        t.spaceRow(60)
        t.endRow(60)
            
        self.que.pop(0)
        print(str(len(self.que)) + ' left in queue')
        print()

        os.system('pause')

    def showQueue(self):
        os.system('cls')

        if self.isEmpty() == True:
            t.warningBox('⛌  Queue is empty ⛌', 60)
        else:
            t.header2Rows('QUEUE', str(len(self.que)) + ' in track', 60)
            t.spaceRow(60)

            for l in self.que:
                t.addRow(l, 60)

            t.spaceRow(60)
            t.sectionRow(60)
            t.addRow('➀ PLAY', 60)
            t.addRow('➁ SORT', 60)
            t.addRow('➂ CLEAR ALL', 60)
            t.addRow('➃ BACK', 60)
            t.endRow(60)
            
            ans = int(input('Choose option ➤  '))
            
            if ans == 1:
                self.showPlaying()
                self.showQueue()
            elif ans == 2:
                self.que.sort()
                self.showQueue()
            elif ans == 3:
                self.que.clear()
                t.warningBox('🗑 Queue is successfully cleared 🗑', 60)
            elif ans == 4:
                pass
            else:
                t.warningBox('! Invalid input !', 60)

action = Action()


while True:
    os.system('cls')

    t.header2Rows('MY PLAYLIST', '◉ Japan Edition ◉', 60)
    t.spaceRow(60)
    t.addRow('➀ ADD TO QUEUE', 60)
    t.addRow('➁ QUEUE', 60)
    t.addRow('➂ EXIT', 60)
    t.spaceRow(60)
    t.endRow(60)

    try:
        pick = int(input('Choose option ➤  '))

        if pick == 1:
            action.addQueue()
        elif pick == 2:
            action.showQueue()
        elif pick == 3:
            break
        else:
            t.warningBox('! Invalid input !', 60)

    except ValueError:
        t.warningBox('! Invalid input !', 60) 
    
    print()
    os.system('pause')
    os.system('cls')