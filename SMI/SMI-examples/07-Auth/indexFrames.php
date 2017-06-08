<!DOCTYPE html>
<?php
require_once '../Lib/lib.php';

$name = webAppName();
?>

<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>User Authentication using PHP</title>

        <link REL="stylesheet" TYPE="text/css" href="../Styles/GlobalStyle.css">
    </head>

    <frameset rows="15%,*">

        <frame name="title" noresize scrolling="no" src="<?php echo $name ?>title.php">

            <frameset cols = "20%,*">
                <frame noresize name="option" src ="<?php echo $name ?>menu.php" />
                <frame name="content" src ="<?php echo $name ?>main.php" />
            </frameset>
    </frameset>
</html>
