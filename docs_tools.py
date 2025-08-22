import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/documents"]

def create_document(title: str = "Placeholder", text: str = "Placeholder") -> str:
    """Cria um Google Docs assumindo que 'token.json' já existe."""
    creds = None
    
    # Obter o diretório atual do script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(current_dir, "token.json")

    if not os.path.exists(token_path):
        return f"Erro: O arquivo 'token.json' não foi encontrado em {token_path}. Execute o script 'authenticate.py' primeiro."

    creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # Se o token estiver expirado, ele será atualizado automaticamente se possível
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    try:
        service = build("docs", "v1", credentials=creds)

        doc = service.documents().create(body={"title": title}).execute()
        document_id = doc.get("documentId")

        requests = [
            {"insertText": {"location": {"index": 1}, "text": text}}
        ]
        service.documents().batchUpdate(documentId=document_id, body={"requests": requests}).execute()

        return f"Documento criado: https://docs.google.com/document/d/{document_id}/edit"

    except HttpError as err:
        return f"Ocorreu um erro na API do Google: {err}"
    except Exception as e:
        return f"Um erro inesperado ocorreu: {e}"