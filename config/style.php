<style type="text/css">
<?php
$kleur = "white";
if ($_GET['kleur']!="") {
  $kleur=$_GET['kleur'];
}
$inv = "black";
if ($_GET['kleur']=="black")
{
  $inv='white';
}
?>
body {
  background-color: <?php echo $kleur;?>;
}
p {
  color: <?php echo $inv;?>;
  text-align: center;
}
h1 {
  color: <?php echo $inv;?>;
  text-align: center;
}
h2 {
  color: <?php echo $inv; ?>;
  text-align: center;
}
h3 {
  color: <?php echo $inv;?>;
  text-align: center;
}
a:link {
  color: <?php echo $inv;?>;
}
a:hover {
  color: red;
}
p {
  text-align: center;
}
.sansserif style {
font-family: Arial, Helvetica, sans-serif;
}
th, td {
  padding: 15px;
  text-align: center;
}
form, label, input {
  text-align: center;
}
.form {
    margin: 50px auto;
    width: 300px;
    padding: 30px 25px;
    background: white;
}
h1.login-title {
    color: #666;
    margin: 0px auto 25px;
    font-size: 25px;
    font-weight: 300;
    text-align: center;
}
.login-input {
    font-size: 15px;
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 25px;
    height: 25px;
    width: calc(100% - 23px);
}
.login-input:focus {
    border-color:#6e8095;
    outline: none;
}
.login-button {
    color: #fff;
    background: #000000;
    border: 0;
    outline: 0;
    width: 100%;
    height: 50px;
    font-size: 16px;
    text-align: center;
    cursor: pointer;
}
.link {
    color: #666;
    font-size: 15px;
    text-align: center;
    margin-bottom: 0px;
}
.link a {
    color: #666;
}
</style>
