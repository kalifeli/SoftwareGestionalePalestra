# SoftwareGestionalePalestra

## Introduzione
Il seguente progetto ha come obiettivo la creazione di un’applicazione desktop pensata per la gestione completa di una palestra/centro fitness.

Al suo interno permette di:

- **Gestire i clienti** (anagrafica, certificati medici)
- **Amministrare i corsi** (Boxe, Pilates, ecc.) e i pacchetti di abbonamento
- **Creare, rinnovare e sospendere abbonamenti** con calcolo automatico delle date di inizio/fine e dello stato
- **Tenere traccia di entrate e uscite finanziarie** legate a iscrizioni, rinnovi e spese varie
- **Assegnare personal trainer e gestire la scheda di ogni cliente**

## Caratteristiche principali

- **Architettura MVC**: separation of concerns tra controller, model e view
- **Pattern Dao**: permette la separazione della logica di business e dell'interazione con il database
- **Persistenza** in tempo reale su Firebase Firestore
- **Test automatici** con unittest e unittest.mock per validare la logica di business
- **Modellazione UML** realizzata con Enterprise Architect (diagrammi di classi, componenti, stati…)

## Tecnlogie utilizzate
- Python 3.9+
- Firebase Firestore (NoSQL, sincronizzazione real-time)
- unittest / MagicMock per i test unitari
- Enterprise Architect per i modelli UML
- Visual Studio Code come IDE

## Come iniziare

1. **Clona il repository**
2. **Crea e attiva un Virtual Enviroment in Python**
  ```python
  python3 -m venv .venv
  source .venv/bin/activate
  ```
3. **Installa le dipendenze**
   ```python
   pip install -r utils/requirements.txt
   ```
4. **Crea un nuovo progetto Firebase** e scarica dalle impostazioni del progetto le credenziali di autenticazione.
5. **Inserisci le credenzial**i nella cartella root del progetto
6. Modifica se necessario la classe utils/firebase_client.py
7. **Avvia l'applicazione**
