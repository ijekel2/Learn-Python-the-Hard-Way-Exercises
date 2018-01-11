class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])
banana_song_lyrics = ["One banana, two banana, three banana, four", "Five banana, six banana, seven banana, more."]
banana_song = Song(banana_song_lyrics)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
banana_song.sing_me_a_song()
	