<?php

require_once( "../../Lib/lib.php" );
require_once( "../../Lib/db.php" );

$serverName = $_SERVER['SERVER_NAME'];
#$serverName = "localhost";

$serverPort = 80;

$name = webAppName();

$baseUrl = "http://" . $serverName . ":" . $serverPort;

$baseNextUrl = $baseUrl . $name;

$username = $_POST['username'];
$password = $_POST['password'];

$userId = isValid($username, $password, "basic");
if ($userId > 0) {
    session_start();
    $_SESSION['username'] = $username;
    $_SESSION['id'] = $userId;

    if (isset($_SESSION['locationAfterAuth'])) {
        $baseNextUrl = $baseUrl;
        $nextUrl = $_SESSION['locationAfterAuth'];
    } else {
        $nextUrl = "pag_1.php";
    }
} else {
    $nextUrl = "formLogin.php";
}

header("Location: " . $baseNextUrl . $nextUrl);
?>