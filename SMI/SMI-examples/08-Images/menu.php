<?php
require_once( "../Lib/lib.php" );

$name = webAppName();
?>

<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Image Processing</title>

        <link REL="stylesheet" TYPE="text/css" href="../Styles/GlobalStyle.css">
    </head>
    <body>
        <a target="content" href="<?php echo $name ?>main.php">Home</a><br>
        <a target="content" href="<?php echo $name ?>formUpload.php">Upload File</a><br>
        <a target="content" href="<?php echo $name ?>list.php">List Files</a><br>
        <a target="content" href="<?php echo $name ?>stats.php">Show Statistics</a><br>
        <a target="content" href="<?php echo $name ?>captcha.php">Generate captcha</a><br>
        <a target="content" href="<?php echo $name ?>links.php">Useful Links</a><br>
        <a target="content" href="<?php echo $name ?>jw/">JWPlayer6 Demo</a><br>
        <br>
        <a target="_top" href="../">Back to Examples Pages</a>
    </body>
</html>
