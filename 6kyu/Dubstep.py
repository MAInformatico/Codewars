def song_decoder(song):
    song = song.split('WUB')
    result = []
    for letter in song:
        if letter != '':
            result += [letter]
    return ' '.join(result)
