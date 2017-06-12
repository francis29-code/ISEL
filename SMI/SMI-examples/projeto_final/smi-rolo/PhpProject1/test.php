<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        require_once( "../Lib/lib.php" );
        require_once( "../Lib/db.php" );

        // TODO validate input data
        $id = 1;

        // Read from the data base details about the file

        dbConnect(ConfigFile);
        mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);
        $query = "Select * from ficheiro where id ='" . $id . "'";
        $result = mysqli_query($GLOBALS['ligacao'], $query);
        $result = mysqli_fetch_array($result);
       
        $thumbFileNameAux = $result['conteudo_thumbs'];
        print_r("thumbFileName: " . $thumbFileNameAux . " ");
        $thumbMimeFileName = $result['mime'];
        print_r("thumbFileMime: " . $thumbMimeFileName . " ");
        $thumbTypeFileName = $result['tipo'];
        print_r("thumbFileType: " . $thumbTypeFileName . " ");
        
        header("Content-type: $thumbMimeFileName/$thumbTypeFileName");
        header("Content-Length: " . filesize($thumbFileNameAux));

        $thumbFileHandler = fopen($thumbFileNameAux, 'rb');
        //retorna toda a data de um apontador
        fpassthru($thumbFileHandler);
        fclose($thumbFileHandler);

        mysqli_free_result($result);
        dbDisconnect();
        ?>
    </body>
</html>
