# 这是项目最终的主入口
from fastapi import FastAPI
from app.db.base import Base, engine
from app.api.v1.endpoints.users import router as user_router

# 创建数据库表（自动执行）
Base.metadata.create_all(bind=engine)

# 创建 FastAPI 应用
app = FastAPI(
    title="简历级用户管理系统",
    description="FastAPI + 分层架构",
    version="1.0.0"
)

# 加载所有接口
app.include_router(user_router)

# 首页测试
@app.get("/")
def home():
    return {"message": "✅ 项目启动成功！"}