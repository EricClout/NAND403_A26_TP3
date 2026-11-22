from maya import cmds
import random

# ------------------------------------------------------------------------------------------
#                                    GÉNÉRATION DE L'ANIMATION
# ------------------------------------------------------------------------------------------
#   - cmds.setKeyframe() permet de créer des clés d'animation.
#   - cmds.cutKey() permet de supprimer des clés d'animation.
#   - cmds.undoInfo(openChunk=True) = Sert à stocker les actions qui seront faites dans Maya pour permettre de faire CTRL+Z one shot
#   - cmds.undoInfo(closeChunk=True) = Ferme le stockage des actions pour appliquer le CTRL+Z one shot
# ------------------------------------------------------------------------------------------
#                           (principe repris de l'Atelier animationCheval)


# Fonction pour récupérer les objets sélectionnés dans Maya
def generer_animation(ui):

    # Récupère les objets sélectionnés dans la scène
    selection = cmds.ls(selection=True, transforms=True)
#             (principe repris de l'Atelier 10)

    # Vérifie si au moins un objet est sélectionné
    if not selection:
        cmds.warning("Attention! Faut au moins sélectionner un objet dans la scène.")
        return
    
    # Récupère les paramètres généraux de l'animation dans l'interface
    duree = ui.duree_spin.value()
    intervalle = ui.intervalle_spin.value()

    # Calcule les frames où les keys d'animation seront placées
    frames = list(range(0, duree + 1, intervalle))

    # Vérifie si la dernière key est incluse dans la durée totale
    # le [-1] récupère toujours le dernier élément de la liste peu importe la longueur de la liste
    if frames[-1] != duree:
        frames.append(duree)

    # Récupère les valeurs Min/Max de la translation
    translation_min = [ui.translation_x_min.value(), ui.translation_y_min.value(), ui.translation_z_min.value()]
    translation_max = [ui.translation_x_max.value(), ui.translation_y_max.value(), ui.translation_z_max.value()]
#                       --------------------
    # Récupère les valeurs Min/Max de la rotation
    rotation_min = [ui.rotation_x_min.value(), ui.rotation_y_min.value(), ui.rotation_z_min.value()]
    rotation_max = [ui.rotation_x_max.value(), ui.rotation_y_max.value(), ui.rotation_z_max.value()]
#                       --------------------
    # Récupère les valeurs Min/Max du Scale
    scale_min = [ui.scale_x_min.value(), ui.scale_y_min.value(), ui.scale_z_min.value()]
    scale_max = [ui.scale_x_max.value(), ui.scale_y_max.value(), ui.scale_z_max.value()]
#                       --------------------

# ------------------------------------------------------------------------------------------
#                                    CTRL+Z ouverture du stockage
# 1- Ouvre le bloc CTRL+Z.
# 2- Parcourt chaque objet sélectionné.
# 3- Supprime les anciennes keys avec cmds.cutKey(objet, clear=True).
# 4- Prépare les listes de valeurs random.
# 5- Génère la nouvelle animation.
# ------------------------------------------------------------------------------------------
#                       (cmds.cutKey() principe repris de l'Atelier animationCheval)
    try:
        # Regroupe toutes les modifs de l'animation pour permettre un seul Ctrl+Z
        cmds.undoInfo(openChunk=True, chunkName="AnimationAleatoire")

        # Parcourt chaque obj sélectionné 1 à 1 dans Maya
        for objet in selection:

            # Vérifie si l'objet possède déjà des keys d'animation
            nombre_keys = cmds.keyframe(objet, query=True, keyframeCount=True)

            # Vérifie si le résultat contient un nombre de keys
            if nombre_keys is not None:

                # Vérifie si l'objet possède au moins une key
                if nombre_keys > 0:

                    # Supprime les anciennes keys d'animation
                    cmds.cutKey(objet, clear=True)

            # Prépare les listes pour conserver les valeurs random de départ
            translation_depart = []
            rotation_depart = []
            scale_depart = []


# ------------------------------------------------------------------------------------------
#           Créer les trois valeurs XYZ random de départ pour chaque objet sélectionné
# ------------------------------------------------------------------------------------------
#                       (random.uniform() principe repris de l'Atelier 4)
            # Génère des valeurs random de départ pour chaque axe XYZ
            # **append() ajoute chaque valeur à la fin de la liste**
            for i in range(3):

                # Génère une valeur random pour la translation
                valeur_translation = random.uniform(translation_min[i], translation_max[i])
                translation_depart.append(valeur_translation)
#                       --------------------
                # Génère une valeur random pour la rotation
                valeur_rotation = random.uniform(rotation_min[i], rotation_max[i])
                rotation_depart.append(valeur_rotation)
#                       --------------------
                # Génère une valeur random pour le Scale
                valeur_scale = random.uniform(scale_min[i], scale_max[i])
                scale_depart.append(valeur_scale)
# ------------------------------------------------------------------------------------------
#                   Créer les premières keys avec les trois valeurs ci-haut
# ------------------------------------------------------------------------------------------
#                       (principe repris de l'Atelier animationCheval)
            # Crée les premières keys de translation
            cmds.setKeyframe(objet, attribute="translateX", value=translation_depart[0], time=frames[0])
            cmds.setKeyframe(objet, attribute="translateY", value=translation_depart[1], time=frames[0])
            cmds.setKeyframe(objet, attribute="translateZ", value=translation_depart[2], time=frames[0])
