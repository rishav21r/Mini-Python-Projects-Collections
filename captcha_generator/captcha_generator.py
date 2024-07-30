import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def generate_random_text(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def insert_spaces(text):
    if len(text) >= 4:
        text = text[:2] + ' ' + text[2:3] + ' ' + text[3:]
    return text

def draw_distorted_text(image, draw, text, font, width, height):
    x = 20  # Start a bit to the right
    for char in text:
        char_img = Image.new('RGBA', (150, 150), (255, 255, 255, 0))  # Increased from 100x100
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((10, 10), char, font=font, fill=(0, 0, 255))

        # Apply rotation
        char_img = char_img.rotate(random.randint(-30, 30), expand=1)

        # Paste the character on the main image
        image.paste(char_img, (x, (height - char_img.size[1]) // 2), char_img)
        x += char_img.size[0] // 2 + 10  # Added extra spacing between characters

def generate_captcha(text):
    width, height = 600, 200  # Increased from 400x150
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)  # Increased from 70
    except IOError:
        font = ImageFont.load_default()

    spaced_text = insert_spaces(text)
    draw_distorted_text(image, draw, spaced_text, font, width, height)

    # Add some noise
    for _ in range(150):  # Increased from 100
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(0, 0, 0))

    # Add some lines for distortion
    for _ in range(7):  # Increased from 5
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line(((x1, y1), (x2, y2)), fill=(0, 0, 0), width=3)  # Increased width from 2

    image = image.filter(ImageFilter.GaussianBlur(0.5))
    return image

# Run the CAPTCHA generation and save the image
text = generate_random_text()
captcha_image = generate_captcha(text)
captcha_image.show()
captcha_image_path = f"captcha_{text}.png"
captcha_image.save(captcha_image_path)
print(f"Captcha image saved as {captcha_image_path}")