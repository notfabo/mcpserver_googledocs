import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# O mesmo escopo do seu script original
SCOPES = ["https://www.googleapis.com/auth/documents"]

def authenticate():
    """Executa o fluxo de autenticação interativo e salva o token."""
    creds = None
    # Se o token.json já existe, tenta carregá-lo
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # Se não há credenciais válidas, pede para o usuário logar.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Atualizando token expirado...")
            creds.refresh(Request())
        else:
            print("Nenhum token válido encontrado. Por favor, autorize o acesso.")
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Salva as credenciais para o próximo uso
        with open("token.json", "w") as token:
            token.write(creds.to_json())
        print("Autenticação bem-sucedida! O arquivo 'token.json' foi criado.")
    else:
        print("Já autenticado com um token válido.")

if __name__ == "__main__":
    authenticate()