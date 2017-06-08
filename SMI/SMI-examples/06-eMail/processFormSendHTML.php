<?php

require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");
require_once( '../Lib/HtmlMimeMail-class.php' );
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

    $smtpServer = $accountData['smtpServer'];
    $useSSL = $accountData['useSSL'];
    $port = $accountData['port'];
    $loginName = $accountData['loginName'];
    $fromEmail = $accountData['email'];
    $fromName = $accountData['displayName'];

    dbDisconnect();

    /*     * *************************************
     * 
     * Read the file background.gif into $backgrnd.
     * 
     * ************************************* */
    $filenameBackgroud = 'images/background.gif';
    $fdBackgroud = fopen($filenameBackgroud, 'rb');
    $backgrnd = fread($fdBackgroud, filesize($filenameBackgroud));
    fclose($fdBackgroud);

    /*     * *************************************
     * 
     * Read the file test.zip into $attachment.
     * 
     * ************************************* */
    $filenameAttach = 'attachs/example.zip';
    $fpAttach = fopen($filenameAttach, 'rb');
    $attachment = fread($fpAttach, filesize($filenameAttach));
    fclose($fpAttach);

    /*     * *************************************
     * 
     * Read the file image001.gif into $attachment.
     * 
     * ************************************* */
    $filenameAttach2 = 'attachs/image001.gif';
    $fpAttach2 = fopen($filenameAttach2, 'rb');
    $attachment2 = fread($fpAttach2, filesize($filenameAttach2));
    fclose($fpAttach2);

    $filenameAttach3 = 'attachs/Doc.pdf';
    $fpAttach3 = fopen($filenameAttach3, 'rb');
    $attachment3 = fread($fpAttach3, filesize($filenameAttach3));
    fclose($fpAttach3);

    $tos = parseEmailList($toList);
    foreach ($tos as $to) {
        $toName = $to["display"];
        $toEmail = $to["e-mail"];

        /*         * *************************************
         * 
         * Create the mail object.
         * 
         * ************************************* */
        $mail = new HtmlMimeMail();

        /*         * *************************************
         * 
         * Text and HTML components of the e-mail.
         * 
         * ************************************* */
        $text = $message;
        $html = '<HTML>' .
                '  <BODY BACKGROUND="background.gif">' .
                '  <FONT FACE="Verdana, Arial" COLOR="#FF0000">' .
                $text .
                '</FONT>' .
                '  <P>' .
                '  </BODY>' .
                '</HTML>';

        /*         * *************************************
         * 
         * Add the text, html and embedded images.
         * 
         * ************************************* */
        $mail->add_html_image(
                $backgrnd, 'background.gif', 'image/gif');
        $mail->add_html($html, $text);

        /*         * *************************************
         * 
         * Add an attachment to the email.
         * 
         * ************************************* */
        $mail->add_attachment(
                $attachment, 'example.zip', 'application/octet-stream');
        $mail->add_attachment(
                $attachment2, 'image001.gif', 'image/gif');
        $mail->add_attachment(
                $attachment3, 'Doc.pdf', 'application/octet-stream');

        /*         * *************************************
         * 
         * Builds the message.
         * 
         * ************************************* */
        $mail->build_message();

        /*         * *************************************
         * 
         * Sends the message.
         * 
         * ************************************* */
        $result = $mail->send(
                $smtpServer, 
                $useSSL, 
                $port, 
                $loginName, 
                $password, 
                $toName, 
                $toEmail, 
                $fromName, 
                $fromEmail, 
                $subject, 
                "X-Mailer: Html Mime Mail Class");

        if ($result == TRUE) {
            echo "E-mail to $toName &lt;$toEmail&gt; was delivered to e-mail server.\n<br>";
        } else {
            echo "E-mail to $toName &lt;$toEmail&gt; couldn't be delivered to e-mail server.\n<br>";
        }
    }
}
?>