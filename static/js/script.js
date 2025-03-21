class SortingVisualizer {
    constructor() {
        this.array = [];
        this.steps = [];
        this.currentStep = 0;
        this.isSorting = false;
        this.speed = 50;
        this.arraySize = 50;
        this.comparisons = 0;
        this.swaps = 0;
        this.animationTimeout = null;
        this.maxValue = 500; // Maximum value in the array
        
        // DOM elements
        this.container = document.getElementById('array-container');
        this.generateBtn = document.getElementById('generate-array');
        this.startBtn = document.getElementById('start-sort');
        this.stopBtn = document.getElementById('stop-sort');
        this.algorithmSelect = document.getElementById('algorithm-select');
        this.speedSlider = document.getElementById('speed-slider');
        this.sizeSlider = document.getElementById('size-slider');
        this.statsContainer = document.getElementById('stats-container');
        
        // Event listeners
        this.generateBtn.addEventListener('click', () => this.generateNewArray());
        this.startBtn.addEventListener('click', () => this.startSorting());
        this.stopBtn.addEventListener('click', () => this.stopSorting());
        this.speedSlider.addEventListener('input', (e) => this.updateSpeed(e.target.value));
        this.sizeSlider.addEventListener('input', (e) => this.updateArraySize(e.target.value));
        
        // Initial array generation
        this.generateNewArray();
    }
    
    async generateNewArray() {
        try {
            const response = await fetch(`/generate-array?size=${this.arraySize}`);
            this.array = await response.json();
            this.maxValue = Math.max(...this.array);
            this.steps = [];
            this.currentStep = 0;
            this.isSorting = false;
            this.comparisons = 0;
            this.swaps = 0;
            this.updateDisplay();
            this.updateControls();
            this.updateStats();
        } catch (error) {
            console.error('Error generating array:', error);
        }
    }
    
    async startSorting() {
        if (this.isSorting) return;
        
        this.isSorting = true;
        this.updateControls();
        
        try {
            const response = await fetch('/sort', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    array: this.array,
                    algorithm: this.algorithmSelect.value
                })
            });
            
            const data = await response.json();
            this.steps = data.steps;
            this.comparisons = data.comparisons;
            this.swaps = data.swaps;
            this.currentStep = 0;
            this.animateSorting();
        } catch (error) {
            console.error('Error sorting array:', error);
            this.isSorting = false;
            this.updateControls();
        }
    }

    stopSorting() {
        if (!this.isSorting) return;
        
        this.isSorting = false;
        if (this.animationTimeout) {
            clearTimeout(this.animationTimeout);
            this.animationTimeout = null;
        }
        this.updateControls();
        this.updateStats();
    }
    
    animateSorting() {
        if (this.currentStep < this.steps.length && this.isSorting) {
            this.array = this.steps[this.currentStep];
            this.updateDisplay();
            this.currentStep++;
            
            this.animationTimeout = setTimeout(() => this.animateSorting(), 1000 - this.speed * 10);
        } else {
            this.isSorting = false;
            this.updateControls();
            this.updateStats();
        }
    }
    
    updateDisplay() {
        this.container.innerHTML = '';
        const barWidth = 100 / this.array.length;
        const containerHeight = this.container.clientHeight;
        
        this.array.forEach((value, index) => {
            const bar = document.createElement('div');
            bar.className = 'bar';
            // Scale the height to fit within the container
            const scaledHeight = (value / this.maxValue) * containerHeight;
            bar.style.height = `${scaledHeight}px`;
            bar.style.width = `${barWidth}%`;
            
            // Add comparing class to bars being compared
            if (this.isSorting && this.currentStep > 0) {
                const currentStep = this.steps[this.currentStep - 1];
                const prevStep = this.steps[this.currentStep - 2];
                if (prevStep) {
                    const changedIndices = currentStep.map((val, idx) => val !== prevStep[idx] ? idx : -1).filter(idx => idx !== -1);
                    if (changedIndices.includes(index)) {
                        bar.classList.add('comparing');
                    }
                }
            }
            
            this.container.appendChild(bar);
        });
    }
    
    updateStats() {
        this.statsContainer.innerHTML = `
            <div style="display: flex; justify-content: center; gap: 2rem;">
                <div style="text-align: center;">
                    <div style="color: #666; font-size: 0.9rem;">Comparisons</div>
                    <div style="color: #333; font-size: 1.2rem; font-weight: bold;">${this.comparisons}</div>
                </div>
                <div style="text-align: center;">
                    <div style="color: #666; font-size: 0.9rem;">Swaps</div>
                    <div style="color: #333; font-size: 1.2rem; font-weight: bold;">${this.swaps}</div>
                </div>
            </div>
        `;
    }
    
    updateSpeed(value) {
        this.speed = parseInt(value);
    }
    
    updateArraySize(value) {
        this.arraySize = parseInt(value);
        this.generateNewArray();
    }
    
    updateControls() {
        this.generateBtn.disabled = this.isSorting;
        this.startBtn.disabled = this.isSorting;
        this.stopBtn.disabled = !this.isSorting;
        this.algorithmSelect.disabled = this.isSorting;
        this.speedSlider.disabled = this.isSorting;
        this.sizeSlider.disabled = this.isSorting;
    }
}

// Initialize the visualizer when the page loads
window.addEventListener('load', () => new SortingVisualizer()); 