<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Manage e-mail accounts</title>

        <link rel="stylesheet" type="text/css" href="../05-RSS/styles/rss.css">
    </head>

    <body>

        <h2>List existing e-mail accounts</h2>

        <?php
        require_once( "../Lib/db.php");

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $args = $_POST;
        } else {
            $args = $_GET;
        }

        dbConnect(ConfigFile);

        $db = $GLOBALS['configDataBase']->db;

        mysqli_select_db($GLOBALS['ligacao'], $db);

        $query = "SELECT * FROM `smi`.`email-accounts`";
        $result = mysqli_query($GLOBALS['ligacao'], $query);

        if ($result == FALSE) {
            echo "There are no accounts";
        } else {
            echo "<table border=\"1\">\n";
            echo "  <tr>\n";
            echo "    <th>Account Name</th>\n";
            echo "    <th>SMTP Server</th>\n";
            echo "    <th>Use SSL</th>\n";
            echo "    <th>Port</th>\n";
            echo "    <th>Timeout</th>\n";
            echo "    <th>Login Name</th>\n";
            echo "    <th>E-mail</th>\n";
            echo "    <th>Display Name</th>\n";
            echo "  </tr>\n";

            while ($accountData = mysqli_fetch_array($result)) {
                $accountName = $accountData['accountName'];
                $smtpServer = $accountData['smtpServer'];
                $_useSSL = $accountData['useSSL'];
                $port = $accountData['port'];
                $timeout = $accountData['timeout'];
                $login = $accountData['loginName'];
                $fromEmail = $accountData['email'];
                $fromName = $accountData['displayName'];

                if ($_useSSL == 0) {
                    $useSSL = "No";
                } else {
                    $useSSL = "Yes";
                }

                echo "  <tr>\n";
                echo "    <td>$accountName</td>\n";
                echo "    <td>$smtpServer</td>\n";
                echo "    <td>$useSSL</td>\n";
                echo "    <td>$port</td>\n";
                echo "    <td>$timeout</td>\n";
                echo "    <td>$login</td>\n";
                echo "    <td>$fromEmail</td>\n";
                echo "    <td>$fromName</td>\n";
                echo "  <tr>\n";
            }
            echo "</table>\n";

            mysqli_free_result($result);

            dbDisconnect();
        }
        ?>
    </body>
</html>