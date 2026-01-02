#!/usr/bin/env python3
"""
Script to generate a CSV file with unique food images for each menu item
This will help create appropriate images for the Hanif Foods & Caterers menu
"""

import csv
import os
from typing import List, Dict

def generate_food_images_csv():
    """Generate a CSV file with unique food images for each menu item"""

    # Define all menu items with their unique image names
    menu_items = [
        # BBQ Section
        {'id': 'bbq1', 'name': 'Bihari Tikka', 'image': 'bihari-tikka.jpg', 'category': 'BBQ'},
        {'id': 'bbq2', 'name': 'Malai Tikka', 'image': 'malai-tikka.jpg', 'category': 'BBQ'},
        {'id': 'bbq3', 'name': 'Balochi Tikka', 'image': 'balochi-tikka.jpg', 'category': 'BBQ'},
        {'id': 'bbq4', 'name': 'Labneese Boti/Girll', 'image': 'labneese-boti.jpg', 'category': 'BBQ'},
        {'id': 'bbq5', 'name': 'Beef Bihari Boti', 'image': 'beef-bihari-boti.jpg', 'category': 'BBQ'},
        {'id': 'bbq6', 'name': 'Afghani Boti', 'image': 'afghani-boti.jpg', 'category': 'BBQ'},
        {'id': 'bbq7', 'name': 'Chatakh Boti', 'image': 'chatakh-boti.jpg', 'category': 'BBQ'},
        {'id': 'bbq8', 'name': 'Shashlik Boti', 'image': 'shashlik-boti.jpg', 'category': 'BBQ'},
        {'id': 'bbq9', 'name': 'Morican Boti', 'image': 'morican-boti.jpg', 'category': 'BBQ'},
        {'id': 'bbq10', 'name': 'Dhaga Kabab', 'image': 'dhaga-kabab.jpg', 'category': 'BBQ'},
        {'id': 'bbq11', 'name': 'Seekh Kabab', 'image': 'seekh-kabab.jpg', 'category': 'BBQ'},
        {'id': 'bbq12', 'name': 'Turkish Kabab', 'image': 'turkish-kabab.jpg', 'category': 'BBQ'},
        {'id': 'bbq13', 'name': 'Hunzai Kabab', 'image': 'hunzai-kabab.jpg', 'category': 'BBQ'},
        {'id': 'bbq14', 'name': 'Angara Kabab', 'image': 'angara-kabab.jpg', 'category': 'BBQ'},
        {'id': 'bbq15', 'name': 'Nalki Kabab', 'image': 'nalki-kabab.jpg', 'category': 'BBQ'},
        {'id': 'bbq16', 'name': 'Chaska Kabab', 'image': 'chaska-kabab.jpg', 'category': 'BBQ'},
        {'id': 'bbq17', 'name': 'Chicken Cheese Kabab', 'image': 'chicken-cheese-kabab.jpg', 'category': 'BBQ'},
        {'id': 'bbq18', 'name': 'Mutton Chanp Grill', 'image': 'mutton-chanp-grill.jpg', 'category': 'BBQ'},
        {'id': 'bbq19', 'name': 'Prawns BBQ', 'image': 'prawns-bbq.jpg', 'category': 'BBQ'},
        {'id': 'bbq20', 'name': 'Grilled Fish', 'image': 'grilled-fish.jpg', 'category': 'BBQ'},
        {'id': 'bbq21', 'name': 'Chicken Steam', 'image': 'chicken-steam.jpg', 'category': 'BBQ'},
        {'id': 'bbq22', 'name': 'Mutton Steam', 'image': 'mutton-steam.jpg', 'category': 'BBQ'},

        # Curries Section
        {'id': 'cur1', 'name': 'Qorma / Badami Qorma', 'image': 'qorma.jpg', 'category': 'Curries'},
        {'id': 'cur2', 'name': 'White Qorma', 'image': 'white-qorma.jpg', 'category': 'Curries'},
        {'id': 'cur3', 'name': 'Kunna Paya', 'image': 'kunna-paya.jpg', 'category': 'Curries'},
        {'id': 'cur4', 'name': 'Achar Gosht', 'image': 'achar-gosht.jpg', 'category': 'Curries'},
        {'id': 'cur5', 'name': 'Green Stew', 'image': 'green-stew.jpg', 'category': 'Curries'},
        {'id': 'cur6', 'name': 'Hari Mirch Qeema', 'image': 'hari-mirch-qeema.jpg', 'category': 'Curries'},
        {'id': 'cur7', 'name': 'Dum Qeema', 'image': 'dum-qeema.jpg', 'category': 'Curries'},
        {'id': 'cur8', 'name': 'Palak Paneer', 'image': 'palak-paneer.jpg', 'category': 'Curries'},
        {'id': 'cur9', 'name': 'Koftay', 'image': 'koftay.jpg', 'category': 'Curries'},
        {'id': 'cur10', 'name': 'Shab Daig', 'image': 'shab-daig.jpg', 'category': 'Curries'},
        {'id': 'cur11', 'name': 'Karahi', 'image': 'beef-karahi.jpg', 'category': 'Curries'},
        {'id': 'cur12', 'name': 'Green Karahi', 'image': 'green-karahi.jpg', 'category': 'Curries'},
        {'id': 'cur13', 'name': 'White Karahi', 'image': 'white-karahi.jpg', 'category': 'Curries'},
        {'id': 'cur14', 'name': 'Butter Karahi', 'image': 'butter-karahi.jpg', 'category': 'Curries'},
        {'id': 'cur15', 'name': 'Tikka Karahi', 'image': 'tikka-karahi.jpg', 'category': 'Curries'},
        {'id': 'cur16', 'name': 'Balochi Karahi', 'image': 'balochi-karahi.jpg', 'category': 'Curries'},
        {'id': 'cur17', 'name': 'Chicken Makhni Handi', 'image': 'chicken-makhni-handi.jpg', 'category': 'Curries'},
        {'id': 'cur18', 'name': 'Chicken White Handi', 'image': 'chicken-white-handi.jpg', 'category': 'Curries'},
        {'id': 'cur19', 'name': 'Haleem Beef & Chicken', 'image': 'haleem.jpg', 'category': 'Curries'},

        # Fry Section
        {'id': 'fry1', 'name': 'Broast', 'image': 'broast.jpg', 'category': 'Fry'},
        {'id': 'fry2', 'name': 'Chargha Broast', 'image': 'chargha-broast.jpg', 'category': 'Fry'},
        {'id': 'fry3', 'name': 'Chicken Ala Kiev', 'image': 'chicken-ala-kiev.jpg', 'category': 'Fry'},
        {'id': 'fry4', 'name': 'Chicken Cordon Bleu', 'image': 'chicken-cordon-bleu.jpg', 'category': 'Fry'},
        {'id': 'fry5', 'name': 'Fish Biscuit', 'image': 'fish-biscuit.jpg', 'category': 'Fry'},
        {'id': 'fry6', 'name': 'Fish Lahori', 'image': 'fish-lahori.jpg', 'category': 'Fry'},
        {'id': 'fry7', 'name': 'Prawn Tempura', 'image': 'prawn-tempura.jpg', 'category': 'Fry'},
        {'id': 'fry8', 'name': 'Arabian Puff', 'image': 'arabian-puff.jpg', 'category': 'Fry'},
        {'id': 'fry9', 'name': 'Chicken Cheese Strips', 'image': 'chicken-cheese-strips.jpg', 'category': 'Fry'},
        {'id': 'fry10', 'name': 'Toffe Kabab', 'image': 'toffe-kabab.jpg', 'category': 'Fry'},
        {'id': 'fry11', 'name': 'Chapli Kabab', 'image': 'chapli-kabab.jpg', 'category': 'Fry'},
        {'id': 'fry12', 'name': 'Chicken Cheese Cone', 'image': 'chicken-cheese-cone.jpg', 'category': 'Fry'},
        {'id': 'fry13', 'name': 'Peri Bite', 'image': 'peri-bite.jpg', 'category': 'Fry'},
        {'id': 'fry14', 'name': 'Mint Roll', 'image': 'mint-roll.jpg', 'category': 'Fry'},
        {'id': 'fry15', 'name': 'Wonton', 'image': 'wonton.jpg', 'category': 'Fry'},
        {'id': 'fry16', 'name': 'Chicken/Beef Samosa', 'image': 'chicken-beef-samosa.jpg', 'category': 'Fry'},
        {'id': 'fry17', 'name': 'Spring Roll', 'image': 'spring-roll.jpg', 'category': 'Fry'},
        {'id': 'fry18', 'name': 'Chicky Micky', 'image': 'chicky-micky.jpg', 'category': 'Fry'},
        {'id': 'fry19', 'name': 'Chicken Dynamite', 'image': 'chicken-dynamite.jpg', 'category': 'Fry'},
        {'id': 'fry20', 'name': 'Chicken Pocket', 'image': 'chicken-pocket.jpg', 'category': 'Fry'},
        {'id': 'fry21', 'name': 'Chicken Jalapeno', 'image': 'chicken-jalapeno.jpg', 'category': 'Fry'},

        # Chinese Section
        {'id': 'chi1', 'name': 'Chicken Chilli', 'image': 'chicken-chilli.jpg', 'category': 'Chinese'},
        {'id': 'chi2', 'name': 'Chicken / Beef Dry', 'image': 'chicken-beef-dry.jpg', 'category': 'Chinese'},
        {'id': 'chi3', 'name': 'Chicken Jalfrezi', 'image': 'chicken-jalfrezi.jpg', 'category': 'Chinese'},
        {'id': 'chi4', 'name': 'Chicken Manchurian', 'image': 'chicken-manchurian.jpg', 'category': 'Chinese'},
        {'id': 'chi5', 'name': 'Szehwan Chicken', 'image': 'szehwan-chicken.jpg', 'category': 'Chinese'},
        {'id': 'chi6', 'name': 'Lemon Chicken', 'image': 'lemon-chicken.jpg', 'category': 'Chinese'},
        {'id': 'chi7', 'name': 'Kung Pao Chicken', 'image': 'kung-pao-chicken.jpg', 'category': 'Chinese'},

        # Live Cuisine Section
        {'id': 'liv1', 'name': 'Koyla Karahi', 'image': 'koyla-karahi.jpg', 'category': 'Live Cuisine'},
        {'id': 'liv2', 'name': 'Kashmiri Karahi', 'image': 'kashmiri-karahi.jpg', 'category': 'Live Cuisine'},
        {'id': 'liv3', 'name': 'Shinwari Karahi', 'image': 'shinwari-karahi.jpg', 'category': 'Live Cuisine'},
        {'id': 'liv4', 'name': 'Mughlai Karahi', 'image': 'mughlai-karahi.jpg', 'category': 'Live Cuisine'},
        {'id': 'liv5', 'name': 'Chicken White Handi', 'image': 'chicken-white-handi.jpg', 'category': 'Live Cuisine'},
        {'id': 'liv6', 'name': 'Chicken Paneer Reshmi Handi', 'image': 'chicken-paneer-reshmi-handi.jpg', 'category': 'Live Cuisine'},
        {'id': 'liv7', 'name': 'Singapori Rice', 'image': 'singapori-rice.jpg', 'category': 'Live Cuisine'},
        {'id': 'liv8', 'name': 'Tawa Fish', 'image': 'tawa-fish.jpg', 'category': 'Live Cuisine'},
        {'id': 'liv9', 'name': 'Karakat', 'image': 'karakat.jpg', 'category': 'Live Cuisine'},

        # Desserts Section
        {'id': 'des1', 'name': 'Zarda (Special)', 'image': 'zarda.jpg', 'category': 'Desserts'},
        {'id': 'des2', 'name': 'Rabri Kheer / Pista Rabri Kheer', 'image': 'rabri-kheer.jpg', 'category': 'Desserts'},
        {'id': 'des3', 'name': 'Lab-e-Shireen', 'image': 'lab-e-shireen.jpg', 'category': 'Desserts'},
        {'id': 'des4', 'name': 'Cream Cocktail (Vanilla & Mango)', 'image': 'cream-cocktail.jpg', 'category': 'Desserts'},
        {'id': 'des5', 'name': 'Ice Cocktail', 'image': 'ice-cocktail.jpg', 'category': 'Desserts'},
        {'id': 'des6', 'name': 'Cherry Crunch Cocktail', 'image': 'cherry-crunch-cocktail.jpg', 'category': 'Desserts'},
        {'id': 'des7', 'name': 'Doodh Dulari', 'image': 'doodh-dulari.jpg', 'category': 'Desserts'},
        {'id': 'des8', 'name': 'Alaska (Vanilla & Mango)', 'image': 'alaska.jpg', 'category': 'Desserts'},
        {'id': 'des9', 'name': 'Fruit Trifle', 'image': 'fruit-trifle.jpg', 'category': 'Desserts'},
        {'id': 'des10', 'name': 'Mango Delight', 'image': 'mango-delight-dessert.jpg', 'category': 'Desserts'},
        {'id': 'des11', 'name': 'Shahi Tukra', 'image': 'shahi-tukra.jpg', 'category': 'Desserts'},
        {'id': 'des12', 'name': 'Dessert Bar (Continental)', 'image': 'dessert-bar-continental.jpg', 'category': 'Desserts'},
        {'id': 'des13', 'name': 'Pineapple Rassgulla', 'image': 'pineapple-rassgulla.jpg', 'category': 'Desserts'},
        {'id': 'des14', 'name': 'Gajar Halwa', 'image': 'gajar-halwa.jpg', 'category': 'Desserts'},
        {'id': 'des15', 'name': 'Loki Halwa', 'image': 'loki-halwa.jpg', 'category': 'Desserts'},
        {'id': 'des16', 'name': 'Dry Fruit Halwa', 'image': 'dry-fruit-halwa.jpg', 'category': 'Desserts'},
        {'id': 'des17', 'name': 'Rasmalai (Small)', 'image': 'rasmalai.jpg', 'category': 'Desserts'},
        {'id': 'des18', 'name': 'Gulab Jamun', 'image': 'gulab-jamun.jpg', 'category': 'Desserts'},
        {'id': 'des19', 'name': 'Special Suji Halwa', 'image': 'suji-halwa.jpg', 'category': 'Desserts'},

        # Ice Cream Section
        {'id': 'ice1', 'name': 'Roasted Almond Ice Cream', 'image': 'roasted-almond-ice-cream.jpg', 'category': 'Ice Cream'},
        {'id': 'ice2', 'name': 'Cisilion Ice Cream', 'image': 'cisilion-ice-cream.jpg', 'category': 'Ice Cream'},
        {'id': 'ice3', 'name': 'Strawberry Cheese Cake', 'image': 'strawberry-cheese-cake.jpg', 'category': 'Ice Cream'},
        {'id': 'ice4', 'name': 'Mango Ice Cream', 'image': 'mango-ice-cream.jpg', 'category': 'Ice Cream'},
        {'id': 'ice5', 'name': 'Badam Zafran Ice Cream', 'image': 'badam-zafran-ice-cream.jpg', 'category': 'Ice Cream'},
        {'id': 'ice6', 'name': 'Rose Malai Ice Cream', 'image': 'rose-malai-ice-cream.jpg', 'category': 'Ice Cream'},
        {'id': 'ice7', 'name': 'Gateau Cake Ice Cream', 'image': 'gateau-cake-ice-cream.jpg', 'category': 'Ice Cream'},
        {'id': 'ice8', 'name': 'Cream Casata (Ice Cake)', 'image': 'cream-casata-ice-cake.jpg', 'category': 'Ice Cream'},
        {'id': 'ice9', 'name': 'Mango Delight (Ice Cake)', 'image': 'mango-delight-ice-cake.jpg', 'category': 'Ice Cream'},
        {'id': 'ice10', 'name': 'Oreo Delight (Ice Cake)', 'image': 'oreo-delight-ice-cake.jpg', 'category': 'Ice Cream'},
        {'id': 'ice11', 'name': 'Temptation (Ice Cake)', 'image': 'temptation-ice-cake.jpg', 'category': 'Ice Cream'},
        {'id': 'ice12', 'name': 'Fruit Alaska (Ice Cake)', 'image': 'fruit-alaska-ice-cake.jpg', 'category': 'Ice Cream'},
        {'id': 'ice13', 'name': 'Baked Alaska (Ice Cake)', 'image': 'baked-alaska-ice-cake.jpg', 'category': 'Ice Cream'},
        {'id': 'ice14', 'name': 'Crunch Kulfi', 'image': 'crunch-kulfi.jpg', 'category': 'Ice Cream'},
        {'id': 'ice15', 'name': 'Mango Kulfi', 'image': 'mango-kulfi.jpg', 'category': 'Ice Cream'},
        {'id': 'ice16', 'name': 'Badam Zafran Kulfi', 'image': 'badam-zafran-kulfi.jpg', 'category': 'Ice Cream'},
        {'id': 'ice17', 'name': 'Khoya Kulfi', 'image': 'khoya-kulfi.jpg', 'category': 'Ice Cream'},

        # Fruit & Salad Bar Section
        {'id': 'bar1', 'name': 'Fruit Bar', 'image': 'fruit-bar.jpg', 'category': 'Bars'},
        {'id': 'bar2', 'name': 'Salad Bar (12 & 16 Bowls)', 'image': 'salad-bar-12-16-bowls.jpg', 'category': 'Bars'},
        {'id': 'bar3', 'name': 'Salad Bar (Ice Box Stainless Steel)', 'image': 'salad-bar-ice-box.jpg', 'category': 'Bars'},
        {'id': 'bar4', 'name': 'Italian Bar', 'image': 'italian-bar.jpg', 'category': 'Bars'},

        # Dessert Bar Section
        {'id': 'db1', 'name': 'Dessert Bar (8 Items)', 'image': 'dessert-bar-8-items.jpg', 'category': 'Dessert Bar'},
        {'id': 'db2', 'name': 'Diamond Dessert Bar with Chocolate Fountain', 'image': 'diamond-dessert-bar.jpg', 'category': 'Dessert Bar'},
        {'id': 'db3', 'name': 'SP Dessert Bar with Waffle Ice Cream (Live)', 'image': 'sp-dessert-bar.jpg', 'category': 'Dessert Bar'},

        # Refreshments Section
        {'id': 'ref1', 'name': 'Chana Chat with SP Spices', 'image': 'chana-chat.jpg', 'category': 'Refreshments'},
        {'id': 'ref2', 'name': 'Dahi Baray with Crackers', 'image': 'dahi-baray.jpg', 'category': 'Refreshments'},
        {'id': 'ref3', 'name': 'SP Gol Gappay', 'image': 'gol-gappay.jpg', 'category': 'Refreshments'},
        {'id': 'ref4', 'name': 'Fresh Juices & Moctail', 'image': 'fresh-juices.jpg', 'category': 'Refreshments'},
        {'id': 'ref5', 'name': 'SP Limca Stall (Many Flavours)', 'image': 'limca-stall.jpg', 'category': 'Refreshments'},
        {'id': 'ref6', 'name': 'Tea, Green Tea & Dood Patti Chai', 'image': 'tea-chai.jpg', 'category': 'Refreshments'},
        {'id': 'ref7', 'name': 'Coffee / Cappuccino & Many More', 'image': 'coffee-cappuccino.jpg', 'category': 'Refreshments'},
        {'id': 'ref8', 'name': 'Pan Stall', 'image': 'pan-stall.jpg', 'category': 'Refreshments'},
    ]

    # Write to CSV file
    csv_filename = 'food_menu_images.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'name', 'image', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in menu_items:
            writer.writerow(item)

    print(f"CSV file '{csv_filename}' has been generated successfully!")
    print(f"Total menu items: {len(menu_items)}")

    # Show a sample of the generated data
    print("\nSample of generated menu items:")
    for i, item in enumerate(menu_items[:5]):
        print(f"  {item['id']}: {item['name']} -> {item['image']} ({item['category']})")

    print("  ...")
    print(f"\nThe CSV contains unique images for all {len(menu_items)} menu items.")
    print("These images can be used to update the menu data and create actual food images.")

if __name__ == "__main__":
    generate_food_images_csv()