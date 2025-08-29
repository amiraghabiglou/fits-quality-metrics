import os
import tempfile
import numpy as np
from astropy.io import fits
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for
from skimage.metrics import peak_signal_noise_ratio
from werkzeug.utils import secure_filename

# --- Constants ---
# Define the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'fits'}

# --- Flask App Initialization ---
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24) # Needed for flashing messages

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# --- Metric Functions ---
def psnr(ground_truth, prediction):
    """Calculate the Peak Signal-to-Noise Ratio."""
    # Ensure data is float for metric calculation
    gt_float = ground_truth.astype(np.float64)
    pred_float = prediction.astype(np.float64)
    return float(peak_signal_noise_ratio(gt_float, pred_float, data_range=gt_float.max() - gt_float.min()))

def snr(ground_truth, prediction, epsilon=1e-10):
    """Calculate the Signal-to-Noise Ratio."""
    # Ensure data is float for metric calculation
    gt_flat = ground_truth.astype(np.float64).flatten()
    pred_flat = prediction.astype(np.float64).flatten()

    noise = gt_flat - pred_flat
    signal_power = np.linalg.norm(gt_flat)**2
    noise_power = np.linalg.norm(noise)**2

    # Avoid division by zero
    if noise_power < epsilon:
        return float('inf')  # Return infinity for perfect reconstruction

    snr_value = 10 * np.log10(signal_power / (noise_power + epsilon))
    return float(snr_value)

def to_log(im, a=1000.):
    im_cur = np.copy(im)
    im_cur[im < 0] = 0
    return np.log10(a * im_cur + 1.) / np.log10(a)

# --- Helper Functions ---
def allowed_file(filename):
    """Check if the uploaded file has a valid extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- Flask Routes ---
@app.route('/')
def index():
    """Renders the main upload page."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_metrics():
    """Handles file upload and metric calculation."""
    if 'pred_file' not in request.files:
        flash('No file part in the request. Please select a file.')
        return redirect(url_for('index'))

    pred_file = request.files['pred_file']

    if pred_file.filename == '':
        flash('No file selected. Please select a FITS file to upload.')
        return redirect(url_for('index'))

    if not allowed_file(pred_file.filename):
        flash('Invalid file type. Please upload a .fits file.')
        return redirect(url_for('index'))

    # Load ground truth data
    try:
        gt_path = os.path.join('data', 'ground_truth.fits')
        with fits.open(gt_path) as hdul:
            gt_data = hdul[0].data
    except FileNotFoundError:
        flash('Error: ground_truth.fits not found in the /data directory.')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error reading ground truth file: {e}')
        return redirect(url_for('index'))


    # Process the uploaded prediction file
    filename = secure_filename(pred_file.filename)
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    try:
        pred_file.save(temp_path)
        with fits.open(temp_path) as hdul:
            pred_data = hdul[0].data

        # Check for shape mismatch
        if gt_data.shape != pred_data.shape:
            flash(f'Image dimensions do not match! GT: {gt_data.shape}, Pred: {pred_data.shape}')
            return redirect(url_for('index'))

        # Calculate metrics
        psnr_result = psnr(gt_data, pred_data)
        snr_result = snr(gt_data, pred_data)
        logsnr_result = snr(to_log(gt_data), to_log(pred_data))

        # Prepare results for rendering
        results = {
            'psnr': f"{psnr_result:.4f}",
            'snr': f"{snr_result:.4f}",
            'logsnr': f"{logsnr_result:.4f}",
            'filename': filename
        }
        return render_template('results.html', results=results)

    except Exception as e:
        flash(f'An error occurred processing the file: {e}')
        return redirect(url_for('index'))
    finally:
        # Clean up the uploaded file
        if os.path.exists(temp_path):
            os.remove(temp_path)


# --- Run Application ---
if __name__ == '__main__':
    app.run(debug=True)
