from pathlib import Path
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import crud

#from app.config import DATABASE_URL

Base.metadata.create_all(bind=engine)

app = FastAPI()
#app = FastAPI(docs_url=None, redoc_url=None) # use if you want to disable /docs and /redoc urls

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

templates = Jinja2Templates(directory="app/templates")


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    ads = crud.get_ads(db)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "ads": ads,
        },
    )


@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={
            "request": request,
            #"database_url": DATABASE_URL,
        },
    )


@app.get("/create", response_class=HTMLResponse)
def create_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="create.html",
        context={
            "request": request,
        },
    )


@app.post("/create")
def create_ad(
    title: str = Form(...),
    description: str = Form(...),
    price: str = Form(...),
    db: Session = Depends(get_db),
):
    crud.create_ad(db, title, description, price)

    return RedirectResponse(url="/", status_code=303)


@app.get("/edit/{ad_id}", response_class=HTMLResponse)
def edit_page(
    ad_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    ad = crud.get_ad(db, ad_id)

    return templates.TemplateResponse(
        request=request,
        name="edit.html",
        context={
            "request": request,
            "ad": ad,
        },
    )


@app.post("/edit/{ad_id}")
def edit_ad(
    ad_id: int,
    title: str = Form(...),
    description: str = Form(...),
    price: str = Form(...),
    db: Session = Depends(get_db),
):
    crud.update_ad(db, ad_id, title, description, price)

    return RedirectResponse(url="/", status_code=303)


@app.post("/delete/{ad_id}")
def delete_ad(
    ad_id: int,
    db: Session = Depends(get_db),
):
    crud.delete_ad(db, ad_id)

    return RedirectResponse(url="/", status_code=303)


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(str(static_dir / "favicon.ico"), media_type="image/x-icon")
