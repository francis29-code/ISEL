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

    <body>

        <div 
            accesskey="" 
            id="container" 
            class="" 
            style="height:680px;width:100%">

            <div 
                id="header" 
                style="height:20%">
                <iframe
                    width="100%" 
                    height="100%" 
                    src="<?php echo $name ?>titleBody.php">
                </iframe>
            </div>

            <div 
                id="menu" 
                style="height:80%;width:20%;float:left;">

                <iframe 
                    width="100%" 
                    height="100%" 
                    src="<?php echo $name ?>menuBody.php">
                </iframe>
            </div>

            <div 
                id="content"
                style="height:80%;width:75%;float:right;">

                <iframe
                    name="content"
                    width="100%" 
                    height="100%" 
                    src="<?php echo $name ?>linksBody.php">
                </iframe>

            </div>

            <!--
            <div 
              id="footer" 
              style="height:15%;width:100%;clear:both;text-align:center;">
            
              Copyright © Carlos Gonçalves
            
            </div>
            -->

        </div>

    </body>

</html>