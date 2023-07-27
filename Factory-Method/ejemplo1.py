###Implementar un ejemplo sencillo de Factory-Method

import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, name, artist):
        self.song_id = song_id
        self.name = name
        self.artist = artist

class SongSerializer:
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'name': song.name,
                'artist': song.artist
            }
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            name = et.SubElement(song_info, 'name')
            name.text = song.name
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)
    