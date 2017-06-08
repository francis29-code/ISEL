<?php
require_once '../Lib/lib.php';

$name = webAppName();
?>

<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>e-Mail with PHP - Frames</title>

        <link rel="stylesheet" type="text/css" href="../05-RSS/styles/rss.css">

        <script type="text/javascript" src="../05-RSS/scripts/getContent.js">
        </script>

        <script type="text/javascript" src="scripts/mail.js">
        </script>

    </head>

    <frameset rows="10%,*">

        <frame name="title" noresize scrolling="no" src="<?php echo $name ?>title.php">

            <frameset cols = "20%,*">
                <frame noresize name="option" src ="<?php echo $name ?>menu.php" />
                <frame name="content" src ="<?php echo $name ?>formSend.php" />
            </frameset>
    </frameset>
</html>
