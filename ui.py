import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QSpinBox,
    QDoubleSpinBox,
    QGridLayout,
    QPushButton
)

import animator

#   Fait que le popup de l'outil soit tjs apparent dans maya même si on clique à côté
def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)
# ------------------------------------------------------------------------------------------
#   Note à moi-même : Reprendre les codes déjà fait dans les Ateliers et TP2 pour avoir une base.
# ------------------------------------------------------------------------------------------

class AnimationAleatoire(QWidget):

    def __init__(self):
        super().__init__(maya_main_window())            # Va avec les def maya_main_window() ci-haut.
        self.setWindowFlags(Qt.Window)

        # Titre de la fenêtre & ses dimensions
        self.setWindowTitle("Animation aléatoire")
        self.resize(450, 600)

        self.create_ui()

#                       --------------------

    # Lance la génération de l'animation
    def lancer_generation(self):
        animator.generer_animation(self)

#                       --------------------

    # Création de l'interface utilisateur PySide6
    def create_ui(self):
        # Layout principal vertical
        layout = QVBoxLayout(self)

# ------------------------------------------------------------------------------------------
#                                    PARAMÈTRES GÉNÉRAUX
# ------------------------------------------------------------------------------------------
#   Info utile à savoir :
#   - QLabel = Affiche un texte dans l'interface
#   - QVBoxLayout = Organise les éléments verticalement, un sous l'autre
#   - QSpinBox = Champ éditable pour entrer un nombre entier
#   - QDoubleSpinBox = Champ éditable pour entrer un nombre décimal
#   - QGridLayout = Permet d'organiser les éléments en lignes et colonnes
#   - layout.addWidget() = Ajoute un élément au layout principal
#   - setRange(min, max) = Définit la valeur minimale et maximale permise
#   - setValue() = Définit la valeur affichée par défaut
# ------------------------------------------------------------------------------------------
#                           (principe des widgets de l'Atelier 4)

        # Titre de la section
        titre = QLabel("Paramètres de l'animation")
        layout.addWidget(titre)

        # Durée de l'animation en frames
        self.duree_spin = QSpinBox()                    # Crée la case éditable
        self.duree_spin.setRange(1, 1000)               # Range min/max de 1 à 1000 frames
        self.duree_spin.setValue(120)                   # Valeur par défaut de 120 frames

        # Crée la ligne du texte (label) et du spinbox au layout vertical
        layout.addWidget(QLabel("Durée de l'animation (frames)"))
        layout.addWidget(self.duree_spin)

        # Intervalle entre les clés
        self.intervalle_spin = QSpinBox()               # Crée le champ éditable
        self.intervalle_spin.setRange(1, 1000)          # Range min/max de 1 à 1000 frames
        self.intervalle_spin.setValue(10)               # Valeur par défaut de 10 frames

        # Crée la ligne du texte (label) et du spinbox au layout vertical
        layout.addWidget(QLabel("Intervalle entre les clés (frames)"))
        layout.addWidget(self.intervalle_spin)

