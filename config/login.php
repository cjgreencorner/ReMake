<?php
include 'db.php';
if ($_SERVER['REQUEST_METHOD'] == "POST") {
  $gebruikersnaam = $_POST['gebruikersnaam'];
  $password = $_POST['wachtwoord'];
  $query = "select * from users where gebruikersnaam='$gebruikersnaam'
            and wachtwoord='".md5($password)."'";
	$result = mysqli_query($conn,$query) or die(mysql_error());
	$rows = mysqli_num_rows($result);
    if($rows==1){
	    $_SESSION['naam'] = $gebruikersnaam;
      echo "<meta http-equiv='refresh' content='0'>";
        }else{
	         echo "<div class='form'>
           <h3>Email of wachtwoord is incorrect.</h3>
           <center><br/>Probeer <a href='index.php'>opnieuw</a></div</center>";
}
    }else{
?>
    	<form class="form" action="" method="post" name="login">
        <h2 class="login-title">Login</h2>
        <input type="text" class="login-input" name="gebruikersnaam" placeholder="Gebruikersnaam" autofocus>
        <input type="password" class="login-input" name="wachtwoord" placeholder="Wachtwoord">
        <input type="submit" value="Login" name="submit" class="login-button">
      <p class="login-lost">Nog geen account? Klik <a href="/config/register.php">hier</a></p>
      </form>

<?php } ?>
