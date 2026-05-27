from pydantic import BaseModel

# 注册入参
class UserRegister(BaseModel):
    username: str
    password: str
    email: str | None = None

# 用户信息返回
class UserInfo(BaseModel):
    id: int
    username: str
    email: str | None

    class Config:
        from_attributes = True

# 修改信息入参
class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None