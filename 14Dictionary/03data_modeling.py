playlist = {
    'title': "Patagonia Bus",
    'author': "Humayun",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}

total_duration = 0.0
for song in playlist['songs']:
    total_duration += song['duration']
    print(song['song_title'])
print(total_duration)