# Design a class named `Track` that represents an
# audio recording and implements built-in Python behaviors using magic methods.

# Requirements:
# 1. Initialization:
#    - Accepts `title` (str), `artist` (str),
#      `duration` (int in seconds), and `db_level` (int, can be negative).

# 2. Magic Methods:
#    - Implement `__repr__`: Returns a developer-friendly string formatted
#      exactly as: Track('Title', 'Artist', duration, db_level).
#    - Implement `__str__`: Returns a user-friendly string formatted as: Artist — Title (duration sec.).
#    - Implement `__len__`: Returns the track's duration as an integer.
#    - Implement `__abs__`: Returns the absolute value of the db_level (removing the negative sign).


class Track:
    def __init__(self, title: str, artist: str, duration: int, db_level: int) -> None:
        self._title = title
        self._artist = artist
        self._duration = duration
        self._db_level = db_level

    def __repr__(self):
        return (
            f"Track({self._title}, {self._artist}, {self._duration}, {self._db_level})"
        )

    def __str__(self):
        return f"{self._artist} - {self._title} ({self._duration} sec.)"

    def __len__(self):
        return self._duration

    def __abs__(self):
        return abs(self._db_level)


if __name__ == "__main__":
    track = Track("Blinding Lights", "The Weeknd", 200, -6)

    print(repr(track))  # Track('Blinding Lights', 'The Weeknd', 200, -6)
    print(track)  # The Weeknd - Blinding Lights (200 sec.)
    print(len(track))  # 200
    print(abs(track))  # 6
