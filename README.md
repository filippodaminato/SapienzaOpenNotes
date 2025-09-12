# Sapienza Open Notes 📘✨

Raccolta collaborativa di appunti, esercizi e risorse per i corsi di Fisica alla Sapienza Università di Roma.
Strutturato per **anni → corsi → lezioni**, con appunti in **LaTeX** e materiali multimediali.

---

## 🚀 Obiettivi

* Creare un archivio accessibile e collaborativo per studenti di Fisica.
* Fornire appunti ordinati e ben formattati in LaTeX.
* Permettere a chiunque di contribuire con correzioni, figure, esempi ed esercizi.

---

## 📂 Struttura cartelle

* `PrimoAnno/Corso/lezioni/`

  * `lezioneXX.tex` → file LaTeX con appunti
  * `immagini/` → grafici, schemi, figure
  * `appunti.pdf` → versione compilata (opzionale)
* `main.tex` → file principale che importa tutte le lezioni
* `preamble.tex` → preambolo condiviso
* `SecondoAnno/`, `TerzoAnno/` → stessi schemi

---

## 🛠️ Setup su VS Code + LaTeX Workshop

Questo progetto è pensato per essere usato con **VS Code** e l’estensione **LaTeX Workshop**.
Per una guida completa all’installazione di VS Code, LaTeX Workshop e LaTeX sul tuo sistema operativo, consultare questo link:

[Guida VS Code + LaTeX Workshop](https://mathjiajia.github.io/vscode-and-latex/)

---

<!-- ## 🛠️ Come compilare

* **Compilazione singolo corso**:

  ```bash
  make course COURSE=Analisi1
  ```

  oppure

  ```bash
  python build.py Analisi1
  ```

* **Compilazione di tutti i corsi**:

  ```bash
  make
  ```

  oppure

  ```bash
  python build.py
  ```

--- -->

## 🛠️ Come contribuire

1. Fai un **fork** del progetto.
2. Crea un **branch** con il nome del corso/lezione su cui lavori.
3. Aggiungi o modifica i tuoi file.
4. Manda una **pull request** 🚀

Vedi [CONTRIBUTING.md](CONTRIBUTING.md) per le linee guida.

---

## 📜 Licenza

Questo progetto è rilasciato sotto licenza **MIT**.
Puoi usarlo, modificarlo e ridistribuirlo liberamente, a patto di includere la licenza originale.
