#!/usr/bin/env python3
"""
Script to update the menu data file with unique images for each menu item
This script will read the menu data file and replace repeated images with unique ones
"""

import re
import csv
from typing import Dict

def load_menu_images_from_csv(csv_file: str) -> Dict[str, str]:
    """Load menu images mapping from CSV file"""
    images_map = {}
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            images_map[row['id']] = f"/src/assets/food/{row['image']}"
    return images_map

def update_menu_data_file(menu_data_file: str, images_map: Dict[str, str]):
    """Update the menu data file with unique images"""
    with open(menu_data_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # For each menu item ID, replace the image
    for item_id, new_image in images_map.items():
        # Create a regex pattern to find the specific menu item and its image
        # Pattern looks for { id: 'item_id', ... image: 'old_image.jpg' }
        pattern = rf"(\{{\s*id:\s*['\"]{item_id}['\"].*?image:\s*['\"])[^'\"]*(['\"])"

        # Replace the image in the matched item
        def replace_image(match):
            return f"{match.group(1)}{new_image}{match.group(2)}"

        content = re.sub(pattern, replace_image, content, flags=re.DOTALL)

    # Write the updated content back to the file
    with open(menu_data_file, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Updated menu data file with unique images for {len(images_map)} menu items")

def main():
    csv_file = 'food_menu_images.csv'
    menu_data_file = 'src/data/menuData.ts'

    print("Loading menu images from CSV...")
    images_map = load_menu_images_from_csv(csv_file)

    print(f"Loaded {len(images_map)} menu items from CSV")

    print("Updating menu data file...")
    update_menu_data_file(menu_data_file, images_map)

    print("Menu data file updated successfully!")

    # Show a sample of changes
    print("\\nSample of updated menu items:")
    for i, (item_id, image_path) in enumerate(list(images_map.items())[:5]):
        print(f"  {item_id} -> {image_path}")

if __name__ == "__main__":
    main()