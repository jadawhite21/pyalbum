# Pyalbum

Piece together an album with the help of Python and Wikipedia!

## Installation

### Dependencies

* requests
* BeautifulSoup
* [wikipedia](https://github.com/goldsmith/Wikipedia)
* [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)
* [youtube-dl](https://github.com/ytdl-org/youtube-dl)

Clone the repository and install the above dependencies using `pip`.

```bash
git clone https://github.com/megaultraok/pyalbum.git
python setup.py install
```

It is recommended to install the dependencies using a Python virtual
environment to keep possible existing versions of the dependencies on the host
machine from conflicting with the required versions for this program.

#### Other dependencies

Please install the following dependencies using your distribution's package
manager.

* ffmpeg

## Usage

To use Pyalbum, first make sure the album has a proper Wikipedia page
with a tracklist table. Then, invoke the `pyalbum` module, followed by the album
name and artist within double quotes, respectively.

```bash
python -m pyalbum "Floral Shoppe" "Macintosh Plus"
```
You will then be prompted with a list of available Wikipedia results related to
either the album or the artist. Choose the one related to the desired album.
Finally, the program will begin creating the album.

It will use the first studio album released by the artist. Studio albums with
"Side A/Side B" track order will also be considered. Allow some time to run
backend processes. You will know the program is successfully running once the
output "Now downloading..." appears.

### Troubleshoot

There may be some bugs when creating the album that are planned to be fixed in
future versions.

1. If the inputted album name has a similar name to other Wikipedia entries
&mdash; whether they are related to the desired album or not &mdash; the program
will throw a DisambiguationError.

    **Solutions:** Instead of passing only the album name, try these other input
    methods to get your desired result:

    ```bash
    # Including (<artist name> album) in the album name
    python -m pyalbum "Floral Shoppe (Macintosh Plus album)" "Macintosh Plus"
    ```

    ```bash
    # Passing artist name as the album name
    python -m pyalbum "Macintosh Plus" "Macintosh Plus"
    ```

    These should work as intended. After the album creation is complete, change
    the album directory name &mdash; located in the host machine's Music directory
    &mdash; to the actual album name.

2. Sometimes Pyalbum may download an instrumental or a concert version of the
track, even though there are checks for that in the program. Since the backend
involves YouTube, certain videos may not have "instrumental" or "concert"
explicitly in their title, but their audio definitely is.

    **Solution:** If this is an issue, you may try to rectify this yourself by
    replacing affected tracks with their appropriate studio versions, using a
    downloading/streaming tool like `youtube-dl` and naming the audio files in
    respect to their order in the album.

    Perhaps in the future, I will implement a machine learning algorithm to
    detect whether the audio is the studio version of a track. But until then,
    please be patient! :)

3. Pyalbum may throw an HTTPError (403 Forbidden).

    **Solution:** Just restart the program and it will continue where it stopped.

4. The desired album may not download all listed tracks.

    **Solution:** Please raise an issue, including the album name and artist, so
    that I can take a look and find a solution. Otherwise, you may finish filling
    in the album yourself by using a downloading/streaming tool like `youtube-dl`.

## Disclaimer

This program was made with no intention of circumventing copyright laws. This
program should not be used as means to download copyrighted content, unless used
for terms described in Copyright and Fair Use Protection policies according to
the user's local legislation. Please do not use this program to physically or
digitally distribute or sell generated albums containing copyrighted material
without appropriate permission or allowance. Give all credit where credit is due.

Above all else, the responsibility is of the user.

## Notes

* All contributions welcomed.

* Please report issues not mentioned in this README to the issue tracker of this
 repository.
