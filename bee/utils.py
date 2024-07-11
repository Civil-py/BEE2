# utils.py
import requests
from django.conf import settings

def cognito_login(request):
    code = request.GET.get('code')
    if not code:
        return None

    token_url = f'https://{settings.AWS_COGNITO_REGION}.amazoncognito.com/oauth2/token'
    userinfo_url = f'https://{settings.AWS_COGNITO_REGION}.amazoncognito.com/oauth2/userInfo'

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': settings.AWS_COGNITO_REDIRECT_URL,
        'client_id': settings.AWS_COGNITO_APP_CLIENT_ID,
        'client_secret': settings.AWS_COGNITO_APP_CLIENT_SECRET,
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get('access_token')

        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        userinfo_response = requests.get(userinfo_url, headers=headers)
        if userinfo_response.status_code == 200:
            return userinfo_response.json()
    return None



mongo_password = "fbwWzJSvLL9D3p6Q"
connection = 'mongosh "mongodb+srv://cluster0.jzcsqkh.mongodb.net/" --apiVersion 1 --username civilmotha'

mongodb_uri = "mongodb+srv://civilmotha:<fbwWzJSvLL9D3p6Q>@cluster0.jzcsqkh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"