<?php

require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $args = $_POST;
} else {
    $args = $_GET;
}

$email = $args['email'];
$fromName = $args['displayName'];

if (
        $email == NULL ||
        $fromName == NULL) {
    redirectToLastPage("E-mail with PHP", 5);
} else {
    header('Content-type: text/html; charset=utf-8');

    dbConnect(ConfigFile);

    $db = $GLOBALS['configDataBase']->db;

    mysqli_select_db($GLOBALS['ligacao'], $db);

    $query = "INSERT INTO `smi`.`email-contacts`" .
            "(`email`, `displayName`) values " .
            "('$email', '$fromName')";

    $result = mysqli_query($GLOBALS['ligacao'], $query);

    $recordsInserted = mysqli_affected_rows($GLOBALS['ligacao']);

    if ($recordsInserted == -1) {
        echo "Insert has failed!";
    } else {
        echo "Contact added with success.";
    }

    dbDisconnect();
}
?>