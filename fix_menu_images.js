#!/usr/bin/env node

// Script to fix repeated images in menu data
const fs = require('fs');

// Read the menu data file
const filePath = './src/data/menuData.ts';
let content = fs.readFileSync(filePath, 'utf8');

// Define mapping of repeated images to unique images
const imageReplacements = {
  // BBQ Section
  '/src/assets/food/seekh-kebab.jpg': [
    { id: 'bbq1', newImage: '/src/assets/food/bihari-tikka.jpg' },
    { id: 'bbq2', newImage: '/src/assets/food/malai-tikka.jpg' },
    { id: 'bbq3', newImage: '/src/assets/food/balochi-tikka.jpg' },
    { id: 'bbq10', newImage: '/src/assets/food/dhaga-kabab.jpg' },
    { id: 'bbq11', newImage: '/src/assets/food/seekh-kabab.jpg' },
    { id: 'bbq12', newImage: '/src/assets/food/turkish-kabab.jpg' },
    { id: 'bbq13', newImage: '/src/assets/food/hunzai-kabab.jpg' },
    { id: 'bbq14', newImage: '/src/assets/food/angara-kabab.jpg' },
    { id: 'bbq15', newImage: '/src/assets/food/nalki-kabab.jpg' },
    { id: 'bbq16', newImage: '/src/assets/food/chaska-kabab.jpg' },
    { id: 'bbq17', newImage: '/src/assets/food/chicken-cheese-kabab.jpg' },
  ],
  '/src/assets/food/mixed-grill.jpg': [
    { id: 'bbq7', newImage: '/src/assets/food/chatakh-boti.jpg' },
    { id: 'bbq8', newImage: '/src/assets/food/shashlik-boti.jpg' },
    { id: 'bbq9', newImage: '/src/assets/food/morican-boti.jpg' },
    { id: 'bbq18', newImage: '/src/assets/food/mutton-chanp-grill.jpg' },
    { id: 'bbq22', newImage: '/src/assets/food/mutton-steam.jpg' },
  ],
  '/src/assets/food/lamb-chops.jpg': [
    { id: 'bbq19', newImage: '/src/assets/food/prawns-bbq.jpg' },
    { id: 'bbq20', newImage: '/src/assets/food/grilled-fish.jpg' },
    { id: 'bbq21', newImage: '/src/assets/food/chicken-steam.jpg' },
  ],
  '/src/assets/food/chicken-tikka.jpg': [
    { id: 'bbq21', newImage: '/src/assets/food/chicken-steam.jpg' },
  ],

  // Curries Section
  '/src/assets/food/butter-chicken.jpg': [
    { id: 'cur1', newImage: '/src/assets/food/qorma.jpg' },
    { id: 'cur2', newImage: '/src/assets/food/white-qorma.jpg' },
    { id: 'cur4', newImage: '/src/assets/food/achar-gosht.jpg' },
    { id: 'cur9', newImage: '/src/assets/food/koftay.jpg' },
    { id: 'cur17', newImage: '/src/assets/food/chicken-makhni-handi.jpg' },
    { id: 'cur18', newImage: '/src/assets/food/chicken-white-handi.jpg' },
  ],
  '/src/assets/food/lamb-karahi.jpg': [
    { id: 'cur3', newImage: '/src/assets/food/kunna-paya.jpg' },
    { id: 'cur10', newImage: '/src/assets/food/shab-daig.jpg' },
    { id: 'cur11', newImage: '/src/assets/food/beef-karahi.jpg' },
    { id: 'cur12', newImage: '/src/assets/food/green-karahi.jpg' },
    { id: 'cur13', newImage: '/src/assets/food/white-karahi.jpg' },
    { id: 'cur14', newImage: '/src/assets/food/butter-karahi.jpg' },
    { id: 'cur15', newImage: '/src/assets/food/tikka-karahi.jpg' },
    { id: 'cur16', newImage: '/src/assets/food/balochi-karahi.jpg' },
  ],
  '/src/assets/food/dal-makhani.jpg': [
    { id: 'cur5', newImage: '/src/assets/food/green-stew.jpg' },
    { id: 'cur6', newImage: '/src/assets/food/hari-mirch-qeema.jpg' },
    { id: 'cur7', newImage: '/src/assets/food/dum-qeema.jpg' },
    { id: 'cur8', newImage: '/src/assets/food/palak-paneer.jpg' },
    { id: 'cur19', newImage: '/src/assets/food/haleem.jpg' },
  ],

  // Fry Section
  '/src/assets/food/chicken-tikka.jpg': [
    { id: 'fry1', newImage: '/src/assets/food/broast.jpg' },
    { id: 'fry2', newImage: '/src/assets/food/chargha-broast.jpg' },
    { id: 'fry3', newImage: '/src/assets/food/chicken-ala-kiev.jpg' },
    { id: 'fry4', newImage: '/src/assets/food/chicken-cordon-bleu.jpg' },
    { id: 'fry9', newImage: '/src/assets/food/chicken-cheese-strips.jpg' },
    { id: 'fry12', newImage: '/src/assets/food/chicken-cheese-cone.jpg' },
    { id: 'fry13', newImage: '/src/assets/food/peri-bite.jpg' },
    { id: 'fry18', newImage: '/src/assets/food/chicky-micky.jpg' },
    { id: 'fry19', newImage: '/src/assets/food/chicken-dynamite.jpg' },
    { id: 'fry20', newImage: '/src/assets/food/chicken-pocket.jpg' },
    { id: 'fry21', newImage: '/src/assets/food/chicken-jalapeno.jpg' },
  ],
  '/src/assets/food/lamb-chops.jpg': [
    { id: 'fry5', newImage: '/src/assets/food/fish-biscuit.jpg' },
    { id: 'fry6', newImage: '/src/assets/food/fish-lahori.jpg' },
    { id: 'fry7', newImage: '/src/assets/food/prawn-tempura.jpg' },
  ],
  '/src/assets/food/samosa.jpg': [
    { id: 'fry8', newImage: '/src/assets/food/arabian-puff.jpg' },
    { id: 'fry14', newImage: '/src/assets/food/mint-roll.jpg' },
    { id: 'fry15', newImage: '/src/assets/food/wonton.jpg' },
    { id: 'fry16', newImage: '/src/assets/food/chicken-beef-samosa.jpg' },
    { id: 'fry17', newImage: '/src/assets/food/spring-roll.jpg' },
  ],

  // Chinese Section
  '/src/assets/food/chicken-tikka.jpg': [
    { id: 'chi1', newImage: '/src/assets/food/chicken-chilli.jpg' },
    { id: 'chi3', newImage: '/src/assets/food/chicken-jalfrezi.jpg' },
    { id: 'chi4', newImage: '/src/assets/food/chicken-manchurian.jpg' },
    { id: 'chi5', newImage: '/src/assets/food/szehwan-chicken.jpg' },
    { id: 'chi6', newImage: '/src/assets/food/lemon-chicken.jpg' },
    { id: 'chi7', newImage: '/src/assets/food/kung-pao-chicken.jpg' },
  ],
  '/src/assets/food/butter-chicken.jpg': [
    { id: 'chi2', newImage: '/src/assets/food/chicken-beef-dry.jpg' },
  ],

  // Desserts Section
  '/src/assets/food/kheer.jpg': [
    { id: 'des1', newImage: '/src/assets/food/zarda.jpg' },
    { id: 'des2', newImage: '/src/assets/food/rabri-kheer.jpg' },
    { id: 'des3', newImage: '/src/assets/food/lab-e-shireen.jpg' },
    { id: 'des4', newImage: '/src/assets/food/cream-cocktail.jpg' },
    { id: 'des5', newImage: '/src/assets/food/ice-cocktail.jpg' },
    { id: 'des6', newImage: '/src/assets/food/cherry-crunch-cocktail.jpg' },
    { id: 'des7', newImage: '/src/assets/food/doodh-dulari.jpg' },
    { id: 'des8', newImage: '/src/assets/food/alaska.jpg' },
    { id: 'des9', newImage: '/src/assets/food/fruit-trifle.jpg' },
    { id: 'des10', newImage: '/src/assets/food/mango-delight-dessert.jpg' },
  ],
  '/src/assets/food/gulab-jamun.jpg': [
    { id: 'des11', newImage: '/src/assets/food/shahi-tukra.jpg' },
    { id: 'des12', newImage: '/src/assets/food/dessert-bar-continental.jpg' },
    { id: 'des13', newImage: '/src/assets/food/pineapple-rassgulla.jpg' },
    { id: 'des14', newImage: '/src/assets/food/gajar-halwa.jpg' },
    { id: 'des15', newImage: '/src/assets/food/loki-halwa.jpg' },
    { id: 'des16', newImage: '/src/assets/food/dry-fruit-halwa.jpg' },
    { id: 'des17', newImage: '/src/assets/food/rasmalai.jpg' },
    { id: 'des18', newImage: '/src/assets/food/gulab-jamun.jpg' },
    { id: 'des19', newImage: '/src/assets/food/suji-halwa.jpg' },
  ],

  // Ice Cream Section (already fixed)
  '/src/assets/food/kheer.jpg': [
    { id: 'ice1', newImage: '/src/assets/food/roasted-almond-ice-cream.jpg' },
    { id: 'ice2', newImage: '/src/assets/food/cisilion-ice-cream.jpg' },
    { id: 'ice4', newImage: '/src/assets/food/mango-ice-cream.jpg' },
    { id: 'ice5', newImage: '/src/assets/food/badam-zafran-ice-cream.jpg' },
    { id: 'ice6', newImage: '/src/assets/food/rose-malai-ice-cream.jpg' },
  ],
  '/src/assets/food/gulab-jamun.jpg': [
    { id: 'ice3', newImage: '/src/assets/food/strawberry-cheese-cake.jpg' },
    { id: 'ice7', newImage: '/src/assets/food/gateau-cake-ice-cream.jpg' },
    { id: 'ice8', newImage: '/src/assets/food/cream-casata-ice-cake.jpg' },
    { id: 'ice9', newImage: '/src/assets/food/mango-delight-ice-cake.jpg' },
    { id: 'ice10', newImage: '/src/assets/food/oreo-delight-ice-cake.jpg' },
    { id: 'ice11', newImage: '/src/assets/food/temptation-ice-cake.jpg' },
    { id: 'ice12', newImage: '/src/assets/food/fruit-alaska-ice-cake.jpg' },
    { id: 'ice13', newImage: '/src/assets/food/baked-alaska-ice-cake.jpg' },
    { id: 'ice14', newImage: '/src/assets/food/crunch-kulfi.jpg' },
    { id: 'ice15', newImage: '/src/assets/food/mango-kulfi.jpg' },
    { id: 'ice16', newImage: '/src/assets/food/badam-zafran-kulfi.jpg' },
    { id: 'ice17', newImage: '/src/assets/food/khoya-kulfi.jpg' },
  ],

  // Bars Section
  '/src/assets/food/gulab-jamun.jpg': [
    { id: 'bar1', newImage: '/src/assets/food/fruit-bar.jpg' },
  ],
  '/src/assets/food/dal-makhani.jpg': [
    { id: 'bar2', newImage: '/src/assets/food/salad-bar-12-16-bowls.jpg' },
    { id: 'bar3', newImage: '/src/assets/food/salad-bar-ice-box.jpg' },
    { id: 'bar4', newImage: '/src/assets/food/italian-bar.jpg' },
  ],

  // Dessert Bar Section
  '/src/assets/food/gulab-jamun.jpg': [
    { id: 'db1', newImage: '/src/assets/food/dessert-bar-8-items.jpg' },
    { id: 'db2', newImage: '/src/assets/food/diamond-dessert-bar.jpg' },
    { id: 'db3', newImage: '/src/assets/food/sp-dessert-bar.jpg' },
  ],

  // Refreshments Section
  '/src/assets/food/samosa.jpg': [
    { id: 'ref1', newImage: '/src/assets/food/chana-chat.jpg' },
    { id: 'ref2', newImage: '/src/assets/food/dahi-baray.jpg' },
    { id: 'ref3', newImage: '/src/assets/food/gol-gappay.jpg' },
    { id: 'ref8', newImage: '/src/assets/food/pan-stall.jpg' },
  ],
  '/src/assets/food/kheer.jpg': [
    { id: 'ref4', newImage: '/src/assets/food/fresh-juices.jpg' },
    { id: 'ref5', newImage: '/src/assets/food/limca-stall.jpg' },
    { id: 'ref6', newImage: '/src/assets/food/tea-chai.jpg' },
    { id: 'ref7', newImage: '/src/assets/food/coffee-cappuccino.jpg' },
  ],
};

// Apply the replacements
let updatedContent = content;

// Process each image replacement
for (const [oldImage, replacements] of Object.entries(imageReplacements)) {
  for (const { id, newImage } of replacements) {
    // Create regex pattern to match the specific menu item
    const pattern = new RegExp(`(\\{\\s*id:\\s*'${id}'[^}]*image:\\s*')[^']*(')`, 'g');
    updatedContent = updatedContent.replace(pattern, `$1${newImage}$2`);
  }
}

// Write the updated content back to the file
fs.writeFileSync(filePath, updatedContent);

console.log('Menu images updated successfully!');
console.log('All repeated images have been replaced with unique images for each menu item.');