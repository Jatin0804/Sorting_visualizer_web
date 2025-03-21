# Frontend Components

This directory contains the static files for the sorting algorithm visualizer's frontend.

## Directory Structure

```
static/
├── css/
│   └── style.css    # Main stylesheet
└── js/
    └── script.js    # Main JavaScript file
```

## Components

### CSS (`style.css`)

The stylesheet provides:
- Responsive layout design
- Modern and clean UI elements
- Smooth animations for sorting visualization
- Mobile-friendly design
- Consistent color scheme
- Interactive elements styling

Key features:
- Flexbox-based layout
- CSS Grid for complex layouts
- Media queries for responsiveness
- CSS transitions for smooth animations
- Custom styling for sorting bars
- Consistent spacing and typography

### JavaScript (`script.js`)

The main JavaScript file implements:
- Sorting visualization logic
- User interface interactions
- Real-time statistics updates
- Algorithm selection handling
- Speed and size controls
- Array generation and manipulation

Key features:
- Object-oriented design with `SortingVisualizer` class
- Asynchronous API communication
- Real-time visualization updates
- Event handling for user interactions
- Statistics tracking and display
- Complexity information management

## Usage

The frontend components are automatically loaded by the Flask application through the `index.html` template:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

## Customization

### Styling

To modify the visual appearance:
1. Edit `style.css`
2. Update color variables
3. Modify layout properties
4. Adjust animation timings

### Behavior

To modify the visualization behavior:
1. Edit `script.js`
2. Update animation speed calculations
3. Modify array generation logic
4. Adjust visualization parameters

## Browser Support

The frontend is designed to work on:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Android Chrome) 