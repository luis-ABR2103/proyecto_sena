from .aprendiz_bp import aprendiz_bp

def CargarRutas(app):
    app.register_blueprint(aprendiz_bp)