from pytube import YouTube
from pytube import Search
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from io import BytesIO
import base64

st.set_page_config(page_title="Youtube Downloader",page_icon=":music:")

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

selected = option_menu(None, ["MP3", 'MP4'], 
    icons=['music', 'video'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    )



def main():
    if selected=="MP3":
        st.title("Youtube  MP3 Downloader")
        status1=False
        status2=False
        status3=False
        query= st.text_input('Enter Name of YouTube Video')
        songs = Search(query)

        try :
            for i in range (1,11):
                st.write("{} : {} :{} views".format(i,songs.results[i].title,songs.results[i].views))
            st.write("-----------------")
            status1=True
        except IndexError:
            st.error("Enter Song")

        if status1==True:
            try :
                song=st.text_input('Enter song number')
                song=int(song)
                if song not in [1,2,3,4,5,6,7,8,9,10]:
                    st.error("incorrect song number")
                id=songs.results[int(song)].video_id
                status2=True

            except ValueError:
                st.error("Enter Song number")    

        if status2==True:
            yt = YouTube(str("https://www.youtube.com/watch?v={}".format(id)))
            video = yt.streams.get_audio_only() 
            buffer = BytesIO()
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            size=(video.filesize)//(1024*1024)
            name="{}+.mp3".format(yt.title)
            st.write("{} size:{} MB".format(yt.title,size))
          
            status3=True
            

        if status3==True:
            st.download_button('Download mp3 file',buffer,file_name=name,mime="audio/mp3")
            #st.success("File is Downloaded")
            
            

    if selected=="MP4":
        st.title("Youtube  MP4 Downloader")
        status1=False
        status2=False
        status3=False
        query= st.text_input('Enter Name of YouTube Video')
        songs = Search(query)

        try :
            for i in range (1,6):
                st.write("{} : {} :{} views".format(i,songs.results[i].title,songs.results[i].views))
            st.write("-----------------")
            status1=True
        except IndexError:
            st.error("Enter Song")

        if status1==True:
            try :
                song=st.text_input('Enter song number')
                song=int(song)
                if song not in [1,2,3,4,5]:
                    st.error("incorrect song number")
                id=songs.results[int(song)].video_id
                status2=True

            except ValueError:
                st.error("Enter Song number")    

        if status2==True:
            yt = YouTube(str("https://www.youtube.com/watch?v={}".format(id)))
            try:
                res=st.select_slider('Pick a resolution',["1080p","720p", "480p","360p","240p","144p"])
            except TypeError:
                st.error("Enter video resolution")  

            video = yt.streams.get_by_resolution(res) 
            try:
                size=(video.filesize)//(1024*1024)
                st.write("{} | size:{} MB".format(yt.title,size))
                st.write("Processing your file...")
                buffer = BytesIO()
                video.stream_to_buffer(buffer)
                buffer.seek(0)
                name="{}+.mp4".format(yt.title)
                status3=True
                
                if status3==True:
                    st.download_button('Download mp4 file',buffer,file_name=name,mime="video/mp4")
                    #st.success("File is Downloaded")

            except AttributeError:
                st.warning('File Format not available')    

           
        
if __name__ == '__main__':
	main()
