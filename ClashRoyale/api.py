from curses.panel import bottom_panel
import matplotlib
import requests
import matplotlib.pyplot as plt
import io
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

base = 'https://api.clashroyale.com/v1/'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjMwZTE1OTIyLTcxNDQtNDZmZi04MWFiLTZmMjA5NzU5OGQyZCIsImlhdCI6MTY0NTEwMTY2NCwic3ViIjoiZGV2ZWxvcGVyLzM1MWNiYzQzLTU4Y2EtN2VhMS05MDYzLWY4M2YzYmM5NWFiZiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIzNi4zLjE3MS4xNyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.WxWUDdg62XXWFy4WDV01NIaxtzw1fz46DMTTUEb1TT6An0-Knpqk5WxYh5HRSTRoL9KkuOiGfkE3gffOn_K-tA'
myID = '2UJR0JRU'
headers = {'Authorization': 'Bearer {}'.format(TOKEN)}

def show_player_deck(player : dict):
    PlayerItemLevelList = player['currentDeck']
    Images = []
    for i in range(8):
        url = PlayerItemLevelList[i]['iconUrls']['medium']
        Images.append(Image.open(io.BytesIO(requests.get(url).content)))


    plt.figure(figsize=(10, 10))
    plt.suptitle(player['name'] + '\'s deck', size=25)

    for i in range(8):
        level = PlayerItemLevelList[i]['level']
        mxlevel = PlayerItemLevelList[i]['maxLevel']
        level += 14 - mxlevel

        plt.subplot(2, 4, i + 1)
        plt.tick_params(color='white')
        plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
        plt.title('Lv.' + str(level) + '\n' + PlayerItemLevelList[i]['name'])
        plt.imshow(Images[i])
    
    plt.show()

    
def player_log(log : dict):
    return

def about_player(id : str):
    player = 'players/%23' + id
    battle_log = player + 'battlelog'
    PLAYER = requests.get(base + player, headers=headers).json()
    show_player_deck(PLAYER)
    # BATTLE_LOG = requests.get(base + battle_log, headers=headers).json()


def main():
    about_player(myID)

main()