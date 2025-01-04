# Traceroute TP6 - Script Python

## **Présentation**
Ce projet est un script Python permettant d'effectuer un traceroute vers une URL ou une adresse IP donnée. Il affiche la liste des adresses IP des différents sauts du chemin réseau.

Le script prend en charge les systèmes **Windows**, **Linux** et **macOS** et offre deux options supplémentaires pour un fonctionnement flexible :
- Affichage des résultats au fur et à mesure.
- Enregistrement des résultats dans un fichier de sortie.

---

## **Installation**
### **Prérequis**
- Python 3.x installé sur votre machine.
- Fonctionnalité **traceroute** activée (ou `tracert` sur Windows).

### **Étapes d'installation**
1. **Cloner le dépôt Git** :
   ```bash
   git clone <url_du_depot_git>
   cd tp-traceroute
   ```
2. **Exécuter le script** directement avec Python (voir la section Utilisation).

---

## **Utilisation**
Le script prend une URL ou une adresse IP comme argument obligatoire et propose deux options facultatives.

### **Commande de base**
```bash
python traceroute.py <URL ou adresse IP>
```

**Exemple** :
```bash
python traceroute.py www.google.com
```
Cette commande affiche la liste des adresses IP des différents sauts une fois le traceroute terminé.

### **Options disponibles**

#### **1. Option `-p` / `--progressive`**
Affiche les résultats au fur et à mesure de l'exécution du traceroute.

**Commande** :
```bash
python traceroute.py <URL ou adresse IP> -p
```

**Exemple** :
```bash
python traceroute.py www.google.com -p
```

#### **2. Option `-o` / `--output-file`**
Enregistre les résultats dans un fichier spécifié.

**Commande** :
```bash
python traceroute.py <URL ou adresse IP> -o <nom_du_fichier>
```

**Exemple** :
```bash
python traceroute.py www.google.com -o resultats_traceroute.txt
```
Le fichier `resultats_traceroute.txt` contiendra la liste des adresses IP des différents sauts.

#### **3. Combinaison des options**
Vous pouvez combiner les options `-p` et `-o` pour afficher les résultats au fur et à mesure tout en les enregistrant dans un fichier :

**Commande** :
```bash
python traceroute.py <URL ou adresse IP> -p -o <nom_du_fichier>
```

**Exemple** :
```bash
python traceroute.py www.google.com -p -o resultats_traceroute.txt
```

---

## **Fonctionnalités détaillées**
1. **Détection automatique du système d'exploitation** :
   - Utilisation de la commande `traceroute` sur Linux/macOS.
   - Utilisation de la commande `tracert` sur Windows.
2. **Affichage des résultats** :
   - Affichage complet à la fin ou progressif selon l'option choisie.
3. **Enregistrement des résultats** dans un fichier texte (si spécifié).
4. **Gestion des erreurs** :
   - Le script affiche un message d'erreur clair en cas de problème (mauvaise URL, absence de connexion, etc.).

---

## **Notes**
- Ce script a été développé dans le cadre du TP6 de réseau.
- Il a été testé sur Windows et Linux. Pour macOS, la compatibilité est assurée avec la commande `traceroute` native.
- En cas de problème, consultez les logs ou contactez le développeur via le dépôt GitHub.

---

## **Auteur**
Ce projet a été réalisé dans le cadre d’un exercice pratique de réseau, avec l’aide d’outils d’IA pour la génération du code et de la documentation.

---

