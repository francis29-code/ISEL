<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Manage e-mail accounts</title>

        <link rel="stylesheet" type="text/css" href="../05-RSS/styles/rss.css">
    </head>

    <body>
        <h2>Change an existing e-mail account</h2>

        <form action="processFormManageAccountsChange.php" method="post">
            Account:<br>

            <select name="accountId">
                <?php
                require_once( "../Lib/db.php");

                dbConnect(ConfigFile);

                $db = $GLOBALS['configDataBase']->db;

                mysqli_select_db($GLOBALS['ligacao'], $db);

                $query = "SELECT `id`, `accountName` FROM `smi`.`email-accounts`";
                $result = mysqli_query($GLOBALS['ligacao'], $query);

                if ($result) {
                    while ($record = mysqli_fetch_array($result)) {
                        $id = $record['id'];
                        $accountName = $record['accountName'];
                        echo "                <option value=\"$id\">$accountName</option>\n";
                    }

                    mysqli_free_result($result);
                } else {
                    echo "                <option value=\"-1\">No e-mail accounts available</option>\n";
                }
                dbDisconnect();
                ?>
            </select><br>

            <input type="submit" name="change" value="Change Account">
        </form>

    </body>
</html>
