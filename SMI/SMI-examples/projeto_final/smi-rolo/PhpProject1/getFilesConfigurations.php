<?php

$destino;
$thumbsDestino;
$thumbsWidth;
$thumbsHeight;

function getFilesConfigurations(){
    
    global $destino;
    global $thumbsDestino;
    global $thumbsWidth;
    global $thumbHeight;
    
    $configFile = "../FilesConfigurations/files_config.xml";
    ($aux = simplexml_load_file( $configFile )) or die ("Can't read configuration file.");
    $fileConfig = $aux[0];
    $destino           = $fileConfig->destino_base;
    $thumbsDestino     = $fileConfig->thumb_dst;
    $thumbsWidth       = $fileConfig->thumb_Width;
    $thumbHeight       = $fileConfig->thumb_Height;
    
    /*print_r($destino);
    print_r($thumbsDestino);
    print_r($thumbsWidth);
    print_r($thumbHeight);
    */
    
        
    
}



?>