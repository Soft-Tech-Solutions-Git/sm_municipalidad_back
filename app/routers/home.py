from app import bp

@bp.route('/')
def index():
    print('Hola')