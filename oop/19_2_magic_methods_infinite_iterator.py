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