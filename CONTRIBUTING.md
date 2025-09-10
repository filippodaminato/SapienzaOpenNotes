# Guida per contribuire 🗑️

Benvenuto! Grazie per voler contribuire a **Sapienza Physics Notes**.
Questa guida serve a mantenere ordine, chiarezza e uniformità nel repository.

---

## 1️⃣ Struttura generale del repository

Il repository è organizzato per **anno ➔ corso ➔ lezioni**.
Ogni corso ha una struttura simile a questa:

```
Corso/
│── main.tex           # File principale che importa tutte le lezioni
│── preamble.tex       # Preambolo condiviso per uniformare lo stile
│── lezioni/
│   ├── lezione01/
│   │   ├── lezione01.tex  # Appunti della lezione
│   │   └── media/          # File multimediali e dati raw (grafici, schemi, dataset)
│   ├── lezione02/
│   │   ├── lezione02.tex
│   │   └── media/
│   └── ...
│── immagini/          # Eventuali immagini comuni al corso
```

* **main.tex**: importa tutte le lezioni con `\input{lezioni/lezioneXX/lezioneXX.tex}`.
* **preamble.tex**: contiene pacchetti LaTeX standard, stili e comandi personalizzati.
* **lezioni/**: ogni lezione ha la propria cartella con `.tex` e `media/`.

---

## 2️⃣ Regole di naming

* **Cartelle lezioni**: `lezioneXX/` con due cifre, es. `lezione01/`.
* **File LaTeX**: `lezioneXX.tex` all’interno della cartella della lezione.
* **File multimediali**: tutti i file di supporto vanno in `media/`.

  * Esempi: `grafico1.png`, `dati_raw.xlsx`.
  * Se possibile, usa nomi chiari e coerenti con la lezione: `lezione01_media_grafico1.png`.
* **Immagini comuni** al corso possono stare in `immagini/` a livello di corso.

---

## 3️⃣ Contenuto dei file LaTeX

* Ogni `.tex` di lezione deve iniziare con un **header standard**:

```latex
% ==============================
% Corso: Analisi 1
% Professore: Rossi
% Anno Accademico: 2023/2024
% Lezione: 01
% ==============================
```

* Usa **titoli chiari** (`\section{}`, `\subsection{}`) e commenti dove necessario.
* Usa sempre **preambolo condiviso** (`preamble.tex`).
* Inserisci immagini solo con `\includegraphics{...}` se vuoi che compaiano nel PDF.
* Evita di committare file temporanei di compilazione (`*.aux`, `*.log`, etc.).

---

## 4️⃣ File multimediali e dati raw

* Tutti i file di supporto della lezione vanno in `media/`.
* Non è necessario che siano inclusi nel PDF, ma servono come **backup o riferimento**.
* Se i file sono grandi (>10 MB), valuta l’uso di [Git LFS](https://git-lfs.github.com/) per non appesantire il repository.

---

## 5️⃣ Contributi e pull request

1. Fai un **fork** del repository.
2. Crea un **branch** chiaro, es. `analisi1-lezione03` o `fisica1-media`.
3. Aggiungi o modifica file seguendo le regole sopra.
4. Aggiorna `main.tex` se aggiungi nuove lezioni:

```latex
\input{lezioni/lezioneXX/lezioneXX.tex}
```

5. Manda una **pull request** con un messaggio chiaro:

   * Esempio: `"Aggiunti appunti Lezione 3 di Analisi 1"`
   * Oppure: `"Aggiunti file multimediali Lezione 2 di Fisica 1"`

---

## 6️⃣ Pulizia e compilazione

* Tutti i file temporanei generati da LaTeX (`*.aux`, `*.log`, `*.toc`, etc.) **non devono essere committati**.
* Compila sempre `main.tex` per verificare che tutto funzioni.
* Puoi usare il **Makefile** o lo **script Python** fornito per compilare automaticamente tutti i corsi.

---

Grazie per contribuire a mantenere gli appunti **ordinati, coerenti e condivisibili**! 🚀
