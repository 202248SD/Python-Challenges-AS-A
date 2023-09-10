import random

song_list = [
  ["A1","A1S1","A1S2","A1S3","A1S4","A1S5","A1S6","A1S7","A1S8","A1S9","A1S10",],
  ["A2","A2S1","A2S2","A2S3","A2S4","A2S5","A2S6","A2S7","A2S8","A2S9","A2S10",],
  ["A3","A3S1","A3S2","A3S3","A3S4","A3S5","A3S6","A3S7","A3S8","A3S9","A3S10",],
  ["A4","A4S1","A4S2","A4S3","A4S4","A4S5","A4S6","A4S7","A4S8","A4S9","A4S10",],
  ["A5","A5S1","A5S2","A5S3","A5S4","A5S5","A5S6","A5S7","A5S8","A5S9","A5S10",],
  ["A6","A6S1","A6S2","A6S3","A6S4","A6S5","A6S6","A6S7","A6S8","A6S9","A6S10",],
  ["A7","A7S1","A7S2","A7S3","A7S4","A7S5","A7S6","A7S7","A7S8","A7S9","A7S10",],
  ["A8","A8S1","A8S2","A8S3","A8S4","A8S5","A8S6","A8S7","A8S8","A8S9","A8S10",],
  ["A9","A9S1","A9S2","A9S3","A9S4","A9S5","A9S6","A9S7","A9S8","A9S9","A9S10",],
  ["AX","AXS1","AXS2","AXS3","AXS4","AXS5","AXS6","AXS7","AXS8","AXS9","AXS10",],
]

play_list = []
recent_artists = [-1,-1]
for i in range(100):
  artist = random.randint(0,9)
  song_ = random.randint(1,10)
  
  while song_list[artist][song_] in play_list or artist in recent_artists:
    artist = random.randint(0,9)
    song_ = random.randint(1,10)
    
  recent_artists.append(artist)
  del recent_artists[0]
  song = song_list[artist][song_]
  
  play_list.append(song)

print(play_list)
