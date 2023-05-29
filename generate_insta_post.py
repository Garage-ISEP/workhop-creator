import os
import re
from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_instagram_post(event_name, lab, description, date, hour, location, classroom):
    # Create the title and description for the Instagram post
    title = f"{event_name}"
    lines = textwrap.wrap(description, width=30)
    description = "\n".join(lines)

    # Generate the image with the post content
    image_path = os.path.join("assets",f"{lab}.png")
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype("fonts/LeagueSpartan-Bold.ttf", 50)
    desc_font = ImageFont.truetype("fonts/LeagueSpartan-Bold.ttf", 40)
    draw.text((150, 535), title, fill=(0, 0, 0), font=title_font)
    draw.text((110, 250), f"{hour}", fill=(255, 255, 255), font=desc_font)
    draw.text((830, 250), f"{date}", fill=(255, 255, 255), font=desc_font)
    draw.text((450, 950), f"{location} - {classroom}", fill=(255, 255, 255), font=desc_font)

    # Save the generated image
    post_image_path = "output/generated_post.png"
    img.save(post_image_path)
    print("Instagram post generated!")

    # Display the image
    img.show()