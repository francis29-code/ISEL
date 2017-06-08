<?php
require_once( "../Lib/lib.php" );
require_once( "../Lib/db.php" );

$configurations = getConfiguration();
?>
<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>Image Processing - Upload file</title>

        <link REL="stylesheet" TYPE="text/css" href="../Styles/GlobalStyle.css">
    </head>

    <body>
        <form 
            enctype="multipart/form-data"
            action="processFormUpload.php"
            method="POST"
            name="FormUpload">

            Title<br>
            <input type="text" name="title"><br>

            Description: (Please enter up to 512 characters maximum.)<br>
            <textarea name="description" rows="4" cols="50"></textarea><br>

            Select file to upload:<br>
            <input 
                type="hidden" 
                name="MAX_FILE_SIZE" 
                value="<?php echo $configurations['maxFileSize'] ?>">
            <input 
                type="file" 
                name="userFile" 
                size="64"><br>
            <input type="submit" name="Submit" value="Upload file">
        </form>
    </body>
</html>