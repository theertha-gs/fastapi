from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv
load_dotenv()
key=os.getenv("GEMINI_API_KEY")
app=FastAPI()
'''curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'''
class A(BaseModel):
    text: str

class B(BaseModel):
    parts: List[A]

class C(BaseModel):
    contents: List[B]


@app.get("/")
def read_root(condition:Optional[bool]=True):
    if condition:
        return {"message":f"Hello World"}
    else:
        return {"message":f"Goodbye World"}

@app.get("/{id}")
def read_root(id: int):
    return {"message":f"Hello World {id}"}

@app.post("/ask")
def ask(ques: C):
    response= requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}",json=ques.model_dump())
    answer=response.json()
    return answer["candidates"][0]["content"]["parts"][0]["text"]