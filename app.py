from flask import Flask, render_template
from models import db, MenuItem, SpecialItem
import config


def create_app():
    app = Flask(__name__, static_folder='assets', static_url_path='/assets')
    app.config.from_object(config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from admin_views import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    @app.route('/')
    def index():
        iced_coffee = MenuItem.query.filter_by(category='iced_coffee', is_active=True)\
            .order_by(MenuItem.display_order).all()
        hot_coffee = MenuItem.query.filter_by(category='hot_coffee', is_active=True)\
            .order_by(MenuItem.display_order).all()
        juice = MenuItem.query.filter_by(category='juice', is_active=True)\
            .order_by(MenuItem.display_order).all()
        specials = SpecialItem.query.filter_by(is_active=True)\
            .order_by(SpecialItem.display_order).all()

        return render_template('index.html',
                               iced_coffee=iced_coffee,
                               hot_coffee=hot_coffee,
                               juice=juice,
                               specials=specials)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
