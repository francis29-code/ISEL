<?php

require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $args = $_POST;
} else {
    $args = $_GET;
}

$accountId = $args['accountId'];

if ($accountId == NULL) {
    redirectToLastPage("E-mail with PHP", 5);
} else {
    header('Content-type: text/html; charset=utf-8');

    dbConnect(ConfigFile);

    $db = $GLOBALS['configDataBase']->db;

    mysqli_select_db($GLOBALS['ligacao'], $db);

    $query = "SELECT * FROM `smi`.`email-accounts` WHERE `id` = '$accountId'";

    $result = mysqli_query($GLOBALS['ligacao'], $query);

    if ($result == FALSE) {
        echo "Invalid account";
    } else {
        echo "<form action=\"processFormManageAccountsChangeUpdate.php\" method=\"post\">\n";
        echo "  <table border=\"1\">\n";
        echo "    <tr>\n";
        echo "      <th>Fields</th>\n";
        echo "      <th>Old Values</th>\n";
        echo "      <th>New value</th>\n";
        echo "    </tr>\n";

        $accountData = mysqli_fetch_array($result);

        $id = $accountData['id'];
        $accountName = $accountData['accountName'];
        $smtpServer = $accountData['smtpServer'];
        $useSSL = $accountData['useSSL'];
        $port = $accountData['port'];
        $timeout = $accountData['timeout'];
        $loginName = $accountData['loginName'];
        $fromEmail = $accountData['email'];
        $fromName = $accountData['displayName'];

        echo "    <tr>\n";
        echo "      <td>Account Name</td>\n";
        echo "      <td>$accountName</td>\n";
        echo "      <td><input type=\"text\" size=32 name=\"accountName\" value=\"$accountName\"></td>\n";
        echo "    </tr>\n";

        echo "    <tr>\n";
        echo "      <td>SMTP Server</td>\n";
        echo "      <td>$smtpServer</td>\n";
        echo "      <td><input type=\"text\" size=32 name=\"smtpServer\" value=\"$smtpServer\"></td>\n";
        echo "    </tr>\n";


        echo "    <tr>\n";
        echo "      <td>Use SSL</td>\n";
        if ($useSSL == 0) {
            echo "      <td>No</td>\n";
            echo "      <td><select name=\"useSSL\" ><option value=\"0\">No</option><option value=\"1\">Yes</option></select></td>\n";
        } else {
            echo "      <td>Yes</td>\n";
            echo "      <td><select name=\"useSSL\" ><option value=\"1\">Yes</option><option value=\"0\">No</option></select></td>\n";
        }
        echo "    </tr>\n";

        echo "    <tr>\n";
        echo "      <td>Port</td>\n";
        echo "      <td>$port</td>\n";
        echo "      <td><input type=\"text\" size=32 name=\"port\" value=\"$port\"></td>\n";
        echo "    </tr>\n";

        echo "    <tr>\n";
        echo "      <td>Timeout</td>\n";
        echo "      <td>$timeout</td>\n";
        echo "      <td><input type=\"text\" size=32 name=\"timeout\" value=\"$timeout\"></td>\n";
        echo "    </tr>\n";

        echo "    <tr>\n";
        echo "      <td>Login Name</td>\n";
        echo "      <td>$loginName</td>\n";
        echo "      <td><input type=\"text\" size=32 name=\"loginName\" value=\"$loginName\"></td>\n";
        echo "    </tr>\n";

        echo "    <tr>\n";
        echo "      <td>E-mail</td>\n";
        echo "      <td>$fromEmail</td>\n";
        echo "      <td><input type=\"text\" size=32 name=\"email\" value=\"$fromEmail\"></td>\n";
        echo "    </tr>\n";

        echo "    <tr>\n";
        echo "      <td>Display Name</td>\n";
        echo "      <td>$fromName</td>\n";
        echo "      <td><input type=\"text\" size=32 name=\"displayName\" value=\"$fromName\"></td>\n";
        echo "    </tr>\n";

        echo "  </table>\n";

        echo "<input type=\"hidden\" size=32 name=\"id\" value=\"$id\">";

        echo "  <input type=\"submit\" name=\"update\" value=\"Update account\"><br>\n";
    }
    dbDisconnect();
}
?>
