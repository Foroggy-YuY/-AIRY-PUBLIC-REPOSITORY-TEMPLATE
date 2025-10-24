/**
 * HUD - управление интерфейсом пользователя
 */

class HUD {
    constructor() {
        this.statusElement = null;
        this.indicatorElement = null;
    }
    
    init() {
        this.statusElement = document.getElementById('status');
        this.indicatorElement = document.getElementById('indicator');
        
        console.log('HUD initialized');
        
        // Показать подсказки управления
        this.showControls();
    }
    
    updateStatus(text) {
        if (this.statusElement) {
            this.statusElement.textContent = text;
        }
    }
    
    showControls() {
        // Временное сообщение о клавишах
        setTimeout(() => {
            console.log(`
╔════════════════════════════════════╗
║     УПРАВЛЕНИЕ AIRY                ║
╠════════════════════════════════════╣
║ ПРОБЕЛ       - idle ↔ listening   ║
║ КЛИК         - idle ↔ listening   ║
║ 1, 2, 3, 4   - выбор состояния    ║
║ ← →          - переключение       ║
╚════════════════════════════════════╝
            `);
        }, 500);
    }
    
    showNotification(message, duration = 2000) {
        // Создание временного уведомления
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 14px;
            z-index: 1000;
            animation: slideDown 0.3s ease;
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideUp 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, duration);
    }
}

// Создание глобального экземпляра
const hud = new HUD();
