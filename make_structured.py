import os
import shutil
import random

base_dir = 'Main' 
output_dir = '' 

os.makedirs(os.path.join(output_dir, 'train'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'test'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'val'), exist_ok=True)


class_folders = [folder for folder in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, folder))]
#print(class_folders)

train_ratio = 0.8
test_ratio = 0.1
val_ratio = 0.1


for class_folder in class_folders:
    class_path = os.path.join(base_dir, class_folder)

    #print(class_folder, class_path)

    os.makedirs(os.path.join(output_dir, 'train', class_folder), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'test', class_folder), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'val', class_folder), exist_ok=True)

    images = [img for img in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, img))]

    #print(images)
    
    
    random.shuffle(images)
    
    total_images = len(images)
    train_count = int(total_images * train_ratio)
    test_count = int(total_images * test_ratio)
    val_count = total_images - train_count - test_count  # Remaining images for validation

    train_images = images[:train_count]
    test_images = images[train_count:train_count + test_count]
    val_images = images[train_count + test_count:]

    for img in train_images:
        shutil.move(os.path.join(class_path, img), os.path.join(output_dir, 'train', class_folder, img))

    for img in test_images:
        shutil.move(os.path.join(class_path, img), os.path.join(output_dir, 'test', class_folder, img))

    for img in val_images:
        shutil.move(os.path.join(class_path, img), os.path.join(output_dir, 'val', class_folder, img))

print("Dataset restructuring completed with train, test, and validation splits!")

