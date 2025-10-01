movie_manager/
├── app/
│   ├── api/                                 # تمام روترها و اندپوینت‌ها
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── movies.py
│   │       │   └── stats.py
│   │       └── __init__.py
│   ├── core/                        # تنظیمات کلی، config و startup
│   │   └── config.py
│   ├── models/                                # مدل‌های SQLAlchemy
│   │   └── movie.py
│   ├── schemas/                                 # مدل‌های Pydantic
│   │   └── movie.py
│   ├── crud/                                          # عملیات DB
│   │   └── movie.py
│   ├── db/                                        # اتصال به دیتابیس
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   └── main.py                                 # اپ اصلی FastAPI
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
