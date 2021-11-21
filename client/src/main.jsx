import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import App from './App'
import Home from "./Home"
import { Auth0Provider } from "@auth0/auth0-react"
import Header from "./Header"
import { Route } from "wouter"

ReactDOM.render(
  <React.StrictMode>
  <Auth0Provider
    domain="energify.us.auth0.com"
    clientId="MIKYklJLL5kDfvfCvzzpjaOlVZXXdPNM"
    redirectUri={window.location.origin}
  >
    <Header/>
    <Route path="/">
      <Home /> 
    </Route>
    <Route path="/app">
      <App />
    </Route>
  </Auth0Provider>
  </React.StrictMode>,
  document.getElementById('root')
)
