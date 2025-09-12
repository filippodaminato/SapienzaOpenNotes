# Guida per contribuire 🗑️

Benvenuto! Grazie per voler contribuire a **Sapienza Physics Open Notes**.  
Questa guida serve a mantenere ordine, chiarezza e uniformità nel repository e a facilitare la pubblicazione automatica dei PDF.

---

## 1️⃣ Struttura generale del repository

Il repository è organizzato per **anno ➔ corso ➔ lezioni**.  
Ogni corso ha una struttura simile a questa:

```
Corso/
│── main.tex           # File principale che importa tutte le lezioni
│── config.json        # Configurazione del corso (titolo, professore, anno)
│── preamble.tex       # Preambolo condiviso per uniformare lo stile
│── lezioni/
│   ├── lezione01/
│   │   ├── lezione01.tex  # Appunti della lezione
│   │   └── media/          # File multimediali e dati raw
│   ├── lezione02/
│   │   ├── lezione02.tex
│   │   └── media/
│   └── ...
│── immagini/          # Eventuali immagini comuni al corso
```

- **main.tex**: importa tutte le lezioni (`\input{lezioni/lezioneXX/lezioneXX.tex}`).  
- **config.json**: contiene `title`, `professor` e `year`, usato dal workflow per generare `pdfs.json`.  
- **preamble.tex**: pacchetti LaTeX, stili e comandi personalizzati.  
- **lezioni/**: ogni lezione ha `.tex` e cartella `media/`.

---

## 2️⃣ Regole di naming

- **Cartelle lezioni**: `lezioneXX/` con due cifre, es. `lezione01/`.  
- **File LaTeX**: `lezioneXX.tex` all’interno della cartella della lezione.  
- **File multimediali**: tutti i file di supporto vanno in `media/` con nomi chiari, es. `lezione01_media_grafico1.png`.  
- **Immagini comuni**: nella cartella `immagini/` a livello di corso.  

---

## 3️⃣ Contenuto dei file LaTeX

- Ogni `.tex` di lezione deve iniziare con **header standard**:

```latex
% ==============================
% Corso: Analisi 1
% Professore: Rossi
% Anno Accademico: 2023/2024
% Lezione: 01
% ==============================
```

- Usa **titoli chiari** (`\section{}`, `\subsection{}`).  
- Usa sempre il **preambolo condiviso** (`preamble.tex`).  
- Inserisci immagini solo con `\includegraphics{...}`.  
- Evita di committare file temporanei (`*.aux`, `*.log`, etc.).

---

## 4️⃣ Configurazione del corso

Ogni corso deve avere un file `config.json` nella cartella principale del corso, con questo schema:

```json
{
  "title": "Nome del corso",
  "professor": "Nome del professore",
  "year": "Anno accademico"
}
```

Questo file viene letto dal workflow GitHub Actions per generare `pdfs.json` e aggiornare automaticamente i PDF pubblicati su GitHub Pages.

---

## 5️⃣ File multimediali e dati raw

- Tutti i file di supporto della lezione vanno in `media/`.  
- Non è necessario che siano inclusi nel PDF.  
- Se i file sono grandi (>10 MB), valuta [Git LFS](https://git-lfs.github.com/).  

---

## 6️⃣ Workflow di compilazione e pubblicazione

- Ogni push su `main` compila i `main.tex` dei corsi e genera PDF nella cartella `public/`.  
- Il workflow legge i `config.json` dei corsi e crea `pdfs.json`, contenente:

```json
[
  {
    "title": "Meccanica",
    "professor": "Prof. Rossi",
    "year": "2023/2024",
    "file_name": "Meccanica.pdf"
  }
]
```

- `pdfs.json` e i PDF vengono pubblicati su GitHub Pages.  
- Il sito principale (`index.html`) legge `pdfs.json` e mostra i PDF disponibili, titolo, professore e anno.

---

## 7️⃣ Contributi e pull request

1. Fai un **fork** del repository.  
2. Crea un **branch chiaro**, es. `analisi1-lezione03` o `fisica1-media`.  
3. Aggiungi o modifica file seguendo le regole sopra.  
4. Aggiorna `main.tex` se aggiungi nuove lezioni:

```latex
\input{lezioni/lezioneXX/lezioneXX.tex}
```

5. Manda una **pull request** con un messaggio chiaro:

   - `"Aggiunti appunti Lezione 3 di Analisi 1"`  
   - `"Aggiunti file multimediali Lezione 2 di Fisica 1"`

---

## 8️⃣ Pulizia e compilazione

- Tutti i file temporanei LaTeX (`*.aux`, `*.log`, etc.) **non devono essere committati**.  
- Compila sempre `main.tex` per verificare che tutto funzioni.  
- Puoi usare il **workflow GitHub Actions**, il **Makefile** o lo **script Python** fornito per compilare automaticamente tutti i corsi e aggiornare `pdfs.json`.  

---

Grazie per contribuire a mantenere gli appunti **ordinati, coerenti e condivisibili**! 🚀
