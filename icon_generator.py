"""
Creates both android and wpf icons.
"""
import argparse
import os
from PIL import Image

def make_square(img):
    """Crops image to square while maintaining aspect ratio"""
    size = min(img.size)
    left = (img.width - size) / 2
    top = (img.height - size) / 2
    right = left + size
    bottom = top + size
    return img.crop((left, top, right, bottom))

def generate_icons(input_path, output_dir='icons', formats=['wpf', 'android']):
    """Generates icons for WPF and Android from an input image"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open and prepare source image
    with Image.open(input_path) as img:
        # Convert to square image while preserving aspect ratio
        img = make_square(img).convert('RGBA')
        
        # Generate WPF .ico file with multiple sizes
        if 'wpf' in formats:
            ico_path = os.path.join(output_dir, 'app_icon.ico')
            wpf_sizes = [(16,16), (24,24), (32,32), (48,48), (256,256)]
            img.save(ico_path, format='ICO', sizes=wpf_sizes)
            print(f"WPF icons created at: {ico_path}")
        
        # Generate Android PNGs with different sizes
        if 'android' in formats:
            android_sizes = [48, 72, 96, 144, 192, 512]
            android_dir = os.path.join(output_dir, 'android_icons')
            if not os.path.exists(android_dir):
                os.makedirs(android_dir)
            
            for size in android_sizes:
                resized_img = img.resize((size, size), Image.LANCZOS)
                png_path = os.path.join(android_dir, f'icon_{size}x{size}.png')
                resized_img.save(png_path)
            print(f"Android icons created in: {android_dir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate WPF and Android icons from an image.')
    parser.add_argument('input_image', help='Path to the input image file')
    parser.add_argument('--output_dir', default='icons', help='Directory to save generated icons (default: icons)')
    parser.add_argument('--formats', nargs='+', default=['wpf', 'android'], 
                      help='Which formats to generate: wpf, android (default: both)')
    args = parser.parse_args()
    
    generate_icons(args.input_image, args.output_dir, args.formats)
