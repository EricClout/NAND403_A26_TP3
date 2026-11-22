import sys
# Ajoute le dossier du projet dans les chemins de recherche Python
sys.path.insert(0, r"F:\UQAC\Cours\2e\Creation App 3D\TP\NAND403_A26_TP3")

from ui import AnimationAleatoire

def main():
    global widget               # Ça tool_window ou widget.close ça fait la même chose
    try:
        widget.close()
    except Exception:
        pass

    widget = AnimationAleatoire()
    widget.show()


main()
