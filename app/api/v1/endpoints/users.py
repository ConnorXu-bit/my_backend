from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.base import SessionLocal
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.models.user import User
from app.core.security import verify_password, get_password_hash, create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ======================
# 1. 用户注册
# ======================
@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    exist = db.query(User).filter(User.username == user.username).first()
    if exist:
        raise HTTPException(status_code=400, detail="用户名已存在")
    hashed_pwd = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pwd
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ======================
# 2. 用户登录
# ======================
@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form.username).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    access_token_expires = timedelta(minutes=30)
    token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": token, "token_type": "bearer"}

# ======================
# 3. 获取所有用户
# ======================
@router.get("/users", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# ======================
# 4. 根据ID获取单个用户
# ======================
@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user

# ======================
# 5. 修改用户信息
# ======================
@router.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    if user_in.username:
        user.username = user_in.username
    if user_in.email:
        user.email = user_in.email
    if user_in.password:
        user.hashed_password = get_password_hash(user_in.password)
    
    db.commit()
    db.refresh(user)
    return user

# ======================
# 6. 删除用户
# ======================
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    db.delete(user)
    db.commit()
    return {"message": "删除成功"}