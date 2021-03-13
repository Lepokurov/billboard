# billboard
Information about songs, artists and genres at top billboard


This program show the main information about songs, artists, genres, years and their dependencies.

Database was created by myself by parsing from https://en.wikipedia.org/ and https://genius.com/.
The pasres is [here](https://github.com/Lepokurov/parser) (That's look soooo scary even for me)


The program have 4 main selection:

1. **Year** - It's having the page with list of years and the solo page of year.
    1. Page with list of years:
       1. It contains the all years of billboard (1946 - 2020). 
       2. It have a search by year.
    2. Solo page year:
       1. It contains the songs, the artists and genres with count of a songs of the current year.
  
2. **Song** - It's having the page with list of songs and the solo page of song.
    1. Page with list of songs:
        1. It contains all songs, whos was in billboard. Songs having a title, performers, album name, year and position at billbord.
        2. It have a search by song title, artist, genre, year and the button to show songs, whos was at billbord more then once.
    2. Solo page song:
        1. It contains the album name and title of the song, the performers, the genres of the song.
        2. It contains the links to the wikipedia page and the сlip of the song at youtube.
        3. It contains a list of the years the song has been on the billboard with number on the chart, and some other songs of the performers.
  
3. **Artist** - It's having the page with list of artists and the solo page of artist.     
    1. Page with list of artists:
        1. It contains all artist, whos song was in billboard. Songs having a name, age and count songs in billboard.
        2. It have a search by name, song, genre and the button to show artists, whos alredy dead.
    2. Solo page artist:
        1. It contains the age, name and genres of the artist.
        2. It contains the links to the wikipedia page and a short bio.
        3. It contains a list of the song, whos has been on the billboard with number on the chart, with whom the artist featuring with, and all other songs of the artist.
  
4. **Genre** - It's having the page with list of genes and the solo page of genre.
    1. Page with list of gemre:
       1. It contains the all genre of songs and artsits
       2. It have the button of sort by song and artsits.
    2. Solo page year:
       1. It contains the years with count of a songs of current genre, the song and the artists of the current genre
  
