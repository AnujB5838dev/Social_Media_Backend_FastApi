from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas, oauth2
from typing import Optional, List
from sqlalchemy import func


router = APIRouter(prefix="/posts", tags=['Posts'])



# @router.get("/",response_model=List[schemas.PostOut])
@router.get("/",response_model=List[schemas.PostOut])
def get_post(db:Session=Depends(get_db),current_user: int = Depends(oauth2.get_current_user), limit : int = 10, skip: int = 0, search : Optional[str] = ""):
    # cursor.execute("""SELECT * FROM  posts""")
    # posts = cursor.fetchall()
    # print(posts)
    # post = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()   #this lines of code is to make post private 
    print(limit)
    # post = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()  
    posts = db.query(models.Post, func.count(models.Votes.post_id).label('votes')).join(models.Votes, models.Votes.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # print(results)
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # print(post)
    # print(post.title)
    # print(post.content)
    # print(post.published)
    # print(post.model_dump())
    # post_dict = post.model_dump()
    # post_dict['id'] = randrange(0,1000000)
    # my_post.append(post_dict) 

    
    # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """, (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # print(new_post)



    # new_post = models.Post(title=post.title,content=post.content, published = post.published)
    print(current_user)
    new_post = models.Post( owner_id = current_user.id ,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id:int, db:Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):  #here response ab needed nhi hai bcoz httpexpception use kar rhe hai
    
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    # post = cursor.fetchone()
    # print(post)
    # post = find_post(id)
    # print(post)

    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Votes.post_id).label('votes')).join(models.Votes, models.Votes.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    # print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"message":f'Post with id {id} was not found'}


    # if post.owner_id != current_user.id:        #this lines of code is to make post private 
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorize to perform requested action")
    return post






@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int ,db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} was not found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorize to perform requested action")
    post_query.delete(synchronize_session = False )
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
 






@router.put("/{id}", response_model=schemas.Post)
def update_post(id:int, updated_post : schemas.PostCreate, db:Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published=%s WHERE id = %s RETURNING * """, (post.title,post.content,post.published,str(id),))
    # Updated_post = cursor.fetchone()
    # conn.commit()
    # print(Updated_post)

    post_query = db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} was not found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorize to perform requested action")

    
    post_query.update(updated_post.model_dump(),synchronize_session= False)
    db.commit()
    # db.refresh(post_query)
    # post_dict = post.model_dump()
    # post_dict['id'] = id 
    # my_post[index] = post_dict
    return post_query.first()

























