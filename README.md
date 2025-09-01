# ⭐ FITS Image Quality Metrics Calculator  

A lightweight yet powerful **Flask web application** for calculating **Peak Signal-to-Noise Ratio (PSNR)**, **Signal-to-Noise Ratio (SNR)**, and **logSNR** for astronomical **FITS images**.  

This tool allows users to upload a reconstructed (prediction) FITS image and compare it against a ground-truth image, providing a quick assessment of reconstruction quality.  

---

## 🚀 About The Project  

This project was motivated by the need for a simple and accessible tool to evaluate the performance of **Deep Neural Networks (DNNs)** in radio-interferometric imaging.  

An example prediction file is included in the `/data` directory. It is the output of the  
![equation](https://latex.codecogs.com/svg.latex?R2D2_{\mathcal{A}_2,\mathcal{T}_2}) algorithm, as described in the paper:  

> _Towards a robust R2D2 paradigm for radio-interferometric imaging: revisiting DNN training and architecture_  

This repository also demonstrates how to build a **web-based interface for scientific computing tasks**.  

---

## 🛠️ Built With  

- [Flask](https://flask.palletsprojects.com/)  
- [NumPy](https://numpy.org/)  
- [scikit-image](https://scikit-image.org/)  
- [Astropy](https://www.astropy.org/)  
- [Docker](https://www.docker.com/)  

---

## ⚡ Getting Started  

You can run the project locally or with Docker.  

### ✅ Prerequisites  

- Python **3.7+**  
- `pip` package manager  
- (Optional) Docker  

---

### 🔹 Local Installation  

1. **Clone the repository**  
    ```bash
    git clone https://github.com/amiraghabiglou/fits-quality-metrics.git
    cd fits-quality-metrics


2. **Create and activate a virtual environment**

# macOS/Linux  

    python3 -m venv venv
    source venv/bin/activate
    

# Windows

    python -m venv venv
    .\venv\Scripts\activate

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt


4. **Prepare your data**

Place your ground-truth FITS file in /data and name it:

    ground_truth.fits


Example ground_truth.fits and example_prediction.fits are already provided.

5. **Run the Flask app**
    ```bash
    flask run


6. **Open in browser**

http://127.0.0.1:5000

🔹 **Docker Usage**

Build the image

docker build -t fits-metrics-app .


Run the container

docker run -p 5000:5000 fits-metrics-app


Open in browser

http://127.0.0.1:5000

📖 **Usage**

Open the web application in your browser.

Click "Choose a .fits file..." to upload your prediction FITS file.

Click "Calculate Metrics".

View calculated PSNR, SNR, and logSNR values on the results page.

📂 **Project Structure**
```bash
fits-quality-metrics
├── app.py              # Main Flask application logic
├── requirements.txt    # Python package dependencies
├── Dockerfile          # Instructions for building Docker image
├── .dockerignore       # Files to exclude from Docker builds
├── .gitignore          # Git ignore rules
├── /data/              # FITS data files
│   ├── ground_truth.fits
│   └── example_prediction.fits
├── /static/            # Static assets
│   └── css/
│       └── style.css   # Web app styles
└── /templates/         # HTML templates
    ├── index.html      # Upload page
    └── results.html    # Results display
```
🙌 **Acknowledgements**

Astropy
 for astronomical FITS file handling

scikit-image
 for image quality metrics

The [BASPLib](https://basp-group.github.io/BASPLib/) for R2D2 imaging algorithm