#                       --------------------
            # Crée les premières keys de rotation
            cmds.setKeyframe(objet, attribute="rotateX", value=rotation_depart[0], time=frames[0])
            cmds.setKeyframe(objet, attribute="rotateY", value=rotation_depart[1], time=frames[0])
            cmds.setKeyframe(objet, attribute="rotateZ", value=rotation_depart[2], time=frames[0])
#                       --------------------
            # Crée les premières keys de Scale
            cmds.setKeyframe(objet, attribute="scaleX", value=scale_depart[0], time=frames[0])
            cmds.setKeyframe(objet, attribute="scaleY", value=scale_depart[1], time=frames[0])
            cmds.setKeyframe(objet, attribute="scaleZ", value=scale_depart[2], time=frames[0])

# ------------------------------------------------------------------------------------------
#           Créer les keys random au centre (Première et Dernière sont exclues)
# ------------------------------------------------------------------------------------------
            # Parcourt les frames entre la première et la dernière
            for i in range(1, len(frames) - 1):

                frame = frames[i]
#                       -------------------- translation
                # Génère une valeur random pour chaque axe XYZ de la translation
                valeur_translation_x = random.uniform(translation_min[0], translation_max[0])
                valeur_translation_y = random.uniform(translation_min[1], translation_max[1])
                valeur_translation_z = random.uniform(translation_min[2], translation_max[2])

                # Crée les keys de translation
                cmds.setKeyframe(objet, attribute="translateX", value=valeur_translation_x, time=frame)
                cmds.setKeyframe(objet, attribute="translateY", value=valeur_translation_y, time=frame)
                cmds.setKeyframe(objet, attribute="translateZ", value=valeur_translation_z, time=frame)
#                       -------------------- rotation
                # Génère une valeur random pour chaque axe XYZ de la rotation
                valeur_rotation_x = random.uniform(rotation_min[0], rotation_max[0])
                valeur_rotation_y = random.uniform(rotation_min[1], rotation_max[1])
                valeur_rotation_z = random.uniform(rotation_min[2], rotation_max[2])

                # Crée les keys de rotation
                cmds.setKeyframe(objet, attribute="rotateX", value=valeur_rotation_x, time=frame)
                cmds.setKeyframe(objet, attribute="rotateY", value=valeur_rotation_y, time=frame)
                cmds.setKeyframe(objet, attribute="rotateZ", value=valeur_rotation_z, time=frame)
#                       -------------------- scale
                # Génère une valeur random pour chaque axe XYZ du Scale
                valeur_scale_x = random.uniform(scale_min[0], scale_max[0])
                valeur_scale_y = random.uniform(scale_min[1], scale_max[1])
                valeur_scale_z = random.uniform(scale_min[2], scale_max[2])

                # Crée les keys de Scale
                cmds.setKeyframe(objet, attribute="scaleX", value=valeur_scale_x, time=frame)
                cmds.setKeyframe(objet, attribute="scaleY", value=valeur_scale_y, time=frame)
                cmds.setKeyframe(objet, attribute="scaleZ", value=valeur_scale_z, time=frame)

# ------------------------------------------------------------------------------------------
#   Créer les dernières keys pour fermer la boucle seamless (copie des premières keys, excepté [0] devient [-1])
# ------------------------------------------------------------------------------------------
            # Crée les dernières keys de translation avec les valeurs de départ
            cmds.setKeyframe(objet, attribute="translateX", value=translation_depart[0], time=frames[-1])
            cmds.setKeyframe(objet, attribute="translateY", value=translation_depart[1], time=frames[-1])
            cmds.setKeyframe(objet, attribute="translateZ", value=translation_depart[2], time=frames[-1])
#                       --------------------
            # Crée les dernières keys de rotation avec les valeurs de départ
            cmds.setKeyframe(objet, attribute="rotateX", value=rotation_depart[0], time=frames[-1])
            cmds.setKeyframe(objet, attribute="rotateY", value=rotation_depart[1], time=frames[-1])
            cmds.setKeyframe(objet, attribute="rotateZ", value=rotation_depart[2], time=frames[-1])
#                       --------------------
            # Crée les dernières keys de Scale avec les valeurs de départ
            cmds.setKeyframe(objet, attribute="scaleX", value=scale_depart[0], time=frames[-1])
            cmds.setKeyframe(objet, attribute="scaleY", value=scale_depart[1], time=frames[-1])
            cmds.setKeyframe(objet, attribute="scaleZ", value=scale_depart[2], time=frames[-1])

# ------------------------------------------------------------------------------------------
#                              PLAGE DE LECTURE DE L'ANIMATION
# ------------------------------------------------------------------------------------------
        # Ajuste la plage de lecture selon la durée choisie dans l'interface
        cmds.playbackOptions(minTime=0, maxTime=duree, animationStartTime=0, animationEndTime=duree)
#                           (principe repris de l'Atelier animationCheval)

# ------------------------------------------------------------------------------------------
#                                   CTRL+Z fermeture du stockage
# ------------------------------------------------------------------------------------------
    finally:
        # Ferme le bloc CTRL+Z pour regrouper toutes les modifs et pouvoir faire undo one shot
        cmds.undoInfo(closeChunk=True)
