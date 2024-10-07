from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import os 
import yt_dlp
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credential=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



cur_dir = os.getcwd()
@app.post("/download")
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(cur_dir,"abc.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return{"status": "Download started"}
download_video("https://youtu.be/DMIXJdibM_k?si=DrFza8tDO9_zCEGH")

