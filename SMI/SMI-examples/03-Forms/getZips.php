<!DOCTYPE html>
<?php
header('Content-Type: text/html; charset=utf-8');
//ID do county recebido
$county = $_GET["county"];

$options = "";

require_once("../Lib/db.php");

dbConnect(ConfigFile);

mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

$query = "SELECT `postalCode`, `nameLocation` FROM `forms-zips` WHERE `idCounty`=$county";
$resultado = mysqli_query($GLOBALS['ligacao'], $query);
$notFirst = FALSE;

//refatorizar para codigos postais
if ($resultado) {
  $options .= "0| @";
  while ($registo = mysqli_fetch_array($resultado)) {
    $postalCode = $registo['postalCode'];
    $nameLocation = $registo['nameLocation'];
    if ($notFirst) {
      $options .= "@";
    } else {
      $notFirst = TRUE;
    }
    $options .= "$postalCode|$nameLocation";
  }
} else {
  $options = '-1|No Counties Available';
}

echo $options;
?>
