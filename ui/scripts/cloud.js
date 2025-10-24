/**
 * Cloud Visual - анимация частиц облака
 */

class CloudVisual {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) {
            console.error('Canvas not found:', canvasId);
            return;
        }
        
        this.ctx = this.canvas.getContext('2d');
        this.time = 0;
        this.animationId = null;
        
        this.init();
    }
    
    init() {
        this.resize();
        this.start();
        
        // Обработка изменения размера окна
        window.addEventListener('resize', () => this.resize());
    }
    
    resize() {
        const size = 320;
        this.canvas.width = size;
        this.canvas.height = size;
        this.canvas.style.width = `${size}px`;
        this.canvas.style.height = `${size}px`;
    }
    
    start() {
        if (!this.animationId) {
            this.animate();
        }
    }
    
    stop() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
    }
    
    animate() {
        this.drawNoise();
        this.time += 0.02;
        this.animationId = requestAnimationFrame(() => this.animate());
    }
    
    drawNoise() {
        const { width, height } = this.canvas;
        const imageData = this.ctx.createImageData(width, height);
        const data = imageData.data;
        
        // Генерация шума
        for (let i = 0; i < data.length; i += 4) {
            const pixelIndex = i / 4;
            const x = pixelIndex % width;
            const y = Math.floor(pixelIndex / width);
            
            // Расстояние от центра
            const centerX = width / 2;
            const centerY = height / 2;
            const dx = x - centerX;
            const dy = y - centerY;
            const distance = Math.sqrt(dx * dx + dy * dy);
            const maxDistance = width / 2;
            
            // Создание круглой маски
            const mask = 1 - Math.min(distance / maxDistance, 1);
            
            // Шум с анимацией
            const noise = (Math.sin(i * 0.00007 + this.time) * 0.5 + 0.5);
            const intensity = noise * mask * 255 * 0.3;
            
            // RGB (белый) + Alpha
            data[i] = 255;
            data[i + 1] = 255;
            data[i + 2] = 255;
            data[i + 3] = intensity;
        }
        
        this.ctx.putImageData(imageData, 0, 0);
    }
}

// Инициализация после загрузки DOM
let cloudVisual;
document.addEventListener('DOMContentLoaded', () => {
    cloudVisual = new CloudVisual('cloudCanvas');
});
