<?php
require_once( "../../Lib/lib.php" );

$serverName = $_SERVER['SERVER_NAME'];
#$serverName = "localhost";

$serverPortSSL = 443;
$serverPort = 80;

$name = webAppName();

$nextUrl = "https://" . $serverName . ":" . $serverPortSSL . $name . "processFormLogin.php";
#$nextUrl = "http://" . $serverName . ":" . $serverPort . $name . "processFormLogin.php";
?>

<form action="<?php echo $nextUrl ?>" method="POST">
    <table>
        <tr>
            <td>User Name</td>
            <td><input type="text" name="username"></td>
        </tr>
        <tr>
            <td>Password</td>
            <td><input type="password" name="password"></td>
        </tr>
    </table>

    <input type="submit" value="Login">
</form>
