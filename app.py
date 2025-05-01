import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Conversión de Texto a Audio")
image = Image.open('gato_raton.png')
st.image(image, width=350)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("El zorro y las uvas.")
st.write('Una cálida tarde de verano, un zorro caminaba por el bosque buscando algo para comer. Tras horas de vagar sin suerte, sintió que el hambre le apretaba el estómago. Justo cuando estaba a punto de rendirse, vio a lo lejos un hermoso racimo de uvas moradas colgando de una parra alta, madura y llena de hojas verdes.

El zorro se relamió los labios y se acercó rápidamente. Las uvas se veían jugosas, brillaban bajo el sol y parecían ser justo lo que necesitaba. Se preparó, tomó impulso y saltó... pero no alcanzó. Lo intentó una y otra vez, dando brincos cada vez más altos, incluso se trepó a un tronco cercano para tener más ventaja, pero todo fue inútil. Las uvas estaban demasiado altas.

Agotado, el zorro se sentó en el suelo jadeando. Miró de nuevo el racimo, suspiró, y se levantó murmurando con desdén:
—¡Bah! Ni que valieran tanto... seguro estaban verdes y agrias. No me interesaban de verdad.

Y se alejó cojeando lentamente, ocultando su decepción bajo un velo de orgullo.

Moraleja:
Muchas veces despreciamos lo que no podemos conseguir, no porque no lo deseemos, sino porque no queremos admitir nuestra incapacidad para lograrlo.'
        
        )
           
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
