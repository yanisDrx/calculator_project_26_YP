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

# ⚙️ Installation du projet

```bash
git clone https://github.com/yanisDrx/calculator_project_26_YP
cd calculator_project_26_YP
pip install -e .
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

### `divide(a: int, b: int) -> float

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
Your code has been rated at 6.00/10 (previous run: 5.50/10, +0.50)
```

Pour améliorer la qualité du code, les corrections suivantes ont été appliquées :

- ✅ Suppression des espaces inutiles
- ✅ Ajout de lignes vides en fin de fichier
- ✅ Respect des conventions de nommage
- ✅ Ajout de docstrings aux classes et méthodes
- ✅ Correction de l'indentation
- ✅ Suppression des imports inutilisés
- ✅ Respect des longueurs de ligne

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

### Échelle Radon :

Échelle Radon :

- A (1–5) : Très simple
- B (6–10) : Acceptable
- C (11–20) : Complexité moyenne
- D+ : Code complexe


Dans le cas de ce projet, outes les méthodes ont un score **A**.
Le code est simple, lisible et maintenable.

---

# 🧹 Gestion des fichiers inutiles avec `.gitignore`

Afin de respecter les bonnes pratiques Git, certains fichiers générés automatiquement ne doivent pas être versionnés.

Ces fichiers peuvent être recréés à tout moment et ne font pas partie du code source.

---

## 📄 Contenu du fichier `.gitignore`

Le fichier `.gitignore` (placé à la racine du projet) contient :

```gitignore
# Build
build/
dist/

# Egg metadata
*.egg-info/

# Python cache
__pycache__/
*.pyc

# Pytest cache
.pytest_cache/

# Virtual environments
venv/
.package_env/
.env/

# OS files
.DS_Store
Thumbs.db
```

---

## 📌 Pourquoi ces éléments sont ignorés ?

| Élément | Raison |
|----------|--------|
| `build/` | Dossier généré lors du packaging |
| `dist/` | Contient les fichiers `.whl` et `.tar.gz` générés |
| `*.egg-info/` | Métadonnées générées par `pip install -e .` |
| `__pycache__/` | Fichiers compilés Python |
| `*.pyc` | Bytecode Python |
| `.pytest_cache/` | Cache automatique de pytest |
| `venv/` | Environnement virtuel local |
| Fichiers OS | Fichiers système inutiles |

---

## 🛠️ Commandes utilisées pour nettoyer le repository

Après avoir ajouté le `.gitignore`, les fichiers déjà suivis par Git ont dû être retirés de l’index.

### Méthode propre utilisée :

```bash
git rm -r --cached .
git add .
git commit -m "Apply proper gitignore and clean repository"
```

### Explication :

- `git rm -r --cached .`
  → Supprime tous les fichiers de l’index Git (sans les supprimer du disque)

- `git add .`
  → Réajoute uniquement les fichiers non ignorés

- `git commit`
  → Valide le nettoyage

---

## 🔎 Vérification

Pour vérifier que tout est propre :

```bash
git status
```

Les dossiers suivants ne doivent plus apparaître :

- `build/`
- `dist/`
- `*.egg-info/`
- `__pycache__/`
- environnements virtuels

---

# 📦 Déploiement sur PyPI Test (TestPyPI)

Une fois votre package Python prêt et testé localement, il est possible de le publier sur **TestPyPI**, un environnement de test officiel de PyPI, avant de le publier sur le dépôt officiel. Cela permet de vérifier que le package peut être installé et utilisé correctement.

---

## 🔧 Prérequis

- Installer **twine** pour la gestion de la publication :
```bash
pip install twine
```

- Vérifier que votre `pyproject.toml` contient bien les informations nécessaires :
  - `name` : nom du package
  - `version` : version du package
  - `authors` : auteur(s)
  - `description` : description courte
  - `dependencies` : dépendances éventuelles
  - `readme` : chemin vers le README.md

---

## 🏗️ Construction des distributions

Depuis la racine du projet, exécuter :

```bash
python -m build
```

Cela génère un dossier `dist/` contenant :
- `calculator_project_26_YP-x.x.x-py3-none-any.whl` → fichier binaire
- `calculator_project_26_YP-x.x.x.tar.gz` → fichier source

---

## 🚀 Publication sur TestPyPI

1. Publier le package sur TestPyPI :
```bash
twine upload --repository testpypi dist/*
```

2. Lorsque vous y êtes invité, entrer vos identifiants TestPyPI :
- Nom d’utilisateur
- Mot de passe

---

## 📥 Installation depuis TestPyPI

Pour tester l’installation de votre package depuis TestPyPI, créer un environnement virtuel et exécuter :

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple calculator_project_26_YP
```

---

## ✅ Vérification

Après l’installation, vérifier que le package fonctionne correctement :

```python
from calculator.simple_calculator import SimpleCalculator

calc = SimpleCalculator()
print(calc.add(3, 5))  # Doit afficher 8
```

---

## ⚠️ Conseils

- Toujours tester votre package sur TestPyPI avant de le publier sur le dépôt officiel.
- Mettre à jour le numéro de version dans `pyproject.toml` pour chaque nouvelle publication.
- Nettoyer les fichiers générés (`dist/`, `build/`) avant chaque nouveau build pour éviter les conflits.

---

## 🌐 Publication finale sur PyPI

Une fois les tests réussis sur TestPyPI, publier sur PyPI officiel :

```bash
twine upload dist/*
```

# 🎯 Résultat

Le repository final ne contient que :

- Le code source
- Les tests
- Les fichiers de configuration
- La documentation

Cela garantit :

- Un dépôt propre
- Une meilleure lisibilité
- Le respect des standards professionnels
- Une collaboration facilitée
- Un package prêt à être déployé sur TestPyPI ou PyPI officiel

---

# 🎯 Qualité globale du projet

Le projet respecte :

- Organisation modulaire
- Séparation code / tests
- Tests automatisés
- Analyse statique
- Analyse de complexité
- Bonnes pratiques PEP8
- Package installable et déployable sur PyPI
- Processus de publication documenté (TestPyPI et PyPI)

---

# 🚀 Améliorations possibles

- Ajouter une interface CLI
- Ajouter plus de cas de tests
- Ajouter un workflow GitHub Actions pour automatiser tests et déploiement
- Ajouter couverture de code (coverage.py)
- Intégrer la publication automatisée sur TestPyPI pour chaque version

> Ces améliorations sont des propositions **générées par IA**, et ne sont **pas expliquées** ici pour la simple et bonne raison que **je ne les maîtrise pas**.

---

# 📌 Conclusion

Ce projet démontre :

- La création complète d’un package Python
- L’implémentation de tests unitaires
- L’analyse de qualité professionnelle
- Le respect des standards industriels
- La préparation et documentation du processus de déploiement sur PyPI

Projet prêt pour publication, distribution et évolution future.

