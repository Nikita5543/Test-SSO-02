from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.core.database import init_db
import importlib
import os

app = FastAPI(title="NetOps API", docs_url="/docs")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение основных маршрутов
app.include_router(api_router, prefix="/api/v1")

# Автоматическая регистрация плагинов
PLUGIN_DIR = os.path.join(os.path.dirname(__file__), "plugins")

def load_plugins():
    for entry in os.listdir(PLUGIN_DIR):
        plugin_path = os.path.join(PLUGIN_DIR, entry)
        if os.path.isdir(plugin_path) and "__pycache__" not in entry:
            try:
                spec = importlib.util.spec_from_file_location(
                    f"app.plugins.{entry}.plugin", os.path.join(plugin_path, "plugin.py")
                )
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    if hasattr(module, "register"):
                        module.register(app, api_router)
                        print(f"✅ Плагин '{entry}' успешно загружен")
            except Exception as e:
                print(f"❌ Ошибка загрузки плагина {entry}: {e}")

@app.on_event("startup")
async def startup_event():
    await init_db()
    load_plugins()

@app.get("/")
def root():
    return {"message": "Welcome to NetOps System"}