import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Make output directory
os.makedirs("outputs/problem2", exist_ok=True)

# === 1. LOAD THE NOISY IMAGE ===
image_path = "sleepycat.jpg"   # <-- your uploaded image
image_color = cv2.imread(image_path)

if image_color is None:
    raise FileNotFoundError("Could not load sleepycat.jpg. Make sure it's in the project folder.")

# Convert BGR → RGB for display
image_rgb = cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

# Save original
plt.figure(figsize=(6,5))
plt.imshow(image_rgb)
plt.title("Original Noisy Image (RGB)")
plt.axis("off")
plt.tight_layout()
plt.savefig("outputs/problem2/task2_original_noisy.png", dpi=300)
plt.close()


# === 2. GAUSSIAN SMOOTHING ===
gaussian = cv2.GaussianBlur(image_gray, (7, 7), sigmaX=1.5)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.imshow(image_gray, cmap="gray")
plt.title("Original Noisy (Grayscale)")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(gaussian, cmap="gray")
plt.title("Gaussian Denoised (7x7 kernel, σ=1.5)")
plt.axis("off")

plt.suptitle("Task 2: Gaussian Smoothing", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/problem2/task2_gaussian.png", dpi=300)
plt.close()


# === 3. LAPLACIAN EDGE DETECTION ===
laplacian = cv2.Laplacian(gaussian, cv2.CV_64F)
laplacian_abs = np.uint8(np.absolute(laplacian))

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.imshow(gaussian, cmap="gray")
plt.title("Gaussian Denoised")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(laplacian_abs, cmap="gray")
plt.title("Laplacian Edges")
plt.axis("off")

plt.suptitle("Task 3: Laplacian Edge Detection", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/problem2/task3_laplacian_edges.png", dpi=300)
plt.close()


# === 4. FINAL COMPARISON (for the report) ===
plt.figure(figsize=(18,6))

plt.subplot(1,3,1)
plt.imshow(image_rgb)
plt.title("Original Noisy Image", fontweight="bold")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(gaussian, cmap="gray")
plt.title("Gaussian Denoised", fontweight="bold")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(laplacian_abs, cmap="gray")
plt.title("Edges (Laplacian)", fontweight="bold")
plt.axis("off")

plt.suptitle("Problem II: Noisy → Denoised → Edges", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/problem2/task4_problem2_summary.png", dpi=300)
plt.close()

print("Problem II complete! Check outputs/problem2/")