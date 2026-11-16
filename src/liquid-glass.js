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

// Gives the MR22 remote (without physical colour keys) a path via TVLight's app menu.
if (new URLSearchParams(window.location.search).get('tvlightOptions') === '1') {
  window.ytaf_showOptionsPanel(true);
}
