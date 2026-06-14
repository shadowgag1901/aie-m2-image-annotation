import cv2
import os

# load image
image_path = "input.jpg"

if not os.path.exists(image_path):
    print(f"File not found: {image_path}")
    exit()

img = cv2.imread(image_path)

if img is None:
    print("Couldn't read the image.")
    exit()

print(f"Loaded: {image_path} | shape: {img.shape}")

h, w = img.shape[:2]

# --- draw shapes ---

# line: (img, start, end, color, thickness)
cv2.line(img, (50, 50), (w - 50, 50), (0, 255, 0), 2)  # green line at top

# rectangle: (img, top-left, bottom-right, color, thickness)
cv2.rectangle(img, (50, 80), (200, 180), (255, 0, 0), 2)  # blue rect

# filled rectangle (thickness=-1 fills it)
cv2.rectangle(img, (250, 80), (400, 180), (0, 0, 255), -1)  # red filled rect

# circle: (img, center, radius, color, thickness)
cv2.circle(img, (w // 2, h // 2), 80, (0, 255, 255), 3)  # yellow circle center

# ellipse: (img, center, axes, angle, startAngle, endAngle, color, thickness)
cv2.ellipse(img, (w - 150, h - 100), (60, 40), 30, 0, 360, (255, 0, 255), 2)  # magenta ellipse

# polygon (triangle)
pts = [(w // 2, h - 50), (w // 2 - 60, h - 150), (w // 2 + 60, h - 150)]
cv2.polylines(img, [pts], isClosed=True, color=(255, 128, 0), thickness=2)  # orange triangle

print("Drew line, rectangle, circle, ellipse, and polygon.")

# --- text annotations ---

# putText: (img, text, position, font, scale, color, thickness)
cv2.putText(img, "OpenCV Annotation", (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# label the shapes
cv2.putText(img, "Line", (w - 100, 40), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 1)
cv2.putText(img, "Rect", (50, 200), cv2.FONT_HERSHEY_PLAIN, 0.7, (255, 0, 0), 1)
cv2.putText(img, "Circle", (w // 2 - 30, h // 2 + 100), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 255), 1)

print("Added text labels.")

# --- measurements ---

# draw a line and show its length
p1 = (100, h - 60)
p2 = (400, h - 60)
cv2.line(img, p1, p2, (255, 255, 0), 2)

# calculate distance
dist = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5
cv2.putText(img, f"Length: {int(dist)}px", (120, h - 70), cv2.FONT_HERSHEY_PLAIN, 0.7, (255, 255, 0), 1)

print(f"Measured line distance: {int(dist)} pixels.")

# image dimensions text
cv2.putText(img, f"Size: {w}x{h}", (w - 120, h - 10), cv2.FONT_HERSHEY_PLAIN, 0.6, (200, 200, 200), 1)

# save
cv2.imwrite("output_annotated.jpg", img)

print("Saved: output_annotated.jpg")
print("Done.")
