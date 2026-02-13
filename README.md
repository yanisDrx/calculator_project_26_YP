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

# 🏗️ Processus de création du package

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

### 3️⃣ Installation en mode editable

```bash
pip install -e .
```

Cela permet :
- D’installer le package localement
- De modifier le code sans réinstaller à chaque changement

---

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

### `divide(a: int, b: int) -> int`

Divise deux entiers.

Retourne un entier.

---

# 🧪 Tests unitaires

## 📦 Package utilisé

Les tests ont été réalisés avec :

```
pytest
```

Installation :

```bash
pip install pytest
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

## 🧪 Modifier les tests pour expérimenter

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

## 📦 Installation

```bash
pip install pylint
```

## ▶️ Commande utilisée

```bash
pylint src/calculator
```

---

## 🛠️ Corrections apportées

Pour améliorer la qualité du code, les corrections suivantes ont été appliquées :

- ✅ Suppression des espaces inutiles
- ✅ Ajout de lignes vides en fin de fichier
- ✅ Respect des conventions de nommage
- ✅ Ajout de docstrings aux classes et méthodes
- ✅ Correction de l'indentation
- ✅ Suppression des imports inutilisés
- ✅ Respect des longueurs de ligne

Objectif : respecter les standards PEP8 et améliorer la lisibilité.

---

# 📊 Analyse de complexité avec Radon

## 📦 Installation

```bash
pip install radon
```

## ▶️ Commande utilisée

```bash
radon cc src/calculator -s
```

## 📈 Résultats obtenus

```
M 20:4 SimpleCalculator._validate_operands - A (5)
C 12:0 SimpleCalculator - A (3)
M 40:4 SimpleCalculator.divide - A (2)
M 17:4 SimpleCalculator.__init__ - A (1)
M 25:4 SimpleCalculator.add - A (1)
M 30:4 SimpleCalculator.subtract - A (1)
M 35:4 SimpleCalculator.multiply - A (1)
```

### Interprétation

Toutes les méthodes ont un score **A**.

Échelle Radon :

- A (1–5) : Très simple
- B (6–10) : Acceptable
- C (11–20) : Complexité moyenne
- D+ : Code complexe

Conclusion :

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

---

# 🎯 Qualité globale du projet

Le projet respecte :

- Organisation modulaire
- Séparation code / tests
- Tests automatisés
- Analyse statique
- Analyse de complexité
- Bonnes pratiques PEP8
- Package installable

---

# 🚀 Améliorations possibles

- Ajouter une interface CLI
- Ajouter plus de cas de tests
- Ajouter un workflow GitHub Actions
- Ajouter couverture de code (coverage.py)

---

# 📌 Conclusion

Ce projet démontre :

- La création complète d’un package Python
- L’implémentation de tests unitaires
- L’analyse de qualité professionnelle
- Le respect des standards industriels

Projet prêt pour publication et évolution future.
