# Classification automatique de produits e-commerce

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/TensorFlow-2.19-orange?logo=tensorflow">
  <img src="https://img.shields.io/badge/PyTorch-2.7-red?logo=pytorch">
  <img src="https://img.shields.io/badge/scikit--learn-1.7-yellow?logo=scikit-learn">
  <img src="https://img.shields.io/badge/Gensim-4.3-green?logo=gensim">
  <img src="https://img.shields.io/badge/Transformers-4.52-purple?logo=huggingface">
  <img src="https://img.shields.io/badge/OpenCV-4.11-brightgreen?logo=opencv">
</p>

Projet de classification multimodale d'articles en ligne basé sur des descriptions textuelles (en anglais) et des images produits. L'objectif est de démontrer la faisabilité technique d'un système d'assignation automatique de catégories pour une marketplace en phase de croissance.

## Objectifs

- Étudier des méthodes non supervisées (vectorisation + clustering) pour explorer la séparabilité des catégories.
- Développer un modèle supervisé basé sur CNN pour prédire les catégories à partir des images.
- Intégrer des techniques avancées d'embedding (Word2Vec, BERT, USE) et de vision (ORB, VGG16, ResNet50).
- Évaluer l'impact de la data augmentation sur la robustesse des modèles.

## Structure du projet

- `01_pretraitement_feature_extraction_faisabilite.ipynb` : Analyse exploratoire, extraction de features texte/image, clustering.
- `02_classification_supervisee_images.ipynb` : Classification CNN avec VGG16 et ResNet50 (avec/sans data augmentation).

## Technologies

- Python, scikit-learn, TensorFlow, PyTorch
- NLP : TF-IDF, Word2Vec, BERT, USE
- Vision : ORB, VGG16, ResNet50
- Clustering : PCA, t-SNE, KMeans
- Modèles supervisés : KNN, CNN

## Résultats clés

| Méthode                | ARI / Accuracy | Observations principales                             |
|------------------------|----------------|------------------------------------------------------|
| TF-IDF / CountVector   | ARI ≈ 0.46     | Bonne séparation des clusters                       |
| Word2Vec               | ARI ≈ 0.20     | Moins discriminant                                  |
| BERT                   | ARI ≈ 0.29     | Séparation modérée, catégories confondues           |
| USE                    | ARI ≈ 0.46     | Bon compromis global                                |
| ORB (non supervisé)    | ARI ≈ 0.02     | Inefficace pour cette tâche                         |
| VGG16 (non supervisé)  | ARI ≈ 0.30     | Amélioration par rapport à ORB                      |
| VGG16 (CNN supervisé)  | Acc ≈ 74 %     | Meilleure performance globale, surtout sur Watches  |
| ResNet50 (CNN)         | Acc ≈ 25 %     | Moins performant, sensible à la variabilité         |

## Lancer le projet

```bash
# Créer un environnement virtuel et installer les dépendances
pip install -r requirements.txt
```

## Données
Les données utilisées sont fournies à des fins pédagogiques. Aucune contrainte de propriété intellectuelle. Le fichier principal est flipkart_sample.csv.