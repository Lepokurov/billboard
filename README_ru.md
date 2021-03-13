# billboard
Информация о песнях и артистах, жанрах в топ биллборд.


Программа показывает основную иформацию о песнях, артистах, жанрах, годах и их заваисимостях.

База данных создана мной путем парсигна https://en.wikipedia.org/ и https://genius.com/.
Парсер [здесь](https://github.com/Lepokurov/parser) (Смотреть его совершенно не обязательно)


В программе имеется 4 основные вкладки:

1. **Год** - Имеет страницу со списком лет и одиночную страницу года.
    1. Страница со списком лет:
       1. Содердит все года биллборда (1946 - 2020). 
       2. Имеет поиск по году.
    2. Одиночная страница:
       1. Содержит песни, артистов и жанры с количеством песен выбраного года.
  
2. **Песня** -  Имеет страницу со списком песен и одиночную страницу песни.
    1. Страница со списком песен:
        1. Содержит все песни, которые были в биллборд. Песни имеют название, исполнителей, название альбома, год и позицию.
        2. Имеет поиск песни по названию, артисту, жанру, году и кнопку для получения песен, которые были в биллборд больше 1 раза.
    2. Одиночная страница песни:
        1. It contains the album name and title of the song, the performers, the genres of the song.
        2. It contains the links to the wikipedia page and the сlip of the song at youtube.
        3. It contains a list of the years the song has been on the billboard with number on the chart, and some other songs of the performers.
  
3. **Артист** - It's having the page with list of artists and the solo page of artist.     
    1. Page with list of artists:
        1. It contains all artist, whos song was in billboard. Songs having a name, age and count songs in billboard.
        2. It have a search by name, song, genre and the button to show artists, whos alredy dead.
    2. Solo page artist:
        1. It contains the age, name and genres of the artist.
        2. It contains the links to the wikipedia page and a short bio.
        3. It contains a list of the song, whos has been on the billboard with number on the chart, with whom the artist featuring with, and all other songs of the artist.
  
4. **Жанр** - It's having the page with list of genes and the solo page of genre.
    1. Page with list of gemre:
       1. It contains the all genre of songs and artsits
       2. It have the button of sort by song and artsits.
    2. Solo page year:
       1. It contains the years with count of a songs of current genre, the song and the artists of the current genre
  
