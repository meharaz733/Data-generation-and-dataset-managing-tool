import os
import random
import cv2
import numpy as np
from imgaug import augmenters as iaa
from tqdm import tqdm

# === CONFIGURATION ===
DATASET_ROOT = input("Enter the path to your dataset root folder: ").strip()
TARGET_IMAGES = 2500
IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# === AUGMENTATION SETUP ===
augmenter = iaa.Sequential([
    iaa.Affine(rotate=(-15, 15)),  # Small rotations
    iaa.ElasticTransformation(alpha=30, sigma=5)  # Elastic distortion
])

# === HELPER FUNCTIONS ===
def is_image_file(filename):
    return filename.lower().endswith(IMG_EXTENSIONS)

def load_images_from_folder(folder):
    return [f for f in os.listdir(folder) if is_image_file(f)]

def augment_image(image):
    return augmenter(image=image)


# path = 'Main/4/01_0001_0_17_0916_0261_4.png'
# img = cv2.imread(path)
# img = augmenter(image=img)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# === MAIN PROCESS ===

for class_folder in tqdm(sorted(os.listdir(DATASET_ROOT)), desc="Processing classes"):
    class_path = os.path.join(DATASET_ROOT, class_folder)

    if not os.path.isdir(class_path):
        continue  # Skip non-directory files

    images = load_images_from_folder(class_path)
    current_count = len(images)

    if current_count >= TARGET_IMAGES:
        continue  # Already has enough images

    needed = TARGET_IMAGES - current_count
    print(f"\n🖋️ Class: {class_folder} | Current: {current_count} | Augmenting: {needed}")

    for i in range(needed):
        random_img_name = random.choice(images)
        img_path = os.path.join(class_path, random_img_name)

        # Load the original image
        img = cv2.imread(img_path)  #Use cv2.IMREAD_GRAYSCALE in the func as parameter if you need to load the image as grayscale. 
        if img is None:
            print(f"❌ Skipped unreadable image: {img_path}")
            continue

        # Augment and save
        aug_img = augment_image(img)
        save_name = f"{random_img_name}_aug_{i}.png"
        save_path = os.path.join(class_path, save_name)
        cv2.imwrite(save_path, aug_img)

