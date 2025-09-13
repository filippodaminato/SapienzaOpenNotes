# Sapienza Open Notes 📘✨

Raccolta collaborativa di appunti, esercizi e risorse per i corsi universitari alla Sapienza Università di Roma.
Strutturato per **faculty → level (undergraduate/graduate) → course → instructor → lectures**, con appunti in **LaTeX** e materiali multimediali.
I PDF compilati sono disponibili anche online tramite il sito web del progetto: [https://filippodaminato.github.io/SapienzaOpenNotes/](https://filippodaminato.github.io/SapienzaOpenNotes/)

---

## 🚀 Obiettivi

* Creare un archivio accessibile e collaborativo per studenti della Sapienza.
* Fornire appunti ordinati e ben formattati in LaTeX.
* Permettere a chiunque di contribuire con correzioni, figure, esempi ed esercizi.
* Rendere disponibili i PDF compilati direttamente online per lo studio.

---

## 👁️ Struttura cartelle

* `<faculty>/<level>/<course>/<instructor>/lectures`
  `/<lectureXX>`
    * `lectureXX.tex` → file LaTeX con appunti
    * `media/` → grafici, schemi, figure
* `main.tex` → file principale che importa tutte le lezioni del corso
* `config.json` → configurazione del corso (facoltà, titolo, professore, anno, ...)
* `preamble.tex` → preambolo condiviso

**Esempi concreti:**

```
physics/undergraduate/classical_mechanics/rossi/lectures/lecture01/lecture01.tex
physics/undergraduate/classical_mechanics/rossi/lectures/lecture02/lecture02.tex
physics/graduate/quantum_mechanics/caprara/lectures/lecture01/lecture01.tex
chemistry/undergraduate/organic_chemistry/bianchi/lectures/lecture01/lecture01.tex
```

---

## 🛠️ Setup su VS Code + LaTeX Workshop

Questo progetto è pensato per essere usato con **VS Code** e l’estensione **LaTeX Workshop**.
Per una guida completa all’installazione di VS Code, LaTeX Workshop e LaTeX sul tuo sistema operativo, consultare questo link:

[Guida VS Code + LaTeX Workshop](https://mathjiajia.github.io/vscode-and-latex/)

---

## 🛠️ Come contribuire

1. Fai un **fork** del progetto.
2. Crea un **branch** chiaro con il nome del corso/lezione su cui lavori.
3. Aggiungi o modifica i tuoi file seguendo le linee guida.
4. Manda una **pull request** 🚀

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) per ulteriori dettagli su struttura, naming e regole di commit.
Tutti i contributori saranno citati nella pagina **Contributors** del sito.

---

## 🌐 Sito web del progetto

I PDF compilati e aggiornati automaticamente sono disponibili su:
[https://filippodaminato.github.io/SapienzaOpenNotes/](https://filippodaminato.github.io/SapienzaOpenNotes/)

---

## 📜 Licenza

Questo progetto è rilasciato sotto licenza **MIT**.
Puoi usarlo, modificarlo e ridistribuirlo liberamente, a patto di includere la licenza originale.
