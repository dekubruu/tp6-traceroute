import argparse
import subprocess
import re
import platform

def traceroute(target, progressive=False, output_file=None):
    """
    Effectue un traceroute vers l'URL ou l'adresse IP cible.

    Args:
        target (str): URL ou adresse IP cible.
        progressive (bool): Si True, affiche les résultats au fur et à mesure.
        output_file (str): Chemin du fichier où enregistrer les résultats (optionnel).

    Returns:
        list: Liste des adresses IP des sauts.
    """
    try:
        # Détecter le système d'exploitation et utiliser la commande appropriée
        if platform.system().lower() == "windows":
            command = ["tracert", target]
        else:
            command = ["traceroute", target]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        ip_list = []

        # Ouvrir le fichier si l'option output_file est fournie
        f = open(output_file, "w") if output_file else None

        for line in process.stdout:
            match = re.search(r"\d{1,3}(?:\.\d{1,3}){3}", line)
            if match:
                ip = match.group(0)
                ip_list.append(ip)
                if progressive:
                    print(ip)
                if f:
                    f.write(ip + "\n")

        process.wait()
        if f:
            f.close()
        return ip_list

    except Exception as e:
        print(f"Erreur lors de l'exécution du traceroute : {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description="Script traceroute TP6")
    parser.add_argument("target", help="URL ou adresse IP cible")
    parser.add_argument(
        "-p", "--progressive", action="store_true", help="Affiche les résultats au fur et à mesure"
    )
    parser.add_argument(
        "-o", "--output-file", help="Chemin du fichier où enregistrer les résultats"
    )

    args = parser.parse_args()
    traceroute(args.target, args.progressive, args.output_file)


if __name__ == "__main__":
    main()
