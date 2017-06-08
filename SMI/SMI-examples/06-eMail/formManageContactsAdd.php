<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Manage e-mail contacts</title>

        <link rel="stylesheet" type="text/css" href="../05-RSS/styles/rss.css">
    </head>

    <body>
        <h2>Add new e-mail contact</h2>

        <form action="processFormManageContactsAdd.php" method="post">
            <table>
                <tr>
                    <td>
                        * E-mail address:
                    </td>
                    <td>
                        <input type="text" size=32 name="email">
                    </td>
                </tr>
                <tr>
                    <td>
                        * Display name:
                    </td>
                    <td>
                        <input type="text" size=32 name="displayName">
                    </td>
                </tr>
            </table>

            <input type="submit" name="add" value="Add Contact"> <input type="reset" name="reset" value="Clear">

            <br>
            The fields marked with a * are mandatory.    
        </form>

    </body>
</html>