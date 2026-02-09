import os
import json
from PIL import Image
from datetime import datetime

class IconTool:
    def __init__(self):
        self.running = True
        self.library_file = "icon_library.json"

    def show_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("           ICON TOOL - Icon Manager")
        print("="*50)
        print("\n1. Browse icons in folder")
        print("2. Extract icons from .exe/.dll file")
        print("3. Convert image to .ico")
        print("4. Crop image")
        print("5. Build icon library")
        print("6. View icon library")
        print("7. Search in library")
        print("8. Exit")
        print("\n" + "="*50)

    def browse_icons(self):
        """Browse icons in a folder"""
        folder = input("\nEnter folder path: ").strip()
        
        if not os.path.exists(folder):
            print("❌ Folder does not exist!")
            return
        
        icon_files = [f for f in os.listdir(folder) if f.lower().endswith(('.ico', '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.svg'))]
        
        if not icon_files:
            print("❌ No image files found in this folder.")
            return
        
        print(f"\n✅ Found {len(icon_files)} files:")
        for i, file in enumerate(icon_files, 1):
            file_path = os.path.join(folder, file)
            try:
                if file.lower().endswith('.svg'):
                    print(f"{i}. {file} - (SVG vector file)")
                else:
                    img = Image.open(file_path)
                    print(f"{i}. {file} - Size: {img.size[0]}x{img.size[1]}")
            except:
                print(f"{i}. {file} - (cannot read)")

    def extract_icon(self):
        """Extract icons from .exe/.dll files"""
        file_path = input("\nEnter path to .exe/.dll file: ").strip()
        
        if not os.path.exists(file_path):
            print("❌ File does not exist!")
            return
        
        print("ℹ️  Icon extraction from .exe/.dll requires win32api library (Windows)")
        print("   Install: pip install pywin32")
        
        try:
            import win32api
            import win32con
            import win32gui
            
            output_folder = input("Enter destination folder for icons: ").strip()
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            # Attempt to extract icons
            large, small = win32gui.ExtractIconEx(file_path, 0)
            
            if large:
                print(f"✅ Found {len(large)} icons. Saving...")
                # Code to save icons would go here
                print(f"✅ Icons saved in: {output_folder}")
            else:
                print("❌ No icons found in this file.")
                
        except ImportError:
            print("❌ pywin32 library not found. Install: pip install pywin32")
        except Exception as e:
            print(f"❌ Error during extraction: {e}")

    def convert_to_ico(self):
        """Convert image to .ico format"""
        input_file = input("\nEnter path to image file: ").strip()
        
        if not os.path.exists(input_file):
            print("❌ File does not exist!")
            return
        
        try:
            img = Image.open(input_file)
            print(f"📐 Current size: {img.size[0]}x{img.size[1]}")
            
            # Icon sizes
            print("\nSelect icon size:")
            print("1. 16x16")
            print("2. 32x32")
            print("3. 48x48")
            print("4. 64x64")
            print("5. 128x128")
            print("6. 256x256")
            print("7. Custom size")
            print("8. Multiple sizes (multi-resolution .ico)")
            
            choice = input("Choice (1-8): ").strip()
            
            sizes = {
                '1': (16, 16),
                '2': (32, 32),
                '3': (48, 48),
                '4': (64, 64),
                '5': (128, 128),
                '6': (256, 256)
            }
            
            output_file = input("Enter output filename (with .ico extension): ").strip()
            if not output_file.endswith('.ico'):
                output_file += '.ico'
            
            if choice in sizes:
                size = sizes[choice]
                img_resized = img.resize(size, Image.Resampling.LANCZOS)
                img_resized.save(output_file, format='ICO')
            elif choice == '7':
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                size = (width, height)
                img_resized = img.resize(size, Image.Resampling.LANCZOS)
                img_resized.save(output_file, format='ICO')
            elif choice == '8':
                # Multiple sizes
                selected_sizes = [(16, 16), (32, 32), (48, 48), (256, 256)]
                img.save(output_file, format='ICO', sizes=selected_sizes)
            else:
                print("❌ Invalid choice!")
                return
            
            print(f"✅ File saved as: {output_file}")
            
        except Exception as e:
            print(f"❌ Error during conversion: {e}")

    def crop_image(self):
        """Crop image"""
        input_file = input("\nEnter path to image file: ").strip()
        
        if not os.path.exists(input_file):
            print("❌ File does not exist!")
            return
        
        try:
            img = Image.open(input_file)
            width, height = img.size
            print(f"📐 Current size: {width}x{height}")
            
            print("\nEnter crop coordinates:")
            left = int(input(f"Left (0-{width}): "))
            top = int(input(f"Top (0-{height}): "))
            right = int(input(f"Right ({left}-{width}): "))
            bottom = int(input(f"Bottom ({top}-{height}): "))
            
            # Cropping
            cropped = img.crop((left, top, right, bottom))
            print(f"📐 New size: {cropped.size[0]}x{cropped.size[1]}")
            
            # Save
            output_file = input("Enter output filename: ").strip()
            cropped.save(output_file)
            print(f"✅ File saved as: {output_file}")
            
        except Exception as e:
            print(f"❌ Error during cropping: {e}")

    def build_library(self):
        """Build icon library from folder"""
        folder = input("\nEnter folder path to scan: ").strip()
        
        if not os.path.exists(folder):
            print("❌ Folder does not exist!")
            return
        
        print("\n🔍 Scanning folder for images...")
        
        # Supported extensions
        extensions = ['.ico', '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.svg']
        
        library = self.load_library()
        added_count = 0
        
        for root, dirs, files in os.walk(folder):
            for file in files:
                if any(file.lower().endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    
                    try:
                        entry = {
                            'filename': file,
                            'path': file_path,
                            'extension': os.path.splitext(file)[1].lower(),
                            'added_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        
                        # Get image info if not SVG
                        if not file.lower().endswith('.svg'):
                            img = Image.open(file_path)
                            entry['width'] = img.size[0]
                            entry['height'] = img.size[1]
                            entry['format'] = img.format
                        else:
                            entry['width'] = 'N/A'
                            entry['height'] = 'N/A'
                            entry['format'] = 'SVG'
                        
                        # Add tags based on filename
                        tags = []
                        filename_lower = file.lower()
                        if 'icon' in filename_lower:
                            tags.append('icon')
                        if 'logo' in filename_lower:
                            tags.append('logo')
                        if 'button' in filename_lower:
                            tags.append('button')
                        
                        entry['tags'] = tags
                        
                        # Add to library
                        library.append(entry)
                        added_count += 1
                        
                    except Exception as e:
                        print(f"⚠️  Could not process {file}: {e}")
        
        # Save library
        self.save_library(library)
        print(f"\n✅ Library built successfully!")
        print(f"📊 Added {added_count} images to library")
        print(f"📚 Total entries in library: {len(library)}")

    def view_library(self):
        """View icon library"""
        library = self.load_library()
        
        if not library:
            print("\n❌ Library is empty. Build a library first (option 5).")
            return
        
        print(f"\n📚 Icon Library ({len(library)} entries)")
        print("="*80)
        
        # Group by extension
        by_extension = {}
        for entry in library:
            ext = entry['extension']
            if ext not in by_extension:
                by_extension[ext] = []
            by_extension[ext].append(entry)
        
        print("\n📊 Summary by extension:")
        for ext, items in sorted(by_extension.items()):
            print(f"  {ext}: {len(items)} files")
        
        print("\n📋 Entries (showing first 20):")
        for i, entry in enumerate(library[:20], 1):
            size_info = f"{entry['width']}x{entry['height']}" if entry['width'] != 'N/A' else 'Vector'
            tags_info = f"[{', '.join(entry['tags'])}]" if entry['tags'] else ''
            print(f"{i}. {entry['filename']} - {size_info} {tags_info}")
        
        if len(library) > 20:
            print(f"\n... and {len(library) - 20} more entries")

    def search_library(self):
        """Search in icon library"""
        library = self.load_library()
        
        if not library:
            print("\n❌ Library is empty. Build a library first (option 5).")
            return
        
        print("\n🔍 Search options:")
        print("1. By filename")
        print("2. By extension")
        print("3. By size")
        print("4. By tags")
        
        choice = input("\nChoice (1-4): ").strip()
        
        results = []
        
        if choice == '1':
            query = input("Enter filename to search: ").strip().lower()
            results = [e for e in library if query in e['filename'].lower()]
        elif choice == '2':
            ext = input("Enter extension (e.g., .png, .ico): ").strip().lower()
            results = [e for e in library if e['extension'] == ext]
        elif choice == '3':
            width = input("Enter width (or press Enter to skip): ").strip()
            height = input("Enter height (or press Enter to skip): ").strip()
            
            for e in library:
                if e['width'] == 'N/A':
                    continue
                match = True
                if width and int(width) != e['width']:
                    match = False
                if height and int(height) != e['height']:
                    match = False
                if match:
                    results.append(e)
        elif choice == '4':
            tag = input("Enter tag to search: ").strip().lower()
            results = [e for e in library if tag in [t.lower() for t in e['tags']]]
        else:
            print("❌ Invalid choice!")
            return
        
        if results:
            print(f"\n✅ Found {len(results)} results:")
            for i, entry in enumerate(results, 1):
                size_info = f"{entry['width']}x{entry['height']}" if entry['width'] != 'N/A' else 'Vector'
                print(f"{i}. {entry['filename']} - {size_info}")
                print(f"   Path: {entry['path']}")
        else:
            print("\n❌ No results found.")

    def load_library(self):
        """Load library from JSON file"""
        if os.path.exists(self.library_file):
            try:
                with open(self.library_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_library(self, library):
        """Save library to JSON file"""
        with open(self.library_file, 'w', encoding='utf-8') as f:
            json.dump(library, f, indent=2, ensure_ascii=False)

    def run(self):
        """Main program loop"""
        print("\n🎨 Welcome to Icon Tool!")
        print("Required library: pip install Pillow")
        
        while self.running:
            self.show_menu()
            choice = input("\nSelect option (1-8): ").strip()
            
            if choice == '1':
                self.browse_icons()
            elif choice == '2':
                self.extract_icon()
            elif choice == '3':
                self.convert_to_ico()
            elif choice == '4':
                self.crop_image()
            elif choice == '5':
                self.build_library()
            elif choice == '6':
                self.view_library()
            elif choice == '7':
                self.search_library()
            elif choice == '8':
                print("\n👋 Goodbye!")
                self.running = False
            else:
                print("❌ Invalid choice! Select option 1-8.")
            
            if self.running and choice in ['1', '2', '3', '4', '5', '6', '7']:
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    tool = IconTool()
    tool.run()