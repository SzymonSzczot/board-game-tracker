import './app.css'
import App from './App.svelte'
// Import our custom CSS
import './scss/styles.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'

const app = new App({
  target: document.getElementById('app'),
})

export default app
