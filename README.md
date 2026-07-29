# 📦 SAH Lilas Distribution - Gestion Avancée des Conditionnements

![Odoo Version](https://img.shields.io/badge/Odoo-19.0-purple?style=for-the-badge&logo=odoo)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![OWL](https://img.shields.io/badge/OWL-Framework-orange?style=for-the-badge&logo=javascript)

## 📖 À propos

**SAH Lilas Distribution** optimise la gestion des conditionnements dans Odoo 19. Le module affiche automatiquement la quantité en unités de base et le vrai prix unitaire sur l'ensemble de l'ERP (Ventes, Achats, Stocks) et permet aux caissiers du Point de Vente (POS) de basculer l'unité de vente à la volée.

Dans un environnement de distribution où les produits sont manipulés sous différentes unités de mesure (Packs, Cartons, Palettes), il est crucial d'éviter les erreurs de calcul mental. Ce module harmonise l'affichage de l'ensemble de l'ERP en fournissant des données fiables et claires en temps réel.

## ✨ Fonctionnalités Principales

* **Conversion Dynamique (Backend)** : Ajout automatique des colonnes `Qté Unités` et `PU Unité` sur les lignes de documents. Le système convertit la quantité et le prix du conditionnement choisi vers l'unité de base du produit.
* **Couverture Totale de l'ERP** : Fonctionnalité implémentée de bout-en-bout sur :
    * 🛒 **Ventes** (`sale.order`)
    * 🤝 **Achats** (`purchase.order`)
    * 📦 **Inventaire & Logistique** (`stock.picking`)
    * 🧾 **Facturation** (`account.move`)
* **Transparence Documentaire (Rapports PDF)** : Modification des rapports imprimables (Devis, Factures, Bons de réception) pour inclure ces données cruciales pour les clients et fournisseurs.
* **Point de Vente Augmenté (POS)** :
    * Interface tactile enrichie d'un bouton "Balance" pour switcher l'unité de vente à la volée (ex: basculer de "Unité" à "Pack de 6").
    * Affichage en temps réel de la `Qté Unités` et du `PU Unité` directement dans le panier (Ticket POS) de la caisse.

## 🛠️ Architecture Technique

Ce module a été conçu en respectant scrupuleusement les *Best Practices* de développement Odoo :

* **DRY (Don't Repeat Yourself)** : La logique de conversion mathématique est centralisée dans un modèle abstrait (`sah.packaging.mixin`). Les modèles Odoo (Achats, Ventes, Factures, Stock) héritent simplement de ce Mixin, garantissant un code propre et hautement maintenable.
* **OWL (Odoo Web Library) Patching** : Le frontend du Point de Vente (POS) a été modifié en utilisant la méthode native `patch()` d'Odoo 19 sur `PosOrderline` et `ControlButtons`. Cela assure une compatibilité parfaite et d'excellentes performances sans modifier le noyau d'Odoo.

## 🚀 Installation

1. Clonez ce repository dans votre dossier d'addons Odoo.
2. Redémarrez votre service Odoo.
3. Activez le "Mode Développeur" dans Odoo.
4. Allez dans **Applications** > **Mise à jour de la liste des applications**.
5. Cherchez `sah_packaging_qty` et cliquez sur **Activer**.
