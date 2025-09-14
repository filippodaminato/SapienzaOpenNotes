#!/usr/bin/env python3
import os
import subprocess
import json
from pathlib import Path

# Percorsi principali
LATEX_ROOT = Path("latex_courses")
PUBLIC_DIR = Path("public")
PDF_JSON = PUBLIC_DIR / "pdfs.json"

# Crea cartella pubblica se non esiste
PUBLIC_DIR.mkdir(exist_ok=True)

# --- Funzioni di utilità ---

def get_all_courses():
    """Ritorna tutte le cartelle dei corsi contenenti main.tex"""
    return [p.parent for p in LATEX_ROOT.rglob("main.tex")]

def get_changed_courses():
    """Ritorna corsi modificati rispetto all'ultimo commit"""
    try:
        output = subprocess.check_output(["git", "diff", "--name-only", "HEAD~1", "HEAD"], text=True)
        changed_files = [line.strip() for line in output.splitlines() if line.strip().endswith(".tex")]
        changed_courses = sorted(set([Path(f).parent.parent for f in changed_files]))
        return changed_courses
    except subprocess.CalledProcessError:
        return []

def compile_course(course_dir):
    """Compila main.tex del corso usando latexmk in Docker"""
    print(f"📄 Compilo corso: {course_dir}")
    try:
        subprocess.run([
            "docker", "run", "--rm",
            "-v", f"{os.getcwd()}:/data",
            "-w", f"/data/{course_dir}",
            "texlive/texlive:latest",
            "latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"
        ], check=True)
    except subprocess.CalledProcessError:
        print(f"⚠️ Compilazione fallita per {course_dir}, PDF esistente se presente rimarrà")

def get_metadata(course_dir):
    """Estrae metadata dal config.json e da git"""
    config_file = course_dir / "config.json"
    if config_file.exists():
        with open(config_file) as f:
            config = json.load(f)
        title = config.get("title", "Corso sconosciuto")
        faculty = config.get("faculty", "N/D")
        level = config.get("level", "N/D")
        professor = config.get("professor", "N/D")
        semester = config.get("semester", "N/D")
        year = config.get("year", "N/D")
    else:
        title = "Corso sconosciuto"
        faculty = level = professor = semester = year = "N/D"

    # Metadata git
    last_edit_date = subprocess.check_output(
        ["git", "log", "-1", "--format=%cs", "--", str(course_dir)],
        text=True
    ).strip()

    contributors_raw = subprocess.check_output(
        ["git", "log", "--format=%an|%ae", "--", str(course_dir)],
        text=True
    ).splitlines()
    contributors_set = sorted(set(contributors_raw))
    contributors = [
        {"name": n.split("|")[0],
         "profile_url": "https://github.com/" + n.split("|")[1].split("@")[0]}
        for n in contributors_set
    ]

    return {
        "faculty": faculty,
        "semester": semester,
        "level": level,
        "title": title,
        "professor": professor,
        "year": year,
        "last_edit_date": last_edit_date,
        "contributors": contributors
    }

# --- Main ---

all_courses = get_all_courses()
changed_courses = get_changed_courses()
print(f"🔹 Totale corsi: {len(all_courses)}, corsi modificati: {len(changed_courses)}")

pdf_entries = []

for course_dir in all_courses:
    relative_path = course_dir.relative_to(LATEX_ROOT)
    sanitized_name = f"latex_courses_{relative_path}".replace("/", "_")
    pdf_file = PUBLIC_DIR / f"{sanitized_name}.pdf"

    # Decide se compilare
    compile_needed = False
    if course_dir in changed_courses:
        compile_needed = True
    elif not pdf_file.exists() or not (course_dir / "main.pdf").exists():
        compile_needed = True

    if compile_needed:
        compile_course(course_dir)

    # Copia PDF nella cartella pubblica
    main_pdf = course_dir / "main.pdf"
    if main_pdf.exists():
        subprocess.run(["cp", str(main_pdf), str(pdf_file)])

    # Aggiungi metadata JSON
    metadata = get_metadata(course_dir)
    metadata["file_name"] = pdf_file.name
    pdf_entries.append(metadata)

# Salva il JSON finale
with open(PDF_JSON, "w") as f:
    json.dump(pdf_entries, f, indent=2, ensure_ascii=False)

print(f"✅ PDF e JSON aggiornati in {PUBLIC_DIR}")
