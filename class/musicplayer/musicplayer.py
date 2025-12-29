from abc import ABC, abstractmethod


class BasePlaylist(ABC):
    def __init__(self):
        # TODO: store the label name and initialize an empty list to store tracks 
        self.track = []
        self._label = ""
      

    def add(self, track_name):
        # TODO: append track_name (string) to self._tracks
        if isinstance(track_name,str) :
          self.track.append(track_name)
        
    

    def __len__(self):
        # TODO: return number of tracks
        return len(self.track)
    

    def __repr__(self):
        # TODO:
        return f"{self._label}: {self.track}"
      

    def __add__(self, other):
        # TODO:
        new_player = SequentialPlaylist()
        
        new_player.track = self.track + other.track

        return new_player

    @abstractmethod
    def __iter__(self):
        pass


class SequentialPlaylist(BasePlaylist):
    def __init__(self):
      super().__init__()
    def __iter__(self):
        # TODO: iterator in insertion order
        #self.track is a list has list_iterator class
        its = iter(self.track)
        return  its


class ReversePlaylist(BasePlaylist):
    def __iter__(self):
        # TODO: iterator in reverse insertion order
        itr = reversed(self.track)
        return  itr


""" Do not change the code below """

q = int(input())
playlists = {}  # label (str) -> BasePlaylist instance

for _ in range(q):
    op = input().split()

    if op[0] == "NEW_SEQ":
        label = op[1]
        playlist = SequentialPlaylist()
        playlist._label = label
        playlists[label] = playlist

    elif op[0] == "NEW_REV":
        label = op[1]
        playlist = ReversePlaylist()
        playlist._label = label
        playlists[label] = playlist

    elif op[0] == "ADD":
        label = op[1]
        track_name = op[2]
        playlists[label].add(track_name)

    elif op[0] == "LEN":
        label = op[1]
        print(len(playlists[label]))

    elif op[0] == "PLAY":
        label = op[1]
        k = int(op[2])
        it = iter(playlists[label])
        played = []
        for _ in range(k):
            played.append(next(it))
        print(" -> ".join(played))

    elif op[0] == "MERGE":
        new_label = op[1]
        l1 = op[2]
        l2 = op[3]
        merged = playlists[l1] + playlists[l2]
        merged._label = new_label
        playlists[new_label] = merged

    elif op[0] == "PRINT":
        label = op[1]
        print(playlists[label])