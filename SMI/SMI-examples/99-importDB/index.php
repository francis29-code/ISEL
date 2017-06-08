<!DOCTYPE html>

<?php
//db.php - ficheiro PHP com funções que tratam da informação da base de dados
require_once("../Lib/db.php");

//permite ao script executar o tempo que for necessário
set_time_limit(0);

dbConnect(ConfigFile);

mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

//parse ao ficheiro
$count =0;
if(($handle = fopen("cp-utf8.csv","rt")) !== FALSE){
  //while incrementa a cada linha do ficheiro CSV
  while(($data = fgetcsv($handle,1000,";")) !== FALSE){
    //parse de cada string
    $newLine = $data;
    print_r($newLine);
    //query SQL - INSERTs
    $query = "INSERT INTO `forms-zips` (idDistrict,idCounty,idLocation,nameLocation,postalCode,postalCodeExtension,postalCodeName) VALUES ('$newLine[0]','$newLine[1]','$newLine[2]','$newLine[3]','$newLine[4]','$newLine[5]','$newLine[6]')";
    $resultado = mysqli_query($GLOBALS['ligacao'], $query);

    $count++;

    if($count > 33){
      break;
    }

  }
}

dbDisconnect();
?>
