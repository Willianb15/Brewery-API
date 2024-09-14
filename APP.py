import requests
import sqlite3

def get_brewery():
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(url)
    data = response.json()
    return data

def save_brewery(brewery):
    conn = sqlite3.connect("API_DB.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT OR REPLACE INTO Cervejaria (id, nome, tipo_de_cervejaria, cidade, país, estado)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (brewery.get("id"), brewery.get("name"), brewery.get("brewery_type"), brewery.get("city"), brewery.get("country"), brewery.get("state_province")))
    conn.commit()
    conn.close()

def main():
    breweries = get_brewery()
    for brewery in breweries:
        save_brewery(brewery)

if __name__ == "__main__":
    main()