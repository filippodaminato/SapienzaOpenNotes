# Contributing Guide 🗑️

Benvenuto! Grazie per voler contribuire a **Sapienza Open Notes**.
Questa guida serve a mantenere ordine, chiarezza e uniformità nel repository e a facilitare la pubblicazione automatica dei PDF.

---

## 1️⃣ Struttura generale del repository

Il repository è organizzato per **faculty → level → course → instructor → lectures → lectureXX → lectureXX.tex**.
Ogni corso ha una struttura simile a questa:

```
physics/undergraduate/classical_mechanics/rossi/lectures/lecture01/lecture01.tex
physics/undergraduate/classical_mechanics/rossi/lectures/lecture02/lecture02.tex
physics/graduate/quantum_mechanics/caprara/lectures/lecture01/lecture01.tex
chemistry/undergraduate/organic_chemistry/bianchi/lectures/lecture01/lecture01.tex
```

* **lectureXX.tex**: file principale della lezione.
* **config.json**: contiene `faculty`, `level`, `title`, `professor` e `year`, usato dal workflow per generare `pdfs.json`.
* **preamble.tex**: pacchetti LaTeX, stili e comandi personalizzati.
* **media/**: cartella per file multimediali e dati raw.

---

## 2️⃣ Regole di naming

* **Cartelle lezioni**: `lectureXX/` con due cifre, es. `lecture01/`.
* **File LaTeX**: `lectureXX.tex` all’interno della cartella della lezione.
* **File multimediali**: tutti i file di supporto vanno in `media/` con nomi chiari, es. `lecture01_media_graph1.png`.
* **Immagini comuni**: nella cartella `images/` a livello di corso.

---

## 3️⃣ Contenuto dei file LaTeX

* Ogni `.tex` di lezione deve iniziare con **header standard**:

```latex
% ==============================
% Course: Classical Mechanics
% Instructor: Rossi
% Academic Year: 2023/2024
% Lecture: 01
% ==============================
```

* Usa **titoli chiari** (`\section{}`, `\subsection{}`).
* Usa sempre il **preambolo condiviso** (`preamble.tex`).
* Inserisci immagini solo con `\includegraphics{...}`.
* Evita di committare file temporanei (`*.aux`, `*.log`, etc.).

---

## 4️⃣ Configurazione del corso

Ogni corso deve avere un file `config.json` nella cartella principale del corso, con questo schema:

```json
{
  "faculty": "physics",
  "level": "undergraduate",
  "title": "Course Name",
  "professor": "Instructor Name",
  "year": "Academic Year"
}
```

Questo file viene letto dal workflow GitHub Actions per generare `pdfs.json` e aggiornare automaticamente i PDF pubblicati su GitHub Pages.

---

## 5️⃣ File multimediali e dati raw

* Tutti i file di supporto della lezione vanno in `media/`.
* Non è necessario che siano inclusi nel PDF.
* Se i file sono grandi (>10 MB), valuta [Git LFS](https://git-lfs.github.com/).

---

## 6️⃣ Workflow di compilazione e pubblicazione

* Ogni push su `main` compila i `lectureXX.tex` dei corsi e genera PDF nella cartella `public/`.
* Il workflow legge i `config.json` dei corsi e crea `pdfs.json`, contenente:

```json
[
  {
    "faculty": "physics",
    "level": "undergraduate",
    "title": "Classical Mechanics",
    "professor": "Prof. Rossi",
    "year": "2023/2024",
    "file_name": "classical_mechanics_rossi.pdf"
  }
]
```

* `pdfs.json` e i PDF vengono pubblicati su GitHub Pages.
* Il sito principale (`index.html`) legge `pdfs.json` e mostra i PDF disponibili, titolo, professore, anno, livello e faculty.

---

## 7️⃣ Contributi e pull request

1. Fai un **fork** del repository.
2. Crea un **branch chiaro**, es. `classical_mechanics-lecture03` o `organic_chemistry-media`.
3. Aggiungi o modifica file seguendo le regole sopra.
4. Aggiorna `main.tex` se aggiungi nuove lezioni:

```latex
\input{lectures/lectureXX/lectureXX.tex}
```

5. Manda una **pull request** con un messaggio chiaro:

   * `Added Lecture 3 notes for Classical Mechanics`
   * `Added media files for Lecture 2 of Organic Chemistry`

---

## 8️⃣ Pulizia e compilazione

* Tutti i file temporanei LaTeX (`*.aux`, `*.log`, etc.) **non devono essere committati**.
* Compila sempre `lectureXX.tex` per verificare che tutto funzioni.
* Puoi usare il **workflow GitHub Actions**, il **Makefile** o lo **script Python** fornito per compilare automaticamente tutti i corsi e aggiornare `pdfs.json`.

---

Grazie per contribuire a mantenere gli appunti **ordinati, coerenti e condivisibili**! 🚀
