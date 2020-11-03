from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

# 파일이 있는 위치를 선택함  
VIDEO_PATH = Path("../tests/media/test_media_1.mp4") 

# 이렇게 하면 바로 구동됨  
player = OMXPlayer(VIDEO_PATH)

# 구동되는 시간을 의미함, 초 단위
sleep(5)

# 동영상 구동을 멈춤  
player.quit()
