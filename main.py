from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
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

@app.get("/")
def read_root(condition:Optional[bool]=True):
    if condition:
        return {"message":f"Hello World"}
    else:
        return {"message":f"Goodbye World"}

@app.get("/{id}")
def read_root(id: int):
    return {"message":f"Hello World {id}"}