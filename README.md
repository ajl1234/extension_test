# extension_test

Instructions: 

1. Run uvicorn {FILENAME}:app --reload

2. Go to https://github.com/settings/apps and create a new app.
3. You can set your callback URL to be https://github.com
4. Deactivate webhook
5. Go into Account Permissions and then enable Read-Only access for Copilot Chat and Copilot Editor Context
6. Now create Github App
7. Run ngrok http 8000 to expose local dev server on the internet and retrieve the forwarding url
8. Take the forward url and paste it in the Agent definition field under the Copilot tab and append "completion" to the url: {forward_url}/completion
9. Now install the app and use the @ symbol to reference the github app in copilot chat


Run ngrok http 8000 and then retrieve forwarding url and place in URL field of Agent definition
