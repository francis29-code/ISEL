<?php

require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");
require_once( "../Lib/lib-mail-v2.php" );

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $args = $_POST;
} else {
    $args = $_GET;
}

if (isset($args['accountId'])) {
    $accountId = $args['accountId'];
} else {
    $accountId = NULL;
}
if (isset($args['password'])) {
    $password = $args['password'];
} else {
    $password = NULL;
}
if (isset($args['toList'])) {
    $toList = $args['toList'];
} else {
    $toList = NULL;
}
if (isset($args['ccList'])) {
    $ccList = $args['ccList'];
} else {
    $ccList = NULL;
}
if (isset($args['bccList'])) {
    $bccList = $args['bccList'];
} else {
    $bccList = NULL;
}
if (isset($args['subject'])) {
    $subject = $args['subject'];
} else {
    $subject = NULL;
}
if (isset($args['message'])) {
    $message = $args['message'];
} else {
    $message = NULL;
}
if (isset($args['showSMTP'])) {
    $showSMTP = $args['showSMTP'];
} else {
    $showSMTP = NULL;
}

if (
        $accountId == NULL ||
        $password == NULL ||
        $toList == NULL ||
        $subject == NULL ||
        $message == NULL) {
    redirectToLastPage("E-mail with PHP", 5);
} else {
    header( 'Content-type: text/html; charset=utf-8' );

    // Get Account details
    dbConnect(ConfigFile);

    $db = $GLOBALS['configDataBase']->db;

    mysqli_select_db($GLOBALS['ligacao'], $db);

    $query = "SELECT * FROM `smi`.`email-accounts` WHERE `id` = '$accountId'";
    $resultado = mysqli_query($GLOBALS['ligacao'], $query);

    if ($resultado == FALSE) {
        echo "Can't read account details from data base (account#$accountId)";
        dbDisconnect();
        exit;
    }

    $accountData = mysqli_fetch_array($resultado);

    $smtpServer = $accountData['smtpServer'];
    $useSSL = $accountData['useSSL'];
    $port = $accountData['port'];
    $timeout = $accountData['timeout'];
    $loginName = $accountData['loginName'];
    $fromEmail = $accountData['email'];
    $fromName = $accountData['displayName'];

    dbDisconnect();

    $showProtocol = FALSE;
    if ($showSMTP != NULL) {
        $showProtocol = TRUE;
    }

    #$caFileName = "C:\\xampp\\certs\\MailShield.pem";
    #$caFileName = "C:\\xampp\\certs\\cacert.pem";
    $caFileName = NULL;

    $result = sendAuthEmail(
            $smtpServer, 
            $useSSL, 
            $port, 
            $timeout, 
            $loginName, 
            $password, 
            $fromEmail, 
            $fromName, 
            $toList, 
            $ccList, 
            $bccList, 
            $subject, 
            $message, 
            $showProtocol, 
            $caFileName);

    if ($result == TRUE) {
        echo "E-mail was delivered to e-mail server.";
    } else {
        echo "E-mail couldn't be delivered to e-mail server.";
    }
}
?>