# ------------------------------------------------------------------------------------------
#                                       TRANSLATION
# ------------------------------------------------------------------------------------------
#   Info utile à savoir :
#   - Les valeurs Min/Max déterminent les limites aléatoires possibles pour chaque axe de translation.
#   - Les axes XYZ sont configurés indépendamment.
#   - setDecimals() = Définit le nombre de chiffres après la virgule
#   - setSingleStep() = Définit l'incrément lorsqu'on utilise les flèches du champ
# ------------------------------------------------------------------------------------------
#               (principe des grilles et des champs Min/Max de l'Atelier 4)
    
        # Titre de la section
        titre_translation = QLabel("Translation")
        layout.addWidget(titre_translation)

        # Création de la grille pour organiser les axes et les valeurs Min/Max
        grille_translation = QGridLayout()
        layout.addLayout(grille_translation)

        # Titres des colonnes
        grille_translation.addWidget(QLabel("Axe"), 0, 0)
        grille_translation.addWidget(QLabel("Min"), 0, 1)
        grille_translation.addWidget(QLabel("Max"), 0, 2)

        # Création des champs pour l'axe X
        self.translation_x_min = QDoubleSpinBox()
        self.translation_x_min.setRange(-1000, 1000)
        self.translation_x_min.setValue(-10)
        self.translation_x_min.setDecimals(2)
        self.translation_x_min.setSingleStep(0.1)

        self.translation_x_max = QDoubleSpinBox()
        self.translation_x_max.setRange(-1000, 1000)
        self.translation_x_max.setValue(10)
        self.translation_x_max.setDecimals(2)
        self.translation_x_max.setSingleStep(0.1)

        # Création des champs pour l'axe Y
        self.translation_y_min = QDoubleSpinBox()
        self.translation_y_min.setRange(-1000, 1000)
        self.translation_y_min.setValue(-10)
        self.translation_y_min.setDecimals(2)
        self.translation_y_min.setSingleStep(0.1)

        self.translation_y_max = QDoubleSpinBox()
        self.translation_y_max.setRange(-1000, 1000)
        self.translation_y_max.setValue(10)
        self.translation_y_max.setDecimals(2)
        self.translation_y_max.setSingleStep(0.1)

        # Création des champs pour l'axe Z
        self.translation_z_min = QDoubleSpinBox()
        self.translation_z_min.setRange(-1000, 1000)
        self.translation_z_min.setValue(-10)
        self.translation_z_min.setDecimals(2)
        self.translation_z_min.setSingleStep(0.1)

        self.translation_z_max = QDoubleSpinBox()
        self.translation_z_max.setRange(-1000, 1000)
        self.translation_z_max.setValue(10)
        self.translation_z_max.setDecimals(2)
        self.translation_z_max.setSingleStep(0.1)

        # Ajout des axes et des champs Min/Max dans la grille
        grille_translation.addWidget(QLabel("X"), 1, 0)
        grille_translation.addWidget(self.translation_x_min, 1, 1)
        grille_translation.addWidget(self.translation_x_max, 1, 2)

        grille_translation.addWidget(QLabel("Y"), 2, 0)
        grille_translation.addWidget(self.translation_y_min, 2, 1)
        grille_translation.addWidget(self.translation_y_max, 2, 2)

        grille_translation.addWidget(QLabel("Z"), 3, 0)
        grille_translation.addWidget(self.translation_z_min, 3, 1)
        grille_translation.addWidget(self.translation_z_max, 3, 2)

# ------------------------------------------------------------------------------------------
#                                      ROTATION
# ------------------------------------------------------------------------------------------
#   Info utile à savoir :
#   - IDEM à TRANSLATION
#   - Les valeurs de rotation sont exprimées en degrés.
# ------------------------------------------------------------------------------------------
#           (même principe que Translation, adapté aux valeurs de rotation)

        # Titre de la section
        titre_rotation = QLabel("Rotation")
        layout.addWidget(titre_rotation)

        # Création de la grille pour organiser les axes et les valeurs Min/Max
        grille_rotation = QGridLayout()
        layout.addLayout(grille_rotation)

        # Titres des colonnes
        grille_rotation.addWidget(QLabel("Axe"), 0, 0)
        grille_rotation.addWidget(QLabel("Min"), 0, 1)
        grille_rotation.addWidget(QLabel("Max"), 0, 2)

        # Création des champs pour l'axe X
        self.rotation_x_min = QDoubleSpinBox()
        self.rotation_x_min.setRange(-360, 360)
        self.rotation_x_min.setValue(-45)
        self.rotation_x_min.setDecimals(2)
        self.rotation_x_min.setSingleStep(1)

        self.rotation_x_max = QDoubleSpinBox()
        self.rotation_x_max.setRange(-360, 360)
        self.rotation_x_max.setValue(45)
        self.rotation_x_max.setDecimals(2)
        self.rotation_x_max.setSingleStep(1)

        # Création des champs pour l'axe Y
        self.rotation_y_min = QDoubleSpinBox()
        self.rotation_y_min.setRange(-360, 360)
        self.rotation_y_min.setValue(-180)
        self.rotation_y_min.setDecimals(2)
        self.rotation_y_min.setSingleStep(1)

        self.rotation_y_max = QDoubleSpinBox()
        self.rotation_y_max.setRange(-360, 360)
        self.rotation_y_max.setValue(180)
        self.rotation_y_max.setDecimals(2)
        self.rotation_y_max.setSingleStep(1)

        # Création des champs pour l'axe Z
        self.rotation_z_min = QDoubleSpinBox()
        self.rotation_z_min.setRange(-360, 360)
        self.rotation_z_min.setValue(-45)
        self.rotation_z_min.setDecimals(2)
        self.rotation_z_min.setSingleStep(1)

        self.rotation_z_max = QDoubleSpinBox()
        self.rotation_z_max.setRange(-360, 360)
        self.rotation_z_max.setValue(45)
        self.rotation_z_max.setDecimals(2)
        self.rotation_z_max.setSingleStep(1)

        # Ajout des axes et des champs Min/Max dans la grille
        grille_rotation.addWidget(QLabel("X"), 1, 0)
        grille_rotation.addWidget(self.rotation_x_min, 1, 1)
        grille_rotation.addWidget(self.rotation_x_max, 1, 2)

        grille_rotation.addWidget(QLabel("Y"), 2, 0)
        grille_rotation.addWidget(self.rotation_y_min, 2, 1)
        grille_rotation.addWidget(self.rotation_y_max, 2, 2)

        grille_rotation.addWidget(QLabel("Z"), 3, 0)
        grille_rotation.addWidget(self.rotation_z_min, 3, 1)
        grille_rotation.addWidget(self.rotation_z_max, 3, 2)

