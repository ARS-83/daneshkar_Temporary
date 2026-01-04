from .book import Book


class Audiobook(Book):
    _sample_audio_link: str = "https://soundcloud.com/reza-pishro-rail/entekhab?si=87613952da194e35abcfdc8850ddd597&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"

    def __init__(self, title: str, author: str, genre: str, pages: int, date_added, duration: int, narrator: str, sample_audio_link: str = ""):
        super().__init__(title, author, genre, pages, date_added)
        self.duration = duration  # in minutes
        self.narrator = narrator
        self.sample_audio_link = sample_audio_link if sample_audio_link else Audiobook._sample_audio_link

    def __str__(self):
        return super().__str__() + f" [Narrated by {self.narrator} - {self.duration} mins]"