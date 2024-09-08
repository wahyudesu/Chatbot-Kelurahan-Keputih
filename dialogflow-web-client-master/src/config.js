import {
    get_gateway_url
} from './utils'

export default {
    app: {
        gateway: get_gateway_url(), // <- enter your gateway URL here, the function is just a helper function for my hosted integration. You don't normally need it
        muted: true, // <- mute microphone at start
        start_suggestions: [], // <- array of suggestions, displayed at the start screen
        fallback_lang: 'en', // <- fallback language code, if history mode or network is unavailable,
        voice: 'native' // <- voice of Text-To-Speech; for reference, see: https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisVoice/voiceURI
    },
    i18n: {
        en: {
            welcomeTitle: 'Welcome to',
            muteTitle: 'Mute',
            unMuteTitle: 'Unmute',
            inputTitle: 'Type your message',
            sendTitle: 'Send',
            microphoneTitle: 'Voice Input',
            recognitionUnavailable: 'Speech recognition is not available'
        },
        ru: {
            welcomeTitle: 'Добро пожаловать в',
            muteTitle: 'Звук',
            unMuteTitle: 'Без звука',
            inputTitle: 'Введите ваше сообщение',
            sendTitle: 'Отправить',
            microphoneTitle: 'Голосовой ввод'
        },
        de: {
            welcomeTitle: 'Wilkommen bei',
            muteTitle: 'Stumm',
            unMuteTitle: 'Nicht stumm',
            inputTitle: 'Schreiben Sie ihre Nachricht',
            sendTitle: 'Senden',
            microphoneTitle: 'Spracheingabe'
        },
        fr: {
            welcomeTitle: 'Bienvenue à',
            muteTitle: 'Son',
            unMuteTitle: 'Silent',
            inputTitle: 'Entrez votre message',
            sendTitle: 'Envoyer',
            microphoneTitle: 'Entrée vocale'
        }
    }
}
