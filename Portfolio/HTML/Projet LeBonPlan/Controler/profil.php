<?php
header('Content-Type: text/html; charset=utf-8');

$host = "localhost";
$dbname = "stage";
$username = "root";
$password = "root";

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erreur de connexion : " . $e->getMessage());
}

// ⚠️ Si on reçoit une requête AJAX de recherche, on retourne uniquement les résultats
if (isset($_GET['search']) && !empty($_GET['search'])) {
    $search = trim($_GET['search']);
   
    $query = "SELECT a.ID_ano, a.description, e.nom_ent
              FROM Annonce a
              JOIN Entreprise e ON a.ID_ent = e.ID_ent
              WHERE a.description LIKE :search";
   
    $stmt = $pdo->prepare($query);
    $stmt->execute(['search' => "%$search%"]);
    $annonces = $stmt->fetchAll(PDO::FETCH_ASSOC);

    if (count($annonces) > 0) {
        foreach ($annonces as $annonce) {
            echo '<div class="annonce">';
            echo '  <div class="box">';
            echo '    <h2 class="annonce-title">Société: ' . htmlspecialchars($annonce['nom_ent']) . ' |</h2>';
            echo '    <p class="annonce-description">' . htmlspecialchars($annonce['description']) . '</p>';
            echo '    <p class="annonce-mode">Mode : ' . htmlspecialchars($annonce['mode']) . '</p>';
            echo '    <button class="voir-offre-btn">Voir l\'offre</button>';
            echo '  </div>';
            echo '</div>';
        }
    } else {
        echo '<p>Aucune offre trouvée.</p>';
    }

    exit; // 👈 important : empêche d'afficher tout le HTML ci-dessous
}
?>


<!doctype html> 
<html lang="fr"> 
   <head> 
      <meta charset="utf-8">
      <meta name="description" content="Postuler à une offre de stage">
      <title>Lebonplan</title>
      <link rel="stylesheet" href="profil_etu.css">
      <link rel="icon" href="logo_chap.png">
    </head> 
    <body>
    <header style="text-align: center; padding: 20px;">
        <img src="logo.png" alt="Logo" style="width: 500px;"> 
    </header>
    <header>
        <div class="navbar">
            <!-- Bouton hamburger -->
            <button class="menu-toggle" id="menu-toggle" aria-label="Ouvrir le menu">&#9776;</button>

            <nav class="nav-items-container">
                <ul class="main-menu" id="main-menu">
                    <li class="menu-item"><a href="accueil_etu.php" class="top-level-entry ">Accueil</a></li>
                    <li class="menu-item"><a href="contact_etu.HTML" class="top-level-entry">Contact</a></li>
                    <li class="menu-item"><a href="profil.HTML" class="top-level-entry active">Profil</a></li>
                    <li class="menu-item"><a href="recherche_etu.php" class="top-level-entry">Offre</a></li>


                </ul>

                <!-- Liens de Connexion et S'inscrire à droite -->
                <div class="auth-links">
                    <a href="index.php" class="button">Déconnexion</a>
                </div>
            </nav>
        </div>
        <nav>
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="./profil.HTML">Profil</a></li>

            </ol>
        </nav>
        <br>
     </header>

    <!-- Contenu principal -->
    <main class="content">
        <section class="company">
            <img src="anakin.png"  class="company-logo">
            <div class="company-info">
                <h2>Anakin Skywalker</h2>
                <p>2eme année d'ingénieurie</p>
                <p>
                    Etudie l'informatique en école d'ingénieur. Etidiant motivé et dynamique
                </p>


                <a href="modifierprofil_etu.html">
                    <button class="profile">Modifier mon profil</button>
                </a>
                
            </div>
        </section>

        <section class="job-offer">
            <img src="./images/cesi.png"  class="hiring-img">
            <div class="job-info">
                <h3>CESI</h3>
                  <p>Capus de Montpellier</p>
                <p>Réseau de campus d’enseignement supérieur et de formation professionnelle, CESI permet à des étudiants, alternants et salariés de devenir acteurs des transformations des entreprises et de la société.</p>
            </div>
        </section>
    </main>
   <!-- Barre de recherche -->
