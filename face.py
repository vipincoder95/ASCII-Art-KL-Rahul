from PIL import Image
import os

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", " ", " "]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    
  
    new_height = int(new_width * ratio * 0.5)
    
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ""
    for pixel in pixels:
        index = pixel // 25
        if index >= len(ASCII_CHARS):
            index = len(ASCII_CHARS) - 1
        characters += ASCII_CHARS[index]
    return characters

def main():
    
    target_filename = "kl rahul2.jpg"
    image_path = None
    
    
    possible_paths = [target_filename, "/" + target_filename, "/content/" + target_filename]
    
    for path in possible_paths:
        if os.path.exists(path):
            image_path = path
            break
            
    if image_path is None:
        print(f"[ERROR] फोटो '{target_filename}' नहीं मिली!")
        print("कृपया चेक करें कि आपने फोटो का नाम 'kl rahul2.jpg' ही रखा है ना?")
        return

    print(f"Processing Image: {image_path} ...")
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

   
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + 100)] 
                             for index in range(0, pixel_count, 100)])
    
    
    print(ascii_image)
    
    
    with open("project_kl_rahul.txt", "w") as f:
        f.write(ascii_image)
    print("\n[Success] आपका प्रोजेक्ट 'project_kl_rahul.txt' फाइल में सेव हो गया है!")

if __name__ == "__main__":
    main()