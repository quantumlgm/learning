# Design a class named `TrackPlaylist` that implements
# a custom infinite iterator to simulate a looping music playlist.

# Requirements:
# 1. Properties to store: a list of track names (strings).
# 2. Implement custom iteration capability allowing the instance to
#    be used directly in iteration processes.
# 3. Each iteration step must yield the current track name and
#    advance the internal pointer to the next track.
# 4. The iterator must be infinite and never raise `StopIteration`.
#    When the end of the playlist is reached, it must seamlessly loop back to the first track.


class TrackPlaylist:
    def __init__(self, playlist: list) -> None:
        if not isinstance(playlist, list):
            raise ValueError("The value must be a list")
        self.playlist = playlist
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.playlist):
            self.index = 0
        track = self.index
        self.index += 1
        return self.playlist[track]


if __name__ == "__main__":
    Track = TrackPlaylist(["Song A", "Song B", "Song C"])
    for t in Track:
        print(t)
