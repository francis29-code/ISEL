<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Manage e-mail contacts</title>

        <link rel="stylesheet" type="text/css" href="../05-RSS/styles/rss.css">
    </head>

    <body>
        <h2>Delete an existing e-mail contact</h2>

        <form action="processFormManageContactsDelete.php" method="post">
            Account:<br>

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
                        $displayName = $record['displayName'];
                        echo "                <option value=\"$id\">$displayName</option>\n";
                    }

                    mysqli_free_result($result);
                } else {
                    echo "                <option value=\"-1\">No e-mail contacts available</option>\n";
                }
                dbDisconnect();
                ?>
            </select><br>

            <input type="submit" name="delete" value="Delete Contact">
        </form>

    </body>
</html>
