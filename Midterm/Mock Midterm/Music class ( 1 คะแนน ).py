class Song:
    def __init__(self, name, genre, durations ):
        self.name = name
        self.genre = genre
        self.durations = f"{durations//60}.{durations%60:>02}"
    def show_info(self):
        return (f"{self.name} <|> {self.genre} <|> {self.durations}")
Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())