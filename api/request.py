import requests

def get_stock_data(ticker, token):
    """Busca dados da API para um único ativo"""
    url = f"https://brapi.dev/api/quote/{ticker}?token={token}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["results"][0]
    else:
        print(f"Erro ao acessar API ({ticker}): {response.status_code}")
        return None