"use strict";
Object.defineProperty(exports, "__esModule", {
    value: true
});
var Client = /** @class */ (function () {
    /**
     * Dialogflow Gateway Client
     * @param endpoint - URL pointing to the Agent on Dialogflow Gateway
     * ```typescript
     * const client = new Client('https://dialogflow-web-v2.gateway.dialogflow.cloud.ushakov.co')
     * ```
     */
    function Client(endpoint) {
        var _this = this;
        this.endpoint = endpoint;
        /**
         *  Get Agent linked to this Client
         * ```typescript
         * const client = new Client('https://dialogflow-web-v2.gateway.dialogflow.cloud.ushakov.co')
         * client.get()
         * .then(agent => {
         *   console.log(agent)
         * })
         * .catch(error => {
         *   // Handle error
         * })
         * ```
         */
        this.get = function () {
            return new Promise(function (resolve, reject) {
                if (!_this.agent) {
                    fetch(`${_this.endpoint}/agent`)
                        .then(function (res) {
                            return res.json();
                        })
                        .then(function (agent) {
                            if (agent.error)
                                reject(new Error(agent.error));
                            resolve(agent);
                        })
                        .catch(function (error) {
                            return reject(error);
                        });
                } else
                    resolve(_this.agent);
            });
        };
        /**
         * Send request to Dialogflow Gateway
         * @param request - Request body
         * ```typescript
         * const client = new Client('https://dialogflow-web-v2.gateway.dialogflow.cloud.ushakov.co')
         * client.send({
         *   session: 'test',
         *   queryInput: {
         *     text: {
         *       text: 'Hello',
         *       languageCode: 'en'
         *     }
         *   }
         * })
         * .then(response => {
         *   console.log(response)
         * })
         * .catch(error => {
         *   // Handle error
         * })
         * ```
         */
        this.send = function (request) {
            return new Promise(function (resolve, reject) {
                fetch(`${_this.endpoint}/gateway`, {
                        method: 'POST',
                        body: JSON.stringify(request),
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(function (res) {
                        return res.json();
                    })
                    .then(function (message) {
                        if (message.error)
                            reject(new Error(message.error));
                        resolve(message);
                    })
                    .catch(function (error) {
                        return reject(error);
                    });
            });
        };
        this.endpoint = endpoint;
    }
    return Client;
}());
exports.Client = Client;
