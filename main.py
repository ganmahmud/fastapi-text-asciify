import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pyfiglet import Figlet, FigletFont
# from typing import Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    home_art = Figlet(font="standard").renderText("ASCII ART API")
    return templates.TemplateResponse("home.html",{"request": request, "home_art": home_art})

@app.get("/api/")
async def asciify_api(text: str = "ASCII ART", font: str = "standard"):
    ascii_art = Figlet(font=font).renderText(text)
    return {"text" : text, "font" : font, "art" : ascii_art}

@app.get("/asciify/")
async def text_to_ascii(request: Request, text: str = "ASCII ART", font: str = "standard"):
    ascii_art = Figlet(font=font).renderText(text)
    return templates.TemplateResponse("art.html",{"request": request, "art" : ascii_art})

@app.get("/fonts/")
async def get_fonts(request: Request):
    fonts = FigletFont.getFonts()
    return templates.TemplateResponse("fonts.html",{"request": request, "font_list" : fonts})

if __name__ == "__main__":
        uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True, log_level="info")