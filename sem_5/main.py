import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = []


class Movie(BaseModel):
    id_: int
    title: str
    description: str
    genre: str


movies.append(Movie(id_=1,
                    title='Sing 2',
                    description='It s hard to be a producer when you re a koala and have paws',
                    genre='animation'))
movies.append(Movie(id_=2,
                    title='Iron Man',
                    description='Billionaire inventor Tony Stark is captured by Afghan terrorists',
                    genre='action'))

movies.append(Movie(id_=3,
                    title='avatar2',
                    description='After taking on the avatar identity of soldier Jake '
                                'Sully, he becomes the leader of the Navi people.',
                    genre='fantasy'))


@app.get('/movies/')
async def all_movies():
    return {'movies': movies}


@app.post('/movie/add')
async def add_movie(movie: Movie):
    movies.append(movie)
    return {"movie": movie, "status": "added"}


@app.get('/movies/{genre}')
async def get_movies_by_genre(genre: str):
    tmp = []
    for m in movies:
        if m.genre == genre:
            tmp.append(m)
        if not tmp:
            raise HTTPException(404, 'Genre not found')
        return {'movies': tmp}


@app.put('/movie/update/{movie_id}')
async def update_movie(movie_id: int, movie: Movie):
    for m in movies:
        if m.id_ == movie_id:
            m.title = movie.title
            m.description = movie.description
            m.genre = movie.genre
            return {"movie": movie, "status": "updated"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080)
