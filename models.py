from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)  # iced_coffee, hot_coffee, juice
    name_zh = db.Column(db.String(100), nullable=False)
    name_en = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description_zh = db.Column(db.String(500), nullable=False)
    description_en = db.Column(db.String(500), nullable=False)
    image_path = db.Column(db.String(200), nullable=False)
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<MenuItem {self.name_zh}>'


class SpecialItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_zh = db.Column(db.String(100), nullable=False)
    name_en = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=True)
    description_zh = db.Column(db.String(500), nullable=False)
    description_en = db.Column(db.String(500), nullable=False)
    image_path = db.Column(db.String(200), nullable=False)
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<SpecialItem {self.name_zh}>'
