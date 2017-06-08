<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Manage e-mail contacts</title>

        <link rel="stylesheet" type="text/css" href="../05-RSS/styles/rss.css">
    </head>

    <body>

        <h2>List existing e-mail contacts</h2>

        <?php
        require_once( "../Lib/db.php");

        dbConnect(ConfigFile);

        $db = $GLOBALS['configDataBase']->db;

        mysqli_select_db($GLOBALS['ligacao'], $db);

        $query = "SELECT * FROM `smi`.`email-contacts`";
        $result = mysqli_query($GLOBALS['ligacao'], $query);

        if ($result == FALSE) {
            echo "There are no contacts";
        } else {
            echo "<table border=\"1\">\n";
            echo "  <tr>\n";
            echo "    <th>Display Name</th>\n";
            echo "    <th>e-mail</th>\n";
            echo "  </tr>\n";

            while ($contactData = mysqli_fetch_array($result)) {
                $fromName = $contactData['displayName'];
                $email = $contactData['email'];

                echo "  <tr>\n";
                echo "    <td>$fromName</td>\n";
                echo "    <td>$email</td>\n";
                echo "  <tr>\n";
            }
            echo "</table>\n";

            mysqli_free_result($result);

            dbDisconnect();
        }
        ?>
    </body>
</html>