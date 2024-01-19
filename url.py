#Librería que acorta la URL
#Librería que crea la página web
import pyshorteners
import streamlit as st

def shorten_url(url): #Función que recibe la URL
    s = pyshorteners.Shortener() #Creamos un objeto de esta librería
    shortened_url = s.tinyurl.short(url) #Llamamos al método que nos acorta la URL
    return shortened_url

#creamos app web con stremamlit
#Configuración de la página: título, el ícono y la forma en cómo se verá la página
st.set_page_config(page_title="URL Shortener", page_icon="✏️", layout="centered")
st.image("rosko.jpg", use_column_width=True)
st.title("URL Shortener")
url = st.text_input("Enter the URL")
if st.button("Generate new URL"):
    st.write("URL shortened: ", shorten_url(url))
