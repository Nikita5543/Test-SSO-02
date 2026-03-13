def register(app, router):
    from .endpoints import router as plugin_router
    app.include_router(plugin_router, prefix="/api/v1/plugins/monitoring")
    print("🔌 Плагин 'monitoring' зарегистрирован")