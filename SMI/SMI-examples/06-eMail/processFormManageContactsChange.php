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
    redirectToLastPage("E-mail with PHP", 5);
} else {
    header('Content-type: text/html; charset=utf-8');

    dbConnect(ConfigFile);

    $db = $GLOBALS['configDataBase']->db;

    mysqli_select_db($GLOBALS['ligacao'], $db);

    $query = "SELECT * FROM `smi`.`email-contacts` WHERE `id` = '$contactId'";

    $result = mysqli_query($GLOBALS['ligacao'], $query);

    if ($result == FALSE) {
        echo "Invalid contact";
    } else {
        echo "<form action=\"processFormManageContactsChangeUpdate.php\" method=\"post\">\n";
        echo "  <table border=\"1\">\n";
        echo "    <tr>\n";
        echo "      <th>Fields</th>\n";
        echo "      <th>Old Values</th>\n";
        echo "      <th>New value</th>\n";
        echo "    </tr>\n";

        $accountData = mysqli_fetch_array($result);

        $id = $accountData['id'];
        $fromName = $accountData['displayName'];
        $email = $accountData['email'];

        echo "    <tr>\n";
        echo "      <td>Display Name</td>\n";
        echo "      <td>$fromName</td>\n";
        echo "      <td><input type=\"text\" size=32 name=\"displayName\" value=\"$fromName\"></td>\n";
        echo "    </tr>\n";

        echo "    <tr>\n";
        echo "      <td>E-mail Address</td>\n";
        echo "      <td>$email</td>\n";
        echo "      <td><input type=\"text\" size=32 name=\"email\" value=\"$email\"></td>\n";
        echo "    </tr>\n";

        echo "  </table>\n";

        echo "<input type=\"hidden\" size=32 name=\"id\" value=\"$id\">";

        echo "  <input type=\"submit\" name=\"update\" value=\"Update contact\"><br>\n";
    }
    dbDisconnect();
}
?>
