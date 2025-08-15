# Pientere Tuinen – Home Assistant Integratie

Deze integratie haalt bodemtemperatuur en bodemvochtigheid op van je Pientere Tuinen sensor via de GoodCitySense API.

## Installatie via HACS

### Aanbevolen installatie:
Gebruik deze button om de Pientere Tuinen integratie toe te voegen via [HACS](https://my.home-assistant.io/redirect/supervisor_addon/?addon=cb646a50_get&repository_url=https%3A%2F%2Fgithub.com%2Fhacs%2Faddons).

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=roelvanderkraan&repository=pientere-tuinen-home-assistant&category=integration)

### Handmatig instellen
1. Open **HACS** in Home Assistant.
2. Ga naar **Integraties** → **Custom repositories**.
3. Voeg deze repository toe als type **Integration**.
4. Installeer de integratie via HACS.

## Integratie toevoegen
1. Ga naar **Instellingen → Apparaten & diensten** en voeg de integratie toe.
1. Vul je API-sleutel in. Je vindt deze na inloggen op [Pientere Tuinen API](https://portal.goodcitysense.nl/api-subscriptions).

## Functies
- Bodemtemperatuur (°C)
- Bodemvochtigheid (%)
- Extra metadata: meetmoment, locatie

---

## Vereisten
- Home Assistant 2025.1.0 of nieuwer
- Actieve Pientere Tuinen sensor
- Geldige API-sleutel

## Ondersteuning
Maak issues aan op de [issue tracker](https://github.com/JE_GITHUB_NAAM/pientere_tuinen/issues).
