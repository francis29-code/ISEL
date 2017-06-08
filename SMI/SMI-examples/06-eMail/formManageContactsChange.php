<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Manage e-mail contacts</title>

        <link rel="stylesheet" type="text/css" href="../05-RSS/styles/rss.css">
    </head>

    <body>
        <h2>Change an existing e-mail contact</h2>

        <form action="processFormManageContactsChange.php" method="post">
            Contact:<br>

            <select name="contactId">
                <?php
                require_once( "../Lib/db.php");

                dbConnect(ConfigFile);

                $db = $GLOBALS['configDataBase']->db;

                mysqli_select_db($GLOBALS['ligacao'], $db);

                $query = "SELECT `id`, `displayName` FROM `smi`.`email-contacts`";
                $result = mysqli_query($GLOBALS['ligacao'], $query);

                if ($result) {
                    while ($record = mysqli_fetch_array($result)) {
                        $id = $record['id'];
                        $fromName = $record['displayName'];
                        echo "                <option value=\"$id\">$fromName</option>\n";
                    }

                    mysqli_free_result($result);
                } else {
                    echo "                <option value=\"-1\">No e-mail contacts available</option>\n";
                }
                dbDisconnect();
                ?>
            </select><br>

            <input type="submit" name="change" value="Change Contact">
        </form>
    </body>
</html>