# ------------------------------------------------------------------------------------------
#                                    SCALE
# ------------------------------------------------------------------------------------------
#   Info utile à savoir :
#   - IDEM à TRANSLATION
#   - Une valeur de 1 représente la taille originale de l'objet.
#   - Une valeur de 2 double la taille et une valeur de 0.5 réduit la taille de moitié.
# ------------------------------------------------------------------------------------------
#           (même principe que Translation, adapté aux valeurs du scale)

        # Titre de la section
        titre_scale = QLabel("Scale")
        layout.addWidget(titre_scale)

        # Création de la grille pour organiser les axes et les valeurs Min/Max
        grille_scale = QGridLayout()
        layout.addLayout(grille_scale)

        # Titres des colonnes
        grille_scale.addWidget(QLabel("Axe"), 0, 0)
        grille_scale.addWidget(QLabel("Min"), 0, 1)
        grille_scale.addWidget(QLabel("Max"), 0, 2)

        # Création des champs pour l'axe X
        self.scale_x_min = QDoubleSpinBox()
        self.scale_x_min.setRange(0.01, 10)
        self.scale_x_min.setValue(0.8)
        self.scale_x_min.setDecimals(2)
        self.scale_x_min.setSingleStep(0.1)

        self.scale_x_max = QDoubleSpinBox()
        self.scale_x_max.setRange(0.01, 10)
        self.scale_x_max.setValue(1.2)
        self.scale_x_max.setDecimals(2)
        self.scale_x_max.setSingleStep(0.1)

        # Création des champs pour l'axe Y
        self.scale_y_min = QDoubleSpinBox()
        self.scale_y_min.setRange(0.01, 10)
        self.scale_y_min.setValue(0.8)
        self.scale_y_min.setDecimals(2)
        self.scale_y_min.setSingleStep(0.1)

        self.scale_y_max = QDoubleSpinBox()
        self.scale_y_max.setRange(0.01, 10)
        self.scale_y_max.setValue(1.2)
        self.scale_y_max.setDecimals(2)
        self.scale_y_max.setSingleStep(0.1)

        # Création des champs pour l'axe Z
        self.scale_z_min = QDoubleSpinBox()
        self.scale_z_min.setRange(0.01, 10)
        self.scale_z_min.setValue(0.8)
        self.scale_z_min.setDecimals(2)
        self.scale_z_min.setSingleStep(0.1)

        self.scale_z_max = QDoubleSpinBox()
        self.scale_z_max.setRange(0.01, 10)
        self.scale_z_max.setValue(1.2)
        self.scale_z_max.setDecimals(2)
        self.scale_z_max.setSingleStep(0.1)

        # Ajout des axes et des champs Min/Max dans la grille
        grille_scale.addWidget(QLabel("X"), 1, 0)
        grille_scale.addWidget(self.scale_x_min, 1, 1)
        grille_scale.addWidget(self.scale_x_max, 1, 2)

        grille_scale.addWidget(QLabel("Y"), 2, 0)
        grille_scale.addWidget(self.scale_y_min, 2, 1)
        grille_scale.addWidget(self.scale_y_max, 2, 2)

        grille_scale.addWidget(QLabel("Z"), 3, 0)
        grille_scale.addWidget(self.scale_z_min, 3, 1)
        grille_scale.addWidget(self.scale_z_max, 3, 2)

# ------------------------------------------------------------------------------------------
#                                    GÉNÉRATION
# ------------------------------------------------------------------------------------------
#   Info utile à savoir :
#   - QPushButton = Bouton cliquable
# ------------------------------------------------------------------------------------------
#                       (principe des boutons de l'Atelier 6)

        # Bouton pour générer une nouvelle animation
        self.bouton_generation = QPushButton("Générer l'animation")     # Crée le bouton
        layout.addWidget(self.bouton_generation)                        # Affiche le bouton
        self.bouton_generation.clicked.connect(self.lancer_generation)  # Connecte le bouton

