<?php

require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $args = $_POST;
} else {
    $args = $_GET;
}

$contactId = $args['contactId'];

if ($contactId == NULL) {
    header("Status: 404 Not Found");
    exit;
}

dbConnect(ConfigFile);

$db = $GLOBALS['configDataBase']->db;

mysqli_select_db($GLOBALS['ligacao'], $db);

$query = "SELECT * FROM `smi`.`email-contacts` WHERE `id`='$contactId'";
$result = mysqli_query($GLOBALS['ligacao'], $query);

if ($result == FALSE) {
    header("Status: 404 Not Found");
} else {
    $contactData = mysqli_fetch_array($result);

    $email = $contactData['email'];

    header('Content-type: text/html; charset=utf-8');
    echo "$email";
}

mysqli_free_result($result);

dbDisconnect();
?>