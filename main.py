import requests

def get_http_data(host: str):
    try:
        
        url = host.replace("\\", "/")

        response = requests.get(url)

        data = {
            'headers': dict(response.headers),
            'content': response.text,
            'cookies': response.cookies.get_dict()
        }

        return data

    except requests.RequestException as e:
        return {'erro': str(e)}

if __name__ == "__main__":
    endpoint = "ultimas"
    host = f"https://www.uol.com.br\\{endpoint}"

    dados = get_http_data(host)

    if 'erro' in dados:
        print("Erro:", dados['erro'])
    else:
        print("\n🔸 Headers:\n", dados['headers'])
        print("\n🔸 Cookies:\n", dados['cookies'])
        print("\n🔸 Conteúdo (início):\n", dados['content'][:1000])  # Mostra só os primeiros 1000 caracteres
