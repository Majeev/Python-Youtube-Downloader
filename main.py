from pytube import YouTube

def GetFile(URL):
    youtubeFile = YouTube(URL)
    youtubeFile = youtubeFile.streams.get_highest_resolution()
    try:
        youtubeFile.download('C:\Users\majew\Desktop')
    except:
        print('oops something went wrong.')
    print("File download has been completed")

url = input("Paste URL here: ")
GetFile(url)
