import json
import urllib.request

VERSION_ACTUELLE = "3.2"
REPO_GITHUB = "Scratch-OS-X/OS-Cert-Center"


print(f"\nVersion actuelle : \033[1m[v. {VERSION_ACTUELLE}]\033[0m.\n")

def maj():
    url = f"https://api.github.com/repos/{REPO_GITHUB}/releases/latest"
    headers = {"User-Agent": "OS-Cert-Center-App"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=3) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                derniere_version = data["tag_name"].lstrip("v")

                if derniere_version != VERSION_ACTUELLE:
                    print(
                        f"\033[93m⚠️  [MISE À JOUR] Une nouvelle version ({derniere_version}) est disponible !"
                    )
                    print(
                        f"Tapez 'git pull origin main' dans votre terminal pour la récupérer.\033[0m\n"
                    )
                else:
                    return True
    except Exception:
        pass
    return False


maj()
