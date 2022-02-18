import datetime
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pyfiglet import Figlet, FigletFont

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

@app.get("/api/greet")
async def ascii_greet(request: Request, text: str = "", font: str = "standard"):
    hour = datetime.datetime.now().hour
    greeting = "Good morning" if 5<=hour<12 else "Good afternoon" if hour<18 else "Good evening"
    ascii_art = Figlet(font=font).renderText(greeting + ' , ' + text)
    # return templates.TemplateResponse("art.html",{"request": request, "art" : ascii_art})
    return {"font" : font, "art" : ascii_art}

@app.get("/fonts/")
async def get_fonts(request: Request, text: str = "ASCII ART"):
    fonts = FigletFont.getFonts()
    res = []
    for font in fonts:
        out_dict = {}
        out_dict["font"] = font
        out_dict["art"] = Figlet(font=font).renderText(text)
        res.append(out_dict)
    
    return templates.TemplateResponse("fonts.html",{"request": request, "text" : text, "font_list" : res})

if __name__ == "__main__":
        uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, log_level="info")