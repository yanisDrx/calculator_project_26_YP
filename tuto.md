# 📝 Guide rapide pour créer un package Python complet avec CI/CD

Ce guide fournit une **checklist concise et complète** des étapes pour créer, tester, analyser et déployer un package Python, avec CI/CD automatisé. Idéal pour répéter rapidement ce workflow pour un projet similaire ou un partiel.

---

## 1️⃣ Préparer le projet et l’arborescence

1. Créer le dossier du projet :

```
my_project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── main_module.py
├── tests/
│   └── test_main_module.py
├── pyproject.toml
├── README.md
```

2. Créer un environnement virtuel pour isoler les dépendances :

```bash
python -m venv .env_project
# Activation Windows
.env_project\Scripts\activate
# Activation Linux/macOS
source .env_project/bin/activate
```

3. Ajouter un `.gitignore` pour ignorer fichiers temporaires, venv, build, dist, caches Python.

---

## 2️⃣ Créer et configurer le package

- Remplir `pyproject.toml` :
  - `name` : nom du package
  - `version` : version initiale (ex: 0.1.0)
  - `authors` : auteur(s)
  - `description` : courte description
  - `dependencies` : dépendances nécessaires
  - `readme` : chemin vers README.md
  - `build-system` : pour `setuptools` ou `flit`

- Implémenter les classes et fonctions dans `src/my_package/`.
- Ajouter **docstrings PEP 257** pour toutes les classes et méthodes.

---

## 3️⃣ Installation en mode développement

```bash
pip install -e .
```

- Permet d’appliquer instantanément les modifications sans réinstaller.

---

## 4️⃣ Écriture des tests unitaires

- Utiliser **pytest** pour les tests fonctionnels et erreurs attendues :

```python
import pytest
from my_package.main_module import MyClass

def test_addition():
    obj = MyClass()
    assert obj.add(2, 3) == 5

def test_divide_by_zero():
    obj = MyClass()
    with pytest.raises(ValueError):
        obj.divide(5, 0)
```

- Couvrir tous les cas, incluant les erreurs.

- Commande de test :

```bash
pytest -v --cov=my_package --cov-report=term-missing
```

---

## 5️⃣ Analyse qualité et complexité

1. **Pylint** pour vérifier conformité PEP8 et bonnes pratiques :

```bash
pylint src/my_package
```

2. **Radon** pour complexité cyclomatique :

```bash
radon cc src/my_package -s
```

- Scores attendus : A (1–5) pour fonctions simples.
- Corriger les problèmes identifiés : indentation, noms, docstrings, lignes trop longues.

---

## 6️⃣ Build du package

- Installer build :

```bash
pip install build
python -m build
```

- Génère `dist/` contenant `.whl` et `.tar.gz`.

---

## 7️⃣ Publication sur TestPyPI

1. Installer **twine** :

```bash
pip install twine
```

2. Publier sur TestPyPI :

```bash
twine upload --repository testpypi dist/*
```

- Utiliser **API token** dans GitHub/GitLab Secrets pour l’authentification.
- Tester installation depuis TestPyPI :

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple my_package
```

---

## 8️⃣ Automatisation CI/CD avec GitHub Actions

- Créer `.github/workflows/ci_cd.yml` :

**Jobs recommandés :**
1. `lint_test` : lint + tests unitaires + coverage
2. `metrics` : radon cyclomatic complexity
3. `build` : build package et upload artifact
4. `deploy_testpypi` : publication automatique sur TestPyPI sur **tag push** uniquement

- Points clés :
  - Installer toutes les dépendances dans chaque job
  - Authentification via secrets
  - Déclenchement du déploiement uniquement sur tags (`refs/tags/*`)

- Créer un tag et push pour déclencher le CD :

```bash
git tag v0.1.0
git push origin v0.1.0
```

---

## 9️⃣ Gestion Git et historique

- Commits clairs et fréquents.
- Branches pour fonctionnalités (`feature/`) ou corrections (`fix/`).
- Tags pour versions publiées.
- Nettoyer le repo après ajout `.gitignore` :

```bash
git rm -r --cached .
git add .
git commit -m "Clean repo and apply .gitignore"
```

---

## 10️⃣ Documentation

- Ajouter README complet :
  - Installation depuis GitHub
  - Installation depuis TestPyPI
  - Commandes de tests
  - Instructions CI/CD
  - Arborescence du projet
  - Exemples d’usage
  - Résumé du workflow

---

## 11️⃣ Checklist finale

- [ ] Package structuré et modulaire
- [ ] Tests complets, incluant erreurs et limites
- [ ] Analyse qualité et complexité passée
- [ ] Build et publication TestPyPI fonctionnels
- [ ] CI/CD configuré et testé
- [ ] Tags et versions claires sur Git
- [ ] README complet et lisible
- [ ] Docstrings PEP 257 présentes
- [ ] Environnement isolé via venv

---

## 🔹 Notes pour réutilisation rapide

- **venv** : indispensable pour l’isolation
- **tags Git** : déclenchent CD automatique
- **Tests** : pytest + coverage, gérer erreurs
- **Analyse qualité** : pylint + radon
- **CI/CD** : lint, test, metrics, build, deploy sur TestPyPI
- **README** : centralise toutes les étapes pour reproductibilité

> Ce guide synthétique permet de répéter le workflow complet pour tout nouveau projet Python en suivant exactement les bonnes pratiques professionnelles et académiques.