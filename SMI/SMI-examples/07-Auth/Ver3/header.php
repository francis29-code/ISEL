<?php
require_once( "../../Lib/lib.php" );
require_once( "../../Lib/db.php" );

$userName = $_SERVER['PHP_AUTH_USER'];
$password = $_SERVER['PHP_AUTH_PW'];

$userId = isValid($userName, $password, "basic");
if ($userId > 0) {
    $userRole = getRole($userId);

    echo "<p align=\"right\">$userName, your role is $userRole</p>";
}
?>
<hr>