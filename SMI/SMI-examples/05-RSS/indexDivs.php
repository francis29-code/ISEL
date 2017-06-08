<?php
require_once '../Lib/lib.php';

$name = webAppName();
?>

<html>

    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Rich Site Summary - RSS - Divs</title>

        <link rel="stylesheet" type="text/css" href="styles/rss.css">

        <script type="text/javascript" src="scripts/getContent.js">
        </script>

    </head>

    <body>

        <div 
            accesskey="" 
            id="containerDiv"
            style="height:99%;width:99%;background-color:lightgrey">

            <div 
                id="headerDiv" 
                style="height:15%;width:99.5%;background-color:lightgrey">

                <?php include( "titleBody.php" ) ?>

            </div>

            <div 
                id="menuDiv" 
                style="height:77.5%;width:14%;float:left;background-color:lightgrey">

                <?php include( "menuBodyDivs.php" ) ?>

            </div>

            <div 
                id="contentDiv"
                style="height:77.5%;width:84%;float:right;overflow-y: scroll;background-color:lightgrey">

                <?php include( "formAddNewBody.php" ) ?>

            </div>

        </div>

    </body>

</html>