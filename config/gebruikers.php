<?php
include 'header.php';
include 'db.php';
$sql = "SELECT naam, mail, gebruikersnaam FROM users";
$result = $conn->query($sql);
if ($result->num_rows > 0) { ?>
  <table style='width:100%'>
    <tr>
      <th>Naam</th>
      <th>E-mail</th>
      <th>Gebruikersnaam</th>
    </tr>
    <?php
  while($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td>" . $row["naam"] . "</td>";
    echo "<td>" . $row["mail"] . "</td>";
    echo "<td>" . $row["gebruikersnaam"] . "</td>";
    echo "</tr>";
  }
  echo "</table>";
} else {
  echo "0 results";
}
$conn->close();
?>


<?php include 'footer.php';?>
