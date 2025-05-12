import requests

def get_stock_data(ticker, token):
    """Busca dados da API para um único ativo"""
    url = f"https://brapi.dev/api/quote/{ticker}?token={token}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()["results"][0]
        return {
            "nome": data.get("longName", "Desconhecido"),
            "simbolo": data.get("symbol", simbolo),
            "preco": data.get("regularMarketPrice", 0),
            "variacao": data.get("regularMarketChangePercent", 0),
            "logo": data.get("logourl", "")
        }
        return Nome
    else:
        print(f"Erro ao acessar API ({ticker}): {response.status_code}")
        return None