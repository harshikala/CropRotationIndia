from flask import Flask, send_file, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    num_plots = request.form.get('num_plots')
    num_periods = request.form.get('num_periods')
    season = request.form.get('season')
    soil_texture = request.form.get('soil_texture')
    
    # Run the crop rotation planner script with the provided parameters
    result = subprocess.run(
        ['python', 'scripts/crop_rotation_planner.py'],
        input=f"{num_plots}\n{num_periods}\n{season}\n{soil_texture}\n",
        text=True,
        capture_output=True
    )
    
    # Extract the filename from the script output
    output_file = result.stdout.strip()
    
    return send_file(output_file, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
