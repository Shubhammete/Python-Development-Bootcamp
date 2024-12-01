from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True # Here we explicitly tell to give value true if not given by user so it will not give error of missing
    rating: int = None # This is optional 

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Body is used for getting the post data. We get all data in form of dictonary here
# issue here is frontend user can send any type of data and to tackle this we use pydantic base model
@app.post("/createPost")
async def createPost(newPosts: Post):
    print(newPosts) # title='Top hackers in Akurdi' content='All failed in infront of Shubham' published=True rating=None
    print(newPosts.dict()) # {'title': 'Top hackers in Akurdi', 'content': 'All failed in infront of Shubham', 'published': True, 'rating': None}
    return f"{newPosts.title} : {newPosts.content}"
# async def createPost(data: dict = Body(...)):
#     print(data)
#     return {"new Post": f"title: {data["title"]} and content {data["content"]}"}
