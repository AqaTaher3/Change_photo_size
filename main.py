from PIL import Image
import os, shutil


def find_jpg_files(source_folder):
    jpg_files = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.jpg'):
                jpg_files.append(os.path.join(root, file))
    return jpg_files


def resize_image_to_target_size(image_path, target_size_kb, output_path):
    target_size = target_size_kb * 1024
    with Image.open(image_path) as img:
        quality = 95
        while True:
            img.save(output_path, format="JPEG", quality=quality)
            if os.path.getsize(output_path) <= target_size or quality <= 10:
                break
            quality -= 5


def copy_and_resize_images(jpg_files, source_folder, destination_folder):
    for file in jpg_files:
        relative_path = os.path.relpath(file, source_folder)
        destination_path = os.path.join(destination_folder, relative_path)

        # ایجاد پوشه‌های لازم در مقصد
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

        # تغییر اندازه و ذخیره فایل در مکان جدید
        resize_image_to_target_size(file, 400, destination_path)


source_folder = r"D:\000_Maroochi"
destination_folder = r"D:\000_site_pic"

def main():
    jpg_files = find_jpg_files(source_folder)
    print(f"{len(jpg_files)} فایل یافت شد.")

    copy_and_resize_images(jpg_files, source_folder, destination_folder)
    print("تمام فایل‌ها با موفقیت کپی و تغییر اندازه داده شدند.")


if __name__ == "__main__":
    main()
