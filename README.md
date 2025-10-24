# CSCI 6367 Final Project - Digital Image Processing

A comprehensive implementation of FFT-based image processing and image denoising/edge detection techniques for medical imaging analysis.

## Project Overview

This project implements two fundamental digital image processing problems:

### Problem I: FFT-Based Image Processing (50 points)
- 2D Fourier Transform analysis of a lung CT scan
- Image downsampling and interpolation techniques
- Comparison of frequency domain vs. spatial domain interpolation
- Quantitative error analysis using Mean Squared Error (MSE)

### Problem II: Image Denoising and Edge Detection (50 points)
- Multiple denoising techniques (Gaussian, Median, Bilateral, Non-local Means)
- Edge detection methods (Sobel, Canny, Laplacian of Gaussian)
- Comparative analysis of different filtering approaches

## Technologies Used

- **Python 3.13.2**
- **UV** - Modern Python package manager
- **NumPy** - Numerical computing
- **OpenCV** - Computer vision and image processing
- **Matplotlib** - Data visualization
- **SciPy** - Scientific computing and FFT operations
- **Scikit-image** - Advanced image processing algorithms
- **Jupyter Notebook** - Interactive development environment

## Project Structure

```
final_project_code/
├── README.md                          # This file
├── CLAUDE.md                          # Development documentation (ignored)
├── pyproject.toml                     # UV project configuration
├── .gitignore                         # Git ignore rules
├── lung_ct.jpg                        # Input CT image
├── CSCI6367_FinalProject.pdf         # Project requirements (ignored)
├── problem1_fft_interpolation.ipynb  # Problem I notebook
├── problem2_denoising_edges.py       # Problem II implementation (TBD)
└── outputs/                           # Generated results (ignored)
    ├── problem1/                      # Problem I outputs
    └── problem2/                      # Problem II outputs
```

## Installation

### Prerequisites
- Python 3.10 or higher
- UV package manager

### Setup

1. **Clone or navigate to the project directory**:
   ```bash
   cd digital_image_processing
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

   This will install all required packages:
   - numpy (2.3.4)
   - opencv-python (4.11.0.86)
   - matplotlib (3.10.7)
   - scipy (1.16.2)
   - scikit-image (0.25.2)
   - pillow (12.0.0)

3. **Create output directories** (if not exists):
   ```bash
   mkdir -p outputs/problem1 outputs/problem2
   ```

## Usage

### Problem I: FFT and Interpolation

Open the Jupyter notebook:

```bash
code problem1_fft_interpolation.ipynb
```

Run each cell sequentially to generate all visualizations and analyses.

### Problem II: Denoising and Edge Detection

```bash
uv run python problem2_denoising_edges.py
```

*(To be implemented)*

## Problem I Implementation Details

### Task 1: Image Loading
- Loads grayscale lung CT image
- Reports dimensions (M×N)
- Displays image with proper formatting

### Task 2: 2D FFT Analysis
- Computes 2D Fourier Transform
- Displays magnitude and phase (before fftshift)
- Displays magnitude and phase (after fftshift)
- Uses log-scale for magnitude visualization

### Task 3: Downsampling
- Reduces image to half-size (M/2 × N/2)
- Method: Discards odd-numbered samples (keeps indices 0, 2, 4, ...)

### Task 4: Frequency Domain Interpolation
- FFT of downsampled image
- Zero-padding in frequency domain
- Maintains conjugate symmetry: F(u,v) = F*(-u,-v)
- Inverse FFT to get interpolated image
- Proper scaling to match original intensity

### Task 5: Spatial Domain Interpolation
- Bilinear interpolation using OpenCV
- Upscales downsampled image to original size

### Task 6: Error Analysis
- Computes normalized MSE: `Σ|F(m,n) - F_inter(m,n)|² / Σ|F(m,n)|²`
- Calculates standard MSE and PSNR
- Generates comparison visualizations
- Determines which method performs better

## Output Files

All generated images are saved to `outputs/problem1/`:

- `task1_original_image.png` - Original lung CT scan
- `task2_fft_analysis.png` - FFT magnitude and phase visualizations
- `task3_downsampled.png` - Original vs downsampled comparison
- `task4_freq_interpolation.png` - Frequency domain interpolation results
- `task5_spatial_interpolation.png` - Spatial domain interpolation results
- `task6_error_analysis.png` - Comprehensive error analysis and comparison

## Key Concepts

### Fourier Transform
- Transforms spatial domain image to frequency domain
- Reveals frequency components and patterns
- Essential for frequency-based filtering and analysis

### fftshift
- Centers the zero-frequency component in the middle
- Makes visualization more intuitive
- Required for symmetric frequency domain operations

### Conjugate Symmetry
- For real-valued images: F(u,v) = F*(-u,-v)
- Must be maintained during frequency domain manipulation
- Ensures inverse FFT produces real-valued results

### Interpolation Methods
- **Frequency Domain**: Zero-padding in frequency domain acts as ideal low-pass filter
- **Spatial Domain**: Direct interpolation using neighboring pixels
- Trade-offs: Quality vs. computational complexity

## Tips for Report

1. **Screenshots**: All visualizations are automatically saved
2. **Quantitative Results**: MSE and PSNR values are printed
3. **Code Snippets**: Extract key sections from notebook cells
4. **Analysis**: Compare frequency vs. spatial interpolation performance
5. **Discussion**: Explain why one method performs better than the other

## Common Issues and Solutions

### Issue: Image not found
**Solution**: Ensure `lung_ct.jpg` is in the project root directory

### Issue: Dependencies not installed
**Solution**: Run `uv sync` to install all packages

### Issue: Output directory doesn't exist
**Solution**: Run `mkdir -p outputs/problem1 outputs/problem2`

## Performance Notes

- FFT computation: O(N² log N) for N×N image
- Downsampling: O(N²/4)
- Interpolation: O(N²)
- Total runtime: ~5-10 seconds depending on system



