from pytube import Search
from pytube import YouTube
from io import BytesIO

def search(query):
  return Search(query)

def getMP3(id):
  yt = YouTube(str("https://www.youtube.com/watch?v={}".format(id)))
  video = yt.streams.get_audio_only() 
  buffer = BytesIO()
  video.stream_to_buffer(buffer)
  buffer.seek(0)
  size=(video.filesize)//(1024*1024)
  name="{}+.mp3".format(yt.title)
  return {
    "title": yt.title,
    "size" : size,
    "buffer":buffer,
    "name":name
  }


def getMP4(id,res):
  yt = YouTube(str("https://www.youtube.com/watch?v={}".format(id)))
  video = yt.streams.get_by_resolution(res)
  try: 
    size=(video.filesize)//(1024*1024)
    buffer = BytesIO()
    video.stream_to_buffer(buffer)
    buffer.seek(0)
    name="{}+.mp4".format(yt.title)
  except AttributeError:
    return None
  return {
    "title": yt.title,
    "size" : size,
    "buffer":buffer,
    "name":name
  }