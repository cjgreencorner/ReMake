<?php
include "auth_session.php";
include 'style.php';
?>
<html>
<head>
    <meta charset="utf-8">
    <title>Logged in!</title>
</head>
<body>
    <div class="form">
        <p>Hey, <?php echo $_SESSION['naam']; ?>!</p>
        <p>Welcome back!</p>
        <p><a href="/config/logout.php">Logout</a></p>

    </div>
</body>
</html>
