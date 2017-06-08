<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Manage e-mail accounts</title>

        <link rel="stylesheet" type="text/css" href="../05-RSS/styles/rss.css">
    </head>

    <body>
        <h2>Add new e-mail account</h2>

        <form action="processFormManageAccountsAdd.php" method="post">
            <table>
                <tr>
                    <td>
                        * Account Name:
                    </td>
                    <td>
                        <input type="text" size=32 name="accountName">
                    </td>
                </tr>
                <tr>
                    <td>
                        * Use SSL:
                    </td>
                    <td>
                        <select name="useSSL" >
                            <option value="0">No</option>
                            <option value="1">yes</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td>
                        * SMTP Server:
                    </td>
                    <td>
                        <input type="text" size=32 name="smtpServer">
                    </td>
                </tr>
                <tr>
                    <td>
                        * Port:
                    </td>
                    <td>
                        <input type="text" size=32 name="port">
                    </td>
                </tr>
                <tr>
                    <td>
                        * Timeout:
                    </td>
                    <td>
                        <input type="text" size=32 name="timeout">
                    </td>
                </tr>
                <tr>
                    <td>
                        * Login Name:
                    </td>
                    <td>
                        <input type="text" size=32 name="loginName">
                    </td>
                </tr>
                <tr>
                    <td>
                        * E-mail:
                    </td>
                    <td>
                        <input type="text" size=32 name="email">
                    </td>
                </tr>        
                <tr>
                    <td>
                        * Display Name:
                    </td>
                    <td>
                        <input type="text" size=32 name="displayName">
                    </td>
                </tr>
            </table>

            <input type="submit" name="add" value="Add Account"> <input type="reset" name="reset" value="Clear">

            <br>
            The fields marked with a * are mandatory.    
        </form>
    </body>
</html>
