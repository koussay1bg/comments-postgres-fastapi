from fastapi import FastAPI
import psycopg2 

conn = psycopg2.connect(
    host="localhost",
    database="comments",
    user="postgres",
    password="0000"
)
cur = conn.cursor()

app = FastAPI()

# Save new comment to the database
@app.post("/comments")
async def save_comment(id: int ,comment: str, sentiment: str):
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO comments (id, comment, sentiment) VALUES (%s,%s, %s)", (id,comment, sentiment))
            conn.commit()
        return {"success": True, "message": "Comment saved successfully."}
    except Exception as e:
        print(f"Unable to save comment: {e}")
        return {"success": False, "message": "Error saving comment."}

# Search for comments containing keywords
@app.get("/search")
async def search_comments(q: str):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM comments WHERE comment LIKE %s", ('%' + q + '%',))
            comments =  cur.fetchall()
        return {"success": True, "comments": comments}
    except Exception as e:
        print(f"Unable to search for comments: {e}")
        return {"success": False, "message": "Error searching for comments."}


# Delete comment from the database
@app.delete("/comments")
async def delete_comment(id):
    try:
        with conn.cursor() as cur:
             cur.execute("DELETE FROM comments WHERE id = %s", (id))
        return {"success": True, "message": "Comment deleted successfully."}
    except Exception as e:
        print(f"Unable to delete comment: {e}")
        return {"success": False, "message": "Error deleting comment."}
    
# Update sentiment for existing comment
@app.put("/comments/{id}")
async def update_comment(id: int, comment: str, sentiment: str):
    try:
        with conn.cursor() as cur:
             cur.execute("UPDATE comments SET comment=%s, sentiment=%s WHERE id=%s", (comment, sentiment, id))
        return {"success": True, "message": "Comment updated successfully."}
    except Exception as e:
        print(f"Unable to update comment: {e}")
        return {"success": False, "message": "Error updating comment."}
 