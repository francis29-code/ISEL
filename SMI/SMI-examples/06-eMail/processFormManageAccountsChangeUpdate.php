<?php

require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $args = $_POST;
} else {
    $args = $_GET;
}

$id = $args['id'];
$accountName = $args['accountName'];
$smtpServer = $args['smtpServer'];
$useSSL = $args['useSSL'];
$port = $args['port'];
$timeout = $args['timeout'];
$loginName = $args['loginName'];
$fromEmail = $args['email'];
$fromName = $args['displayName'];

if (
        $id == NULL ||
        $accountName == NULL ||
        $smtpServer == NULL ||
        $useSSL == NULL ||
        $port == NULL ||
        $timeout == NULL ||
        $loginName == NULL ||
        $fromEmail == NULL ||
        $fromName == NULL) {
    redirectToLastPage("E-mail with PHP", 5);
} else {
    header('Content-type: text/html; charset=utf-8');

    dbConnect(ConfigFile);

    $db = $GLOBALS['configDataBase']->db;

    mysqli_select_db($GLOBALS['ligacao'], $db);

    $query = "UPDATE `smi`.`email-accounts` SET " .
            "`accountName`='$accountName', `useSSL`='$useSSL', `smtpServer`='$smtpServer', `port`='$port', `timeout`='$timeout', `loginName`='$loginName', `email`='$fromEmail', `displayName`='$fromName' " .
            "WHERE `id`='$id'";

    mysqli_query($GLOBALS['ligacao'], $query);

    $recordsUpdated = mysqli_affected_rows($GLOBALS['ligacao']);

    if ($recordsUpdated == -1) {
        echo "Update has failed!";
    } else {
        echo "Account updated with success.";
    }

    dbDisconnect();
}
?>