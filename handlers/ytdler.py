import subprocess

anotherdownload = ''

print("""
                    Welcome to the YouTube Video Downloader.
             This program will print the highest quality video/audio.

     """)

while True:
    videoURL = input('Enter the full video URL: ')
    question = input('Are you downloading a playlist? Y/N: ')
    playlist = ''
    anotherdownload = ''

    if question.lower() in ('y', 'yes'):
        playlist = '--yes-playlist'
    elif question.lower() in ('n', 'no'):
        playlist = '--no-playlist'
    else:
        print('Sorry I do not understand, downloading single video.')
        playlist = '--no-playlist'

    print('Now downloading:', videoURL)

    subprocess.call(
        ['youtube-dl', '-f', 'bestvideo+bestaudio',
         playlist, videoURL, '-o', "\\%(title)s\\"])

    anotherdownload = input('Would you like to download another video? Y/N: ')

    if anotherdownload.lower() in ('n', 'no'):
        print('Thanks for using YouTube Video Downloader.')
        input('Press any key to exit')
        break