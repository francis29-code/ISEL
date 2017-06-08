<?php

require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $args = $_POST;
} else {
    $args = $_GET;
}

$accountName = $args['accountName'];
$smtpServer = $args['smtpServer'];
$useSSL = $args['useSSL'];
$port = $args['port'];
$timeout = $args['timeout'];
$login = $args['loginName'];
$fromEmail = $args['email'];
$fromName = $args['displayName'];

if (
        $accountName == NULL ||
        $smtpServer == NULL ||
        $useSSL == NULL ||
        $port == NULL ||
        $timeout == NULL ||
        $login == NULL ||
        $fromEmail == NULL ||
        $fromName == NULL) {
    redirectToLastPage("E-mail with PHP", 5);
} else {
    header('Content-type: text/html; charset=utf-8');

    dbConnect(ConfigFile);

    $db = $GLOBALS['configDataBase']->db;

    mysqli_select_db($GLOBALS['ligacao'], $db);

    $query = "INSERT INTO `smi`.`email-accounts` " .
            "(`accountName`, `smtpServer`, `useSSL`, `port`, `timeout`, `loginName`, `email`, `displayName`) values " .
            "('$accountName', '$smtpServer', '$useSSL', '$port', '$timeout', '$login', '$fromEmail', '$fromName')";

    mysqli_query($GLOBALS['ligacao'], $query);

    $recordsInserted = mysqli_affected_rows($GLOBALS['ligacao']);

    if ($recordsInserted == -1) {
        echo "Insert has failed!";
    } else {
        echo "Account added with success.";
    }

    dbDisconnect();
}
?>