# Contributing

I contributi e le collaborazioni sono i benvenuti! Il progetto è **attivamente sviluppato e mantenuto**: monitoro regolarmente il repository e rispondo in breve tempo a issue, domande e Pull Request. 

Se desideri contribuire, ti invitiamo a seguire le linee guida descritte in questo documento per garantire la qualità e la manutenibilità del codice.

---

## 📖 Documentazione di Riferimento

Prima di iniziare, ti invitiamo a consultare la documentazione ufficiale del progetto per comprendere la struttura generale e le convenzioni adottate:

👉 **[Consulta la Documentazione del Progetto](http://SerialXProject.github.io/serialx-docs)**

---

## ⚠️ Regola Fondamentale per il Core

Per questa repository in particolare, vige una regola tassativa riguardante il modulo **Core**:

- **Nessun `print` nel Core:** Il core del progetto deve essere completamente **silenzioso**. 
- Non devono essere inserite istruzioni di stampa a schermo o output diretto (`print`) nei moduli core.
- Il loro unico compito è svolgere l'elaborazione richiesta.
- In caso di errore o stato imprevisto, la comunicazione deve avvenire **esclusivamente tramite il lancio di eccezioni** (`raise`).
- *(Nota per sviluppi futuri)*: L'integrazione del tracciamento tramite un **logger** dedicato è prevista per le prossime versioni. Per ora, si prega di non aggiungere chiamate di log o di stampa custom all'interno del Core.

> **Esempio:**
> - ❌ *Sbagliato:* `if not data: print("Errore: dati mancanti")`
> - ✅ *Corretto:* `if not data: raise ValueError("Dati mancanti")`

---

## 🚀 Come Contribuire

1. **Fai un Fork** della repository.
2. **Crea un branch** per la tua funzionalità o bugfix (`git checkout -b feature/nuova-funzionalita`).
3. **Rispetta lo stile di codice** e le regole del Core descritte sopra.
4. **Fai il commit** delle tue modifiche con messaggi chiari e descrittivi (`git commit -m 'Aggiunta nuova funzionalità X'`).
5. **Fai il push** sul tuo branch (`git push origin feature/nuova-funzionalita`).
6. **Apri una Pull Request** descrivendo chiaramente le modifiche apportate.

Riceverai un riscontro o un feedback sulla tua Pull Request in tempi brevi! Grazie per il tuo supporto al progetto.