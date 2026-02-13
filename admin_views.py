from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db, MenuItem, SpecialItem
import config

admin_bp = Blueprint('admin', __name__, template_folder='templates')


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('password') == config.ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin.dashboard'))
        flash('密碼錯誤 / Wrong password', 'danger')
    return render_template('admin/login.html')


@admin_bp.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin.login'))


@admin_bp.route('/')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')


# --- Menu CRUD ---

@admin_bp.route('/menu')
@login_required
def menu_list():
    items = MenuItem.query.order_by(MenuItem.category, MenuItem.display_order).all()
    return render_template('admin/menu_list.html', items=items)


@admin_bp.route('/menu/add', methods=['GET', 'POST'])
@login_required
def menu_add():
    if request.method == 'POST':
        item = MenuItem(
            category=request.form['category'],
            name_zh=request.form['name_zh'],
            name_en=request.form['name_en'],
            price=int(request.form['price']),
            description_zh=request.form['description_zh'],
            description_en=request.form['description_en'],
            image_path=request.form['image_path'],
            display_order=int(request.form.get('display_order', 0)),
            is_active='is_active' in request.form,
        )
        db.session.add(item)
        db.session.commit()
        flash('已新增菜單項目', 'success')
        return redirect(url_for('admin.menu_list'))
    return render_template('admin/menu_form.html', item=None)


@admin_bp.route('/menu/<int:item_id>/edit', methods=['GET', 'POST'])
@login_required
def menu_edit(item_id):
    item = MenuItem.query.get_or_404(item_id)
    if request.method == 'POST':
        item.category = request.form['category']
        item.name_zh = request.form['name_zh']
        item.name_en = request.form['name_en']
        item.price = int(request.form['price'])
        item.description_zh = request.form['description_zh']
        item.description_en = request.form['description_en']
        item.image_path = request.form['image_path']
        item.display_order = int(request.form.get('display_order', 0))
        item.is_active = 'is_active' in request.form
        db.session.commit()
        flash('已更新菜單項目', 'success')
        return redirect(url_for('admin.menu_list'))
    return render_template('admin/menu_form.html', item=item)


@admin_bp.route('/menu/<int:item_id>/delete', methods=['POST'])
@login_required
def menu_delete(item_id):
    item = MenuItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('已刪除菜單項目', 'success')
    return redirect(url_for('admin.menu_list'))


# --- Specials CRUD ---

@admin_bp.route('/specials')
@login_required
def specials_list():
    items = SpecialItem.query.order_by(SpecialItem.display_order).all()
    return render_template('admin/specials_list.html', items=items)


@admin_bp.route('/specials/add', methods=['GET', 'POST'])
@login_required
def specials_add():
    if request.method == 'POST':
        item = SpecialItem(
            name_zh=request.form['name_zh'],
            name_en=request.form['name_en'],
            price=int(request.form['price']) if request.form.get('price') else None,
            description_zh=request.form['description_zh'],
            description_en=request.form['description_en'],
            image_path=request.form['image_path'],
            display_order=int(request.form.get('display_order', 0)),
            is_active='is_active' in request.form,
        )
        db.session.add(item)
        db.session.commit()
        flash('已新增特色項目', 'success')
        return redirect(url_for('admin.specials_list'))
    return render_template('admin/specials_form.html', item=None)


@admin_bp.route('/specials/<int:item_id>/edit', methods=['GET', 'POST'])
@login_required
def specials_edit(item_id):
    item = SpecialItem.query.get_or_404(item_id)
    if request.method == 'POST':
        item.name_zh = request.form['name_zh']
        item.name_en = request.form['name_en']
        item.price = int(request.form['price']) if request.form.get('price') else None
        item.description_zh = request.form['description_zh']
        item.description_en = request.form['description_en']
        item.image_path = request.form['image_path']
        item.display_order = int(request.form.get('display_order', 0))
        item.is_active = 'is_active' in request.form
        db.session.commit()
        flash('已更新特色項目', 'success')
        return redirect(url_for('admin.specials_list'))
    return render_template('admin/specials_form.html', item=item)


@admin_bp.route('/specials/<int:item_id>/delete', methods=['POST'])
@login_required
def specials_delete(item_id):
    item = SpecialItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('已刪除特色項目', 'success')
    return redirect(url_for('admin.specials_list'))
