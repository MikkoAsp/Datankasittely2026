import requests

def fetch_data(api_url: str) -> list | None:
    try:
        response = requests.get(api_url, timeout=15)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        print("Palvelin ei vastannut tarpeeksi nopeasti")
    except requests.exceptions.HTTPError as e:
        print("Palvelin palautti virheen:", e)
    except requests.exceptions.JSONDecodeError:
        print("Ei palautettu JSON")
    except requests.exceptions.RequestException as e:
        print("Virhe tapahtui:", e)

    return None