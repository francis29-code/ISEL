<?php




function encodeBase64($path){
    $type = pathinfo($path,PATHINFO_EXTENSION);
    $data = file_get_contents($path);
    return base64_encode($data); 
    
}






?>