<div class="search-container" style="text-align:center; margin:20px;">
  <input type="text" id="search-input" class="search-input" placeholder="Rechercher un stage (par description, mode ou entreprise)">
  <button type="button" class="search-button" onclick="rechercherOffres()">Rechercher</button>
</div>

<h1 class="titre-page">Offres de stage pour vous</h1>

<!-- Conteneur des annonces -->
<div class="container" id="annonces-container">
  <!-- Les résultats AJAX apparaîtront ici -->
</div>

<!-- Script JS AJAX -->
<script>
  function rechercherOffres() {
      const input = document.getElementById("search-input").value.trim();

      // 👉 Si le champ est vide, on efface les résultats et on sort
      if (input === "") {
          document.getElementById("annonces-container").innerHTML = "";
          return;
      }

      const xhr = new XMLHttpRequest();
      xhr.open("GET", window.location.pathname + "?search=" + encodeURIComponent(input), true);
      xhr.onreadystatechange = function () {
          if (xhr.readyState === 4 && xhr.status === 200) {
              document.getElementById("annonces-container").innerHTML = xhr.responseText;
          }
      };
      xhr.send();
  }

  // Rechercher à chaque frappe (optionnel mais fluide)
  document.getElementById("search-input").addEventListener("keyup", function () {
      rechercherOffres();
  });
</script>
</body> 
<footer class="footer">
  <div class="footer-container">
    <!-- Colonne 1 : Logos -->
    <div class="footer-column">
      <img src="logo_chap.png" alt="Logo principal" class="footer-logo">
    </div>

    <!-- Colonne 2 : Coordonnées -->
    <div class="footer-column">
      <h3>Coordonnées</h3>
      <a  style='color:#ffffff'href="https://www.google.fr/maps/place/Campus+CESI/@43.5792319,3.9432547,794m/data=!3m2!1e3!4b1!4m6!3m5!1s0x12b6afdaa52cccbf:0xa4dd1993e0746bd!8m2!3d43.5792281!4d3.9481256!16s%2Fg%2F1v202y6s?entry=ttu&g_ep=EgoyMDI1MDIwMi4wIKXMDSoASAFQAw%3D%3D">Immeuble Le Quatrième Zone Aéroportuaire de Montpellier Méditerranée, 34130 Mauguio</a>
      <p><i class="fa-solid fa-envelope"></i> contact@cesi.fr</p>
      <p><i class="fa-solid fa-phone"></i> +33 6 12 34 56 78</p>
    </div>

    <!-- Colonne 3 : Navigation -->
    <div class="footer-column">
      <h3>Navigation</h3>
      <ul class="footer-links">
        <li><a href="./coockies_etu.html">Cookies</a></li>
        <li><a href="./faq_etu.html">F.A.Q</a></li>
        <li><a href="./cgu_etu.html">Conditions générales</a></li>
        <li><a href="./protection_etu.html">Politique de protection des données</a></li>
        <li><a href="./mentions_legales_etu.html">Mentions légales</a></li>
      </ul>
    </div>

    <!-- Colonne 4 : Réseaux sociaux -->
    <div class="footer-column">
      <h3>Suivez-nous</h3>
      <div class="social-buttons">
        <a class="social-button twitter" href="https://x.com/cesi_officiel?s=21" target="_blank"><i class="fa-brands fa-twitter">
          <img class="twitter" 
                      src="./images/Twitter.png"></i></a>
          <a class="social-button tiktok" href=" https://www.tiktok.com/@bde_cesi_mtp?_t=ZN-8tezCXXQ3tO&_r=1" target="_blank"><i class="fa-brands fa-tiktok">
                  <img class="TikTok" 
                      src="./images/tiktok.png"></i></a>
          <a class="social-button instagram" href=" https://www.instagram.com/bde.cesi.montpellier?igsh=MWVhaWFvNGNvcDZuNw==" target="_blank"><i class="fa-brands fa-instagram">
          <img class="instagram" 
                      src="./images/instagram.png"></i></a>
      </div>
    </div>
  </div>

  <!-- Bas de page -->
  <div class="footer-bottom">
    <p>Copyright © 2025 - Tous droits réservés. <a href="./mentions_legales.html">Mentions légales</a></p>
  </div>
</footer>
<script src="../Controler/menu.js"></script> 
</html>