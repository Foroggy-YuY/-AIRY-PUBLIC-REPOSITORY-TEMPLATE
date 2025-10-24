/**
 * State Manager - управление состояниями UI
 */

class StateManager {
    constructor() {
        this.currentState = 'idle';
        this.states = ['idle', 'listening', 'thinking', 'speaking'];
        this.stateIndex = 0;
    }
    
    init() {
        console.log('StateManager initialized');
        
        // Обработка кликов по облаку
        const cloudContainer = document.querySelector('.cloud-container');
        if (cloudContainer) {
            cloudContainer.addEventListener('click', () => {
                this.toggleState();
            });
        }
        
        // Обработка клавиатуры
        document.addEventListener('keydown', (e) => {
            this.handleKeyboard(e);
        });
        
        // Установка начального состояния
        this.updateUI('idle');
    }
    
    async toggleState() {
        // Переключение между idle и listening
        const newState = this.currentState === 'idle' ? 'listening' : 'idle';
        await this.setState(newState);
    }
    
    async setState(state) {
        if (!this.states.includes(state)) {
            console.error(`Invalid state: ${state}`);
            return;
        }
        
        console.log(`Changing state: ${this.currentState} → ${state}`);
        
        try {
            // Отправка состояния в Python
            const response = await bridge.setState(state);
            
            if (response.changed) {
                this.currentState = state;
                this.updateUI(state);
            }
        } catch (error) {
            console.error('Failed to set state:', error);
        }
    }
    
    updateUI(state) {
        // Обновление атрибута body
        document.body.setAttribute('data-state', state);
        
        // Обновление HUD
        const statusText = this.getStatusText(state);
        hud.updateStatus(statusText);
        
        console.log(`UI updated to state: ${state}`);
    }
    
    handleKeyboard(event) {
        switch(event.key) {
            case ' ': // Пробел - переключение idle/listening
                event.preventDefault();
                this.toggleState();
                break;
                
            case '1': // Цифра 1 - idle
                event.preventDefault();
                this.setState('idle');
                break;
                
            case '2': // Цифра 2 - listening
                event.preventDefault();
                this.setState('listening');
                break;
                
            case '3': // Цифра 3 - thinking
                event.preventDefault();
                this.setState('thinking');
                break;
                
            case '4': // Цифра 4 - speaking
                event.preventDefault();
                this.setState('speaking');
                break;
                
            case 'ArrowRight': // Следующее состояние
                event.preventDefault();
                this.nextState();
                break;
                
            case 'ArrowLeft': // Предыдущее состояние
                event.preventDefault();
                this.previousState();
                break;
        }
    }
    
    nextState() {
        this.stateIndex = (this.stateIndex + 1) % this.states.length;
        this.setState(this.states[this.stateIndex]);
    }
    
    previousState() {
        this.stateIndex = (this.stateIndex - 1 + this.states.length) % this.states.length;
        this.setState(this.states[this.stateIndex]);
    }
    
    getStatusText(state) {
        const statusTexts = {
            'idle': 'Offline',
            'listening': 'Listening...',
            'thinking': 'Thinking...',
            'speaking': 'Speaking...'
        };
        return statusTexts[state] || 'Unknown';
    }
}

// Создание глобального экземпляра
const stateManager = new StateManager();
