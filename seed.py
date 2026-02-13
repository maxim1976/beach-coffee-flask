from app import create_app
from models import db, MenuItem, SpecialItem

app = create_app()

MENU_ITEMS = [
    # Iced Coffee
    dict(category='iced_coffee', name_zh='冰美式咖啡', name_en='Iced Americano', price=80,
         description_zh='冰鎮美式，口感清爽，適合炎熱天氣享用。',
         description_en='Refreshing iced Americano, perfect for hot weather.',
         image_path='iced-americano.png', display_order=1),
    dict(category='iced_coffee', name_zh='冰卡布奇諾', name_en='Iced Cappuccino', price=90,
         description_zh='濃郁奶泡搭配冰鎮咖啡，層次豐富。',
         description_en='Rich foam paired with iced coffee, layered flavors.',
         image_path='iced-cappuccino.png', display_order=2),
    dict(category='iced_coffee', name_zh='冰濃縮咖啡', name_en='Iced Espresso', price=70,
         description_zh='純正濃縮咖啡，冰鎮後更顯醇厚風味。',
         description_en='Pure espresso on ice, bold and rich flavor.',
         image_path='iced-espresso.png', display_order=3),
    dict(category='iced_coffee', name_zh='冰拿鐵', name_en='Iced Latte', price=90,
         description_zh='香醇牛奶與冰咖啡的完美結合。',
         description_en='A perfect blend of smooth milk and iced coffee.',
         image_path='iced-latte.png', display_order=4),
    # Hot Coffee
    dict(category='hot_coffee', name_zh='熱美式咖啡', name_en='Hot Americano', price=70,
         description_zh='經典美式，純粹的咖啡風味。',
         description_en='Classic Americano, pure coffee flavor.',
         image_path='hot-americano.png', display_order=1),
    dict(category='hot_coffee', name_zh='熱卡布奇諾', name_en='Hot Cappuccino', price=85,
         description_zh='細緻奶泡與濃郁咖啡的經典組合。',
         description_en='Delicate foam with rich coffee, a classic combo.',
         image_path='hot-cappuccino.png', display_order=2),
    dict(category='hot_coffee', name_zh='熱濃縮咖啡', name_en='Hot Espresso', price=60,
         description_zh='小杯濃縮，感受最純粹的咖啡香氣。',
         description_en='A small cup of espresso, the purest coffee aroma.',
         image_path='hot-espresso.png', display_order=3),
    dict(category='hot_coffee', name_zh='熱拿鐵', name_en='Hot Latte', price=85,
         description_zh='溫潤牛奶與香醇咖啡的溫暖搭配。',
         description_en='Warm milk and aromatic coffee, a cozy pairing.',
         image_path='hot-latte.png', display_order=4),
    # Juice
    dict(category='juice', name_zh='草莓冰沙', name_en='Strawberry Smoothie', price=100,
         description_zh='新鮮草莓現打，酸甜可口。',
         description_en='Freshly blended strawberries, sweet and tangy.',
         image_path='smoothie-1.png', display_order=1),
    dict(category='juice', name_zh='綜合莓果冰沙', name_en='Mixed Berry Smoothie', price=100,
         description_zh='多種莓果混合，富含維他命。',
         description_en='A blend of mixed berries, rich in vitamins.',
         image_path='smoothie-2.png', display_order=2),
    dict(category='juice', name_zh='鳳梨冰沙', name_en='Pineapple Smoothie', price=95,
         description_zh='花蓮在地鳳梨，香甜清爽。',
         description_en='Local Hualien pineapple, sweet and refreshing.',
         image_path='smoothie-3.png', display_order=3),
    dict(category='juice', name_zh='菠菜綠拿鐵', name_en='Spinach Green Latte', price=95,
         description_zh='菠菜搭配蘋果，營養健康好選擇。',
         description_en='Spinach with apple, a nutritious and healthy choice.',
         image_path='smoothie-4.png', display_order=4),
]

SPECIAL_ITEMS = [
    dict(name_zh='主廚特調', name_en="Chef's Special", price=120,
         description_zh='主廚精心調配的獨家飲品，每日限量供應，錯過不再。',
         description_en="An exclusive drink crafted by our chef, limited daily — don't miss out.",
         image_path='special-01.jpg', display_order=1),
    dict(name_zh='季節限定', name_en='Seasonal Limited', price=150,
         description_zh='依照時令食材製作，品嚐當季最鮮美的滋味。',
         description_en='Made with seasonal ingredients, taste the freshest flavors of the season.',
         image_path='special-02.jpg', display_order=2),
    dict(name_zh='花蓮特選', name_en='Hualien Selection', price=180,
         description_zh='選用花蓮在地優質食材，呈現道地風味。',
         description_en='Premium local Hualien ingredients, authentic local flavors.',
         image_path='special-03.jpg', display_order=3),
    dict(name_zh='手作甜點', name_en='Handmade Desserts', price=90,
         description_zh='每日新鮮手作，搭配咖啡最對味。',
         description_en='Freshly handmade daily, the perfect pairing with coffee.',
         image_path='special-04.jpg', display_order=4),
    dict(name_zh='在地風味', name_en='Local Flavors', price=160,
         description_zh='結合花蓮特色，創造獨一無二的味覺體驗。',
         description_en="Combining Hualien's unique character to create a one-of-a-kind taste experience.",
         image_path='special-05.jpg', display_order=5),
    dict(name_zh='經典組合', name_en='Classic Combo', price=200,
         description_zh='人氣飲品搭配精選點心，超值享受。',
         description_en='Popular drinks paired with selected pastries, great value.',
         image_path='special-06.jpg', display_order=6),
]


def seed():
    with app.app_context():
        if MenuItem.query.first():
            print('Menu items already exist, skipping seed.')
        else:
            for data in MENU_ITEMS:
                db.session.add(MenuItem(**data))
            db.session.commit()
            print(f'Seeded {len(MENU_ITEMS)} menu items.')

        if SpecialItem.query.first():
            # Re-seed specials to update prices
            SpecialItem.query.delete()
            db.session.commit()
            for data in SPECIAL_ITEMS:
                db.session.add(SpecialItem(**data))
            db.session.commit()
            print(f'Re-seeded {len(SPECIAL_ITEMS)} special items with prices.')
        else:
            for data in SPECIAL_ITEMS:
                db.session.add(SpecialItem(**data))
            db.session.commit()
            print(f'Seeded {len(SPECIAL_ITEMS)} special items.')


if __name__ == '__main__':
    seed()
