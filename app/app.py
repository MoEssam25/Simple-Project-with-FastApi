from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse


app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "Second Post", "content": "another test post"},
    3: {"title": "Hello World", "content": "my first blog entry"},
    4: {"title": "FastAPI Tips", "content": "use Pydantic models for validation"},
    5: {"title": "Python Notes", "content": "dicts are great for quick prototypes"},
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="page not found")
    return text_posts.get(id)


# This will enhance the doc of fastAPI cuz it knows what will be returned
# But here why I made it "-> PostResponse:" not "-> PostCreate:"
@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post


