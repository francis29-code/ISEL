<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>User Authentication using HTTP and PHP</title>

        <link REL="stylesheet" TYPE="text/css" href="../Styles/GlobalStyle.css">

    </head>
    <body>
        <h1>User Authentication using HTTP and PHP</h1>
        <h2>Basic, Digest and PHP Sessions</h2>

        <p><a href="indexFrames.php">Using frames</a></p>

        <p><a href="indexDivs.php">Using divs</a></p>

        <p><a target="_top" href="../">Back to Example Pages</a></p>
        <br>
        <br>
        <br>
        <p>Please ensure that:</p>
        <ul>
            <li>Apache Authentication modules are enable:</li>
            <ul>
                <li><code>LoadModule auth_basic_module modules/mod_auth_basic.so</code> in "httpd.conf" file +/- line 77</li>
                <li><code>LoadModule auth_digest_module modules/mod_auth_digest.so</code> in "httpd.conf" file +/- line 78</li>
            </ul>

            <br>

            <li>Paths in Apache Authentication files are updated:</li>
            <ul>
                <li><code><?php echo "" . __DIR__ . DIRECTORY_SEPARATOR . "Ver1" . DIRECTORY_SEPARATOR . ".htaccess"; ?></code></li>
                <li><code><?php echo "" . __DIR__ . DIRECTORY_SEPARATOR . "Ver2" . DIRECTORY_SEPARATOR . ".htaccess"; ?></code></li>
            </ul>

            <br>
        </ul>

        <p>If <code>UseCanonicalName On</code> update <code>ServerName</code> directive in "httpd-ssl.conf" file +/- 125</p>
        <br>
    </body>
</html>
