# FastAPI 用户管理系统
一个基于 FastAPI 开发的完整用户管理后端项目，包含注册、登录、增删改查全套功能。

## 功能列表
- ✅ 用户注册
- ✅ 用户登录（JWT 身份认证）
- ✅ 获取所有用户
- ✅ 获取单个用户信息
- ✅ 修改用户资料
- ✅ 删除用户
- ✅ 密码加密存储
- ✅ 自动生成接口文档

## 技术栈
- FastAPI
- SQLAlchemy
- SQLite
- JWT
- Python

## 启动方式
```bash
# 激活虚拟环境
source venv/bin/activate

# 启动项目
uvicorn main:app --reload

访问接口文档
http://127.0.0.1:8000/docs
项目结构
plaintext
my_backend/
├── main.py
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   └── schemas/
└── README.md
