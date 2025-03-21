# HTML Templates

This directory contains the HTML templates for the sorting algorithm visualizer.

## Directory Structure

```
templates/
└── index.html    # Main application template
```

## Components

### Main Template (`index.html`)

The main template provides:
- Complete application structure
- User interface elements
- Integration with static assets
- Responsive design layout

#### Structure

1. **Header Section**
   - Title
   - Meta tags
   - CSS stylesheet link

2. **Controls Section**
   - Algorithm selection dropdown
   - Array size slider
   - Sorting speed slider
   - Control buttons (Generate, Start, Stop)

3. **Visualization Section**
   - Statistics display
   - Time complexity information
   - Array visualization container

4. **Footer Section**
   - JavaScript file inclusion

#### Key Features

- Clean and intuitive interface
- Real-time updates
- Responsive design
- Mobile-friendly layout
- Interactive controls
- Visual feedback

## Usage

The template is rendered by Flask using:
```python
@app.route('/')
def index():
    return render_template('index.html')
```

## Customization

### Adding New Features

To add new features to the interface:
1. Add new HTML elements in the appropriate section
2. Update the CSS styles
3. Add corresponding JavaScript functionality
4. Update the Flask routes if needed

### Modifying Layout

To modify the layout:
1. Edit the HTML structure
2. Update CSS classes and styles
3. Adjust responsive breakpoints
4. Test on different screen sizes

## Template Variables

The template uses Flask's template engine with:
- `url_for()` for static file paths
- Jinja2 template syntax
- Dynamic content rendering

## Browser Compatibility

The template is designed to work with:
- Modern web browsers
- Mobile devices
- Different screen sizes
- Various input methods 