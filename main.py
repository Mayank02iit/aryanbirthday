from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
from fastapi.staticfiles import StaticFiles
app.mount("/birthdayboyy", StaticFiles(directory=r"C:\Users\Mayank\Desktop\aryanbirthday\project\static",html=True), name="firstpage")
app.mount('/aryan_my_nigga',StaticFiles(directory=r"C:\Users\Mayank\Desktop\aryanbirthday\project\first_page",html=True), name="secondpage")

