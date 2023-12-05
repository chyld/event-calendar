import sqlite3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


class Note(BaseModel):
    note: str
    cal: str
    color: str
    graphic: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Specifies the allowed origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.post("/events/new")
def create_event(note: Note):
    print("the note:", note)
    create_event_db(note)
    return {"item_id": 3}


def create_event_db(note: Note):
    con = sqlite3.connect("./data/database.sqlite")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO notes (note, cal, color, graphic) VALUES(?, ?, ?, ?)",
        (note.note, note.cal, note.color, note.graphic),
    )
    con.commit()
    con.close()
