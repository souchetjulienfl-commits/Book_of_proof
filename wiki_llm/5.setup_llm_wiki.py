import os
import sys

def init_wiki():
    dirs = [
        "raw",
        "wiki/sources",
        "wiki/entities",
        "wiki/concepts",
        "wiki/analyses"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f" Dossier prêt : {d}")

    print("\n LLM Wiki initialisé avec succès !")
    print("Placez vos documents bruts dans 'raw/' puis lancez le workflow Ingest via votre agent.")

if __name__ == "__main__":
    init_wiki()
