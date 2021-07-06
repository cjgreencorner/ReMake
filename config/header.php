<?php
session_start();
?>
<h1>Joel Chapon<h1>
<h3>Ik ben een student die IoT studeert op <a href="https://www.kdg.be/">Karel de Grote Hogeschool</a>!</h3>
<?php
if(!isset($_SESSION['naam']))
    {
        include 'login.php';
    }
    else
    {
        include 'dashboard.php';
    }
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
