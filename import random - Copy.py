import random
import time
import os

def pastrimi_i_ekranit():
    """Pastro ekranin për të simuluar një skenë të re."""
    os.system('cls' if os.name == 'nt' else 'clear')

def printo_ngadalë(str, vonesë=0.05):
    """Printon tekstin ngadalë, shkronjë për shkronjë."""
    for shkronjë in str:
        print(shkronjë, end='', flush=True)
        time.sleep(vonesë)
    print()

def printo_visuale(skena):
    """Printon një pamje ASCII në bazë të skenës."""
    pamjet = {
        "fillim": """
        ============================
        | Mirësevini në Aventurën!|
        ============================
            Udhëtimi juaj fillon këtu...
        """,
        "rruga_krejt": """
        Hyni në pyll...
           ,     ,
         ( o )-( o )
           `----'
        Pemët janë të dendura, ajri është i ftohtë.
        Mund të dëgjoni fërshëllimën e gjetheve...
        """,
        "rruga_djathtas": """
        Hyni në një shpellë të errët...
         _______
        /       \\
       |   o o   |
        \\_______/
        Më shijon një erë e lagur.
        Dëgjoni diçka që pikëllon brenda...
        """,
        "pasuri": """
        Gjetët një arkë të fshehtë thesari!
        _  _  _  _ 
       | | | | | | |
       | | | | | | |
       |_|_|_|_|_|_|
        Brenda gjeni 50 copa ari!
        """,
        "dragua": """
        Një dragua e egër shfaqet!
             __====-_  _-====___
        _--^^^#####//      \\#####^^^--_
       -^##########// (    ) \\##########^-_
      _/##########//  |\^^/|  \\##########\_
     /##########//   (@::@)   \\##########\_
    -^##########//     \\//     \\##########^-_
   -############//       ( )       \\############^-_
  _/##########//         ( )         \\##########\_
 /##########//           ( )           \\##########\_
-^##########//            ( )            \\##########^-_
        """,
        "magjistari": """
        Një magjistar i mençur shfaqet!
              _____
            .-'     `-.
           /         \\
          |           |
          |   O   O   |
           \\   (_)   /
            `-._____.-'
        Magjistari ju jep një magji zjarri!
        """
    }
    printo_ngadalë(pamjet.get(skena, ""))

def zgjedh_aksion():
    """Përgjigje për zgjedhjen e një veprimi."""
    printo_ngadalë("Keni dy rrugë para jush.")
    printo_ngadalë("A doni të shkoni majtas apo djathtas?")
    zgjedhja = input("Shkruani 'majtas' ose 'djathtas': ").lower()
    return zgjedhja

def ngjarje_random():
    """Generon një ngjarje të rastësishme."""
    ngjarje = [
        "Gjetët një arkë të fshehtë thesari! Keni fituar 50 ari.",
        "Një dragua e egër shfaqet! Ai rënkon, por arrini të shpëtoni.",
        "Hyni në një hendek dhe humbni disa pikë shëndeti. Jini më të kujdesshëm!",
        "Takoni një magjistar të mençur që ju dhuron një magji."
    ]
    return random.choice(ngjarje)

def loja_aventura():
    """Funksioni kryesor i lojës."""
    pastrimi_i_ekranit()
    printo_visuale("fillim")
    shëndeti = 100
    ari = 0
    magji = []

    while shëndeti > 0:
        # Merrni zgjedhjen e përdoruesit
        aksioni = zgjedh_aksion()
        pastrimi_i_ekranit()

        # Shfaq pamjen në bazë të rrugës të zgjedhur
        if aksioni == 'majtas':
            printo_visuale("rruga_krejt")
        else:
            printo_visuale("rruga_djathtas")

        # Ngjarja e rastësishme në bazë të rrugës të zgjedhur
        ngjarja = ngjarje_random()
        printo_ngadalë(ngjarja)

        if "ari" in ngjarja:
            ari += 50
        elif "dragua" in ngjarja:
            shëndeti -= 10
        elif "hendek" in ngjarja:
            shëndeti -= 20
        elif "magjistari" in ngjarja:
            magji.append("Zjarri")

        # Shfaq statusin aktual
        printo_ngadalë(f"Shëndeti aktual: {shëndeti} | Ari: {ari} | Magjitë: {magji}")
        
        # Kontrolloni nëse shëndeti bie në zero ose më poshtë
        if shëndeti <= 0:
            printo_ngadalë("Keni humbur të gjithë shëndetin tuaj. Loja ka mbaruar!")
            break
        
        # Pyetni nëse lojtari dëshiron të vazhdojë ose jo
        vazhdo_lojën = input("Doni të vazhdoni aventurën? (po/jo): ").lower()
        if vazhdo_lojën != 'po':
            printo_ngadalë("Faleminderit që luajtët! Mirupafshim.")
            break

if __name__ == "__main__":
    loja_aventura()
