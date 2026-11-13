import os
import re
import json
import datetime
from pathlib import Path

# Paths definition
BASE_DIR = Path("/workspace/scratch/llm_wiki")
RAW_DIR = BASE_DIR / "raw"
WIKI_DIR = BASE_DIR / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
ENTITIES_DIR = WIKI_DIR / "entities"
CONCEPTS_DIR = WIKI_DIR / "concepts"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"

def ensure_directories():
    for d in [RAW_DIR, WIKI_DIR, SOURCES_DIR, ENTITIES_DIR, CONCEPTS_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9_]+', '_', text)
    return text.strip('_')

def run_rowboat_ingest_pipeline(file_path: Path):
    """
    Simule la chaîne d'ingestion Rowboat (Couche 1 -> Couche 2 -> Couche 3)
    """
    ensure_directories()
    file_name = file_path.name
    slug = slugify(file_path.stem)
    content = file_path.read_text(encoding="utf-8")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[Ingest Pipeline] Traitement de : {file_name}")

    # 1. Étape Couche 1 & 3 : Extraction et génération de la fiche source (LLM A)
    source_md_content = f"""---
title: "{file_path.stem.replace('_', ' ').title()}"
raw_source: "raw/{file_name}"
ingested_at: "{timestamp}"
tags: [source, automated_ingest]
---

# Synthèse : {file_path.stem.replace('_', ' ').title()}

## APERÇU HAUT NIVEAU
Ce document synthétise le contenu brut extrait de `raw/{file_name}`.

## CONTENU EXTRAIT ET APPORTS CLÉS
- **Source d'origine :** {file_name}
- **Extrait principal :**
> {content[:300].strip()}...

## LIENS ET CONCEPTS ASSOCIÉS
- Concepts clés : [[karpathy_method]], [[llm_wiki]], [[verifier_loop]]
- Entités associées : [[rowboat_harness]], [[claude_md]]
"""

    # 2. Étape Couche 2 : Vérification par le Verifier (LLM B)
    # Vérification du respect des conventions (frontmatter YAML, titre, liens wiki)
    checks = {
        "frontmatter_valid": source_md_content.startswith("---"),
        "has_summary_section": "## APERÇU HAUT NIVEAU" in source_md_content,
        "has_wiki_links": "[[" in source_md_content and "]]" in source_md_content
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    print(f"[Verifier Loop] Résultat du contrôle qualité : Status={status} ({checks})")

    if status == "PASS":
        # Sauvegarde de la fiche source
        out_source_path = SOURCES_DIR / f"{slug}.md"
        out_source_path.write_text(source_md_content, encoding="utf-8")
        print(f"[LLM Wiki] Fiche créée : {out_source_path.relative_to(BASE_DIR)}")

        # Mise à jour de l'index.md (LLM Wiki - Compilateur de connaissances)
        summary_line = f"- [[sources/{slug}|{file_path.stem.title()}]] : Fiche synthétique compilée à partir de `raw/{file_name}`."
        
        index_content = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else "# Catalog Index\n\n## Sources\n"
        if f"[[sources/{slug}" not in index_content:
            if "## Sources" in index_content:
                index_content = index_content.replace("## Sources", f"## Sources\n{summary_line}")
            else:
                index_content += f"\n\n## Sources\n{summary_line}"
            INDEX_FILE.write_text(index_content, encoding="utf-8")
            print(f"[LLM Wiki] Index.md mis à jour avec la nouvelle fiche.")

        # Inscription dans log.md
        log_entry = f"\n- **[{timestamp}]** `INGEST` : Fichier `raw/{file_name}` compilé vers `wiki/sources/{slug}.md` (Statut Verifier : PASS)."
        if LOG_FILE.exists():
            LOG_FILE.write_text(LOG_FILE.read_text(encoding="utf-8") + log_entry, encoding="utf-8")
        else:
            LOG_FILE.write_text(f"# Log History\n{log_entry}", encoding="utf-8")

        return True
    else:
        print(f"[Verifier Loop] Échec de la vérification pour {file_name}. Ajustement requis.")
        return False

def process_all_raw_files():
    ensure_directories()
    raw_files = [f for f in RAW_DIR.glob("*") if f.is_file() and not f.name.startswith(".")]
    if not raw_files:
        print(f"Aucun fichier trouvé dans {RAW_DIR}. Déposez un fichier .md ou .txt dans raw/ pour l'ingérer.")
        return

    print(f"Trouvé {len(raw_files)} fichier(s) à traiter.")
    for f in raw_files:
        run_rowboat_ingest_pipeline(f)

if __name__ == "__main__":
    process_all_raw_files()
