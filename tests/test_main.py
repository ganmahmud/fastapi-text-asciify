from fastapi.testclient import TestClient
from main import app
from pyfiglet import FigletFont
from json import loads

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.template.name == 'home.html'

def test_raw_api():
    response = client.get("/api/?text=hello&font=standard")
    assert response.status_code == 200
    assert loads(response.content)["text"] == "hello"
    assert loads(response.content)["font"] == "standard"
    assert "art" in loads(response.content)
    assert loads(response.content)["art"] is not None

def test_text_to_ascii():
    response = client.get("/asciify/?text=hello&font=standard")
    assert response.status_code == 200
    assert response.template.name == 'art.html'

def test_font_list():
    response = client.get("/fonts/")
    all_fonts = FigletFont.getFonts()
    assert response.status_code == 200
    assert "acrobatic" in response.text
    
