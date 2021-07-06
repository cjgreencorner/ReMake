<?php
include 'style.php';
include 'db.php';
//  include 'db.php';
if (isset($_GET['x'])) {
  $teller= $_GET['x']+$_GET['y'];
  for ($a = 1; $a <= $teller; $a++) {
    echo "<img src='https://photos.puppyspot.com/6/listing/634596/photo/5402733_large-resize.jpg' width=150>";
  }
}
?>
<h1>Joel Chapon<h1>
<h3>Ik ben een student die IoT studeert op <a href="https://www.kdg.be/">Karel de Grote Hogeschool</a>!</h3>

<?php
  // When form submitted, insert values into the database.
  if ($_SERVER['REQUEST_METHOD'] == "POST") {
      // removes backslashes
      $id       = uniqid("id", true);
      $naam     = $_POST['naam'];
      $username = $_POST['gebruikersnaam'];
      $email    = $_POST['mail'];
      $password = $_POST['wachtwoord'];
      $query    = "insert into users (id, naam, gebruikersnaam, wachtwoord, mail)
                   values ('$id', '$naam', '$username', '" . md5($password) . "', '$email')";
      $result   = mysqli_query($conn, $query);
      if ($result) {
          echo "<div class='form'>
                <h3>You are registered successfully.</h3><br/>
                </div>";
          echo "<p class='login-lost'><a href='/index.php'>Login</a></p>";
      } else {
          echo "<div class='form'>
                <h3>Required fields are missing.</h3><br/>
                </div>";
      }
  } else {
?>
<html>
<body>
  <form class="form" action="" method="post">
      <h2 class="login-title">Een account maken</h2>
      <input type="text" class="login-input" name="naam" placeholder="Naam" required />
      <input type="text" class="login-input" name="gebruikersnaam" placeholder="Gebruikersnaam">
      <input type="text" class="login-input" name="mail" placeholder="E-mail">
      <input type="password" class="login-input" name="wachtwoord" placeholder="Wachtwoord">
      <input type="submit" name="submit" value="Maak een account" class="login-button">
      <p class="login-lost"><a href="/index.php">Login</a></p>
  </form>
<?php } ?>
  <center><img src="/img/pf.jpg" alt="Foto van mezelf"></center>
<?php  include 'footer.php';
?>
