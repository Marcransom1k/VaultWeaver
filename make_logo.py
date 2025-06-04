from PIL import Image, ImageDraw, ImageFont

width, height = 600, 200
image = Image.new("RGB", (width, height), (0, 0, 0))
draw = ImageDraw.Draw(image)

title = "VaultWeaver"
subtitle = "Recon | CVE-Aware | Stealth | Auto-Scan"

font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50)
font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

draw.text((30, 50), title, font=font_title, fill=(0, 255, 128))
draw.text((32, 120), subtitle, font=font_sub, fill=(180, 180, 180))

image.save("vaultweaver_logo.png")
