#!/usr/bin/env python3
"""
Harnais Rowboat - Couche 2 (Vérification Karpathy)
Boucle d'automatisation Générateur (LLM A) / Vérificateur (LLM B)

Ce script orchestre une boucle de rétroaction entre deux modèles :
1. LLM A (Générateur) : produit une réponse selon la spécification.
2. LLM B (Critique / Vérificateur) : évalue la réponse selon la grille de critères.
3. Si statut == FAIL : réinjecte le feedback au LLM A pour réécriture (jusqu'à PASS ou max_retries).
"""

import json
import logging
from typing import Dict, Any, Tuple, Optional

# Configuration du logging pour suivre la boucle de vérification
logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger("RowboatHarness")

# ==============================================================================
# 1. CONFIGURATION YAML ROWBOAT (Exemple de configuration du harnais)
# ==============================================================================
ROWBOAT_CONFIG_YAML = """
version: "1.0"
harness:
  name: "karpathy-layer2-verifier"
  description: "Harnais de vérification à deux LLM avec boucle de rétroaction"
  max_retries: 3

models:
  generator:
    name: "llm-a-generator"
    provider: "local" # ou ollama / vllm / openai
    model: "qwen3.5:9b"
    temperature: 0.7

  verifier:
    name: "llm-b-verifier"
    provider: "local"
    model: "Ling-3.0-tiny-GGUF:latest"
    temperature: 0.1 # Basse température pour une évaluation constante

criteria_grid:
  format_and_structure:
    - "L'output respecte-t-il exactement le format demandé ?"
    - "Toutes les sections requises sont-elles présentes ?"
  accuracy_and_grounding:
    - "L'information est-elle appuyée par le contexte sans hallucination ?"
  internal_logic:
    - "Le raisonnement est-il fluide et exempt de contradictions ?"
"""


# ==============================================================================
# 2. PROMPTS DE SYSTEME ET D'ÉVALUATION
# ==============================================================================

VERIFIER_SYSTEM_PROMPT = """Vous êtes un contrôleur de qualité strict et impartial (LLM Critique).
Votre rôle est d'évaluer l'output produit par un premier LLM en le confrontant à la spécification initiale et à la grille de critères.

VOUS DEVEZ IMPÉRATIVEMENT RÉPONDRE AU FORMAT JSON STRICT RESPECTANT CE SCHÉMA :
{
  "status": "PASS" | "FAIL",
  "score": 0-100,
  "criteria_checks": [
    {
      "criterion": "Nom du critère",
      "passed": true | false,
      "comment": "Explication si échec"
    }
  ],
  "feedback_for_generator": "Instructions de correction concises et directement exploitables si FAIL, ou vide si PASS."
}
"""

VERIFIER_USER_PROMPT_TEMPLATE = """--- SPÉCIFICATION INITIALE ---
{spec}

--- GRILLE DE CRITÈRES ---
{criteria}

--- OUTPUT DU LLM GÉNÉRATEUR ---
{generator_output}

Analysez rigoureusement cet output. Soyez intransigeant : la moindre contradiction ou omission entraîne un statut "FAIL".
"""


# ==============================================================================
# 3. CLASSE D'ORCHESTRATION DU HARNAIS ROWBOAT
# ==============================================================================

