/**
 * Bridge - связь между JavaScript и Python API
 */

class AiryBridge {
    constructor() {
        this.api = null;
        this.ready = false;
        this.mockMode = false;
    }
    
    async init() {
        console.log('Initializing bridge...');
        
        // Проверяем наличие PyWebView API
        if (window.pywebview && window.pywebview.api) {
            this.api = window.pywebview.api;
            console.log('PyWebView API detected');
        } else {
            console.warn('PyWebView API not found, using mock mode');
            this.api = this.createMockAPI();
            this.mockMode = true;
        }
        
        // Проверка связи
        try {
            const response = await this.api.ping();
            this.ready = response.ok;
            console.log('Bridge ready:', response);
            return response;
        } catch (error) {
            console.error('Bridge initialization failed:', error);
            return { ok: false, error: error.message };
        }
    }
    
    // === API Methods ===
    
    async ping() {
        return await this.api.ping();
    }
    
    async getState() {
        return await this.api.get_state();
    }
    
    async setState(state) {
        console.log(`Setting state to: ${state}`);
        return await this.api.set_state(state);
    }
    
    async sendCommand(text) {
        return await this.api.send_command(text);
    }
    
    async getConfig() {
        return await this.api.get_config();
    }
    
    async startListening() {
        return await this.api.start_listening();
    }
    
    async stopListening() {
        return await this.api.stop_listening();
    }
    
    async log(message, level = 'info') {
        return await this.api.log(message, level);
    }
    
    // === Mock API для тестирования в браузере ===
    
    createMockAPI() {
        let mockState = 'idle';
        
        return {
            ping: async () => ({ 
                ok: true, 
                mock: true, 
                version: '0.1.0',
                core: false 
            }),
            
            get_state: async () => ({ 
                state: mockState 
            }),
            
            set_state: async (state) => {
                mockState = state;
                console.log(`[Mock] State changed to: ${state}`);
                return { 
                    state: mockState, 
                    changed: true,
                    timestamp: new Date().toISOString()
                };
            },
            
            send_command: async (text) => ({
                received: text,
                response: `Mock echo: ${text}`,
                mock: true
            }),
            
            get_config: async () => ({
                version: '0.1.0',
                theme: 'default',
                language: 'ru',
                core_connected: false,
                mock: true
            }),
            
            start_listening: async () => {
                mockState = 'listening';
                return { listening: true };
            },
            
            stop_listening: async () => {
                mockState = 'idle';
                return { listening: false };
            },
            
            log: async (message, level) => {
                console.log(`[${level.toUpperCase()}] ${message}`);
                return { logged: true };
            }
        };
    }
}

// Создание глобального экземпляра
const bridge = new AiryBridge();
