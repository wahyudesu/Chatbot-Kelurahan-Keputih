![Dialogflow for Web v2](https://i.imgur.com/J8aTIwt.png)

# Dialogflow Client for Web

This is a unofficial Web Integration for the Dialogflow V2

This project was forked from [mishushakov](https://github.com/mishushakov/dialogflow-web-v2) project, which he develops in his free-time. If you want to support, check out his project.

## Features

- Progressive Web App (100/100 Lighthouse score)
- Accessibility Features
- Extensive Browser Support (IE8+), offline capabilities (history) and great SEO
- Familiar UI & UX, based on the official Google Assistant Design Specifications
- Dark Mode & [Theming](#theming)
- Hands-free interaction with Voice Input and Speech Feedback
- Language Independency
- Docker and Kubernetes support
- Rich-component, Webhook and Actions on Google Support ([demo](https://codepen.io/mishushakov/pen/YMwoEK))
- Floating Widget for embedding on websites ([demo](https://codepen.io/mishushakov/pen/ywWaRW))
- Based on Vue, Webpack, Babel and PostCSS
- Lightweight (build is <50KB gzipped)
- Free and fully Documented
- Made in Germany
- Recommended by [Dialogflow](https://twitter.com/Dialogflow/status/923976390201847809) and [MadeWithVueJS](https://twitter.com/MadeWithVueJS/status/1130147606666063875):

### New in this version

![](https://i.imgur.com/a2DOOeD.gif)

- New tooling: Vue CLI
- Better accessibility & audit
- Better layout, semantics and flexbox
- Better carousels
- Improved speed (~3x) & reliability
- Improved code quality and logic
- Nicer look and feel
- GitHub Pages, Actions and Registry
- Support for Dialogflow SSML
- Updated docs and demos
- More theming option: custom fonts
- Reduced bundle size (~50%)

# Installation

## Requirements

- NodeJS
- npm or Yarn
- Google Account and Dialogflow V2 Agent (if you look for V1, please use my [old repo](https://github.com/mishushakov/dialogflow-web))

## [Read the license](LICENSE)

## Clone the repository

You can use git or download from GitHub

![Clone Dialogflow for Web v2](https://imgur.com/bpHE9K6.png)

## Get the dependencies

Open the cloned folder. Then, using your favorite package manager get the dependencies

Using npm

`npm i`

Using yarn

`yarn`

## Connect your Agent

Open `config.js` and change the `gateway` variable to your Dialogflow Gateway URL

Example

```js
export default {
    app: {
        gateway: "https://lumi-webhook.herokuapp.com/"
        [...]
    }
}

[...]
```

The logo, agent name, description and available languages are fetched from Dialogflow. Change them in Dialogflow and it will sync to the UI. Please note, when adding new languages, you may have to translate some of the UI as well (`i18n` field in `config.js`)

## Developing

Open your cloned folder. Then, using your favorite package manager run the `serve` command

Using npm

`npm run serve`

Using yarn

`yarn serve`

Your default browser should open and redirect to `localhost:8080`. If the port 8080 is already in use, you can give a `port` argument to connect at specified port

Using npm

`npm run serve --port 9090`

Using yarn

`yarn serve --port 9090`

## Building

Your app will be bundled to the `dist` directory

To build it you can use npm or yarn

Using npm

`npm run build`

Using yarn

`yarn build`

## Frequently Asked Questions

- Q: I don't see any changes
- A: Make sure you **cleaned the cache** and **rebuilt the app**. In Safari go to "Develop" > "Empty Caches". In Chrome: "Developer Tools" > "Application" > "Clear storage" > "Clear site data"
