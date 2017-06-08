<?php

require_once( "../../Lib/lib.php" );
require_once( "../../Lib/db.php" );

prepareHeaders();

if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])) {
    showAuth("Basic", "Authentication using PHP", "You must provide a valid user name / password");
} else {
    $userName = $_SERVER['PHP_AUTH_USER'];
    $password = $_SERVER['PHP_AUTH_PW'];

    $userId = isValid($userName, $password, "Basic");
    if ($userId > 0) {
        header("Location: main.php");
    } else {
        showAuth("Basic", "Authentication using PHP", "Invalid user name / password");
    }
}
?>
