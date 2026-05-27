from pydantic import BaseModel
from typing import Optional

# 注册用
class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[str] = None

# 修改信息用
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

# 返回给前端的用户信息
class UserOut(BaseModel):
    id: int
    username: str
    email: Optional[str] = None

    class Config:
        from_attributes = True