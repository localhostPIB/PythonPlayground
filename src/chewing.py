try:
    import schedule
except ImportError:
    from pip._internal import main as pip
    pip(['install', 'schedule'])
    import schedule


import time

try:
    from playsound import playsound
except ImportError:
    from pip._internal import main as pip
    pip(['install', 'playsound==1.2.2'])
    from playsound import playsound


def play_sound():
    playsound('https://cdn.freesound.org/previews/412/412068_5121236-lq.mp3')


def start():
    schedule.every(3).minutes.do(play_sound)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    start()
