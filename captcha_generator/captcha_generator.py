import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def generate_random_text(length=6):
    characters = string.ascii_letters + string.digits  # Includes uppercase, lowercase, and digits
    return ''.join(random.choice(characters) for _ in range(length))

def insert_spaces(text):
    if len(text) >= 4:
        text = text[:2] + ' ' + text[2:3] + ' ' + text[3:]
    return text

def draw_distorted_text(image, draw, text, font, width, height):
    x = 0
    for char in text:
        char_img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((10, 10), char, font=font, fill=(0, 0, 255))

        # Apply rotation
        char_img = char_img.rotate(random.randint(-30, 30), expand=1)

        # Paste the character on the main image
        image.paste(char_img, (x, (height - char_img.size[1]) // 2), char_img)
        x += char_img.size[0] // 2

def generate_captcha(text):
    width, height = 400, 150  # Increase dimensions to accommodate larger text and spaces
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Load a larger font
    try:
        # Attempt to use a truetype font with a specified size
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)  # Increase font size
    except IOError:
        # Fallback to default font if truetype font is not available
        font = ImageFont.load_default()

    # Insert spaces into the text
    spaced_text = insert_spaces(text)

    # Draw the distorted text
    draw_distorted_text(image, draw, spaced_text, font, width, height)

    # Add some noise
    for _ in range(100):  # Increase noise to 100 points
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(0, 0, 0))

    # Add some lines for distortion
    for _ in range(5):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line(((x1, y1), (x2, y2)), fill=(0, 0, 0), width=2)

    # Reduce the blur to make the text more readable
    image = image.filter(ImageFilter.GaussianBlur(0.5))

    return image

# Run the CAPTCHA generation and save the image
text = generate_random_text()
captcha_image = generate_captcha(text)
captcha_image.show()
captcha_image_path = f"captcha_{text}.png"
captcha_image.save(captcha_image_path)
print(f"Captcha image saved as {captcha_image_path}")
