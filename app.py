from pytube import YouTube
from pytube import Search
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from io import BytesIO
import base64
import functionality

st.set_page_config(page_title="Youtube Downloader",page_icon=":music:")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


selected_format = option_menu(None, ["MP3", 'MP4'], 
    icons=['music', 'video'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    )



def main():
    
    st.title("Youtube "+ selected_format +" Downloader")
    status1=False
    status2=False
    status3=False
    
    form = st.form("my_form")
    query= form.text_input('Enter Name or Link of YouTube Video',key="query")
    form.form_submit_button("Submit")

    temp = query.split("https://www.youtube.com/watch?v=")

    if temp[0] != "":
        songs = functionality.search(query)
        
        try :
            for i in range (1,11):
                
                st.write("{} : {} : {} views".format(i,songs.results[i].title,songs.results[i].views))
                st.image(songs.results[i].thumbnail_url,width=200)
                st.write("-----------------")
            status1=True
        except IndexError:
            st.error("Enter Name")

        if status1==True:
            try :
                form = st.form("song_form")
                song = form.text_input('Enter song number',key="num")
                form.form_submit_button("Submit")
                song=int(song)
                if song not in range(1,11):
                    st.error("incorrect song number")
                else:
                    id=songs.results[int(song)].video_id
                    status2=True

            except ValueError:
                st.error("Enter Song number")    

    elif len(temp)>1 :
        id = temp[1]
        status2 =True
        


    if status2==True and selected_format=="MP3":
        ytObj = functionality.getMP3(id)
        st.write("{} size:{} MB".format(ytObj["title"],ytObj["size"]))
        status3=True
        

        if status3==True:
            
            if st.download_button('Download mp3 file',ytObj["buffer"],file_name=ytObj["name"],mime="audio/mp3"):
                st.success("File is being Downloaded")
        
    if status2==True and selected_format=="MP4":    
        
        try:
            res=st.select_slider('Pick a resolution',["1080p","720p", "480p","360p","240p","144p"])
        except TypeError:
            st.error("Enter video resolution")  

        ytObj = functionality.getMP4(id,res)
        if ytObj:
            st.write("{} | size:{} MB".format(ytObj["title"],ytObj["size"]))
            st.write("Processing your file...")
            status3=True
            
            if status3==True:
                if st.download_button('Download mp4 file',ytObj["buffer"],file_name=ytObj["name"],mime="video/mp4"):
                    st.success("File is Downloaded")
        else:
            st.warning('File Format not available')    

    

if __name__ == '__main__':
	main()
