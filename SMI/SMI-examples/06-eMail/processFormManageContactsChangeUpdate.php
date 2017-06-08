<?php

require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $args = $_POST;
} else {
    $args = $_GET;
}

$id = $args['id'];
$fromName = $args['displayName'];
$email = $args['email'];

if (
        $id == NULL ||
        $fromName == NULL ||
        $email == NULL) {
    redirectToLastPage("E-mail with PHP", 5);
} else {
    header('Content-type: text/html; charset=utf-8');

    dbConnect(ConfigFile);

    $db = $GLOBALS['configDataBase']->db;

    mysqli_select_db($GLOBALS['ligacao'], $db);

    $query = "UPDATE `smi`.`email-contacts` SET " .
            "`displayName`='$fromName', `email`='$email' " .
            "WHERE `id`='$id'";

    $result = mysqli_query($GLOBALS['ligacao'], $query);

    $recordsUpdated = mysqli_affected_rows($GLOBALS['ligacao']);

    if ($recordsUpdated == -1) {
        echo "Update has failed!";
    } else {
        echo "Contact updated with success.";
    }

    dbDisconnect();
}
?>