<?php
require_once '../Lib/lib.php';

$name = webAppName();
?>

<html>  
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>e-Mail with PHP - Divs</title>

        <link rel="stylesheet" type="text/css" href="../05-RSS/styles/rss.css">

        <script type="text/javascript" src="../05-RSS/scripts/getContent.js">
        </script>

        <script type="text/javascript" src="scripts/mail.js">
        </script>

    </head>

    <body>

        <div 
            accesskey="" 
            id="containerDiv"
            style="height:99%;width:99%;">

            <div 
                id="headerDiv" 
                style="height:15%;width:99.5%;">

                <?php include( "titleBody.php" ) ?>

            </div>

            <div 
                id="menuDiv" 
                style="height:77.5%;width:14%;float:left;">

                <?php include( "menuBodyDivs.php" ) ?>

            </div>

            <div 
                id="contentDiv"
                style="height:77.5%;width:84%;float:right;overflow-y: scroll;">

                <?php include( "formSendBody.php" ) ?>

            </div>

        </div>

    </body>

</html>