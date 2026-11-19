#!/usr/bin/env python3
"""Draw entry.png: a one-page newspaper front page summarising world news
for Thursday 19 November 2026. Pure PIL vector-style drawing, no photos,
no AI-generated art, no downloaded assets."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)      # warm newsprint
INK = (26, 26, 26)
RED = (163, 22, 33)         # restrained masthead red
MUTED = (90, 86, 78)
RULE = (26, 26, 26)
GOLD = (176, 141, 58)
TEAL = (31, 94, 102)
NAVY = (38, 58, 94)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(d, text, f, max_w):
    """Greedy word wrap using real text widths."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, text, f, max_w, leading, color=INK):
    for line in wrap(d, text, f, max_w):
        d.text((x, y), line, font=f, fill=color)
        y += leading
    return y


def kicker(d, x, y, text, color=RED):
    d.text((x, y), text, font=SANS_B(15), fill=color)
    return y + 22


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- outer frame -------------------------------------------------------
d.rectangle([18, 18, W - 19, H - 19], outline=INK, width=2)
d.rectangle([26, 26, W - 27, H - 27], outline=INK, width=1)

# ---- masthead ----------------------------------------------------------
d.text((W // 2, 44), "T H E   W O R L D   I N   O N E   P A G E",
       font=SERIF_B(26), fill=INK, anchor="ma")
d.line([60, 82, W - 60, 82], fill=RED, width=3)
d.text((W // 2, 96), "19 NOVEMBER 2026",
       font=SERIF_B(66), fill=INK, anchor="ma")
d.text((W // 2, 168), "T H U R S D A Y   •   T H E   D A Y ' S   W O R L D   N E W S ,   I N   O N E   P I C T U R E",
       font=SANS_B(15), fill=MUTED, anchor="ma")
d.line([60, 200, W - 60, 200], fill=INK, width=2)

# ---- hero row: GTA VI (left) + Voyager 1 (right) -----------------------
hero_y, hero_h = 216, 258
col_w = 452
lx, rx = 60, 512

# --- GTA VI block ---
d.rectangle([lx, hero_y, lx + col_w, hero_y + hero_h], outline=INK, width=1)
kicker(d, lx + 18, hero_y + 14, "CULTURE  •  GAMING")
d.text((lx + 18, hero_y + 40), "Welcome back", font=SERIF_B(30), fill=INK)
d.text((lx + 18, hero_y + 76), "to Vice City", font=SERIF_B(30), fill=INK)
para(d, lx + 18, hero_y + 118,
     "After 13 years, GTA VI unlocks at midnight in each market, "
     "starting in New Zealand. Early reviews: 99 on Metacritic.",
     SANS(18), col_w - 36, 24)
d.text((lx + 18, hero_y + 224), "PS5  •  XBOX SERIES X|S",
       font=SANS_B(14), fill=MUTED)
# gamepad icon, bottom-right of block
gx, gy = lx + col_w - 118, hero_y + 178
d.rounded_rectangle([gx, gy, gx + 96, gy + 52], radius=18, fill=NAVY)
d.rounded_rectangle([gx + 8, gy + 26, gx + 26, gy + 44], radius=3, fill=PAPER)
d.rounded_rectangle([gx + 14, gy + 20, gx + 20, gy + 50], radius=3, fill=PAPER)
for cx, cy, c in [(gx + 66, gy + 20, RED), (gx + 78, gy + 32, GOLD),
                  (gx + 66, gy + 44, TEAL), (gx + 54, gy + 32, PAPER)]:
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=c)

# --- Voyager 1 block ---
d.rectangle([rx, hero_y, rx + col_w, hero_y + hero_h], outline=INK, width=1)
kicker(d, rx + 18, hero_y + 14, "SCIENCE  •  SPACE")
d.text((rx + 18, hero_y + 40), "One light-day", font=SERIF_B(30), fill=INK)
d.text((rx + 18, hero_y + 76), "from home", font=SERIF_B(30), fill=INK)
para(d, rx + 18, hero_y + 118,
     "NASA confirms today: Voyager 1, launched in 1977, is now 16 billion miles "
     "away — light takes a full day to reach it.",
     SANS(18), col_w - 36, 24)
d.text((rx + 18, hero_y + 224), "FIRST HUMAN-MADE OBJECT THIS FAR",
       font=SANS_B(14), fill=MUTED)
# spacecraft icon: gold dish + teal body + antenna boom + stars
sx, sy = rx + col_w - 128, hero_y + 172
for px, py in [(sx + 4, sy + 4), (sx + 96, sy + 8), (sx + 108, sy + 52),
               (sx + 8, sy + 66), (sx + 60, sy - 2)]:
    d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=GOLD)
d.line([sx + 34, sy + 34, sx + 10, sy + 56], fill=INK, width=2)   # antenna boom
d.ellipse([sx + 6, sy + 52, sx + 14, sy + 60], fill=RED)          # boom tip
d.polygon([(sx + 26, sy + 30), (sx + 62, sy + 18), (sx + 76, sy + 38),
           (sx + 40, sy + 50)], fill=TEAL)                        # body
d.line([sx + 62, sy + 18, sx + 84, sy + 6], fill=INK, width=3)    # dish arm
d.ellipse([sx + 76, sy - 6, sx + 106, sy + 20], outline=GOLD, width=4)  # dish

# ---- 2 x 2 grid of smaller stories --------------------------------------
grid_y, cell_h, gap = 494, 208, 16
cells = [
    # (x, y, kicker, title, body, icon)
    (lx, grid_y, "ART  •  NEW YORK", "A Van Gogh for $190.4m",
     "“Chataigniers en fleurs” (1890) sets a new auction record for the artist "
     "at Sotheby’s, after a Nazi-era ownership dispute was settled.", "paint"),
    (rx, grid_y, "WEATHER  •  INDIA", "Cyclone Akvan nears India",
     "The severe storm is forecast to cross the Andhra Pradesh–Odisha coast by "
     "noon on 20 Nov, with winds of 90–100 km/h and heavy rain.", "storm"),
    (lx, grid_y + cell_h + gap, "POLITICS  •  EUROPE", "EU plans €45bn Ukraine loan",
     "Brussels proposes a €45 billion loan to support Kyiv, to be repaid once "
     "Russia pays war reparations, officials say.", "euro"),
    (rx, grid_y + cell_h + gap, "DIPLOMACY  •  CHINA", "Trump, Xi and Putin to meet",
     "The three leaders are set for trilateral talks in Shenzhen today, on the "
     "sidelines of the APEC summit.", "flags"),
]

for (cx, cy, kick, title, body, icon) in cells:
    d.rectangle([cx, cy, cx + col_w, cy + cell_h], outline=INK, width=1)
    ix, iy = cx + 18, cy + 52          # icon box
    if icon == "paint":
        d.rectangle([ix, iy, ix + 74, iy + 96], outline=GOLD, width=4)
        d.rectangle([ix + 6, iy + 6, ix + 68, iy + 90], fill=(214, 196, 150))
        d.ellipse([ix + 30, iy + 16, ix + 56, iy + 42], fill=(232, 190, 60))  # sun
        d.ellipse([ix + 12, iy + 58, ix + 36, iy + 82], fill=(74, 110, 58))   # tree
        d.ellipse([ix + 40, iy + 62, ix + 62, iy + 84], fill=(58, 92, 52))
        d.line([ix + 24, iy + 82, ix + 24, iy + 90], fill=(90, 60, 30), width=3)
    elif icon == "storm":
        for r in (34, 25, 16):
            d.arc([ix + 37 - r, iy + 48 - r, ix + 37 + r, iy + 48 + r],
                  20, 300, fill=TEAL, width=5)
        d.ellipse([ix + 33, iy + 44, ix + 41, iy + 52], fill=TEAL)
        d.line([ix + 8, iy + 92, ix + 66, iy + 92], fill=MUTED, width=2)
    elif icon == "euro":
        d.ellipse([ix + 4, iy + 8, ix + 70, iy + 74], outline=NAVY, width=3)
        for k in range(12):
            import math
            a = math.radians(k * 30 - 90)
            px, py = ix + 37 + 26 * math.cos(a), iy + 41 + 26 * math.sin(a)
            d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=GOLD)
        d.text((ix + 37, iy + 41), "€", font=SERIF_B(34), fill=NAVY, anchor="mm")
    elif icon == "flags":
        # three small flags on poles: US, China, Russia
        poles = [(ix + 6, RED), (ix + 30, (222, 41, 16)), (ix + 54, (0, 57, 166))]
        for px, _ in poles:
            d.line([px, iy + 4, px, iy + 92], fill=INK, width=2)
        # US: stripes + blue canton
        for s in range(4):
            d.rectangle([ix + 8, iy + 6 + s * 7, ix + 24, iy + 11 + s * 7],
                        fill=RED if s % 2 == 0 else PAPER)
        d.rectangle([ix + 8, iy + 6, ix + 16, iy + 17], fill=NAVY)
        # China: red field, gold stars
        d.rectangle([ix + 32, iy + 6, ix + 48, iy + 34], fill=(222, 41, 16))
        d.ellipse([ix + 35, iy + 9, ix + 39, iy + 13], fill=GOLD)
        d.ellipse([ix + 42, iy + 9, ix + 44, iy + 11], fill=GOLD)
        # Russia: white / blue / red bands
        d.rectangle([ix + 56, iy + 6, ix + 72, iy + 15], fill=PAPER, outline=INK)
        d.rectangle([ix + 56, iy + 15, ix + 72, iy + 24], fill=(0, 57, 166))
        d.rectangle([ix + 56, iy + 24, ix + 72, iy + 34], fill=RED)
    tx = cx + 112
    kicker(d, tx, cy + 14, kick)
    title_lines = wrap(d, title, SERIF_B(23), col_w - 130)
    ty = cy + 40
    for tl in title_lines:
        d.text((tx, ty), tl, font=SERIF_B(23), fill=INK)
        ty += 28
    para(d, tx, ty + 6, body, SANS(16), col_w - 130, 21)

# ---- footer --------------------------------------------------------------
d.line([60, 950, W - 60, 950], fill=INK, width=1)
d.text((W // 2, 962),
       "Sources: Reuters  •  NASA  •  Sotheby’s  •  India Meteorological Department  •  AP     —     Compiled 19 November 2026",
       font=SANS(13), fill=MUTED, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