class RowboatVerifierHarness:
    def __init__(self, generator_client: Any = None, verifier_client: Any = None, max_retries: int = 3):
        """
        Initialise le harnais avec les clients LLM (ou fonctions d'appel) et le nombre max de tentatives.
        """
        self.generator_client = generator_client
        self.verifier_client = verifier_client
        self.max_retries = max_retries

    def _call_generator(self, spec: str, feedback_history: list) -> str:
        """
        Appelle le LLM A (Générateur). Si un feedback existe, il est ajouté au prompt.
        """
        prompt = f"Spécification : {spec}\n"
        if feedback_history:
            prompt += "\n--- HISTORIQUE DES CRITIQUES DE VÉRIFICATION À CORRIGER ---\n"
            for i, fb in enumerate(feedback_history, 1):
                prompt += f"Tentative {i} - Corrections requises : {fb}\n"
            prompt += "\nVeuillez fournir une version corrigée et améliorée respectant l'ensemble des consignes."

        logger.info("Envoi de la requête au LLM Générateur (LLM A)...")
        if self.generator_client:
            return self.generator_client(prompt)
        
        # Simulation pour démonstration si aucun client n'est injecté
        return f"[Reponse simulee du LLM A basée sur : {spec}]"

    def _call_verifier(self, spec: str, criteria: str, generator_output: str) -> Dict[str, Any]:
        """
        Appelle le LLM B (Vérificateur) pour évaluer la réponse du LLM A.
        """
        user_prompt = VERIFIER_USER_PROMPT_TEMPLATE.format(
            spec=spec,
            criteria=criteria,
            generator_output=generator_output
        )

        logger.info("Envoi de la réponse au LLM Vérificateur (LLM B)...")
        if self.verifier_client:
            raw_response = self.verifier_client(VERIFIER_SYSTEM_PROMPT, user_prompt)
            try:
                return json.loads(raw_response)
            except json.JSONDecodeError:
                logger.warning("Échec du parsing JSON du vérificateur. Passage en réévaluation.")
                return {
                    "status": "FAIL",
                    "score": 0,
                    "criteria_checks": [],
                    "feedback_for_generator": "Le format d'évaluation JSON était invalide. Corrigez le format et la structure."
                }

        # Simulation d'un retour valide pour test
        return {
            "status": "PASS",
            "score": 95,
            "criteria_checks": [{"criterion": "Format", "passed": True, "comment": "Conforme"}],
            "feedback_for_generator": ""
        }

    def run(self, spec: str, criteria: str) -> Tuple[str, Dict[str, Any], int]:
        """
        Exécute la boucle de rétroaction Couche 2 jusqu'à l'obtention d'un PASS ou l'atteinte du max_retries.
        """
        feedback_history = []
        attempt = 0

        while attempt < self.max_retries:
            attempt += 1
            logger.info(f"=== TENTATIVE {attempt}/{self.max_retries} ===")

            # 1. Génération
            current_output = self._call_generator(spec, feedback_history)

            # 2. Vérification par le second LLM
            evaluation = self._call_verifier(spec, criteria, current_output)

            status = evaluation.get("status", "FAIL")
            score = evaluation.get("score", 0)
            feedback = evaluation.get("feedback_for_generator", "")

            logger.info(f"Résultat Vérificateur : Statut={status} | Score={score}/100")

            # 3. Évaluation du résultat
            if status == "PASS":
                logger.info("✅ Vérification validée avec succès ! (Boucle terminée)")
                return current_output, evaluation, attempt

            logger.warning(f"❌ Échec de la vérification (Tentative {attempt}). Feedback : {feedback}")
            feedback_history.append(feedback)

        logger.error("⚠️ Nombre maximum de tentatives atteint sans validation complète.")
        return current_output, evaluation, attempt


# ==============================================================================
# EXEMPLE D'UTILISATION SIMPLE
# ==============================================================================
if __name__ == "__main__":
    print("=== HARNAIS ROWBOAT : DEMO BOUCLE DE VÉRIFICATION COUCHE 2 ===")
    
    spec_exemple = "Rédiger une synthèse de 3 points sur la méthode Karpathy sans inventer de faits."
    criteria_exemple = "1. Exactement 3 points. 2. Aucun jargon inutile. 3. Présence d'un titre."

    harness = RowboatVerifierHarness(max_retries=3)
    final_output, final_eval, total_attempts = harness.run(spec_exemple, criteria_exemple)

    print("\n--- RÉSULTAT FINAL ---")
    print(f"Tentatives effectuées : {total_attempts}")
    print(f"Statut final : {final_eval.get('status')}")
    print(f"Output : {final_output}")
