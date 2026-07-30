# 📦 SAH Lilas Distribution - Gestion Avancée des Conditionnements & Totaux

![Odoo Version](https://img.shields.io/badge/Odoo-19.0-purple?style=for-the-badge&logo=odoo)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![OWL](https://img.shields.io/badge/OWL-Framework-orange?style=for-the-badge&logo=javascript)

## 📖 À propos

**SAH Lilas Distribution** est un module Odoo 19 sur-mesure dont l'objectif est d'optimiser l'expérience utilisateur et la fiabilité des données dans un environnement de vente et distribution. 
Il apporte deux grands axes d'améliorations :
1. **Une lecture sans erreur des quantités et prix** : Affiche automatiquement les quantités réelles en Unités de base, peu importe l'emballage sélectionné (Pack, Carton).
2. **Une transparence des totaux financiers** : Affiche systématiquement le Total des Remises accordées et la taxe FODEC (1%) au bas de tous les documents commerciaux.

Tout ceci en respectant la règle d'or du projet : **Simple et 100% Natif**.

---

## ✨ Fonctionnalités Principales

### 1. 🔄 Conversion Dynamique (Lignes de documents)
* **Colonnes `Qté Unités` et `PU Unité`** : Le système convertit la quantité et calcule le prix réel à l'unité de base de l'article en temps réel, évitant tout calcul mental.
* **Épuration de l'interface** : La colonne standard "Prix unitaire" d'Odoo a été masquée des tableaux pour éviter la confusion, ne laissant que le "PU Unité" visible et pertinent.
* **Couverture Totale** : Fonctionne sur :
    * 🛒 **Ventes** (`sale.order.line`)
    * 🤝 **Achats** (`purchase.order.line`)
    * 📦 **Inventaire & Logistique** (`stock.move`)
    * 🧾 **Facturation** (`account.move.line`)

### 2. 💰 Totaux Globaux (Bas des documents)
* **Total Remise** : Calcule et affiche la somme financière exacte des remises appliquées sur toutes les lignes.
* **FODEC (1%)** : Calcule et affiche la taxe FODEC basée sur le total Hors Taxes.
* Affichage clair, natif, et présent même si la valeur est de 0 pour une totale transparence.
* **Couverture** : Ventes, Achats et Factures.

### 3. 🧾 Impressions PDF (Rapports)
Les rapports imprimables ont été surchargés (via `xpath`) pour inclure ces nouvelles colonnes (`Qté Unités` et `PU Unité`) afin que les clients et fournisseurs aient la même lisibilité.
Les modules et vues (QWeb) qui ont été modifiés sont exactement :
- **Achats** (`purchase`) : Modification de la vue `purchase.report_purchaseorder_document` (Bon de Commande).
- **Facturation** (`account`) : Modification de la vue `account.report_invoice_document` (Facture).
- **Stocks** (`stock`) : Modification de la vue `stock.report_delivery_document` (Bon de Livraison).

### 4. 💻 Caisse Tactile (Point de Vente - POS)
* **Bouton "Unité" sur la caisse** : Permet aux caissiers de changer l'unité de vente (ex: passer de "Unité" à "Pack de 6") à la volée via un popup tactile.
* **Ticket virtuel** : Affiche le "PU Unité" et la "Qté Unités" en direct dans le panier client du Point de Vente.

---

## 🛠️ Architecture Technique & "Best Practices"

Ce module a été codé pour être le plus léger, robuste et maintenable possible, en suivant strictement l'architecture standard d'Odoo ("1 modèle = 1 fichier") et le principe **DRY (Don't Repeat Yourself)**.

### Les 2 "Mixins" (Le cœur du moteur)
Plutôt que de dupliquer des lignes de code dans tous les modèles, la logique mathématique est centralisée dans deux boîtes à outils (Mixins) :
1. **`sah.packaging.mixin`** : S'occupe de la conversion mathématique des quantités et des prix. Il est hérité par toutes les lignes (`sale.order.line`, `purchase.order.line`, `stock.move`, `account.move.line`, `pos.order.line`).
2. **`sah.totals.mixin`** : S'occupe de boucler sur les lignes pour extraire la remise financière totale et calculer le FODEC. Il est hérité par les documents maîtres (`sale.order`, `purchase.order`, `account.move`).

### Adaptations Odoo 19
Le code prend en charge les spécificités des dernières versions d'Odoo, comme l'utilisation intelligente des "Compute Fields" (`sah_actual_qty`) pour contourner les restrictions Read-Only de l'ORM, et la gestion du nouveau système de notes/sections (`display_type = 'product'`).

---

## 🚀 Installation & Utilisation

1. Placez le dossier `sah_packaging_qty` dans votre répertoire d'addons.
2. Redémarrez le service Odoo.
3. Mettez à jour la liste des applications et installez/mettez à jour le module.
4. **Note pour les Ventes :** Assurez-vous d'avoir coché "Remises (Accorder des remises sur les lignes de commande)" dans *Configuration > Ventes > Tarification* pour voir apparaître les remises !
