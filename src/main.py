from fastapi import FastAPI

import services as _services

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Welcome'}

@app.get('/events')
async def all_events():
    return _services.get_all_events()

@app.get('/events/{month}')
async def get_events_of_month(month: str):
    return _services.get_month_events(month)

@app.get('/events/today')
async def get_events_of_today():
    return _services.get_events_of_today()

@app.get('/events/{month}/{day}')
async def get_events_of_the_day(month: str, day: int):
    return _services.get_day_events(month, day)