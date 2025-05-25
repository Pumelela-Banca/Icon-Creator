# Icon-Creator
Creates Icon Images for android apps and GUI's.

### How to Use

1. **Install Pillow** first if you haven't:
```bash
pip install pillow
```

2. **Run from command line**:
```bash
# Generate both WPF and Android icons
python icon_generator.py input_image.png

# Generate only WPF icons
python icon_generator.py input_image.png --formats wpf

# Generate only Android icons
python icon_generator.py input_image.png --formats android
```

### What It Does

1. **For WPF**:
- Creates a `.ico` file containing multiple resolutions (16×16, 24×24, 32×32, 48×48, and 256×256)
- Preserves transparency with PNG compression
- Uses Windows icon format (ICO)

2. **For Android**:
- Creates separate PNG files in standard Android icon sizes:
  - 48×48 (mdpi)
  - 72×72 (hdpi)
  - 96×96 (xhdpi)
  - 144×144 (xxhdpi)
  - 192×192 (xxxhdpi)
  - 512×512 (for Google Play Store)

3. **Features**:
- Automatically crops input image to square
- Preserves transparency (supports PNG with alpha)
- Handles common image formats (PNG, JPEG, etc.)
- Customizable output directory

### Output Structure
```
icons/
├── app_icon.ico          # WPF icon
└── android_icons/
    ├── icon_48x48.png
    ├── icon_72x72.png
    ├── icon_96x96.png
    ├── icon_144x144.png
    ├── icon_192x192.png
    └── icon_512x512.png
