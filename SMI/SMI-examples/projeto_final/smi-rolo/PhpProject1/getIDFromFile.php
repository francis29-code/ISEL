<?php

require_once( "../Lib/lib.php" );
require_once( "../Lib/db.php" );


$id;

function getID() {
    global $id;
    
    dbConnect(ConfigFile);
    mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);
    $query = "SELECT id from ficheiro ORDER BY id DESC";
    $result = mysqli_query($GLOBALS['ligacao'], $query);
    if(mysqli_num_rows($result)==0){
        $id=1;
    }else{
        $id = mysqli_fetch_array($result)["id"]+1; 
    }
    mysqli_free_result($result);
    dbDisconnect();
    
    
    
    
    
}

?>
