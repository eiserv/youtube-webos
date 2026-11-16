import { configRead, configAddChangeListener } from './config.js';
import './liquid-glass.css';

// Deliberately no animation loop, observers or blur passes on the TV GPU.
function applyTheme() {
  document.documentElement.classList.toggle(
    'tvlight-glass',
    configRead('liquidGlass')
  );
}
configAddChangeListener('liquidGlass', applyTheme);
applyTheme();
