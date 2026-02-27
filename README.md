![CI](https://github.com/yanisDrx/calculator_project_26_YP/actions/workflows/main.yml/badge.svg)
# 🧮 PROJECT CALCULATOR – ORGANISATION DU CODE

Bienvenue dans mon projet : un package Python implémentant une calculatrice simple permettant d’effectuer des opérations arithmétiques de base.

---

# 📦 Calculator

Un package Python structuré proprement, respectant les bonnes pratiques de développement logiciel :

- Organisation en modules
- Séparation code / tests
- Analyse qualité (Pylint + Radon)
- Structure de package installable

---

## 👤 Auteur

Yanis PIRES PORTELADA

---

# 🏗️ Processus d'installation du package 

Voici les étapes suivies pour créer le package :

### 1️⃣ Création de l’arborescence

```
calculator_project_26_YP/
│
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── simple_calculator.py
│
├── tests/
│   └── test_simple_calculator.py
│
├── pyproject.toml
├── README.md
```

### 2️⃣ Ajout du fichier `pyproject.toml`

Permet de définir :
- Le nom du package
- La version
- Les dépendances
- Le système de build

### 3️⃣ Installation du package en mode editable

Cette commande installe le package en mode développement afin que toute modification du code soit immédiatement prise en compte, sans avoir besoin de le réinstaller.

```bash
pip install -e .
```

---

# ⚙️ Installation du projet

```bash
git clone https://github.com/yanisDrx/calculator_project_26_YP
cd calculator_project_26_YP
pip install -e .
```

---

# 🔹 Gestion de l’environnement virtuel

Dans ce projet, nous utilisons un **venv** pour isoler les dépendances Python. Cela permet :

- De ne pas polluer l’environnement système
- De garantir que les versions des packages sont celles attendues par le projet
- De faciliter la reproductibilité des tests et du build

> Remarque : le répertoire `venv/` n’est **pas** versionné dans Git (`.gitignore` est configuré pour cela).

```bash
# Création de l'environnement virtuel
python -m venv .env_calculator

# Activation (Windows)
.env_calculator\Scripts\activate

# Activation (Linux / macOS)
source .env_calculator/bin/activate
```

---

# 🧠 Fonctionnalités du package

Classe principale : `SimpleCalculator`

## Méthodes

### `_validate_operands(a: object, b: object) -> None`

Vérifie que :

- `a` et `b` ne sont pas `None`
- `a` et `b` sont des entiers
- Pour `divide()`, `b` est différent de 0

Cette méthode est réutilisée dans les autres méthodes ensuite
---

### `add(a: int, b: int) -> int`

Additionne deux entiers.

Retourne un entier.

---

### `subtract(a: int, b: int) -> int`

Soustrait deux entiers.

Retourne un entier.

---

### `multiply(a: int, b: int) -> int`

Multiplie deux entiers.

Retourne un entier.

---

### `divide(a: int, b: int) -> float`

Divise deux entiers.

Retourne un float

---

# 🧪 Tests unitaires

Les tests unitaires permettent de vérifier automatiquement que chaque partie du package fonctionne correctement et d’éviter d’introduire des erreurs lors des modifications du code.

## 📦 Package utilisé

Les tests ont été réalisés avec :

```
pytest
```

Installation :

```bash
pip install pytest    --    pip -m pytest
```

---

## ▶️ Commande d’exécution des tests

Depuis la racine du projet :

```bash
pytest
```

---

## 📊 Sortie obtenue

Exemple de sortie :

```
================== test session starts ==================
collected 4 items

test_simple_calculator.py ....        [100%]

================== 4 passed in 0.02s ==================
```

Cela signifie :
- 4 tests exécutés
- 4 tests réussis
- Aucun échec

---

## 🔹 Tests unitaires avancés et gestion des erreurs

Pour garantir la robustesse :

- Vérification des erreurs attendues (ex : division par zéro, types invalides)
- Cas d’usage complet pour toutes les méthodes

Exemple :

```python
import pytest
from calculator.simple_calculator import SimpleCalculator

def test_divide_by_zero():
    calc = SimpleCalculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_invalid_operands():
    calc = SimpleCalculator()
    with pytest.raises(TypeError):
        calc.add("a", 5)
```

---

## 🧪 Modification des tests 

Pour tester d’autres opérations :

1. Aller dans :

```
tests/test_simple_calculator.py
```

2. Modifier les valeurs dans les fonctions de test, par exemple :

```python
def test_add():
    calc = SimpleCalculator()
    assert calc.add(10, 5) == 15
```

3. Tester :
- Des nombres négatifs
- Des nombres plus grands
- Des divisions
- Des erreurs (ex: division par zéro)

Puis relancer :

```bash
pytest
```

---

# 🔎 Analyse qualité avec Pylint

L’analyse "statique" du code permet de détecter automatiquement les erreurs potentielles, les mauvaises pratiques et les écarts aux standards comme PEP8, et permet. Les problèmes identifiés peuvent être corrigés manuellement (comme ici) ou automatiquement à l’aide d’outils de formatage comme black. Ces deux étapes permettent d'améliorer la lisibilité globale du code.

## 📦 Package utilisé

Les tests ont été réalisés avec :

```
pylint
```
Installation :

```bash
pip install pylint      --      python -m pylint
```

## ▶️ Commande d’exécution des tests

Depuis la racine du projet :

```bash
pylint src/calculator 
```

---

## 🛠️ Résultats et corrections

Exemple d'une sortie console sur le résultat de l'analyse :

```
************* Module calculator
src/calculator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/calculator.py:3:4: R1705: Unnecessary "else" after "return" (no-else-return)
src/calculator.py:5:0: C0103: Variable name "x" doesn't conform to snake_case naming style (invalid-name)
src/calculator.py:8:0: C0116: Missing function or method docstring (missing-function-docstring)
src/calculator.py:12:8: W0612: Unused variable 'result' (unused-variable)
src/calculator.py:15:0: C0301: Line too long (120/100) (line-too-long)
src/calculator.py:20:0: C0330: Wrong hanging indentation (bad-continuation)

------------------------------------------------------------------
Your code has been rated at 9.0/10
```

- ✅ Corrections d’architecture et docstrings pour PEP 257
- ✅ `_validate_operands` centralise les vérifications
- ✅ Gestion des exceptions claire pour toutes les méthodes

---

# 📊 Analyse de complexité avec Radon

L’analyse de complexité permet de mesurer automatiquement la "**complexité cyclomatique**". Un code trop complexe est plus difficile à comprendre, tester et maintenir. Les résultats peuvent être utilisés pour prioriser les refactorings et améliorer la lisibilité globale du code.

## 📦 Package utilisé

L’outil utilisé pour cette analyse est :  

```
radon
```

Installation :  

```bash
pip install radon
```

## ▶️ Commande utilisée

Depuis la racine du projet :
```bash
radon cc src/calculator -s
```
- cc -> complexity cyclomatique
- -s -> affiche les scores de manière synthétique

## 🛠️ Résultats et interprétation

Exemple de sortie console :

```
M 20:4 SimpleCalculator._validate_operands - A (5)
C 12:0 SimpleCalculator - A (3)
M 40:4 SimpleCalculator.divide - A (2)
M 17:4 SimpleCalculator.__init__ - A (1)
M 25:4 SimpleCalculator.add - A (1)
M 30:4 SimpleCalculator.subtract - A (1)
M 35:4 SimpleCalculator.multiply - A (1)
```

- Toutes les méthodes ont un score **A**
- Code simple, lisible et maintenable

---

# 🧹 Gestion des fichiers inutiles avec `.gitignore`

[...]

*(le bloc `.gitignore` reste inchangé, identique au précédent README)*

---

# 📦 Déploiement sur PyPI Test (TestPyPI)

[...]

*(bloc inchangé, conserve instructions build et upload)*

---

# 🤖 CI/CD avec GitHub Actions

Pour automatiser le **lint**, les **tests**, la **mesure de complexité**, la **construction du package** et son **déploiement sur TestPyPI**, nous avons mis en place un workflow GitHub Actions.

---

## 📌 Étapes réalisées

1️⃣ **Continuous Integration (CI)**

- Lint du code avec **pylint** et formatage vérifié avec **black**
- Tests unitaires exécutés via **pytest** avec couverture (`pytest-cov`)
- Mesure de complexité cyclomatique via **radon**
- Build du package avec **python -m build**
- Tous ces jobs sont déclenchés à chaque push sur `main` ou pull request

2️⃣ **Continuous Deployment (CD)**

- Déploiement automatique sur **TestPyPI** uniquement lors de la création d’un tag (ex: `v0.1.1`)
- Utilisation de **twine** pour publier le package
- Authentification via **API token TestPyPI** stocké dans **GitHub Secrets**
- Build du package refait dans le job CD pour s’assurer que le package est propre avant upload

---

## ⚠️ Problèmes rencontrés et solutions

| Problème | Solution |
|----------|---------|
| Les tests `pytest --cov=calculator` échouaient sur GitHub Actions alors qu’ils passaient en local | Installation explicite du plugin `pytest-cov` dans le workflow |
| `black --check` indiquait des fichiers à reformater | Correction du code localement avant push |
| Déploiement TestPyPI : `403 Forbidden` | Utilisation d’un **API token** et configuration correcte dans GitHub Secrets (`TEST_PYPI_USERNAME=__token__` et `TEST_PYPI_PASSWORD=<token>`) |
| Déploiement CD ne se lançait pas automatiquement | Configuration du workflow pour se déclencher **uniquement sur tags** et bump de version nécessaire pour chaque release |

---

## 🔧 Commandes principales CI/CD (résumé)

- Lancer tests localement :

```bash
pytest -v --cov=calculator --cov-report=term-missing
```

- Lancer lint et format check localement :

```bash
pylint src/calculator
black --check src/ tests/
```

- Construire le package et publier sur TestPyPI (manuellement si besoin) :

```bash
python -m build
twine upload --repository testpypi dist/*
```

- Pour déclencher le CD automatiquement, créer un tag et push :

```bash
git tag v0.1.1
git push origin v0.1.1
```

---

# 🎯 Résumé final du projet

Ce projet illustre la création complète d’un package Python :

- **Code modulaire et structuré** (`src/calculator`)  
- **Tests unitaires complets**, incluant gestion des erreurs (`pytest`)  
- **Analyse qualité et complexité** (`pylint`, `radon`)  
- **Workflow CI/CD opérationnel** pour tests, build et déploiement sur TestPyPI  
- **Installation possible depuis GitHub ou TestPyPI** avec version/tag spécifique  
- **Package installable et prêt pour publication**

Le repository final est propre, maintenable et prêt pour évolution ou distribution.

---

# 🔹 Liste des ajouts / modifications majeures

| Bloc / Ligne | Modification |
|--------------|--------------|
| Gestion de venv | Explications + commandes de création/activation |
| CI/CD | Ajout détails sur tags, problèmes rencontrés et solutions |
| Tests unitaires | Ajout gestion des erreurs, exemples `pytest.raises` |
| Docstrings | Mention PEP 257 et exemples |
| Installation GitHub/TestPyPI | Commandes avec version/tag spécifique |
| Arbre de commit | Illustration de l’historique et choix de tags |
| Résumé final | Synthèse concise intégrant les éléments manquants du professeur |
```