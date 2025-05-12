def generate_html(stock_data, output_file="banner.html"):
    """Cria um banner visual em HTML para exibir os dados"""
    html_template = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <title>Banner de Ações</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; }}
            .banner {{ background: #f4f4f4; padding: 20px; }}
            .stock {{ font-size: 24px; font-weight: bold; }}
            .price {{ font-size: 20px; color: #0077b6; }}
        </style>
    </head>
    <body>
        <div class="banner">
            <div class="stock">{stock_data["symbol"]}</div>
            <div class="price">Preço: R$ {stock_data["regularMarketPrice"]}</div>
        </div>
    </body>
    </html>
    """
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_template)
    print(f"Banner HTML gerado: {output_file}")