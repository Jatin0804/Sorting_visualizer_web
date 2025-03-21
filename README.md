# Sorting Algorithm Visualizer

A web-based visualization tool for various sorting algorithms, built with Flask and PyScript.

## Features

- Visual representation of sorting algorithms
- Multiple sorting algorithms (Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort)
- Adjustable sorting speed
- Generate new random arrays
- Responsive design

## Setup Instructions

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your web browser and navigate to `http://localhost:5000`

## Technologies Used

- Flask
- PyScript
- HTML5
- CSS3
- Python

## Project Structure

```
sorting_visualizer_web/
├── app.py              # Flask application
├── requirements.txt    # Project dependencies
├── static/            # Static files
│   ├── css/          # CSS styles
│   └── js/           # JavaScript files
└── templates/        # HTML templates
    └── index.html    # Main page template
```
