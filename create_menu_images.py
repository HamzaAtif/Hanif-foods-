#!/usr/bin/env python3
"""
Script to create placeholder images for all menu items
"""

import os
from PIL import Image, ImageDraw, ImageFont
import csv

def create_placeholder_image(image_path, text):
    """Create a placeholder image with text"""
    # Create a new image with white background
    width, height = 300, 200
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # Try to use a default font, fall back to default if not available
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", 20)
        except:
            font = ImageFont.load_default()

    # Calculate text position to center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw the text
    draw.text((x, y), text, fill='black', font=font)

    # Save the image
    image.save(image_path)
    print(f"Created placeholder image: {image_path}")

def create_all_menu_images():
    """Create placeholder images for all menu items"""

    # Define all menu items that need images
    menu_images = [
        # BBQ Section
        'bihari-tikka.jpg', 'malai-tikka.jpg', 'balochi-tikka.jpg', 'labneese-boti.jpg',
        'beef-bihari-boti.jpg', 'afghani-boti.jpg', 'chatakh-boti.jpg', 'shashlik-boti.jpg',
        'morican-boti.jpg', 'dhaga-kabab.jpg', 'seekh-kabab.jpg', 'turkish-kabab.jpg',
        'hunzai-kabab.jpg', 'angara-kabab.jpg', 'nalki-kabab.jpg', 'chaska-kabab.jpg',
        'chicken-cheese-kabab.jpg', 'mutton-chanp-grill.jpg', 'prawns-bbq.jpg',
        'grilled-fish.jpg', 'chicken-steam.jpg', 'mutton-steam.jpg',

        # Curries Section
        'qorma.jpg', 'white-qorma.jpg', 'kunna-paya.jpg', 'achar-gosht.jpg',
        'green-stew.jpg', 'hari-mirch-qeema.jpg', 'dum-qeema.jpg', 'palak-paneer.jpg',
        'koftay.jpg', 'shab-daig.jpg', 'beef-karahi.jpg', 'green-karahi.jpg',
        'white-karahi.jpg', 'butter-karahi.jpg', 'tikka-karahi.jpg', 'balochi-karahi.jpg',
        'chicken-makhni-handi.jpg', 'chicken-white-handi.jpg', 'haleem.jpg',

        # Fry Section
        'broast.jpg', 'chargha-broast.jpg', 'chicken-ala-kiev.jpg', 'chicken-cordon-bleu.jpg',
        'fish-biscuit.jpg', 'fish-lahori.jpg', 'prawn-tempura.jpg', 'arabian-puff.jpg',
        'chicken-cheese-strips.jpg', 'toffe-kabab.jpg', 'chapli-kabab.jpg', 'chicken-cheese-cone.jpg',
        'peri-bite.jpg', 'mint-roll.jpg', 'wonton.jpg', 'chicken-beef-samosa.jpg',
        'spring-roll.jpg', 'chicky-micky.jpg', 'chicken-dynamite.jpg', 'chicken-pocket.jpg',
        'chicken-jalapeno.jpg',

        # Chinese Section
        'chicken-chilli.jpg', 'chicken-beef-dry.jpg', 'chicken-jalfrezi.jpg', 'chicken-manchurian.jpg',
        'szehwan-chicken.jpg', 'lemon-chicken.jpg', 'kung-pao-chicken.jpg',

        # Live Cuisine Section
        'koyla-karahi.jpg', 'kashmiri-karahi.jpg', 'shinwari-karahi.jpg', 'mughlai-karahi.jpg',
        'chicken-white-handi.jpg', 'chicken-paneer-reshmi-handi.jpg', 'singapori-rice.jpg',
        'tawa-fish.jpg', 'karakat.jpg',

        # Desserts Section
        'zarda.jpg', 'rabri-kheer.jpg', 'lab-e-shireen.jpg', 'cream-cocktail.jpg',
        'ice-cocktail.jpg', 'cherry-crunch-cocktail.jpg', 'doodh-dulari.jpg',
        'alaska.jpg', 'fruit-trifle.jpg', 'mango-delight-dessert.jpg',
        'shahi-tukra.jpg', 'dessert-bar-continental.jpg', 'pineapple-rassgulla.jpg',
        'gajar-halwa.jpg', 'loki-halwa.jpg', 'dry-fruit-halwa.jpg',
        'rasmalai.jpg', 'gulab-jamun.jpg', 'suji-halwa.jpg',

        # Ice Cream Section
        'roasted-almond-ice-cream.jpg', 'cisilion-ice-cream.jpg', 'strawberry-cheese-cake.jpg',
        'mango-ice-cream.jpg', 'badam-zafran-ice-cream.jpg', 'rose-malai-ice-cream.jpg',
        'gateau-cake-ice-cream.jpg', 'cream-casata-ice-cake.jpg', 'mango-delight-ice-cake.jpg',
        'oreo-delight-ice-cake.jpg', 'temptation-ice-cake.jpg', 'fruit-alaska-ice-cake.jpg',
        'baked-alaska-ice-cake.jpg', 'crunch-kulfi.jpg', 'mango-kulfi.jpg',
        'badam-zafran-kulfi.jpg', 'khoya-kulfi.jpg',

        # Bars Section
        'fruit-bar.jpg', 'salad-bar-12-16-bowls.jpg', 'salad-bar-ice-box.jpg', 'italian-bar.jpg',

        # Dessert Bar Section
        'dessert-bar-8-items.jpg', 'diamond-dessert-bar.jpg', 'sp-dessert-bar.jpg',

        # Refreshments Section
        'chana-chat.jpg', 'dahi-baray.jpg', 'gol-gappay.jpg', 'fresh-juices.jpg',
        'limca-stall.jpg', 'tea-chai.jpg', 'coffee-cappuccino.jpg', 'pan-stall.jpg'
    ]

    # Create the directory if it doesn't exist
    os.makedirs('src/assets/food', exist_ok=True)

    # Create placeholder images for each menu item
    for image_name in menu_images:
        image_path = os.path.join('src/assets/food', image_name)
        if not os.path.exists(image_path):
            # Extract dish name from filename (replace hyphens and extension with spaces)
            dish_name = image_name.replace('.jpg', '').replace('-', ' ').title()
            create_placeholder_image(image_path, dish_name)
        else:
            print(f"Image already exists: {image_path}")

if __name__ == "__main__":
    # Check if PIL is available, if not install it first
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow library not found. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", "Pillow"])
        from PIL import Image, ImageDraw, ImageFont

    create_all_menu_images()
    print("\\nAll placeholder images have been created successfully!")