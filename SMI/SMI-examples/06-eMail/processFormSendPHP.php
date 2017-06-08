<?php

require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");
require_once( "../Lib/lib-mail-v2.php" );

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $args = $_POST;
} else {
    $args = $_GET;
}

#print_r( $args );

if (isset($args['accountId'])) {
    $accountId = $args['accountId'];
} else {
    $accountId = NULL;
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
        $toList == NULL ||
        $subject == NULL ||
        $message == NULL) {
    redirectToLastPage("E-mail with PHP", 5);
} else {
    header('Content-type: text/html; charset=utf-8');

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

    $fromEmail = $accountData['email'];
    $fromName = $accountData['displayName'];

    dbDisconnect();

    $toListAsArray = parseEmailList($toList);
    if ($ccList !== NULL and $ccList !== '' ) {
        $ccListAsArray = parseEmailList($ccList);
    } else {
        $ccListAsArray = NULL;
    }
    if ($bccList !== NULL  and $bccList !== '' ) {
        $bccListAsArray = parseEmailList($bccList);
    } else {
        $bccListAsArray = NULL;
    }

    $to = "";

    $isFirstToList = TRUE;
    foreach ($toListAsArray as $currentEmail) {
        if ($isFirstToList == FALSE) {
            $to .= ", ";
        } else {
            $isFirstToList = FALSE;
        }

        $to .= $currentEmail['display'] . " <" . $currentEmail['e-mail'] . ">";
    }

    $isFirstCcList = TRUE;
    if ($ccListAsArray !== NULL) {
        $to .= ", ";
        foreach ($ccListAsArray as $currentEmail) {
            if ($isFirstCcList == FALSE) {
                $to .= ", ";
            } else {
                $isFirstCcList = FALSE;
            }

            $to .= $currentEmail['display'] . " <" . $currentEmail['e-mail'] . ">";
        }
    }

    $isFirstBccList = TRUE;
    if ($bccListAsArray !== NULL) {
        $to .= ", ";
        foreach ($bccListAsArray as $currentEmail) {
            if ($isFirstBccList == FALSE) {
                $to .= ";";
            } else {
                $isFirstBccList = FALSE;
            }

            $to .= $currentEmail['display'] . " <" . $currentEmail['e-mail'] . ">";
        }
    }

    $message = str_replace("\n.", "\n..", $message);

    $newLine = "\r\n";

    $fromAsArray['display'] = $fromName;
    $fromAsArray['e-mail'] = $fromEmail;

    $headers = "MIME-Version: 1.0" . $newLine;
    $headers .= "Content-Type: text/plain; charset=UTF-8" . $newLine;
    $headers .= encodeHeaderEmailList('From', array($fromAsArray));
    $headers .= encodeHeaderEmailList('To', $toListAsArray);
    if ($ccList !== NULL and $ccList !== '' ) {
        $headers .= encodeHeaderEmailList('Cc', $ccListAsArray);
    }
    if ($bccList !== NULL  and $bccList !== '' ) {
        $headers .= encodeHeaderEmailList('Bcc', $bccListAsArray);
    }
    $headers .= encodeHeaderEmailList('Reply-To', array($fromAsArray));

    $preferences = array(
        "input-charset" => "UTF-8",
        "output-charset" => "ISO-8859-1",
        "scheme" => "Q");

    // Subject
    //$headers .= iconv_mime_encode("Subject", $subject, $preferences) . $newLine;

    echo "TO: " . str_replace(">", "&gt;", str_replace("<", "&lt;", $to)) . "<br>\n";
    echo "Subject: " . str_replace(">", "&gt;", str_replace("<", "&lt;", $subject)) . "<br>\n";
    echo "Message: " . str_replace(">", "&gt;", str_replace("<", "&lt;", $message)) . "<br>\n";
    echo "Headers: " . str_replace(">", "&gt;", str_replace("<", "&lt;", $headers)) . "<br>\n";

    $result = mail($to, $subject, $message, $headers);

    if ($result == TRUE) {
        echo "E-mail was delivered to e-mail server.";
    } else {
        echo "E-mail couldn't be delivered to e-mail server.";
    }
}
?>