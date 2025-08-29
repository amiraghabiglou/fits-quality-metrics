FITS Image Quality Metrics Calculator
A simple yet powerful Flask web application to calculate Peak Signal-to-Noise Ratio (PSNR) and Signal-to-Noise Ratio (SNR) and logSNR for astronomical FITS images.

This tool allows a user to upload a reconstructed (prediction) FITS image, which is then compared against a ground-truth image to evaluate the quality of the reconstruction.

About The Project
This project was inspired by the need for a quick and accessible tool to evaluate the output of Deep Neural Networks (DNNs) used in radio-interferometric imaging. The example prediction file provided in the /data directory is an output from the R2D2$_{\mathcal{A}_2,\mathcal{T}_2}$ algorithm, as published in the paper:

Towards a robust R2D2 paradigm for radio-interferometric imaging: revisiting DNN training and architecture

This project serves as a practical demonstration of building a web-based interface for a scientific computing task.

Built With
Flask

NumPy

scikit-image

Astropy

Docker

Getting Started
You can run this project locally by following the setup instructions or by using the provided Docker container.

Prerequisites
Python 3.7+

pip

Local Installation
Clone the repo

git clone [https://github.com/amiraghabiglou/fits-quality-metrics.git](https://github.com/amiraghabiglou/fits-quality-metrics.git)
cd fits-quality-metrics

Create and activate a virtual environment

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Place your data

Add your ground-truth FITS file to the /data directory and name it ground_truth.fits.

An example ground truth and prediction file are already provided.

Run the app

flask run

Navigate to http://127.0.0.1:5000 in your web browser.

Docker Usage
If you have Docker installed, you can easily build and run the application in a container.

Build the Docker image

docker build -t fits-metrics-app .

Run the Docker container

docker run -p 5000:5000 fits-metrics-app

Navigate to http://127.0.0.1:5000 in your web browser.

Usage
Open the web application in your browser.

Click the "Choose a .fits file..." button to select your prediction FITS file.

Click "Calculate Metrics".

The results page will display the calculated PSNR and SNR values.

Project Structure
/fits-quality-metrics
├── app.py              # Main Flask application logic
├── requirements.txt    # Python package dependencies
├── Dockerfile          # Instructions for building the Docker image
├── .dockerignore       # Files to exclude from the Docker image
├── .gitignore          # Files to ignore for Git
├── /data/              # FITS data files
│   ├── ground_truth.fits
│   └── example_prediction.fits
├── /static/            # Static assets
│   └── /css/
│       └── style.css   # Stylesheet for the web interface
└── /templates/         # HTML templates
    ├── index.html      # Main upload page
    └── results.html    # Page to display results
